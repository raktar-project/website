---
title: Pre-requisites
---

# Preparations

Clone the frontend project:

```shell
git clone git@github.com:raktar-registry/app.git
```

Install the application dependencies by running

```shell
npm install
```

in the project's root directory.

## Create the .env file

Create an `.env` file in `env/`. This file should contain the following variables:

```dotenv
VITE_HOSTED_ZONE_DOMAIN=<same as the backend's hosted zone>
VITE_AWS_REGION=<the region Cognito is in>
VITE_AWS_USER_POOL_ID=<generated during backend deployment>
VITE_AWS_USER_POOL_CLIENT_ID=<generated during backend deployment>
```

## Build the bundle

Run `npm run build` in the root directory - this will generate the
static files in `dist/`.

## Deploy the application

Within the `infrastructure/` directory, run

```shell
cdk deploy --all
```
