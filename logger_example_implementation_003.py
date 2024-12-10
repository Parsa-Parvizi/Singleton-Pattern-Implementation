import logging
import threading

# Define a metaclass Singleton that inherits from type
class SingletonMeta(type):
    # Initialize a dictionary to store instances of the Singleton class
    _instances = {}
    # Initialize a lock to ensure thread-safe Singleton instantiation
    _lock = threading.Lock()

    # Override the __call__ method to control how the class is instantiated
    def __call__(cls, *args, **kwargs):
    # Acquire the lock to ensure thread safety
        with cls._lock:
        # If the class is not in the instances dictionary, create a new instance
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        # Return the existing or newly created instance of the class
        return cls._instances[cls]


# Define a LoggerSingleton class with Singleton as its metaclass
class Logger(metaclass=SingletonMeta):
    _logger = None

    def __init__(self):
        # Initialize the logger during object creation
        self._initialize_logger()

    # Method to initialize the logger 
    def _initialize_logger(self):
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
    
    # getter method
    def getLogger(self):
        return self._logger



# Usage
logger = Logger().getLogger()
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')