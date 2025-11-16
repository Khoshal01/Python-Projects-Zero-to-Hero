
from datetime import datetime

current_year = datetime.now().year

def calculates_age(age):
    if age >= 100:
        print("You already become 100 years old")
    hundrad_years = 100-age
    print("You will become 100 years old in ",hundrad_years," years")
    become_hundrad_year = current_year + hundrad_years
    print("You will become 100 years old in ",become_hundrad_year)

    months = age *12 
    days = months * 30 
    print ("You approximatly lived ",months,"months and ",days,"days")
    






name = input("Enter your name: ")
age = int(input("Enter your age: "))
birth_year = int(input("Enter your birth year: "))
country = input("Enter your country name: ")

calculates_age(age)
