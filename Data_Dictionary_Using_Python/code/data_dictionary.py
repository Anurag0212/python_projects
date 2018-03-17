import json, glob

filename = glob.iglob("C:/Users/Anurag/Desktop/python/python_projects/Data_Dictionary_Using_Python/data_folder/*.json")

for _file in filename:
    data = json.load(open(_file))

def dictionary(word):
    if word in data:
        return data[word]
    else:
        return "please check the word again"

_input = input("please enter your word:").lower()
output = dictionary(_input)

if type(output)==list:
    for name in output:
        print(name)
else:
    print(output)
