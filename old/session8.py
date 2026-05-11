# from session7 import calculate_total

# print(calculate_total("sum", 1,2,3))


# def outer():
#     print("check login state")

#     def inner():
#         print("welcome")

#     inner()


# outer()

# import time
# from functools import wraps

# def timer_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"this function took {end - start} seconds")
#         return result

#     return wrapper

# @timer_decorator
# def fetch_data(n=3):
#     time.sleep(1)
#     return n * [1, 2, 3]


# print(fetch_data(10))


# numbers = (x**2 for x in range(1, 100) if x % 2 == 0)
# for n in numbers:
#     print(n)

# prices = [100, 250, 80, 120]


# expensive = filter(lambda p: p > 100, prices)
# print(list(expensive))
# discounted = map(lambda p: p * 0.8, prices)
# print(list(discounted))


y = lambda x: x**2
print(y(4))
print(type(y))
