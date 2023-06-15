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

The Raktar backend is meant to be hosted on a different subdomain than the frontend.
For example, if you're planning to host the frontend application at `crates.your-domain.com`,
then you may want to host the backend at `api.crates.your-domain.com`.

Create a new `.env` file inside the `infrastructure` folder with the following contents:

```dotenv
DOMAIN_NAME=api.crates.<your-domain>.com
HOSTED_ZONE_DOMAIN_NAME=<your-domain>.com
SSO_METADATA_URL=<metadata file URL from the manual steps>
```

Feel free to tailor the domain and hosted zone domain to your needs.

## Deployment

Run `cdk deploy` either with the virtualenv activated or using `poetry run`.

```shell
poetry run cdk deploy
```