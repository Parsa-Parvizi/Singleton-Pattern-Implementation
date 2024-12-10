import threading

# Define a metaclass SingletonMeta that inherits from type
class ThreadSafeSingleton(type):
    _instances = {}
    _lock = threading.Lock()

    # Override the __call__ method to control how the class is instantiated
    def __call__(cls, *args, **kwargs):
        # Acquire the lock to ensure thread safety
        with cls._lock:
            # If the class is not in the instances dictionary, create a new instance
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            # Return the existing or newly created instance of the class
            return cls._instances[cls]

# Define a Singleton class with SingletonMeta as its metaclass
class Singleton(metaclass=ThreadSafeSingleton):
    pass

def get_singleton_instance():
    s = Singleton()
    print(s)

# Create a list to store threads
threads = []
# Create 10 thread objects, appending each to the threads list
for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

# Start each thread in the threads list
for t in threads:
    t.start()

# Wait for each thread to finish
for t in threads:
    t.join()