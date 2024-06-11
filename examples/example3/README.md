# Example 3
This example is to show what happens when the children configuration is not set but there is an atomic default configuration.
There is also an atomic default higher in the stack. 

- gatewayclass.toml 
    - sets `field_a` to `a`. 
    - type/strategy: default/merge
- gateway.toml 
    - sets `field_b` to `gateway default`. 
    - type/strategy: default/atomic
- route1.toml 
    - sets `field_d` to `d`. 
    - sets `field_e` to `http default`.
    - type/strategy: default/merge
- service.toml
    - sets `field_d` to `service default`.
    - type/strategy: default/atomic


## Expected result
```json
{
  "field_a": "a",
  "field_d": "service default",
  "field_e": "http default"
}
```

## Note
I am not sure if this is the expected output should be. 