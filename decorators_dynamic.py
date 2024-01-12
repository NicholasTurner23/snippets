from typing import Any


def decorator_function(original_function):
    def wrapper_fucntion(*args, **kwargs):
        print('Wrapper executed this before {}.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_fucntion


class Decorator_class(object):
    def __init__(self, original_function) -> None:
        self.original_function = original_function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('Wrapper executed this before {}.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwds)


@decorator_function
def display():
    print('Display function ran.')

display()
display()
# display = decorator_function(display) This is the same as using the @ anotation for decorators.
    
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
print()

@Decorator_class
def display_info_class(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info_class('Sam', 30)