# Example 5
These examples assume there can be multiple configurations at each level. 
It is true that these configurations should have a different type/strategy.
But what happens if there is conflicting types, override/merge and override/atomic.

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
  - sets `field_d` to `http override merge`.
  - sets `field_e` to `http override merge`.
  - type/strategy: override/merge
- route3.toml
  - sets `field_d` to `d`.
  - sets `field_e` to `http override atomic`.
  - type/strategy: override/atomic
- service.toml
    - sets `field_d` to `service default`.
    - sets `field_f` to `f`.
    - type/strategy: default/merge


## Current result
```json
{
  "field_d": "d",
  "field_e": "http override atomic"
}
```

## Note
I do not know how this should work. 
The first thing I want to point out is the order in which the configurations are being added is affecting which gets applied first.
The values from route2.toml are added before the atomic route3.toml changes.

The defaults from the gateway and gateway class are being dropped also because of the atomic override.