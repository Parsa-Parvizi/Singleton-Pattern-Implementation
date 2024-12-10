"""
Question 2:
create a singleton implementation which will write to a common file.
a. imagine that you wanted to audit all the actions in your application.
b. it would make sense to log that into a file with a gyarantee that all callers will write to the same file. (make the file configurable)
i. for each call to the FileAuditManger your code will generate a timestamp and will write the message entry into the file with a newline charcter at the end of each message.
make that implementaion both with eager-instantiation and with lazy-instantiation.
a. which one would you prefer to use and why?
make your implementation thread-safe.
"""

import threading
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class EagerFileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, log_file='audit.log'):
        if cls._instance is None:
            logging.debug("Creating EagerFileAuditManager instance.")
            cls._instance = super(EagerFileAuditManager, cls).__new__(cls)
            cls._instance.log_file = log_file
            cls._instance._initialize_file()
        return cls._instance

    @classmethod
    def _initialize_file(cls):
        try:
            with open(cls._instance.log_file, 'a') as f:
                f.write("=== Audit Log Initialized ===\n")
        except Exception as e:
            logging.error(f"Failed to initialize log file: {e}")

    def log_action(self, message):
        timestamp = datetime.now().isoformat()
        log_entry = f"{timestamp} - {message}\n"
        with self._lock:
            try:
                with open(self.log_file, 'a') as f:
                    f.write(log_entry)
                logging.debug(f"Logged action: {log_entry.strip()}")
            except Exception as e:
                logging.error(f"Failed to write to log file: {e}")


class LazyFileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, log_file='audit.log'):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    logging.debug("Creating LazyFileAuditManager instance.")
                    cls._instance = super(LazyFileAuditManager, cls).__new__(cls)
                    cls._instance.log_file = log_file
                    cls._instance._initialize_file()
        return cls._instance

    @classmethod
    def _initialize_file(cls):
        try:
            with open(cls._instance.log_file, 'a') as f:
                f.write("=== Audit Log Initialized ===\n")
        except Exception as e:
            logging.error(f"Failed to initialize log file: {e}")

    def log_action(self, message):
        timestamp = datetime.now().isoformat()
        log_entry = f"{timestamp} - {message}\n"
        with self._lock:
            try:
                with open(self.log_file, 'a') as f:
                    f.write(log_entry)
                logging.debug(f"Logged action: {log_entry.strip()}")
            except Exception as e:
                logging.error(f"Failed to write to log file: {e}")


def main():
    try:
        # Eager Singleton Usage
        eager_audit_manager = EagerFileAuditManager('eager_audit.log')
        eager_audit_manager.log_action("Eager instance action 1")
        eager_audit_manager.log_action("Eager instance action 2")

        another_eager_audit_manager = EagerFileAuditManager('eager_audit.log')
        another_eager_audit_manager.log_action("Eager instance action 3")

        # Lazy Singleton Usage
        lazy_audit_manager = LazyFileAuditManager('lazy_audit.log')
        lazy_audit_manager.log_action("Lazy instance action 1")
        lazy_audit_manager.log_action("Lazy instance action 2")

        another_lazy_audit_manager = LazyFileAuditManager('lazy_audit.log')
        another_lazy_audit_manager.log_action("Lazy instance action 3")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
