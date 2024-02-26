import aws_cdk as core
import aws_cdk.assertions as assertions

from integration_tests_with_cdk_and_python.integration_tests_with_cdk_and_python_stack import IntegrationTestsWithCdkAndPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in integration_tests_with_cdk_and_python/integration_tests_with_cdk_and_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IntegrationTestsWithCdkAndPythonStack(app, "integration-tests-with-cdk-and-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
