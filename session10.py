import os
os.system('cls')
all_students = []


def add_student():
    name = input("enter the name: ")
    age = input("enter the age: ")
    scores = []
    while True:
        course_name = input("enter course name: ")
        course_score = input("enter course score: ")
        course_info = {"name": course_name, "score": course_score}
        scores.append(course_info)
        if input("do you want to quit (y or n): ").lower().startswith("y"):
            break
    s = {"id": len(all_students) + 1, "name": name, "age": age, "scores": scores}
    all_students.append(s)


def view_all():
    print(all_students[0]["scores"])


def view_student(s):
    print(s["name"])
    for key, value in s.items():
        print(key, value)


def search_student(name):
    for s in all_students:
        if s["name"] == name:
            view_student(s)


while True:
    user_input = input(
        "1 for view all\t 2 for add\t 3 for search\t 4 for update\t 5 for exit:>  "
    )
    if user_input == "5":
        exit()
    elif user_input == "2":
        add_student()
    elif user_input == "1":
        view_all()
    elif user_input == "3":
        name = input("enter the name: ")
        search_student(name)
