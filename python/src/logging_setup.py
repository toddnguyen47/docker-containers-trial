import logging
import logging.config
import yaml


def init_dict_config():
    with open("logger_setup.yaml", "r") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    logging.config.dictConfig(data)


def init_logs_with_python():
    """Initialize the logger that will be used throughout the application.
    """
    # Create logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.NOTSET)

    # Formatter for all levels
    # Ref: https://stackoverflow.com/a/13733863/6323360
    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)-8s] %(message)s [%(filename)s] [%(threadName)s]",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create file handler for all levels
    file_handler_all_levels = logging.FileHandler(
        "{}/{}.log".format("logs", "all_levels"))
    file_handler_all_levels.setLevel(logging.DEBUG)
    file_handler_all_levels.setFormatter(formatter)
    root_logger.addHandler(file_handler_all_levels)

    # Create file handler for errors or higher
    file_handler_errors = logging.FileHandler(
        "{}/{}.log".format("logs", "errors"))
    file_handler_errors.setLevel(logging.ERROR)
    file_handler_errors.setFormatter(formatter)
    root_logger.addHandler(file_handler_errors)

    # Console for DEBUG or higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
