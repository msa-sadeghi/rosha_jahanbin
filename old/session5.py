# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


# # print(str(number)[-2])
# nums = []
# while number // 10 != 0:
#     nums.append(number % 10)
#     number //= 10
# nums.append(number)
# print(nums[1])

# numbers = (1,2,3,4)
# numbers[0] = 12

# favorite_sports = [
#     ["sara", "foot"],
#     ["abtin", "tennis"],
# ]
# print(f"sara likes {favorite_sports[0][1]}")

# favorite_sport = {
#     "sara" : "foot",
#     "abtin" : "tennis",
# }
# print(type(favorite_sport))
# print(f"sara likes {favorite_sport["sara"]}")
# print(f"abtin likes {favorite_sport["abtin"]}")

# favorite_sport["sara"] = input("enter s sport: ")
# print(favorite_sport)
# print(f"sara likes {favorite_sport["sara"]}")
# name = input("enter the name: ")
# sport = input("enter the sport: ")
# del favorite_sport["abtin"]
# favorite_sport[name] = sport
# print(favorite_sport)

# numbers = {1,2,3,4,5,1}
# print(numbers)

# names = ["artin", "nikan", "amir", "nikan"]

# print(len(set(names)))

# try:
#     x = int(input("enter a number: "))
#     y = int(input("enter a number: "))
#     print(x / y)
# except ZeroDivisionError as er:
#     print(f"not valid {er}")
# except ValueError as er:
#     print(f"error {er}")
# finally:
#     print("finally")


# def is_even_or_odd(number):
#     return number % 2 == 0
    

# print(is_even_or_odd(12))
# print(is_even_or_odd(13))
# print(is_even_or_odd(14))
