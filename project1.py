# Student Grade Management System

students = [
    {
        "name": "Krishna Nagini",
        "roll no": 16,
        "marks": {"English": 67, "Maths": 74, "Science": 58}
    },
    {
        "name": "Palani",
        "roll no": 5,
        "marks": {"English": 82, "Maths": 85, "Science": 91}
    }
]

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks.values()) / len(marks)

# Function to assign grade
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Ask user to enter student name
search_name = input("Enter student name: ").strip().lower()
found = False

for student in students:
    if student["name"].lower() == search_name:
        found = True
        avg = calculate_average(student["marks"])
        grade = assign_grade(avg)

        print("\n----- REPORT CARD -----")
        print("Name :", student["name"])
        print("Roll No :", student["roll no"])
        print("Marks:")

        for subject, marks in student["marks"].items():
            print(f"  {subject.capitalize()} : {marks}")

        print(f"Average : {avg:.2f}")
        print(f"Grade   : {grade}")
        print("-----------------------")

if not found:
    print("\n❌ Error: Student not found!")
