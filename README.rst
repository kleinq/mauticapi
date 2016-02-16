===========
 MauticAPI 
===========

** Caution **
This is work under construction
***************

To use::

    from mauticapi.mautic import MauticApi

    api = MauticApi(
        host, 
        public, 
        secret, 
        **{"access_token":access_token, "access_token_secret":access_token_secret})

    api.create_lead(**dict_of_lead_data_using_mautic_lead_field_names)


This also includes a utility functions to retrieve Mautic OAuth1.0A access token, from the command line::

1) Initialize MauticApi (m = MauticApi(host, public, secret))
2) Call request_and_authorize, and go to the returned URL in your browser (m.request_and_authorize())
3) Approve the application
4) Call get_access_token passing the oauth_verifier parameter (m.get_access_token(verifier))
5) Get the access token from access_token (m.access_token)
6) Get the access token secret from access_token_secret (m.access_token_secret)
