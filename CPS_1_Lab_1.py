'''
Ryan Salmon
June 20, 2025
Computational Problem Solving 1 Lab Remake
Class Average Calculator
'''

homework = []
lab = []
MIDTERM = -1
FINAL = 0

COMPLETE = 0

USER_INPUT = 0  # User inputs that takes value and inserts it into the proper list
  # Selects what kind of grade you would like to put in.
while COMPLETE == 0:
    grade_sel = input(
        "What grade would you like to enter?\n1: Homework\n2: Lab\n3: Midterm Exam\n")

    match grade_sel:
        case '1':
            if len(homework) < 4:
                USER_INPUT = input("Input homework grade\n")
                homework.append(int(USER_INPUT))
                print(homework)

            else:
                USER_INPUT = input("All grades for homework are entered, change their values? Y/N\n")
                if USER_INPUT == 'y' or USER_INPUT == 'Y':
                    print("Select which grade to change.", str(homework), "\n")
                    USER_INPUT = input("Type the grade value you wish to change")
                    homework.remove(USER_INPUT)
                    USER_INPUT = input("Input the replacement grade value")
                    homework.append(int(USER_INPUT))

                else:
                    print("No update has been made")

        case '2':
            if len(lab) < 2:
                USER_INPUT = input("Input lab grade\n")
                lab.append(int(USER_INPUT))
                print(lab)

            else:
                USER_INPUT = input( "All grades for lab are entered, change their values? Y/N\n")
                if USER_INPUT == 'y' or USER_INPUT == 'Y':
                    print("Select which grade to change.", str(lab), "\n")
                    USER_INPUT = input( "Type the grade value you wish to change")
                    lab.remove(USER_INPUT)
                    USER_INPUT = input("Input the replacement grade value")
                    lab.append(int(USER_INPUT))

                else:
                    print("No update has been made")
        case '3':
                USER_INPUT = input("Input midterm grade\n")
                MIDTERM = int(USER_INPUT)

        case default:
            print("Invaild Choice")
        
    if ((len(homework) == 4) and (len(lab) == 2) and MIDTERM > -1):
        USER_INPUT = input("All grades fields are input, calculate final grade average? Y/N\n")
        if USER_INPUT == 'y' or USER_INPUT == 'Y':
            FINAL = (((sum(homework) / 400) * 25) + ((sum(lab) / 200) * 25) + ((MIDTERM / 100) * 50))
            print("Final Calculated Average: ", str(FINAL))
            COMPLETE = 1



