class SingletonMeta(type):
    # Initialize a dictionary to store instances of the Singleton class
    _instances = {}

    # Override the __new__ method instantate the class at load time
    def __new__(cls, *args, **kwargs):
        print('initializing <super>...')
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class

    # Return already initialized instance: Eager Loading
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

# Our practical Singleton class which is a singleton by the fact that it is 
# derived from the SingletonMeta metaclass
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print('initializing <child>...')
        # Initialize your attributes here
        self.attribute = "I'm a Singleton"

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1.attribute)  # Output: I'm a Singleton
print(singleton2.attribute)  # Output: I'm a Singleton

print(singleton1 is singleton2)  # Output: True