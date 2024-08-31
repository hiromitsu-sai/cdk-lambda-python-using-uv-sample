import os

import aws_cdk as cdk
from aws_cdk import Environment

from cdk_stacks.lambda_stack import LambdaStack

STACK_NAME = "try-migrating-pyenv2uv"
app = cdk.App()

# Stageごとに環境変数を読み込む
if app.node.try_get_context("env"):
    env_key = app.node.try_get_context("env")
else:
    env_key = "dev"
env_vars = app.node.try_get_context(env_key)
env = Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
)
LambdaStack(app, STACK_NAME, env=env)

app.synth()
