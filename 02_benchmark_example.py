from time import time, sleep

def benchmark(func):
    def wrapper(*args, **kwargs):
        # get time before calling the function
        start_time = time()
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # get time after calling the function
        end_time = time()

        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")

        return result
    
    return wrapper


@benchmark
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        sleep(0.1)
        if n % i == 0:
            return False
    return True




result = is_prime(23)


# result = benchmark(is_prime)(13)

print("Result", result)
