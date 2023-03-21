import time


def speed_calc_decorator(function):
    def measure_speed():
        first_run = time.time()
        function()
        second_run = time.time()
        difference = second_run - first_run
        print(f"{function.__name__} run speed: {difference}s")

    return measure_speed


@speed_calc_decorator
def fast_function():
    #Your code goes here
    for i in range(10000000):
        i * i


@speed_calc_decorator
#Your code goes here
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
