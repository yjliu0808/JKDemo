"""
=================================================
Author : Athena
Time : 2023/8/29 20:22 
=================================================
"""
import unittest
from configparser import ConfigParser
import yaml
from BeautifulReport import BeautifulReport


def get_config(filename,encoding='utf-8') -> dict:
    #获取文件后缀名
    suffix = filename.split('.')[-1]
    #判断这个配置文件类型
    if suffix in ['ini','cnf','conf']:
        # ini配置
        conf = ConfigParser()
        conf.read(filename,encoding = encoding)
        data ={}
        for section in conf.sections() :
            data[section] = dict(conf.items(section))

    elif suffix in ['yml','yaml']:
        # yaml 配置
        with open (filename,'r',encoding = encoding) as f:
            data  = yaml.load(f,Loader=yaml.FullLoader)
    else :
        raise ValueError('不能识别配置文件的后缀')
    return data
class Config:
    def __init__(self,filename,encoding='utf-8'):
        # 初始化
        self.filename = filename
        self.encoding = encoding
        self.suffix = filename.split('.')[-1]
        if self.suffix not in ['ini', 'cnf', 'conf','yml', 'yaml']:
            raise ValueError('不能识别配置文件的后缀')
    def __parse_ini(self):
        # ini配置
        conf = ConfigParser()
        conf.read(self.filename, encoding=self.encoding)
        data = {}
        for section in conf.sections():
            data[section] = dict(conf.items(section))
        return data
    def __parse_yaml(self):
        # yaml 配置
        with open(self.filename, 'r', encoding=self.encoding) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    def parse(self):
        if self.suffix in ['yml','yaml']:
            return self.__parse_yaml()
        else:
            return self.__parse_ini()
if __name__ == '__main__':
    ts = unittest.TestLoader().discover('testcases')
    br = BeautifulReport(ts)
    # config = Config('../config.yaml')
    # br.report(**config['report'])
    # print(data)
    # config = get_config('../config.yaml')
    # print(config['log']['name'])
