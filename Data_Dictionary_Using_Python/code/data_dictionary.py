#Importing libraries using import command

import json, glob
from difflib import get_close_matches

#Storing all the .json files name into a variable

filename = glob.iglob("C:/Users/Anurag/Desktop/python/python_projects/Data_Dictionary_Using_Python/data_folder/*.json")

#Loading data from json file into a python variable

for _file in filename:
    data = json.load(open(_file))   #data will be available in the form of dictionary.


#Definition of a function which takes word as an input and return its meaning
#If the word is not present in the json file it tries to suggest a similar word instead
def dictionary(word):
    if word in data.keys():   #Reviews the word in dictionary and returns its meaning if present.
        return data[word]
    elif word.title() in data.keys():  #Check for titles in the dictionary, for example word like India, Texas etc.
        return data[word.title()]
    elif word.upper() in data:   #Check for the words in uppercase
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) >0 :  #Search for the similar words
        yes_or_no = input("Did you mean %s instead? Please enter Y for yes or N for No:" % get_close_matches(word,data.keys())[0]).lower()
        if yes_or_no == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yes_or_no == "n":
            return "Word doesn't exist. Please double check it."
        else:
            print("we din not understand your input. please try again")
            return new_input()
    else:
        return "Word doesn't exist. Please double check it."


#Definition of a function which takes an input from user, pass it to another function and prints the result.

def new_input():
    _input = input("please enter your word:").lower()
    output = dictionary(_input)
    if type(output)==list:
        for name in output:
            print(name)
    else:
        print(output)


#calling of a function to initial the program.

new_input()
