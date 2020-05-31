import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(word ,data.keys())) > 0:
        # //return "Did ypu mean %s instead" % get_close_matches(word ,data.keys())[0]
        yn = input(f"Did you mean {get_close_matches(word ,data.keys())[0]} instead ? Please enter Y if yes or N if no : ")
        if yn == "Y":
            return data[get_close_matches(word ,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist ,please double check it."
        else:
            return "We didn't undertand your query. Please recheck it."

    else:
        return "The word doesn't exist , Please double check it."

input_value = input("Enter word : ")
output = (translate(input_value))

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)