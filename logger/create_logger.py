import logging.config


def create_logger(config):
    logging.config.dictConfig(config["logger"]["logging"])
    return logging.getLogger("api")
