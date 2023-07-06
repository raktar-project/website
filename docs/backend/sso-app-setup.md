---
title: SSO Application Configuration
---

Now that you have the Cognito user pool ID, it's time to complete the SSO application setup
in IAM Identity Center.

Open the application in Identity Center that you created during the manual steps.
Under `Actions`, select `Edit configuration`. Scroll to the bottom and fill in the fields
under `Application metadata`.

Application ACS URL: 

```
https://<cognito_domain_prefix>.auth.<region>.amazoncognito.com/saml2/idpresponse
```

Application SAML audience:
```
urn:amazon:cognito:sp:<pool-id>
```

Submit the configuration.

Now go to `Edit attribute mappings` under `Actions`. Add a new mapping for `Subject`
with the value `${user:subject}` and Format `transient`. Add mappings for 
`given_name` and `family_name` as well (`${user:givenName}` and `${user:familyName}` respectively).
At the end, it should look like this:

![SAML attribute mappings](/assets/saml-attribute-mappings.png)

Save the changes.