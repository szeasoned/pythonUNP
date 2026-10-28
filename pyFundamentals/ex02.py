def get_name():
    return input("Name: ")

def get_age():
    return int(input("Age: "))

def get_course():
    return input("Course: ")

def get_year_level():
    return int(input("Year Level: "))

def get_gpa():
    return float(input("GPA: "))

def get_is_enrolled():
    return input("Enrolled (y/n): ").lower() == 'y'

def display_student(name, age, course, year_level, gpa, is_enrolled):
    print()
    print("=" * 30)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Year Level: {year_level}")
    print(f"GPA: {gpa}")
    print(f"Enrolled: {is_enrolled}")
    print("=" * 30)

def main():
    name = get_name()
    age = get_age()
    course = get_course()
    year_level = get_year_level()
    gpa = get_gpa()
    is_enrolled = get_is_enrolled()

    display_student(name, age, course, year_level, gpa, is_enrolled)

if __name__ == '__main__':
    main()