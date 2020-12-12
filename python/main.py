import requests
from src import logging_setup
from src.simple_math import SimpleMath
import logging


if __name__ == "__main__":
    # logging_setup.init_logs()
    logging_setup.init_dict_config()
    logger = logging.getLogger(__name__)
    logger.info("HELLO WORLD!")

    output = requests.get("https://api.github.com")
    logger.warning(output)

    simple_math_obj = SimpleMath()
    simple_math_obj.add(5, 10)
