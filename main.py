def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


print("=" * 50)
print("       STUDENT MARKS & GRADE CALCULATOR")
print("=" * 50)

name = input("Enter student name: ")

subjects = ["English", "Mathematics", "Computer", "Biology", "Physics"]
marks = []

print("\nEnter marks between 0 and 100:")

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
percentage = total / len(marks)
average = percentage
highest = max(marks)
lowest = min(marks)
grade = calculate_grade(percentage)

if percentage >= 40 and lowest >= 33:
    result = "PASS"
else:
    result = "FAIL"

print("\n" + "=" * 50)
print("                    RESULT")
print("=" * 50)

print(f"Student Name : {name}")

print("\nSubject Marks:")
for subject, mark in zip(subjects, marks):
    print(f"{subject:<15}: {mark:.2f}")

print("-" * 50)
print(f"Total Marks  : {total:.2f} / 500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Average      : {average:.2f}")
print(f"Highest Mark : {highest:.2f}")
print(f"Lowest Mark  : {lowest:.2f}")
print(f"Grade        : {grade}")
print(f"Result       : {result}")

print("=" * 50)
print("          Thank you for using the program!")
print("=" * 50)
