import logging
from logging.config import dictConfig

from wireup import injectable

from ..models.config import Settings


@injectable
def create_logger(settings: Settings) -> logging.Logger:
    dictConfig(settings.logging)
    logger = logging.getLogger()
    logger.info("✅  Skonfigurowano logger")
    return logger
