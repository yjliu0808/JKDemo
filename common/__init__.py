"""
=================================================
Author : Athena
Time : 2023/8/27 16:49 
=================================================
# """
import settings
from .log_handler import get_logger
from .config_handler import get_config
# config = get_config('config.yaml')
# logger = get_logger('mall','logs/mall.log',debug=False)
# logger = get_logger(name=config['log']['name'],filename=config['log']['filename'],debug=config['log'['debug']])
# logger = get_logger(**config['log'])
logger = get_logger(**settings.LOG_CONFIG)

