import os
import sys
import tomllib as toml
from pprint import pprint


class Node:
    def __init__(self, name):
        self.name = name
        self.parents: list[Node] = []
        self.children = []
        self._config = {}

    def spec(self):
        return self._config["spec"]

    def is_override_merge(self) -> bool:
        return (
            self._config["policyMetadata"]["type"] == "override"
            and self._config["policyMetadata"]["strategy"] == "merge"
        )

    def is_override_atomic(self) -> bool:
        return (
                self._config["policyMetadata"]["type"] == "override"
                and self._config["policyMetadata"]["strategy"] == "atomic"
        )

    def is_default_merge(self) -> bool:
        return (
            self._config["policyMetadata"]["type"] == "default"
            and self._config["policyMetadata"]["strategy"] == "merge"
        )


def merge(a: dict, b: dict):
    copy = a.copy()
    for key in copy:
        if key in b:
            if isinstance(copy[key], dict) and isinstance(b[key], dict):
                copy[key].update(merge(copy[key], b[key]))
            else:
                a[key] = b[key]
    for key in b:
        if key not in copy:
            copy[key] = b[key]
    return copy


def merge_spec(spec: dict, node: Node) -> dict:
    if node.is_override_atomic():
        spec = node.spec()
    if node.is_default_merge():
        spec = merge(spec, node.spec())
    for parent in node.parents:
        spec = merge_spec(spec, parent)

    return spec


def override_spec(spec: dict, node: Node) -> dict:
    if node.is_override_merge():
        spec = merge(node.spec(), spec)
    if node.is_override_atomic():
        spec = node.spec()
    for parent in node.parents:
        spec = override_spec(spec, parent)

    return spec


def main(path):
    nodes: list[Node] = []
    targets: list[Node] = []
    for root, _, filename in os.walk(path):
        print(f"{root = }; {filename = }")
        for f in filename:
            if not f.endswith(".toml"):
                continue
            with open(os.path.join(root, f), "rb") as reader:
                i = toml.load(reader)
                if i["metadata"]["name"] not in [n.name for n in nodes]:
                    node = Node(i["metadata"]["name"])
                    node._config = i
                    nodes.append(node)

    for node in nodes:
        for parent in node._config["metadata"]["parents"]:
            for n in nodes:
                if n.name == parent:
                    n.children.append(node)
                    node.parents.append(n)

    #    breakpoint()
    for node in nodes:
        print(f"node: {node.name}")
        print(f"\tparents: {[a.name for a in node.parents]}")
        print(f"\tchildren: {[a.name for a in node.children]}")

    for node in nodes:
        if len(node.children) == 0:
            targets.append(node)

    print("-" * 50)
    results = {}
    for node in targets:
        a = node.spec()
        a = merge_spec(a, node)
        a = override_spec(a, node)
        results[node.name] = a

    pprint(results)


if __name__ == "__main__":
    root = sys.argv[1]
    main(root)
