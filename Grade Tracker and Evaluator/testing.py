class_dict = {
    "class": ["algebra", "history", "science"],
    "grades": [90.0, 80.0, 70.0]
}

class_select = True

while class_select:
    try:
        class_selection = input("which class: ")
        grade_index = class_dict["class"].index(class_selection)
        print(class_dict["grades"][grade_index])
        class_select = False
    except ValueError:
        print("Class was not found, please type in a new class")
print("You fixed it!")