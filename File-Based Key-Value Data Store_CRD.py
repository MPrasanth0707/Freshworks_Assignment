import threading 
from threading import*
import time

#Global Variables
storageDict = {}
l=[]

#Reading the Key-Value Pairs
            
def read():
    print("\nEnter key to read the pair:")
    key = int(input())
    if key not in storageDict: print("\nError: Key does not Exist")
    else:
        data = storageDict[key]
        if time.time() < data[1] or data[1] == 0: print("\n", key, data[0])
        else: print("\nError: time to live expired")
    update()


#File Update
def update():
    f = open("Data Storage.txt",'w')
    data = str(storageDict)
    f.write(data)
    
#Deleting the Key-Value Pairs

def delete():
    print("\nEnter the key to delete")
    key = int(input())
    if key not in storageDict: print("\nError: Key does not Exist")
    else:
        del storageDict[key]
        print("\nSuccessfully deteled")
    update()

#Creating New Key-Value File

def create():
    print("\nEnter the Key: ")
    key = int(input())
    
    print("\nEnter the Value: ")
    value = input()

    print("\nEnter the Expiration Minute(s): ")
    expiryTime = int(input())
    expiryTime *= 60
    
    if key in storageDict:
        print("\nError: this key is Already exists:")
    else:
        if len(storageDict) < (1024*1024*1024) and key < (16*1024*1024): #Checking the memory limit
            if expiryTime == 0: l = [value, expiryTime]
            else: l = [value, time.time() + expiryTime]
            
            if len(value) <= 32:
                storageDict[key] = l
                
                print("\nSuccessfully Created\n")
            else:
                print("\nError: Invalid Key value\n")
        else:
            print("\nError: Memory Limit exceed\n")
    update()






#Program Starts HERE

print("===================================================================")
print("File based key-value data store supports the basic operation of CRD")
print("===================================================================")

Choice = 0
while(True):
    print("=============================================================")
    print("Choose the operation to be performed (Enter operation Number):")
    print("=============================================================\n")
    print("**********")
    print("1.CREATE\n2.READ\n3.DELETE\n4.SHOW ALL\n5.EXIT")
    print("**********")
    
    
    Choice = int(input())
    if(Choice == 1): create()
    elif(Choice == 2): read()
    elif(Choice == 3): delete()
    elif (Choice == 4):
        if not storageDict: print("No Records Found!\n")
        for x in storageDict:
            print("Key:", x, "| Value:", storageDict[x][0], "| Time:", storageDict[x][1], "\n")
        update()
    elif(Choice == 5):
        print("Program Ended.")
        break
    else:
        print("Invalid Operation\n")
    
                
    print("---------------------------------------------------\n")

#Creating Threads and Writing into the File
if Choice != 5:
    t1 = Thread(target=(create or read or delete)) 
    t1.start()
    time.sleep(1)
    t2 = Thread(target=(create or read or delete))
    t2.start()
    time.sleep(1)

    
