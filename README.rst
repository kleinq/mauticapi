MauticAPI
---------

*** Caution ***
This is work under construction
***************

To use:

```python
from mauticapi.mautic import MauticApi

api = MauticApi(
    host, 
    public, 
    secret, 
    **{"access_token":access_token, "access_token_secret":access_token_secret})

api.create_lead(**dict_of_lead_data_using_mautic_lead_field_names)
```
