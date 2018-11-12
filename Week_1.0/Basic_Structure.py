
#If the given name is not in the Student_DB list, then
#the information about that student shouldn't be 
#accesable

Student_DB = ["Aznad", "Raahim", "Tasnuba", "Mahim"]

name_sem_db = {"Aznad":3, "Raahim":2, "Tasnuba":2,
                 "Mahim":3, "Porosh":7, "Johrul":7, 
                 "Rabbi":7}



#Iterating over lists
for stu_db in Student_DB:
    print(stu_db)



#Iteraring over lists using range
for i in range(len(Student_DB)):
    print(Student_DB[i])


#Iterating over Dictionary
for key, val in name_sem_db.items():
    print(val)

#Nested Loop
for i in range(5):
    for j in range(10):
        print("for i=",str(i)+" j="+str(j))


#From here, we start solving the problem

# 1. You get an input from the user
print("Enter the name of the student: ")
student_name = input()

#2. Check if the given input is in Student_DB variable
if student_name in Student_DB:
    print("Name of the student: "+student_name)
    print("He/She is currently studying in "+str(name_sem_db[student_name])+"th Semester")

else:
    print("This student's information is not public")    


 