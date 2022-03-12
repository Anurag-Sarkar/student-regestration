
try:
    class Student:
        details = {}
        def __init__(self,passcode,owner):
            self.__id = ""
            self.__name = ""
            self.__batchcode = ""
            self.__fees = ""
            self.__passcode = passcode
            self.__owner = owner

        def __getitem__(self,key):
            if key in Student.details:
                return f"{key}: {Student.details[key]}"
            else:
                return "Name Not Found"
        def __setitem__(self,name,key,value):
            Student.details[name][key] = value

        def setdetails(self,name,id,batch,fees):
            Student.details[name] = {}
            self.__setitem__(name,"batch_id",id)
            self.__setitem__(name,"batch_code",batch)
            self.__setitem__(name,"fees",fees)
        
        def show(self,passcode,name = None):
            if passcode == self.__owner:
                return Student.details
            elif passcode == self.__passcode:
                return self.__getitem__(name)
            else:
                return "Wrong Passcode!!!"
    i = 0
    admin = int(input("Set Admin passcode: "))
    owner = int(input("Set Owner passcode: "))
    registe = Student(admin,owner)
    while i != 4:
        print("")
        print("1. To register new student")
        print("2. To view student details (admin)")
        print("3. To view all students (owner)")
        print("4. To exit")
        i = int(input())
        if i == 1:
            name,batch_id,batch_code,fees = input("Enter details: ").split()
            registe.setdetails(name,batch_id,batch_code,fees)
        if i == 2:
            print("Enter Passcode and name: ")
            code,name = input().split()
            print(registe.show(int(code),name))
        if i == 3:
            print("Enter Passcode: ")
            code = input()
            print(registe.show(int(code)))

except ValueError as e:
    print("Enter Correct Values")


#anurag P5 Python 3500 
#anirudh P5 Python 3500 
#sanskar B17 WebDev 4500 
#sanika B17 WebDev 4500 