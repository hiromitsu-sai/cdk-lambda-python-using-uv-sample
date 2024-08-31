from libs.log import logger


def main() -> str:
    msg = "Hello from test!"
    logger.info(msg)
    return msg


def handler(event, context):
    """Lambda handler."""
    return main()
