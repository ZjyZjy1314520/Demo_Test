import os
import logging
base_url=r'G:\UI_Test\Demo_Test'
class Logger:
    def __init__(self,path=base_url+"/log/autotest.log",clever=logging.DEBUG,Flevel=logging.INFO):
        project_dir=os.listdir(base_url)
        dir_name='log'
        if dir_name not in project_dir:
            create_path = base_url + '/' + dir_name
            os.makedirs(create_path)
            file = open(create_path + '/Auto_Test.log', 'w', encoding='utf-8')
            file.close()
        # 创建logger
        self.logger=logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        #防止创建多个logger对象
        if not self.logger.handlers:
            #设置日志格式
            fmt=logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            #设置CMD日志
            sh=logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clever)
            #设置文件日志
            fh=logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

