"""
=================================================
Author : Athena
Time : 2023/8/27 14:55 
=================================================
"""
import logging
def get_logger(name,filename,mode = 'a',encoding = 'utf-8',fmt=None,debug=False):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.INFO
    if fmt is None:
        fmt = '%(asctime)s - %(filename)s - line%(lineno)s - > %(levelname)s : %(message)s'
    file_handler = logging.FileHandler(filename=filename)
    file_handler.setFormatter(file_level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    formatter = logging.Formatter(fmt=fmt)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


if __name__ == '__main__':
    logger  = get_logger(name='mall',filename='../logs/mall.log',debug=True)
    logger.info("A")
    # config = get_config('config.yaml')
    # # logger = get_logger('mall', 'logs/mall.log', debug=False)
    # logger = get_logger(name=config['log']['name'], filename='logs/mall.log', debug=False)
    # logger.info("A")