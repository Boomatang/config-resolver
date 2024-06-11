# Example 1
This examples uses the defaults and overrides in a merge fashion.

- gatewayclass.toml 
    - sets `field_a` to `a`. 
    - type/strategy: default/merge
- gateway.toml 
    - sets `field_b` to `b`. 
    - type/strategy: default/merge
- route1.toml 
    - sets `field_d` to `d`. 
    - sets `field_e` to `http default`.
    - type/strategy: default/merge
- route2.toml
    - sets `field_e` to `http override`.
    - type/strategy: override/merge
- service.toml
    - sets `field_d` to `service default`.
    - sets `field_e` to `e`.
    - type/strategy: default/merge


## Expected result
```json
{
  "field_a": "a",
  "field_b": "b",
  "field_d": "service default",
  "field_e": "http override"
}
```