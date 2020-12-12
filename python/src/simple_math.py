import logging

logger = logging.getLogger(__name__)


class SimpleMath:
    def __init__(self):
        pass

    def add(self, num1: int, num2: int) -> int:
        sum1 = num1 + num2
        logger.info("{} + {} = {}".format(num1, num2, sum1))
        logger.error("IF ANY ERRORS HAPPEN IN add() FUNCTION")
        return sum1
