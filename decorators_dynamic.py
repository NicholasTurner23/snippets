def decorator_function(original_function):
    def wrapper_fucntion(*args, **kwargs):
        print('Wrapper executed this before {}.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_fucntion



@decorator_function
def display():
    print('Display function ran.')

display()

# display = decorator_function(display) This is the same as using the @ anotation for decorators.
    
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)