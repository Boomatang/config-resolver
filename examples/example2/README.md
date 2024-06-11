# Example 2
In this example only defaults are being used.
At the route level the defaults are atomic. 
As there is a service below the route it would be expected that the route defaults will not be used.
But what of the defaults higher in the chain.

- gatewayclass.toml 
    - sets `field_a` to `a`. 
    - type/strategy: default/merge
- gateway.toml 
    - sets `field_b` to `b`. 
    - type/strategy: default/merge
- route1.toml 
    - sets `field_d` to `d`. 
    - sets `field_e` to `http default`.
    - type/strategy: default/atomic
- service.toml
    - sets `field_d` to `service default`.
    - type/strategy: default/merge


## Expected result
```json
{
  "field_a": "a",
  "field_b": "b",
  "field_d": "service default"
}
```
If there was no service.toml the expected result would be.
```json
{
  "field_a": "a",
  "field_b": "b",
  "field_d": "d",
  "field_e": "http default"
}
```

## Notes 
I am not sure if the expected result is correct in this case.
Should the defaults from gatewayclass.toml and gateway.toml be added to the output configuration?
