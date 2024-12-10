from abc import ABC, ABCMeta, abstractmethod
import logging
import os
import datetime
import threading

class SingletonMeta(metaclass=ABCMeta):
    _instances = {}
    # Initialize a lock to ensure thread-safe Singleton instantiation
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Acquire the lock to ensure thread safety
        with cls._lock:
            print('<SingletonMeta> in the _call_...')
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass
    @abstractmethod
    def info(cls, message: str):
        pass
    @abstractmethod
    def warning(cls, message: str):
        pass
    @abstractmethod
    def error(cls, message: str):
        pass
    @abstractmethod
    def critical(cls, message: str):
        pass

class MyLogger(BaseLogger):

    def __init__(self):
        print('<Logger init> initializaing logger...')
        # Create a logger object with the specified name
        self._logger = logging.getLogger('my_logger')
        # Set the logging level to DEBUG
        self._logger.setLevel(logging.DEBUG)

        # Create a file handler to log messages to a file
        file_handler = logging.FileHandler('my_log_file.log')
        # Set the file handler logging level to DEBUG
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler to log messages to the console
        console_handler = logging.StreamHandler()
        # Set the console handler logging level to INFO
        console_handler.setLevel(logging.INFO)

        # Define the log message format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Set the formatter for both the file and console handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the file and console handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)


logger = MyLogger()
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
