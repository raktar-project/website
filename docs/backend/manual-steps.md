---
title: Manual Steps
---

# Manual Steps

There are two things you'll need to do manually before the automated CDK deployment.

## Creating a Public Hosted Zone

If you don't have a public hosted zone already for your domain name, create one on Route 53.

This step is not automated through the CDK stack as you may already have a hosted zone
for your domain. Raktar will be deployed on the `crates` sub-domain, leaving your primary domain
free to use for something else.

!!! info
    Take note of the hosted zone ID, you'll need this later.

## Creating an Application in IAM Identity Center

A SAML-based application in IAM Identity Center will be used for Single Sign-On (SSO)
authentication.

Add a new custom SAML 2.0 application. Give it a meaningful display name and description.

![SAML application configuration](/assets/saml-app-configuration.png)

!!! info
    Take note of the IAM Identity Center SAML metadata file, you'll need this later.

The rest of the fields on this page are not possible to fill in until we've deployed
the CDK stack. However, it won't let you continue without specifying the ACS URL
and the SAML audience, so put in some dummy values.

![SAML application configuration](/assets/saml-app-metadata-dummy.png)

Submit the form to create the application.