#  Decorators are used to modify a function's behavior without altering its original code

#  You can use the '@' sign to apply a decorator to a function

# The same decorator can be applied to a variety of functions



def song_name(name):
    return "Song name: "+ name

def info(name, func):
    return (func(name))
    
print(info("People", song_name))



def outer_function():
    '''
    Nested Function
    Functions Can be used inside a function 
    '''
    print("Hello: Outer Function")
    
    def inner_function():
        print("Hello: INNER function")
    
    inner_function()  #inner_function print

outer_function()  #outer_function print 
print(outer_function.__doc__)
help(outer_function)
 

#  return the result of the nested function directly from within the body of the parent function.

def greet(name):
    print("Hello", name)
    
    def account():
        return "Your account is created! Congratulations .  "

    # message=account()
    return account()
print(greet("Rupesh"))

def greet(name):
    print("Hello", name)    # Prints NOW
    return "Done"

result = greet("Rupesh")
# Output: Hello Rupesh  (prints immediately)
print(result)  # Output: Done

def name_print(name):
    return "Hello dear, "+name  #sends back, does not print 

greet=name_print("Rupesh")
print(greet)

def order():
    def prepare():
        return "Your meal is being prepared! "
    status=prepare()
    return status
print(order())


#Decorators : they modify a functions' behavior without altering its original code 

def greet():
    return 'welcome'
#takes function as arg
def uppercase(func):  #DECCORATOR 
    #wrapper functin to keep the original function code unchanged 
    def wrapper():   #DECORATED VERSION OR MODIFIED VERSION OF THE greet() function 
        orig_message=func()
        modified_message=orig_message.upper()
        return modified_message
    return wrapper
upper_text=uppercase(greet)
print(upper_text())

def uppercase(func):
    def wrapper():
        orig_message=func()
        modified_message=orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return"welcom3!"

#using the decorated function 
print(greet())
        

def light_decorator(func):
    def wrapper():
        result = func()
        
        print("Turning off the lights....")
        
        return result
    return wrapper

def stock_status_decorator(func):
    def wrapper(item):
        result=func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper
@stock_status_decorator
def restock_item(item):
    return "Restocked "

@stock_status_decorator
def sell_item(item):
    return "sold"
print(restock_item("laptop"))
print(sell_item)




# Visual Comparison:

# VERSION 1: print inside
def add_print(a, b):
    print(a + b)     # Shows output
    return None

add_print(2, 3)      # Output: 5 (appears immediately)

# VERSION 2: return inside  
def add_return(a, b):
    return a + b     # No output yet

result = add_return(2, 3)  # Nothing shows
print(result)              # Output: 5 (need print outside)
