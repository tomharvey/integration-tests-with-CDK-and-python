#!/usr/bin/env python3

import aws_cdk as cdk

from integration_tests_with_cdk_and_python.hello_world_stack import HelloWorldStack

app = cdk.App()
HelloWorldStack(
    app,
    "HelloWorldStack",
)

app.synth()
