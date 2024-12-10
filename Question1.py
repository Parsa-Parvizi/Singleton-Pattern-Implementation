"""
question:
create a singleton implementation which will generate a sequence of numbers to the callers.
a. the idea here is that there is only a single number/sequence generator and all the number follow a perfect sequence.
b. so when we do a call to the generator using something like getNextNumber() we should get the next number in the sequence no matter how we obtained the generator.
make that implementation both with eager-instantiation and with lazy-instantiation.
"""


import threading
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class EagerSingletonNumberGenerator:
    _instance = None
    _current_number = 0
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            logging.debug("Creating EagerSingletonNumberGenerator instance.")
            cls._instance = super(EagerSingletonNumberGenerator, cls).__new__(cls)
        return cls._instance

    def get_next_number(self):
        with self._lock:
            self._current_number += 1
            logging.debug(f"Next number generated: {self._current_number}")
            return self._current_number


class LazySingletonNumberGenerator:
    _instance = None
    _current_number = 0
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    logging.debug("Creating LazySingletonNumberGenerator instance.")
                    cls._instance = super(LazySingletonNumberGenerator, cls).__new__(cls)
        return cls._instance

    def get_next_number(self):
        with self._lock:
            self._current_number += 1
            logging.debug(f"Next number generated: {self._current_number}")
            return self._current_number


def main():
    try:
        # Eager Singleton Usage
        eager_generator = EagerSingletonNumberGenerator()
        print(eager_generator.get_next_number())  # Output: 1
        print(eager_generator.get_next_number())  # Output: 2

        another_eager_generator = EagerSingletonNumberGenerator()
        print(another_eager_generator.get_next_number())  # Output: 3

        # Lazy Singleton Usage
        lazy_generator = LazySingletonNumberGenerator()
        print(lazy_generator.get_next_number())  # Output: 1
        print(lazy_generator.get_next_number())  # Output: 2

        another_lazy_generator = LazySingletonNumberGenerator()
        print(another_lazy_generator.get_next_number())  # Output: 3

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
