"""
=================================================
Author : Athena
Time : 2023/8/27 16:49 
=================================================
# """
import settings
from .log_handler import get_logger
from .config_handler import get_config
logger = get_logger(**settings.LOG_CONFIG)

