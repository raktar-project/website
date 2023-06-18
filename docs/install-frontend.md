---
title: Installation (Frontend)
---

Installation
============


## Adding Raktar to IAM Identity Center

### Metadata
Display name: Cargo Registry
Description: A private Cargo registry.

Application start URL: the URL to the application

Application metadata
Application ACS URL: https://<domain>.auth.<region>.amazoncognito.com/saml2/idpresponse
Application SAML audience: urn:amazon:cognito:sp:<pool-id>

### Attribute mappings

Subject: ${user:subject} (transient)