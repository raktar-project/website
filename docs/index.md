Serverless Private Cargo Registry
=================================

Raktar is a private, self-hosted Cargo registry designed around
the use of serverless AWS solutions to minimise operational costs.
It is particularly suited for organisations already utilising AWS,
and who possess sufficient familiarity with the AWS ecosystem
to deploy the service using the [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/).

Users of the frontend application are authenticated through AWS IAM Identity Center.
While future updates may bring compatibility with other solutions,
the current requirement for the frontend is user provisioning via IAM Identity Center.

!!! warning 
    Raktar is work in progress. You are welcome to try it, but the installation steps are incomplete
    and the code is under heavy development.

## Overview

Raktar is composed of two primary components: a backend, written in Rust,
and a frontend, constructed with a conventional Typescript and React stack.

The core functionality of Raktar resides entirely within the backend,
rendering it technically possible to use the service independently of the frontend application. 
However, opting out of the frontend would mean missing out on handy features. 
These include a web UI for efficient search and viewing of crates, as well as streamlined token management.

Raktar is entirely open-source and free of charge, provided under the MIT license.

### The Backend Service

Repository: [Raktar Core](https://github.com/raktar-registry/raktar)

The backend is structured as a serverless API, implemented in Rust,
which operates on Lambda and is made accessible via AWS HTTP API Gateway.
It employs S3 for crate storage and AWS DynamoDB for the retention of application data.

This infrastructure means that the service costs close to nothing when it's not heavily used.

### The Frontend Application

Repository: [Raktar Frontend](https://github.com/raktar-registry/raktar-app)

The frontend is written using common frontend technologies, such as TypeScript, React
and [URQL](https://formidable.com/open-source/urql/).

The frontend is hosted on AWS S3, and it's served through CloudFront.

## Getting Started

The backend and the frontend can be separately installed using
[AWS CDK](https://aws.amazon.com/cdk/).
There are detailed instructions for both.

In order to install the backend, head over to [Backend Installation](/backend).

In order to install the frontend, header over to [Frontend Installation](/frontend).