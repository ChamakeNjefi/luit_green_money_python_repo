#Import libraries

from random import randint
import random
import sys 


# user to input their department name    

department = (input("What is your department name? "))


# user to input number of EC2 instances they want to spin up

instance = int(input("How many instances do you want to create "))


for instance in range(instance):
    
    unique_number = random.randint(0, sys.maxsize)
    print("EC2 instance unique name is: ", department, '/', unique_number)

    
  








