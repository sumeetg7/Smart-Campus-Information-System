import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Global data storage
# ----------------------------
students = []          # for student registration and records
student_ids = []       # for sorting/searching
course_list = []       # for course enrollment
event_a = set()
event_b = set()

FILE_NAME = "student_records.txt"


# ----------------------------
# Q1: Student Registration and Grade Evaluation
# ----------------------------
def student_registration():
    print("\n--- Student Registration and Grade Evaluation ---")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter exam score: "))

    if marks >= 90:
        grade = "A+"
        remark = "Excellent"
    elif marks >= 80:
        grade = "A"
        remark = "Very Good"
    elif marks >= 70:
        grade = "B"
        remark = "Good"
    elif marks >= 60:
        grade = "C"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade,
        "remark": remark
    }
    students.append(student)
    student_ids.append(int(roll_no) if roll_no.isdigit() else len(student_ids) + 1)

    print("\nStudent Registered Successfully")
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Marks:", marks)
    print("Grade:", grade)
    print("Remark:", remark)


# ----------------------------
# Q2: Course Enrollment Management
# ----------------------------
def course_enrollment():
    print("\n--- Course Enrollment Management ---")
    max_courses = 5
    count = 0

    while True:
        if count >= max_courses:
            print("Maximum course limit reached.")
            break

        course_name = input("Enter course name (or type 'stop' to end): ")
        if course_name.lower() == "stop":
            break

        try:
            credits = int(input("Enter credit value: "))
            if credits <= 0:
                print("Invalid credits. Skipping this course.")
                continue
        except ValueError:
            print("Invalid input. Skipping this course.")
            continue

        course_list.append({"course": course_name, "credits": credits})
        count += 1
        print("Course added successfully.")


