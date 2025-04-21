import matplotlib.pyplot as plt
import os

def menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph\n")
def get_student_id(file,student_name):
    try:
        for line in file:
            if line[3:].strip("\n") == student_name:
                return  line[0:3]
    except:
        return None
def main():
    # variables used throughout every selection
    assignment_lines = open("data/assignments.txt").readlines()

    menu()
    selection = int(input("Enter your selection: "))
    if selection == 1:
        student_name = input("What is the student's name: ")
        student_grade = 0
        student_id = get_student_id(open("data/students.txt").readlines(), student_name)
        if student_id:
            for file in os.listdir("data/submissions"):
                line_in_file = open(f"data/submissions/{file}").read()
                weight = line_in_file[3:-2].strip("|")
                weight_p = 0
                for i in range(len(assignment_lines)):
                    if assignment_lines[i].strip("\n") == weight:
                        weight_p = assignment_lines[i+1].strip("\n")

                if line_in_file[0:3] ==  student_id:
                    student_grade += int(line_in_file[-2:]) * (int(weight_p)/100)
            print(f"{float(student_grade/10):.0f}%")
        else:
            print("Student not found")
    elif selection == 2:
        assignment_name =  input("What is the assignment name: ")
        weight = 0
        list_of_scores = []
        for i in range(len(assignment_lines)):
            if assignment_lines[i].strip("\n") == assignment_name:
                weight = assignment_lines[i + 1].strip("\n")
        for file in os.listdir("data/submissions"):
            line_in_file = open(f"data/submissions/{file}").read()
            if line_in_file[3:-2].strip("|") == weight:
                list_of_scores.append(int(f"{int(line_in_file[-2:])}"))
        print(f"Min: {min(list_of_scores)}%")
        print(f"Avg: {sum(list_of_scores)//len(list_of_scores):.0f}%")
        print(f"Max: {max(list_of_scores)}%")
    elif selection == 3:
        assignment_name = input("What is the assignment name: ")
        weight = 0
        list_of_scores = []
        for i in range(len(assignment_lines)):
            if assignment_lines[i].strip("\n") == assignment_name:
                weight = assignment_lines[i + 1].strip("\n")
        for file in os.listdir("data/submissions"):
            line_in_file = open(f"data/submissions/{file}").read()
            if line_in_file[3:-2].strip("|") == weight:
                list_of_scores.append(int(f"{int(line_in_file[-2:])}"))
        list_of_scores.sort()
        plt.hist(list_of_scores, bins = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
        plt.show()


if __name__ == "__main__":
    main()

