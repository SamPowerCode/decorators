def my_decororator(func):
    def wrapper(*args, **kwargs):
        # Do something before the function is called
        print(f"Do something before calling {func.__name__}.")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Do something after the function is called
        print(f"Do something after calling {func.__name__}.")

        return result
    
    return wrapper


# @my_decororator
def say_hello():
    return "Hello, World!"

# result = say_hello()



result = my_decororator(say_hello)()

print("Result of say_hello:", result)
