from time import process_time, perf_counter
from functools import wraps


def print_perf(repetitions=1):
    """
    runs the decorated functions the same of times specified in args, printing
    the total time required.
    """
    def perf_decorator(inner_func):
        @wraps(inner_func)
        def wrapped_function(*args, **kwargs):
            t0 = perf_counter()
            for _ in range(repetitions):
                a = inner_func(*args, **kwargs)
            t1 = perf_counter()
            if repetitions == 1:
                repeat_str = "once"
            elif repetitions == 2:
                repeat_str = "twice"
            else:
                repeat_str = str(repetitions) + "times"
            print("Function {0} executed {1} in {2:.4}".format(
                inner_func.__name__, repeat_str, t1 - t0)
            )
            return a
        return wrapped_function
    return perf_decorator


class Memoize:
    """
    A class-based decorator memoizing the result of a function
    """
    def __init__(self, function):
        self.function = function
        self.memo = {}

    def __call__(self, *arg):
        if tuple(arg) not in self.memo:
            self.memo[arg] = self.function(*arg)
        return self.memo[arg]
