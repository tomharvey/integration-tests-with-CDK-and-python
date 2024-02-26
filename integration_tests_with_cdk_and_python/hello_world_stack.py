import os

from aws_cdk import (
    Stack,
    aws_lambda,
)
from constructs import Construct


class HelloWorldStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.function = aws_lambda.Function(
            self,
            "MyFunction",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=aws_lambda.Code.from_asset(f"{os.getcwd()}/lambda"),
        )
