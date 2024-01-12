def decorator_function(original_function):
    def wrapper_fucntion():
        print('Wrapper executed this before {}.'.format(original_function.__name__))
        return original_function()
    return wrapper_fucntion

@decorator_function
def display():
    print('Display function ran.')

display()