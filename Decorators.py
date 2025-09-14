def my_decorators(func):
    def wrapper():
        print("Running {func.__name__}")
        func()
        print("Finished")
    return wrapper
@my_decorators

def do_this():
    print("Doing this!")

@my_decorators   
 
def do_that():
    print("Doing that!")    
    
do_this()
do_that()    