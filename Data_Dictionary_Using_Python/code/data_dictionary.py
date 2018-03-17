import json, glob
from difflib import get_close_matches

filename = glob.iglob("C:/Users/Anurag/Desktop/python/python_projects/Data_Dictionary_Using_Python/data_folder/*.json")

for _file in filename:
    data = json.load(open(_file))

def dictionary(word):
    if word in data:
        return data[word]
    else:
        print("did you mean:", get_close_matches(word,data.keys())[0])
        yes_or_no = input("Please enter Y or N:")
        if yes_or_no == "y" or yes_or_no == "Y":
            return dictionary(get_close_matches(word,data.keys())[0])
        else:
            return "please check the word again"

_input = input("please enter your word:").lower()
output = dictionary(_input)

if type(output)==list:
    for name in output:
        print(name)
else:
    print(output)
