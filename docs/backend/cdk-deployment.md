---
title: CDK Deployment
---

# CDK Deployment

## Preparations

Clone the backend project:

```shell
git clone git@github.com:raktar-registry/raktar.git
```

Install the Python dependencies by running

```shell
poetry install
```

in the project's root directory. This will create a virtualenv in the same directory.

## Configure the Deployment

Raktar is hosted on sub-domains following a pre-defined naming convention.
All you need to provide is the parent hosted zone. The frontend application
will be hosted at `crates.{parent_hosted_zone}` and the API will be served at
`api.crates.{parent_hosted_zone}`.

Apart from the parent hosted zone domain, you'll also need the SSO metadata
URL from the manual steps and a custom Cognito domain prefix that's not
used by someone else yet.

Create a new `.env` file inside the `infrastructure` folder with the following contents:

```dotenv
HOSTED_ZONE_DOMAIN_NAME=<your-domain>.com
SSO_METADATA_URL=<metadata file URL from the manual steps>
COGNITO_DOMAIN_PREFIX=<unique prefix>
```

The Cognito domain prefix can be anything, but you need to find a unique prefix.

## Deployment

Run `cdk deploy` either with the virtualenv activated or using `poetry run`.

```shell
poetry run cdk deploy
```