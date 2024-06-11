# Example 4
In this example only defaults are being used.
At the route level the defaults are atomic. 
As there is a service below the route it would be expected that the route defaults will not be used.
But what of the defaults higher in the chain.

- gatewayclass.toml 
    - sets `field_a` to `a`. 
    - type/strategy: default/merge
- gatewayclass2.toml
  - sets `field_a` to `gateway class override`.
  - type/strategy: override/merge
- gateway.toml 
    - sets `field_b` to `b`. 
    - type/strategy: default/merge
- route1.toml 
    - sets `field_d` to `d`. 
    - sets `field_e` to `http override`.
    - type/strategy: override/atomic
- service.toml
    - sets `field_d` to `service default`.
    - sets `field_f` to `f`.
    - type/strategy: default/merge


## Expected result
```json
{
  "field_a": "gateway class override",
  "field_d": "d",
  "field_e": "http override"
}
```

## Note
In this example all the defaults were dropped as there was one atomic override in the chain.
I don't know if this is the expected behaviour. 
