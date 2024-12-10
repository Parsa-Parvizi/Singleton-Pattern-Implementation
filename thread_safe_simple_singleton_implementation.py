import threading

class ThreadSafeSingleton:
    _instance = None  # class-level variable to store the single instance of the class
    _lock = threading.Lock()  # class-level lock to ensure thread safety

    def __new__(cls):  # override the __new__ method to create the single instance of the class in a thread-safe way
        with cls._lock:  # acquire the lock to ensure thread safety
            if not cls._instance:  # check if the single instance of the class has been created yet
                cls._instance = super().__new__(cls)  # create the single instance of the class
        return cls._instance  # return the single instance of the class
    


s1 = ThreadSafeSingleton()
s2 = ThreadSafeSingleton()

print(s1 is s2)  # Output: True