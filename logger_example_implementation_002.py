import logging
import threading

# Define a SingletonLogger class
class SingletonLogger:
    # Initialize the class-level instance variable to None
    _instance = None
    # Initialize a lock to ensure thread-safe Singleton instantiation
    _lock = threading.Lock()

    # Class method to get the SingletonLogger instance
    @classmethod
    def get_instance(cls):
        # Acquire the lock to ensure thread safety
        with cls._lock:
            # If an instance of SingletonLogger does not exist, create one
            if cls._instance is None:
                cls._instance = cls()
                # Initialize the logger for the SingletonLogger instance
                cls._instance._initialize_logger()
            # Return the existing or newly created SingletonLogger instance
            return cls._instance

    # Helper method to initialize the logger
    def _initialize_logger(self):
        # Create a logger object with the specified name
        self.logger = logging.getLogger('my_logger')
        # Set the logging level to DEBUG
        self.logger.setLevel(logging.DEBUG)

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
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

# Usage
logger = SingletonLogger.get_instance().logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
