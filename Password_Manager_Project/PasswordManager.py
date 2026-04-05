from cryptography.fernet import Fernet

import hashlib
#Needs to be run only once and aldready done
'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as k:
        k.write(key)
        '''
def load_master_key():
    key=input("Enter the new master key for set up : ")
    hash_key=hashlib.sha256(key.encode()).hexdigest()
    with open("master_key.key","w") as f:
        f.write(hash_key)
    print("Set up security question for reseting the password :")
    teacher=input("Enter your favourite school teacher : ").lower()
    hash_teacher=hashlib.sha256(teacher.encode()).hexdigest()
    song=input("Enter your favourite song : ").lower()
    hash_song=hashlib.sha256(song.encode()).hexdigest()
    with open("Security_Ans_teacher.txt","w") as f1,open("Security_Ans_song.txt","w") as f2:
        f1.write(hash_teacher)
        f2.write(hash_song)
def check_master_key():
    try:
        with open("master_key.key","r") as f:
            actual_master_key=f.read()
        key=input("Enter the master key for verification : ")
        master_key=hashlib.sha256(key.encode()).hexdigest()
        if master_key==actual_master_key :
            print("Verification  was Succesfull !! :)")
            return True
        else:
            print("Verification  failed !!")
            return False
    except FileNotFoundError as e:
        print("Please set up a master key \n")
        load_master_key()
        return True
def reset_master_key():
    print("Answer the security question for reseting the password :")
    teacher=input("Enter your favourite school teacher : ").lower()
    hash_teacher=hashlib.sha256(teacher.encode()).hexdigest()
    song=input("Enter your favourite song : ").lower()
    hash_song=hashlib.sha256(song.encode()).hexdigest()
    with open("Security_Ans_teacher.txt","r") as f1,open("Security_Ans_song.txt","r") as f2:
        actual_teacher=f1.read()
        actual_song=f2.read()
    if(hash_teacher!=actual_teacher or hash_song!=actual_song):
        print("Verification Failed")
        return False
    print("Security check was successfull !!")
    key=input("Enter the new master key for set up : ")
    hash_key=hashlib.sha256(key.encode()).hexdigest()
    with open("master_key.key","w") as f:
        f.write(hash_key)
    return True
# write_key()
print("........WELCOME........\n")
for i in range(3):
    if(check_master_key()==False):
        if i==2:
            print("3 Trials are failed !!!!")
            while(1):
                try:
                    master_key_choice=int(input("Select the option 1. reset password\n2.quit : "))
                    if master_key_choice==1:
                        if(reset_master_key()):
                            break
                        else:
                            quit()
                    if master_key_choice==2:
                        quit()
                    else:
                        continue
                except Exception as e:
                    print(e)
                    print("Invalid input")
                    continue
    else:
        break
def load_key():
    with open("key.key","rb") as k:
        key=k.read()
        return key

key=load_key()
fer=Fernet(key)

def add():
    app=input("Enter the app or web page name : ")
    account=input("Enter the account name : ")
    pwd=input("Enter the password : ")
    with open("Pwd_Manager_File.txt","a") as f :
        line=f"{app}|{account}|{(fer.encrypt(pwd.encode())).decode()}\n"
        #it can also be written as :

        #str=f"{app}|{account}|{str((fer.encrypt(pwd.encode())))}\n" 
        #str=f"{app}|{account}|{((fer.encrypt(pwd.encode())))}\n"
        f.write(line)
def view():
    with open("Pwd_Manager_File.txt","r") as f:
        passLine=f.readline().rstrip()
        while passLine!="":
            app,account,pwd=passLine.split("|")
            print(f"app : {app} , account : {account} , password : {(fer.decrypt(pwd.encode())).decode()}")
            #this above line changes as well as per the above changes: 

            #print(f"app : {app} , account : {account} , password : {(fer.decrypt(pwd)).decode()}")
            passLine=f.readline().rstrip()
while(1):
    try:
        choice=int(input("Select the operation to be performed :\n1.ADD\n2.VIEW\n3.QUIT\nENTER THE No. OF OPERATION :"))
    except Exception as e:
        print("Enter a valid input !!")
        continue
    if choice==3:
        quit()
    if choice==1:
        add()
    elif choice==2:
        view()
    else:
        print("Enter a valid option")