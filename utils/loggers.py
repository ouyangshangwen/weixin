# coding=utf-8
import logging
import logging.handlers

from configs import AppSettings

logs_path = AppSettings.PROJECTPATH + "/logs"


def setup_logger(logs_name, level=None):
    """
    配置日志.

    :param logs_name: 日志名称
    :param level: 日志级别
    :return:
    """

    format_src = '%(asctime)s - %(filename)s:%(lineno)s - %(module)s - %(funcName)s - %(message)s'
    loggerFilePath = AppSettings.PROJECTPATH + '/logs/%s.log' % logs_name  # 设置日志文件路径

    # 实例化handler
    handler = logging.handlers.RotatingFileHandler(loggerFilePath, maxBytes=1024 * 1024, backupCount=10)
    formatter = logging.Formatter(format_src)  # 实例化formatter
    handler.setFormatter(formatter)  # 为handler添加formatter
    LOGGER = logging.getLogger(logs_name)
    LOGGER.addHandler(handler)  # 为logger添加handler

    if level and level in ["info", "warning", "warn", "debug", "error", "notset"]:
        logger_level = getattr(logging, level.upper())
        LOGGER.setLevel(logger_level)
    else:
        LOGGER.setLevel(logging.DEBUG)

    return LOGGER


logs_general = setup_logger("general", 'debug')
