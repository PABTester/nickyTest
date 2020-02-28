#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = 'ljg logging'
__author__ = 'ljg'
__mtime__ = '20190401'


import logging
import colorlog
import os
from logging.handlers import TimedRotatingFileHandler


class Logger:

    def __init__(self, clevel=logging.INFO, Flevel=logging.INFO):
        if not os.path.exists('logs'):
            os.mkdir('logs')
        self.logger = logging.Logger(__name__)  # logging.getLogger('log')

        fmt_sh = colorlog.ColoredFormatter('%(log_color)s%(asctime)s[%(levelname)-7s][%(module)s:%(lineno)04d]%(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt_sh)
        sh.setLevel(clevel)

        # 设置文件日志
        # fh = logging.FileHandler(logfile_dir + '/log.log', 'a', encoding='utf-8')

        # 每天凌晨,备份之前的记录
        fh = TimedRotatingFileHandler(filename="logs/log", when="MIDNIGHT", interval=1, backupCount=30)
        fh.suffix = "%Y-%m-%d.log"  # 此格式必须与上面when对应,否则无法实现backcount设置的保留删除功能
        # fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        # fh.suffix = "%Y-%m-%d_%H-%M.log"
        # fh.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
        fmt = logging.Formatter('%(asctime)s[%(levelname)-7s][%(module)s:%(lineno)04d]%(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

        self.info = self.logger.info
        self.debug = self.logger.debug
        self.war = self.logger.warning
        self.error = self.logger.error
        self.cri = self.logger.critical


def main():
    log = Logger(logging.INFO)
    while True:
        log.info('test')
        log.war('test')
        log.error('test')


if __name__ == '__main__':
    main()
