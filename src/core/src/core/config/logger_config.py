import logging
from logging.config import dictConfig

from ..models.config import Settings
from wireup import service


@service
def create_logger(settings: Settings) -> logging.Logger:
    dictConfig(settings.logging)
    logger = logging.getLogger()
    logger.info("✅  Skonfigurowano logger")
    return logger
