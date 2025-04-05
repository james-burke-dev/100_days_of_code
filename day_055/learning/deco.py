# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        value = function(*args)
        print(f"It returned: {value}")
        


# TODO: Use the decorator 👇

def a_function(*args):
    return sum(args)
    
a_function(1,2,3)