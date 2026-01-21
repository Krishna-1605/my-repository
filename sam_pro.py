# ==============================
# Student Grade Management System
# ==============================

students = []  # List to store all students


# -------------------------------
# Calculate average marks
# -------------------------------
def calculate_average(marks):
    return sum(marks.values()) / len(marks)


# -------------------------------
# Assign grade based on average
# -------------------------------
def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


# -------------------------------
# Add a new student
# -------------------------------
def add_student(name, age, roll_no, marks):
    student = {
        "name": name,
        "age": age,
        "roll no": roll_no,
        "marks": marks
    }
    students.append(student)
    print("✅ Student added successfully!")


# -------------------------------
# Update student marks
# -------------------------------
def update_marks(student_name, subject, new_marks):
    for student in students:
        if student["name"].lower() == student_name.lower():
            student["marks"][subject] = new_marks
            print("✅ Marks updated successfully!")
            return
    print("❌ Student not found!")


# -------------------------------
# Display all students
# -------------------------------
def display_all_students():
    print("\n📋 ALL STUDENTS REPORT\n")

    for student in students:
        average = calculate_average(student["marks"])
        grade = assign_grade(average)

        print(f"Name       : {student['name']}")
        print(f"Roll No    : {student['roll no']}")
        print(f"Average    : {average:.2f}")
        print(f"Grade      : {grade}")
        print("-" * 30)


# -------------------------------
# Generate individual report card
# -------------------------------
def individual_report(student_name):
    for student in students:
        if student["name"].lower() == student_name.lower():
            average = calculate_average(student["marks"])
            grade = assign_grade(average)

            print("\n----- REPORT CARD -----")
            print(f"Name       : {student['name']}")
            print(f"Roll No    : {student['roll no']}")
            print("Marks:")
            for subject, marks in student["marks"].items():
                print(f"  {subject.capitalize()} : {marks}")

            print(f"Average    : {average:.2f}")
            print(f"Grade      : {grade}")
            print("-----------------------")
            return

    print("❌ Student not found!")


# -------------------------------
# Show unique subjects offered
# -------------------------------
def show_unique_subjects():
    subjects = set()

    for student in students:
        subjects.update(student["marks"].keys())

    print("\n📚 Unique Subjects Offered:")
    print(subjects)


# ==============================
# SAMPLE DATA
# ==============================

add_student(
    "Krishna Nagini",
    27,
    16,
    {"english": 67, "maths": 74, "science": 58}
)

add_student(
    "Palani",
    30,
    5,
    {"english": 82, "maths": 85, "science": 91}
)

# ==============================
# FEATURE DEMONSTRATION
# ==============================

show_unique_subjects()
display_all_students()
update_marks("Krishna Nagini", "maths", 85)
individual_report("Krishna Nagini")
