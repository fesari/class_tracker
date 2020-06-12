# Additional features included: Program saves classes to a file which can be remembered when the program is re-run
print('{:=^50s}'.format('='))
print('Class Tracking Organiser')
print('{:=^50s}'.format('=')) # Border for the title.
print('\n')

count = 1 # Declares that this is the first password attempt.
password = str('password') # Specifies passcode.
ask = input('Please enter password > ') # Requests an input for a passcode.


while ask: # Keeps the user in the passcode loop until correct.
    if ask == password:
        print('Correct!')
        break
    elif ask != password or ask == '': # Incorrect passcode.
        print('Incorrect, please try again.')
        count += 1
        ask = input('Please enter password > ')
        while count == 3: # Declares the user is on their final attempt.
            if ask != password:
                print('Too many attempts reached, exiting')
                quit()
            elif ask == password:
                break

# Functions to use later in code.
def createClass(chosenclass, data, students): # Three arguments: a class name, student information, no. of students.
    classoptions = 'Class {}'.format(chosenclass)
    with open(f'{classoptions}.txt', '+w') as file: # File creation.
        file.write(str(students) + '\n') # No. of students on the first line.
        for key,value in data.items():
            studentdata = '{},{}\n'.format(key, value) # Converting dictionary into readable format.
            file.write(studentdata)
    return file

def listClass(classname):  # One argument: a class name.
    with open(f'Class {classname}.txt') as chosen: # Read file info.
        chosen.readline() # Student count is to be ignored.
        for line in chosen:
            split = line.split(',') # Student data divided into NAME and SCORE.
            name = split[0]
            name = name.strip('\n')
            score = split[1]
            score = score.strip('\n')
            printout = 'Name: {}, Score: {}/100\n'.format(name,score) # Converting array into readable format.
            print('\n')
            print(printout)

def editStudent(classfile): # One argument: a class name.
    with open(f'Class {classfile}.txt','r+') as file: # Read and write condition (in order to not overwrite the existing contents)
        studentNo = int(file.readline())
        data = file.readlines()
        save = [] # Initialising an array of dictionaries to refer to later.
        for i in range(0,studentNo): # Loop within student range
            piece = data[i]
            contents = piece.split(',')
            name = contents[0]
            score = contents[1]
            readin = {} # Readin refers to the fact we will read into these dictionaries later via the array.
            readin[name] = int(score)
            errorOk = 0
            while errorOk == 0: # Using variables as binary choices helps keep track of whether an error has occurred.
                try:
                    replacement = int(input('Please enter a new score for ' + name + ' > '))
                    errorOk = 1
                except ValueError:
                    print('Please enter a valid number between 1-100.')
            readin[name] = int(replacement)
            save.append(readin) # Creating our array of dictionaries.
        with open(f'Class {classfile}.txt','w+') as file: # Overwriting existing data.
            file.write(str(studentNo) + '\n')
            for i in range(0,studentNo):
                iteration = save[i] # Index each array item in range
                for key,value in iteration.items():
                    studentdata = '{},{}\n'.format(key, value)
                    file.write(studentdata)


# This function is used for both Menu Item 4 & 5.
def gradeDisplay(classfile,value): # Two arguments: a class name, a value for the selected menu item.
    global gradeDict # We use gradeDict in the below code with sums, therefore it requires global declaration.
    with open(f'Class {classfile}.txt', 'r') as file:
        gradeDict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'P': 0}
        grade = '' # initialise grade var
        studentNo = int(file.readline())
        data = file.readlines()
        for i in range(0,studentNo):
            piece = data[i]
            contents = piece.split(',')
            name = contents[0]
            score = int(contents[1])
            if score >= 90:
                grade = 'A'
                gradeDict['A'] += 1 # Keeping track of how many students achieved which grade by adding to their key, val pairs.
            elif score >= 80:
                grade = 'B'
                gradeDict['B'] += 1
            elif score >= 70:
                grade = 'C'
                gradeDict['C'] += 1
            elif score >= 60:
                grade = 'D'
                gradeDict['D'] += 1
            elif score >= 50:
                grade = 'P'
                gradeDict['E'] += 1
            elif score < 50:
                grade = 'E'
                gradeDict['P'] += 1
            if value == 4: # Declares that if menu item 4 is selected, this information should be printed.
                print('\n')
                print('Mr. ' + str(name) + '\nGrade: ' + str(grade) + ', Score: ' + str(score) + '/100')
            else:
                pass
    
    
            
        

print('\n')
print('Welcome to the Main Menu')
print('\n')

listcommands = print('1 > Create Class\n2 > List Students\n3 > Edit Class\n4 > Display Grades\n5 > Display Class Percentages\n6 > Exit')

                     




command = input('Please enter a command > ') 
while command: # Continue asking for commands until program stops.
    if command == '6':
        print('\n')
        print('Have a good day!')
        print('\n')
        exit()
    elif command == '1': 
        askclass = input('Please enter your class > ')
        studentno = int(input('How many student\'s are in your class? > '))
        data = {} # Dictionary to store student information.
        for i in range(0,studentno): # Adding data to this dictionary.
            askstudent = input('Please enter a student\'s full name > ')
            askscore = int(input('Please enter the student\'s score > '))
            data[askstudent] = askscore
            print('\n')
            print('Student Added!')
            print('\n')
            createClass(askclass,data,studentno) # From here on, existing functions do a lot of the work for us. :D
        command = input('Please enter a command > ')
    elif command == '2':
        try:
            askdetails = input('Which class would you like to print? > ')
            listClass(askdetails) # An example of how input is used as an argument.
        except FileNotFoundError: # In order to prevent the errors if file doesn't exist, we do this.
            print('Sorry, this class could not be found.')
            print('\n')
        command = input('Please enter a command > ')
    elif command == '3':
        try:
            whichfile = input('Which class would you like to edit? > ')
            editStudent(whichfile)
        except FileNotFoundError: # Similar to above.
            print('Sorry, this class could not be found.')
            print('\n')
        command = input('Please enter a command > ')
    elif command == '4':
        global chooseclass # I don't actually think I need this
        try:
            chooseclass = input('Please enter a class to display grades > ')
            command = 4 # For the function's arguments we are declaring that command 4 is being entered, not 5.
            gradeDisplay(chooseclass,command)
        except FileNotFoundError:
            print('Sorry, this class could not be found.')
        command = input('Please enter a command > ')
    elif command == '5':
        try:
            chooseclass = input('Please enter a class to display grades > ')
            command = 5
            gradeDisplay(chooseclass,command)
            total = sum(gradeDict.values()) # The sum of all the grades in the class through the gradeDict dictionary. We use this to calculate %.
            for i in gradeDict:
                percentcalc = int(gradeDict[i])/int(total) * int(100)/int(1) # To find a percentage. Quick maths!
                percentcalc = round(percentcalc) # Rounding for cleanliness.
                if percentcalc != int(0): # Clearing all grades with 0%.
                    print(str(percentcalc) + '% of students received the grade ' + str(i))
                else:
                    pass
        except FileNotFoundError:
            print('Sorry, this class could not be found.')
        command = input('Please enter a command > ')
    else:
        print('Please enter a valid command.') # Preventing invalid commands.
        listcommands = print('1 > Create Class\n2 > List Students\n3 > Edit Class\n4 > Display Grades\n5 > Display Class Percentages\n6 > Exit')
        command = input('Please enter a command > ')
        
        
