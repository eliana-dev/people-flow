import logging
import colorlog
import config

logger = logging.getLogger(config.LOG_NAME)
logger.setLevel(config.LOG_LEVEL)


# Formato con fecha en día/mes/año
stream_formatter = colorlog.ColoredFormatter(
    "%(asctime)s - %(log_color)s%(levelname)s%(reset)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    log_colors=config.LOG_COLORS,
)

# Handler para stdout / stderr
stream_handler = logging.StreamHandler()
stream_handler.setLevel(config.LOG_LEVEL)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)