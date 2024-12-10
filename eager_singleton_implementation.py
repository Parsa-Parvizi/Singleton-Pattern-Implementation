class SingletonMeta(type):
    # Initialize a dictionary to store single instance of the 
    # class for each subclass of the SingletonMeta metaclass
    _instances = {}

    # override: called during creation of sub-types
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instances[cls] = super().__call__()
        print('initializing <super>...')

    # return the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

# Our practical Singleton class which is a singleton by the 
# fact that it is derived from the SingletonMeta metaclass
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