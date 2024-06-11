# Example 6
These examples assume there can be multiple configurations at each level. 
It is true that these configurations should have a different type/strategy.
But what happens if there is conflicting types, default/merge and default/atomic.

- gatewayclass.toml 
    - sets `field_a` to `a`. 
    - type/strategy: default/merge
- gateway.toml 
    - sets `field_b` to `b`. 
    - type/strategy: default/merge
- route1.toml 
    - sets `field_d` to `d`. 
    - sets `field_e` to `http default merge`.
    - type/strategy: default/merge
- route2.toml
  - sets `field_d` to `http default atomic`.
  - sets `field_e` to `http default atomic`.
  - type/strategy: default/atomic
- service.toml
    - sets `field_d` to `service default`.
    - type/strategy: default/merge


## Current result
```json
{
  "field_a": "a",
  "field_b": "b",
  "field_d": "service default",
  "field_e": "http default merge"
}
```

## Note
As there is a lower configuration than the route2.toml the atomic defaults are ignored. 
If the two route configurations were to be on the same level I am not sure what the expected outcome should be.
In the current implementation of the script it would give two configuration objects which would not be correct.