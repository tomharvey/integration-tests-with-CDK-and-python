import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda,
    integ_tests_alpha,
)
from constructs import Construct


class HelloTestStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.function = aws_lambda.Function(
            self,
            "MyFunction",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=aws_lambda.Code.from_asset("./lambda"),
        )


app = cdk.App()
stack = HelloTestStack(app, "HelloTestStack")

integration_test = integ_tests_alpha.IntegTest(app, "Integ", test_cases=[stack])

function_invoke = integration_test.assertions.invoke_function(
    function_name=stack.function.function_name,
)

function_invoke.expect(
    integ_tests_alpha.ExpectedResult.object_like(
        {"StatusCode": 200, "Payload": '"Hello world"'}
    )
)

app.synth()
