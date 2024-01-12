from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO, force=True)

    @wraps(orig_func)
    def wrapper(*args, **kwds):
        logging.info(
            'Ran with args: {}, and kwds: {}'.format(args, kwds)
        )
        return orig_func(*args, **kwds)
    return wrapper


def my_timer(orig_func):
    import time
    import logging

    @wraps(orig_func)
    def wrapper(*args, **kwds):
        logging.basicConfig(filename='{}time.log'.format(orig_func.__name__), level=logging.INFO, force=True)
        t1 = time.time()
        result = orig_func(*args, **kwds)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        logging.info("{} run for {} seconds".format(orig_func.__name__, t2))
        return result
    return wrapper
         

@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info('John', 30)
# print()

#Chaining decorators
@my_logger
@my_timer
def display_info_timed(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info_timed('Sam Winchester', 35)