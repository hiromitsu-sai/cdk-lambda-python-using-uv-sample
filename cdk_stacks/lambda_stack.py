from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class LambdaStack(Stack):
    """Invoice Checker Stack"""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.stage = self.node.try_get_context("env")
        _lambda.DockerImageFunction(
            scope=self,
            id=f"{self.stack_name}-lambda-{self.stage}",
            function_name=f"{self.stack_name}-lambda-{self.stage}",
            code=_lambda.DockerImageCode.from_image_asset(
                directory=".", cmd=["hello.handler"]
            ),
        )
