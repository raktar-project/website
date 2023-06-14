#!/usr/bin/env python3
import aws_cdk as cdk

from stack import StaticWebsiteStack


app = cdk.App()
StaticWebsiteStack(app, "RaktarWebsite")

app.synth()
