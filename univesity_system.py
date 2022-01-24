import csv
def masterus():  
    user_master = input('enter your username: ')
    pass_master = input('enter your password: ')
    with open('masus.csv', 'r') as file:  
        users = csv.reader(file)
        for user in users:
            if user[0] == user_master and user[1] == pass_master:
                master_options()  
                break
                
def employee_userpass():
    user_employee = input('enter your username: ')
    pass_employee = input('enter your password: ')
    with open('Employee_information.csv', 'r') as file:  
        users = csv.reader(file)
        for user in users:
            if user[3] == user_employee and user[4] == pass_employee:
                employee_options()  
                break
                
def student_userpass():
    global user_student
    global pass_student
    user_student = input('enter your username: ')
    pass_student = input('enter your password: ')
    with open('Student_information.csv', 'r') as file:  
        users = csv.reader(file)
        for user in users:
            if user[3] == user_student and user[4] == pass_student:
                student_options()  
                break

def home():
    c1 = int(input(
        'Hello, Welcome to your university online system!\n\n'
        'What is your position?\n1.Manager\n2.Employee\n3.Student\n0.exit\n⇨  '
    ))
    if c1 == 1:
        masterus()
         
        
    elif c1 == 2:
        employee_userpass()
            

         
    elif c1 == 3:
      student_userpass()
            
    elif c1 == 0:
        exit()        
    else:
        print('💢💢Wrong number! please only use the defined bids!💢💢')

