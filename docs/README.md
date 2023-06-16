Serverless Private Cargo Registry
=================================

Raktar is a self-hosted private Cargo registry built on top of serverless AWS solutions
to minimise costs. It's suitable for organisations who are already on AWS and familiar
enough with the ecosystem to install the service using
[AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/).

Users of the frontend application are authenticated using AWS IAM Identity Center.
There may be other solutions Raktar will support in the future, but for now,
having users provisioned in IAM Identity Center is a pre-requisite for the frontend.

{% warning Warning! %}

Raktar is work in progress. You are welcome to try it, but the installation steps are incomplete
and the code is under heavy development.

{% end %}


## Overview

Raktar is split into two distinct parts - the backend written in Rust, and the frontend
leveraging a traditional Typescript and React stack.

The core functionality is entirely on the backend, and it's technically possible to use
it without the frontend application. However, you'd be missing out on convenient features,
such as a web UI for searching and viewing crates and token management.

Raktar is entirely open-source and free (MIT license).

### The Backend Service

Repository: [Raktar Core](https://github.com/raktar-registry/raktar)

The backend consists of a serverless API written in Rust, running on Lambda and exposed through
AWS HTTP API Gateway. It uses S3 to store crates and AWS DynamoDB to store application data.

This infrastructure means that the service costs close to nothing when it's not heavily used.

### The Frontend Application

Repository: [Raktar Frontend](https://github.com/raktar-registry/raktar-app)

The frontend is written using common frontend technologies, such as TypeScript, React
and [URQL](https://formidable.com/open-source/urql/).

The frontend is hosted on AWS S3 and it's served through CloudFront.

## Getting Started

The backend and the frontend can be separately installed using
[AWS CDK](https://aws.amazon.com/cdk/).
There are detailed instructions for both.

In order to install the backend, head over to [Backend Installation](/backend).

In order to install the frontend, header over to [Frontend Installation](/frontend).