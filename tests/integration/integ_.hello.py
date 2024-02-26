import aws_cdk as cdk
from aws_cdk import (
    integ_tests_alpha,
)
from cdk_integ_runner_cwd_fix import fix_cwd

# This needs to be before any import from your CDK app to work around a bug in the CDK
fix_cwd()

from integration_tests_with_cdk_and_python.hello_world_stack import HelloWorldStack

app = cdk.App()
stack = HelloWorldStack(app, "HelloTestStack")

integration_test = integ_tests_alpha.IntegTest(app, "Integ", test_cases=[stack])

function_invoke = integration_test.assertions.invoke_function(
    function_name=stack.function.function_name,
)

function_invoke.expect(
    integ_tests_alpha.ExpectedResult.object_like(
        {"StatusCode": 200, "Payload": '"Hello real world"'}
    )
)

app.synth()