def master_options():
    cm1 = int(input(
        'What operation do you want to perform on the employee?\n'
        '1.Add employee\n'
        '2.Remove employee\n'
        '3.Show employee profile\n'
        '4.Change employee profile\n⇨ '
    ))
    if cm1 == 1:
        employee_information = [
            input('Enter the name of the new employee\n⇨ '),
            input('Enter the new employees last name\n⇨ '),
            int(input('Enter the employees age\n⇨ ')),
            int(input('Enter the ID or username of the new employee\n⇨ ')),
            input('Enter the new employee password\n⇨ ')
        ]
        with open('Employee_information.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(employee_information)
            print('Information successfully recorded')
            # here many values must get the information
            file.close()
    elif cm1 == 2:
        employee_information=[]
        employee_id=input('Enter the ID of the employee you want to delete\n⇨ ')
        employee_password=input('Enter the password of the employee you want to delete\n⇨ ')
        with open('Employee_information.csv','r') as file:
            reader=csv.reader(file)
            for i in reader:
                #print(i)
                employee_information.append(i)   
            #print(employee_information)
            
            for  ii in range(0,len(employee_information)): 
             if employee_id==employee_information[ii][3] and employee_password==employee_information[ii][4]:
                   print(ii)
                   print(employee_information[ii])
                   del employee_information[ii]
                   print(employee_information)
                   with open('Employee_information.csv','w',newline='') as file:
                       writer=csv.writer(file)
                       writer.writerows(employee_information)    
    elif cm1 == 3:#not done yet
        employee_information=[]
        all_or_some=int(input('Do you want to see the information of all employees or a specific employee?\n1.all employees\n2.specific employee\n'))
        if all_or_some==1:
            with open('Employee_information.csv','rt') as file:
                 reader=csv.reader(file)
                 for i in reader:
                  print(i)
                  employee_information.append(i)
        elif all_or_some==2:
            employee_information=[]
            employee_id=input('Enter the employee ID\n ')
            with open('Employee_information.csv','rt') as file:
                reader=csv.reader(file)
                for i in reader:
                        
                    employee_information.append(i)
                
                for ii in range(0,len(employee_information)):
                    if employee_id==employee_information[ii][3]:
                       print(employee_information[ii]) 

                    elif ii==len(employee_information)-1:
                        print('not found!')    
                    
        else:
            print('💢💢Wrong number! please only use the defined bids!💢💢')        
            master_options()
    elif cm1 == 4:
        employee_id=input('Enter the employee ID\n')
        employee_information=[]
        with open('Employee_information.csv','r') as file:
            reader=csv.reader(file)
            for i in reader:
                employee_information.append(i)   
            for i in range(0,len(employee_information)):
                if employee_id==employee_information[i][3]:
                    
                    print('find it')
                    new_employee_information = [
            input('Enter the name of the new employee\n⇨ '),
            input('Enter the new employees last name\n⇨ '),
            int(input('Enter the employees age\n⇨ ')),
            int(input('Enter the ID or username of the new employee\n⇨ ')),
            input('Enter the new employee password\n⇨ ')
        ]    
                    employee_information[i][0]=new_employee_information[0]
                    employee_information[i][1]=new_employee_information[1]
                    employee_information[i][2]=new_employee_information[2]
                    employee_information[i][3]=new_employee_information[3]
                    employee_information[i][4]=new_employee_information[4]
                    with open('Employee_information.csv','w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(employee_information)
                        print('done!')
            
              
    else:
        print('💢💢Wrong number!💢💢')
        o1 = input('Do you want to try again?(Yes/No)\n')
        if o1[0] == 'y' or o1[0] == 'Y':
            master_options()
        elif o1[0] == 'n' or o1[0] == 'N':
            home()

def employee_options():
    cm1=int(input('What operation do you want to do?'
    '\n1.Add student'
    '\n2.Delete student'
    '\n3.Change student information'
    '\n4.Add lessons for the student'
    '\n5.show student lessons'
    '\n6.Delete lessons for students'
    '\n7.Add lessons'
    '\n8.Delete lessons'
    '\n9.show lessons'
    '\n10.show student information'
    '\n: '))
    if cm1==1:
        Student_information=[
        input('Enter the students name:')
        ,input('Enter the students last name:')
        ,int(input('Enter the students age:'))
        ,int(input('Enter the student ID:'))
        ,int(input('Enter the new password:'))
        ,int(input('Enter the course code that the student is studying:'))
        ]
        with open('Student_information.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(Student_information)
            print('done!')
    elif cm1==2:
        Student_id=int(input('Enter the student ID:'))
        with open('Student_information.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            for i in range(0,len(reader)):
                if str(Student_id)==reader[i][3]:
                    del reader[i]
                    with open('Student_information.csv','w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(reader)
                    print('done!')
    elif cm1==3:
        Student_id=int(input('Enter the student ID:'))
        with open('Student_information.csv','r',newline='') as file:
            reader=csv.reader(file)
            reader=list(reader)
            for i in range(0,len(reader)):
                if str(Student_id)==reader[i][3]:
                    print(reader[i])
                    Student_information=[
                    input('Enter the students name:')
                    ,input('Enter the students last name:')
                    ,int(input('Enter the students age:'))
                    ,int(input('Enter the student ID:'))
                    ,int(input('Enter the new password:'))
                    ,int(input('Enter the course code that the student is studying:'))
                    ]           
                    reader[i]=Student_information
                    with open('Student_information.csv','w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(reader)
                        print('done!')

    elif cm1==4:
        Num_lessons=int(input('How many lessons do you want to add?: ')) 
        i=1
        lessons=[]
        while i<=Num_lessons:
            lessons.append(int(input('Enter the lesson code:')))
            i+=1
        with open('Student_information.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            Student_id=int(input('Enter the student ID:'))
            for i in range(0,len(reader)):
                if str(Student_id)==reader[i][3]:
                    reader[i].append(lessons)
                    print('done!')
                    with open('Student_information.csv','w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(reader)
    elif cm1==5:
        Student_id=int(input('Enter the student ID: '))
        with open('Student_information.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            for i in range(0,len(reader)):
                if str(Student_id)==reader[i][3]:
                  print(reader[i][6:])

    elif cm1==6:
        lessons=[]
        lessons.append(int(input('Enter the lesson code:')))
                   
        Student_id=int(input('Enter the student ID: '))
        with open('Student_information.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            
            for i in range(0,len(reader)):
                if str(Student_id)==reader[i][3]:
                     newlist=reader[i][6:]
                     kia=newlist.count(lessons[0])
                     del newlist[kia]
                     reader[i][6:]=newlist
                     with open('Student_information.csv','w',newline='') as file:
                         writer=csv.writer(file)
                         writer.writerows(reader)
                         print('done!')
    elif cm1==7:
        lessons_info=[int(input('Enter the lesson code')),input('Enter the name of the lesson:'),int(input('Enter the lesson units :'))]
        with open('lessons.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(lessons_info)
            print('done!')
    elif cm1==8:
        lessons_info=int(input('Enter the lesson ID:'))
        with open('lessons.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            for i in range(0,len(reader)-1):
                if str(lessons_info)==reader[i][0]:
                    del reader[i]
                    with open('lessons.csv','w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(reader)
                        print('done!')
    elif cm1==9:
        lessons=int(input('Do you want to see the information of one lesson or all lessons?\n1.all lessons\n2.specific lesson\n⇨ '))
        if lessons==1:
            with open('lessons.csv','r') as file:
                reader=csv.reader(file)
                for i in reader:
                    print(i)
        elif lessons==2:
            lesson_id=int(input('Enter the lesson ID:'))
            with open('lessons.csv','r') as f:
                reader=csv.reader(f)
                reader=list(reader)
                for i in range(0,len(reader)):
                    if str(lesson_id)==reader[i][0]:
                        print(reader[i])
        else:
            print('Wrong number!')
    elif cm1==10:
        ec=int(input('Do you want to see the information of all students or special student:\n1.all students\n2.special special student'))
        if ec==1:
            with open('Student_information.csv','r') as f:
                reader=csv.reader(f)
                reader=list(reader)
                for i in reader:
                    print(i)
        elif ec==2:
            student_user=int(input('Enter the student ID: '))
            with open('Student_information.csv','r') as f:
                reader=csv.reader(f)
                reader=list(reader)
                for i in range(0,len(reader)):
                    if str(student_user)==reader[i][3]:
                        print(reader[i])
        else:
            print('Wrong number!')
    else:
        print('💢💢Wrong number! please only use the defined bids!💢💢')
        o1 = input('Do you want to try again?(Yes/No)\n')
        if o1[0] == 'y' or o1[0] == 'Y':
            employee_options()
        elif o1[0] == 'n' or o1[0] == 'N':
            home()

def student_options():
    sc=int(input('What operation do you want to do?\n'
'1. Viewing profile\n'
'2. Add lessons\n'
'3. delete lessons\n'))
    if sc==1:  
        with open('Student_information.csv','r') as f:
            reader=csv.reader(f)
            reader=list(reader)
            for i in range(0,len(reader)):
                if str(user_student)==reader[i][3] and str(pass_student)==reader[i][4]:
                    print(reader[i])
    elif sc==2:
        lessons=[]
        lessons.append(int(input('Enter the lesson code:')))
        with open('Student_information.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            for i in range(0,len(reader)):
                if str(user_student)==reader[i][3]:
                    reader[i].append(lessons)
                    print('done!')
                    with open('Student_information.csv','w',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerows(reader)
    elif sc==3:
        lessons=int(input('Enter the lesson code:'))
        with open('Student_information.csv','r') as file:
            reader=csv.reader(file)
            reader=list(reader)
            
            for i in range(0,len(reader)):
                if str(user_student)==reader[i][3]:
                     newlist=reader[i][6:]
                     kia=newlist.count(lessons)
                     del newlist[kia]
                     reader[i][6:]=newlist
                     with open('Student_information.csv','w',newline='') as file:
                         writer=csv.writer(file)
                         writer.writerows(reader)
home()