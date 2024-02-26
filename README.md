# Integration tests with CDK and Python

To serve as a guide to using integ-runner with your Python CDK projects.

The code to support blog posting on dev.to https://dev.to/tomharvey/integration-tests-with-cdk-and-python-is-my-cloud-native-app-doing-what-i-want-2805


## Setup

This has a .devcontainer folder to allow you to use the Remote - Containers extension in VSCode to develop in a container.
If you make use of this, you use the VS COde DevContainers extension to open the project in a container.

You'll need to authenticate with AWS in your preferred manner; either using an IAM key, or better, using aws-sso-util
to assume a role through the IAM Identity Center.

## Running the tests

To run the tests, you can use the following command:

```bash

integ-runner --update-on-failed

```

And, you should see the following output:

```bash

Verifying integration test snapshots...

  NEW        integ_.hello 8.644s

Snapshot Results: 

Tests:    1 failed, 1 total
Failed: /workspaces/integration-tests-with-CDK-and-python/test/integ_.hello.py

Running integration tests for failed tests...

Running in parallel across regions: us-east-1, us-east-2, us-west-2
Running test /workspaces/integration-tests-with-CDK-and-python/test/integ_.hello.py in us-east-1
  SUCCESS    integ_.hello-Integ/DefaultTest 193.543s
       AssertionResultsLambdaInvoke24cf31b9b6a07a940ece1b49bb7eb7b2 - success

Test Results: 

Tests:    1 passed, 1 total
```

