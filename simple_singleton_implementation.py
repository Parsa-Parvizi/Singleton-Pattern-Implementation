class Singleton:
    # class-level variable to store the single 
    # instance of the class
    _instance = None 
 
    # override the __new__ method to 
    # control how new objects are created
    def __new__(cls): 
        # check if instance of the class has 
        # been created before. NOTE: lazy instantiation
        print('<new> creating...')
        if not cls._instance: 
            # create new instance of the class 
            # and store it in _instance  
            cls._instance = super().__new__(cls)  
        # return the single instance of the class, either 
        # newly created one or existing one
        return cls._instance
    
    # override the __init__ method to control initialization
    def __init__(self): 
        print('<init> called...')

