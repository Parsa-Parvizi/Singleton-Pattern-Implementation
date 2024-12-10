class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None 
 
    # override the __init__ method to control initialization
    def __init__(self): 
        print('<init> called...')
        # raise an error to prevent constructor utilization 
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        print('<get_instance> called...')
        if not cls._instance: 
            # create new instance of the class 
            cls._instance = cls.__new__(cls)  
        # return the single instance of the class, either 
        # newly created one or existing one
        return cls._instance 
    
# s0 = ClassicSingleton()
s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()

print(s1 is s2)
print(s1)
print(s2)