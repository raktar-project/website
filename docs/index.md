Serverless Private Cargo Registry
=================================

Raktar is a private, self-hosted [Cargo registry](https://doc.rust-lang.org/cargo/reference/registries.html)
designed around the use of serverless AWS solutions to minimise operational costs.
It is particularly suited for organisations already utilising AWS,
and who possess sufficient familiarity with the AWS ecosystem
to deploy the service using the [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/).

Users of the frontend application are authenticated through AWS IAM Identity Center.
While future updates may bring compatibility with other solutions,
the current requirement for the frontend is user provisioning via IAM Identity Center.

!!! warning 
    Raktar is work in progress. The core registry logic is functional,
    but the installation steps may not always be up-to-date. If you have
    any issues getting started or would like to request new features,
    please raise a [GitHub issue](https://github.com/raktar-project/raktar/issues).

## Overview

Raktar is composed of two primary components: a backend, written in Rust,
and a frontend, implemented as a standard Typescript and React SPA.

The core functionality of Raktar resides entirely within the backend,
rendering it technically possible to use the service independently of the frontend application. 
However, opting out of the frontend would mean missing out on handy features. 
These include a web UI for efficient search and viewing of crates, as well as streamlined token management.

Raktar is entirely open-source and free of charge, provided under the MIT license.

Features:

- [x] Core functionality of an [alternative Cargo registry](https://doc.rust-lang.org/cargo/reference/registries.html#using-an-alternate-registry).
    * [x] Publishing crates.
    * [x] Downloading crates.
    * [x] Authentication using tokens.
    * [x] Support for [sparse registries](https://doc.rust-lang.org/cargo/reference/registries.html#registry-protocols).
    * [ ] Stable Rust - this will be available when [registry auth](https://github.com/rust-lang/cargo/issues/10474)
      is [stabilised](https://github.com/rust-lang/cargo/issues/8933#issuecomment-1711990123).
    * [ ] Support for [Git-based registries](https://doc.rust-lang.org/cargo/reference/registries.html#registry-protocols).
      There is no plan to support this.
- [x] Web UI.
    * [x] Single Sign-On (SSO) authentication for the application.
    * [x] Self-managed authentication tokens through the UI.
    * [x] Searching crates.
    * [x] Showing crate details, 
- [ ] [crates.io](https://crates.io/) mirroring.
- [ ] Hosted documentation, generated using [cargo doc](https://doc.rust-lang.org/cargo/commands/cargo-doc.html).


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

In order to install the backend, head over to [Backend Installation](/backend/pre-requisites).

In order to install the frontend, header over to [Frontend Installation](/frontend/pre-requisites).