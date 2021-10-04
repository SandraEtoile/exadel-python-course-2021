import time


def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        print(f"calling {function_name}")
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        elapsed_time = round(end - start, 1)
        print(f"{function_name} call took {elapsed_time} seconds")
        return value
    return wrapper


@measure_elapsed_time
def my_fn1(arg1, arg2):
    time.sleep(0.5)
    return arg1 + arg2


@measure_elapsed_time
def my_fn2():
    time.sleep(0.8)
    print("I do nothing! What a life")


@measure_elapsed_time
def my_fn3(arg1, **kwargs):
    time.sleep(0.3)
    print(f"I also do nothing, but I have arg1 = {arg1} and kwargs = {kwargs}")


print("my_fn1 result:", my_fn1(1, 2))
my_fn2()
my_fn3(12, kwarg1='lol', kwarg2='kek')