# ----------------------------
# Q3: Student Record Management using lists, dicts, sets
# ----------------------------
def record_management():
    print("\n--- Student Record Data Management ---")
    while True:
        print("\n1. Add student record")
        print("2. Display all records")
        print("3. Event participation using sets")
        print("4. Back to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            students.append({"name": name, "age": age, "grade": grade})
            print("Record added.")

        elif choice == "2":
            if not students:
                print("No records found.")
            else:
                for i, s in enumerate(students, start=1):
                    print(i, s)

        elif choice == "3":
            print("Enter students for Event A (comma separated names):")
            a = input().split(",")
            print("Enter students for Event B (comma separated names):")
            b = input().split(",")

            global event_a, event_b
            event_a = set(name.strip() for name in a if name.strip())
            event_b = set(name.strip() for name in b if name.strip())

            print("Event A participants:", event_a)
            print("Event B participants:", event_b)
            print("Common participants:", event_a.intersection(event_b))
            print("Only in Event A:", event_a - event_b)
            print("Only in Event B:", event_b - event_a)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# ----------------------------
# Q4: Sorting and Searching of Student IDs
# ----------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def search_and_sort():
    print("\n--- Sorting and Searching of Student IDs ---")
    ids = []
    n = int(input("How many student IDs do you want to enter? "))

    for i in range(n):
        sid = int(input(f"Enter ID {i + 1}: "))
        ids.append(sid)

    sorted_ids = bubble_sort(ids.copy())
    print("Sorted IDs:", sorted_ids)

    key = int(input("Enter student ID to search: "))
    pos1 = linear_search(sorted_ids, key)
    pos2 = binary_search(sorted_ids, key)

    if pos1 != -1:
        print("Linear Search: Found at position", pos1)
    else:
        print("Linear Search: Not found")

    if pos2 != -1:
        print("Binary Search: Found at position", pos2)
    else:
        print("Binary Search: Not found")


# ----------------------------
# Q5: Fee Calculation using Functions
# ----------------------------
def calculate_fee(tuition_fee, hostel_fee=0, transport_fee=0):
    return tuition_fee + hostel_fee + transport_fee


def fee_calculation():
    print("\n--- Student Fee Calculation ---")
    tuition = float(input("Enter tuition fee: "))
    hostel = input("Enter hostel fee (press Enter if none): ")
    transport = input("Enter transportation fee (press Enter if none): ")

    hostel_fee = float(hostel) if hostel.strip() != "" else 0
    transport_fee = float(transport) if transport.strip() != "" else 0

    total = calculate_fee(tuition, hostel_fee, transport_fee)
    print("Total Payable Fee:", total)


# ----------------------------
# Q6: File Handling for Student Academic Records
# ----------------------------
def file_handling():
    print("\n--- File Handling for Student Academic Records ---")
    while True:
        print("\n1. Write records to file")
        print("2. Read records from file")
        print("3. Generate simple report")
        print("4. Back to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            with open(FILE_NAME, "w") as f:
                for s in students:
                    f.write(str(s) + "\n")
            print("Records saved to file.")

        elif choice == "2":
            try:
                with open(FILE_NAME, "r") as f:
                    data = f.read()
                    print("\n--- File Content ---")
                    print(data if data else "File is empty.")
            except FileNotFoundError:
                print("File not found.")

        elif choice == "3":
            try:
                with open(FILE_NAME, "r") as f:
                    lines = f.readlines()
                    print("Total records in file:", len(lines))
            except FileNotFoundError:
                print("File not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# ----------------------------
# Q7: Directory Scanning with Exception Handling
# ----------------------------
class DirectoryError(Exception):
    pass


def scan_directory(path, level=0):
    if not os.path.exists(path):
        raise DirectoryError("Invalid directory path")

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        print("    " * level + "|-- " + item)
        if os.path.isdir(item_path):
            scan_directory(item_path, level + 1)


def directory_scanning():
    print("\n--- Directory Scanning with Exception Handling ---")
    path = input("Enter directory path: ")

    try:
        scan_directory(path)
    except DirectoryError as e:
        print("Custom Error:", e)
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("Error:", e)


# ----------------------------
# Q8: Student Performance Analysis using NumPy, Pandas, Matplotlib
# ----------------------------
def performance_analysis():
    print("\n--- Student Performance Analysis ---")
    file_path = input("Enter CSV file path (or press Enter for sample.csv): ").strip()

    if file_path == "":
        file_path = "sample.csv"

    # create sample CSV if not exists
    if not os.path.exists(file_path):
        df_sample = pd.DataFrame({
            "Name": ["Asha", "Bharat", "Chandu", "Divya", "Esha"],
            "Marks": [85, 72, 91, 64, 78]
        })
        df_sample.to_csv(file_path, index=False)
        print("Sample CSV created:", file_path)

    try:
        df = pd.read_csv(file_path)

        print("\nData:")
        print(df)

        marks = df["Marks"].to_numpy()

        print("\nStatistical Summary:")
        print("Mean:", np.mean(marks))
        print("Max:", np.max(marks))
        print("Min:", np.min(marks))
        print("Median:", np.median(marks))

        print("\nPandas Description:")
        print(df.describe())

        plt.figure(figsize=(8, 5))
        plt.bar(df["Name"], df["Marks"])
        plt.xlabel("Student Name")
        plt.ylabel("Marks")
        plt.title("Student Performance Analysis")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error in performance analysis:", e)


# ----------------------------
# Main Dashboard
# ----------------------------
def main_menu():
    while True:
        print("\n===================================")
        print("SMART CAMPUS INFORMATION SYSTEM")
        print("===================================")
        print("1. Student Registration and Grade Evaluation")
        print("2. Course Enrollment Management")
        print("3. Student Record Management")
        print("4. Sorting and Searching of Student IDs")
        print("5. Student Fee Calculation")
        print("6. File Handling for Student Academic Records")
        print("7. Directory Scanning with Exception Handling")
        print("8. Student Performance Analysis")
        print("9. Exit")
        print("===================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            student_registration()
        elif choice == 2:
            course_enrollment()
        elif choice == 3:
            record_management()
        elif choice == 4:
            search_and_sort()
        elif choice == 5:
            fee_calculation()
        elif choice == 6:
            file_handling()
        elif choice == 7:
            directory_scanning()
        elif choice == 8:
            performance_analysis()
        elif choice == 9:
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


main_menu()