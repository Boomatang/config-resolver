# Config Resolver

This is a playground for testing defaults and overrides in configuration files.
The aim is to help give an understanding of defaults and overrides interact with each other.
Not only is there the defaults and overrides, there is also the merge and atomic strategies.  

There is also a third type which would be the direct attachment. 
This type is not covered here, as this should not be affected by other configurations.

In the examples folders there are a number of different scenarios that are covered.
each example has its own README explaining what scenario is being covered.

## Understanding the toml files.
For easy of use toml files are used to represent the configuration files and to outline their relationship.
There are three main field groups in the configuration. 

### metadata
```toml
[metadata]
name = "configuration name" # requied, should be unquie accross examples
parents = [] # at minimum, it most be an empty list, but can be a list of strings which match the names of the configuration files that  are regarded to be their parent.
```

### policyMetadata
```toml
[policyMetadata]
type = "default or override" # reuired
strategy = "merge or atomic" # reuired
```

### spec
```toml
[spec] # reuired
```
The `spec` section is required but what fields are there are flexable.
Have not tried the scripts with emtpy spec fields, so do that at your own risk.
The `spec` can have nested objects but can not have any list of objects.

## Running the examples
All the examples can be run at the same time doing the following.
```sh
python -m config_resolver examples
```

Single examples can be run by using that folder.
```sh
python -m config_resolver examples/example1
```
