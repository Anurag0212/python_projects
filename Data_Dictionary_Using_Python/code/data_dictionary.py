#Importing libraries using import command
import json, glob
from difflib import get_close_matches

#Storing all the .json files into a variable name
filename = glob.iglob("C:/Users/Anurag/Desktop/python/python_projects/Data_Dictionary_Using_Python/data_folder/*.json")

#writing a function to load data from all the json file into a variable
#data will be available in the form of dictionary.
for _file in filename:
    data = json.load(open(_file))

#Defining a function which will search for the word from the dictionary
#It will provide suggestions to the user of the user input is not present in the dictionary
def dictionary(word):
    if word in data.keys():   #Checks for the word in dictionary
        return data[word]
    elif word.title() in data.keys():  #Check for titles in the dictionary for ex. India, Texas etc.
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

#A function which will take the user input and provide its meaning.
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
