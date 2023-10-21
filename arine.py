


import random # used for testing
import string # used for testing
import json # used to load the sampleObject for testing
from typing import Optional # my python version needed this for the signature given in q5 
import datetime # used in q5 to cleanly compare dates- I assumed built-in libaries are fair use for this. 


"""
Write a program that prints the numbers from 1 to 100. But for multiples of 3 print “Fizz” instead
of the number and for the multiples of 5 print “Buzz”. For numbers which are multiples of both 3
and 5 print “FizzBuzz”.
Use the following function signature:
def fizzbuzz() -> None
"""

def fizzbuzz() -> None:
    # Prints the numbers from 1 to 100. Print “Fizz” for multiples of 3, for the multiples of 5 print “Buzz”. For numbers which are multiples of both 3 and 5 print “FizzBuzz”.
  
    # Comments: I've solved this problem before so this time I did it with a string concatenation twist. 
  
    for i in range(1, 101):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if result == "":
            result = i
        print(result)

"""
Write a function that takes a string that may be a float, and returns either the converted string as
float or the default value provided as an argument if the string does not represent a float.
Use the following function signature:
def convert_to_float(input_str: str, default: float) -> float
"""

def convert_to_float(input_str: str, default: float) -> float:
    # converts an input string into a float, if it is a float, return that, otherwise return default
    try:
        return float(input_str)
    except:
        return default
    
def test_Convert_to_float(N = 100):
    for i in range(N):
        seed = random.randint(0, 20)
        if seed > 10:
            test = random.uniform(0, 1000000)
        else:
            test = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=seed)) # this snippet is taken from https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/ for testing purposes
        print(convert_to_float(test, 42), seed > 10) #True means it is a float, false means it's not


"""
Write a function that takes a data object (see Sample Data Object below) as an argument and
returns the list of all medications that have “antihtn” in their “drugGroup”. If there are no
matching medications, return an empty list.
Use the following function signature:
def get_antihtn_meds(data_obj: dict) -> list
"""
def get_antihtn_meds(data_obj: dict) -> list:
    # from the provided data_obj, returns a list of medications that have antihtn in their drugGroup
    medications = data_obj["medications"]
    antihtn_meds = []
    for medication in medications:
        for drug in medication["drugGroup"]:
            if drug == "antihtn":
                antihtn_meds.append(medication["brandName"]) # comment this line out and uncomment the next line to get the medication structure rather than just the name
                # antihtn_meds.append(medication) 
                break
    return antihtn_meds
            
        
def test_get_antihtn_meds():
    with open('sampleObject.json') as json_file:
        data = json.load(json_file)
    print(get_antihtn_meds(data))
    
    
# test_get_antihtn_meds()


"""
Write a function that takes a data object (see Sample Data Object below) as an argument and
returns the list of medications whose “doseForm” is any form of “tablet”. If there are no
matching medications, return an empty list.
Use the following function signature:
def get_tablet_meds(data_obj: dict) -> list
"""

def get_tablet_meds(data_obj: dict) -> list:
    # from the provided data_obj, returns a list of medications whose doseForm is any form of tablet
    medications = data_obj["medications"]
    tablet_meds = []
    for medication in medications:
        for doseForm in medication["doseForm"].split(","):
            if doseForm.strip() == "tablet":
                tablet_meds.append(medication["brandName"]) # comment this line out and uncomment the next line to get the medication structure rather than just the name
                # tablet_meds.append(medication)
                break
    return tablet_meds

def test_get_tablet_meds():
    with open('sampleObject.json') as json_file:
        data = json.load(json_file)
    print(get_tablet_meds(data))
    
# test_get_tablet_meds()

"""
Write a function that takes a data object (see Sample Data Object below) as an argument and
returns the “ndc9” value of the medication that was filled most recently. If there’s a tie, return
any of the “ndc9” for medications filled on that day. If there are no medications, return None.
Use the following function signature:
def get_latest_med_ndc(data_obj: dict) -> Optional[str]
"""

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    # from the provided data_obj, returns the ndc9 of the medication that has been filled most recently. If no medications was filled, return None.
    medications = data_obj["medications"]
    newestFill = None
    for medication in medications:
        fills = medication["fills"]
        for fill in fills:
            date = datetime.datetime(*[int(entry) for entry in fill["fillDate"].split("-")]) # converts the string format of the date to a datetime object
            if newestFill == None:
                newestFill = [date, medication["ndc9"]]
            else:
                if newestFill[0] < date:
                    newestFill = [date, medication["ndc9"]]
    return newestFill[1]
            
def test_get_latest_med_ndc():
    with open('sampleObject.json') as json_file:
        data = json.load(json_file)  
    print(get_latest_med_ndc(data))
    
# these are examples of my tests
    
# fizzbuzz()
# test_Convert_to_float(3)
# test_get_antihtn_meds()
# test_get_tablet_meds()
# test_get_latest_med_ndc()