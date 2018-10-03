import json
from difflib import get_close_matches

data = json.load(open("data.json"))
# print (data)
def wordToSearch(word):
    word=word.lower()
    if word in data :
        return (data[word])
    elif word.title() in data:
        return (data[word.title()])
    elif word.upper() in data:
        return (data[word.upper()])
    elif len(get_close_matches(word , data.keys()))>0 :
        yn=input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return (data[get_close_matches(word, data.keys())[0]])
        elif yn== "N" :
            return ("Sorry Couln't find it ")
        else :
            return ("Wrong Option")
    else:
        return ("Sorry Couln't find it ")

word=input("Enter the word you want to search the meaning for::  ")
output= wordToSearch(word)
if type(output)==list :
    for item in (output):
        print(item)
else:
    print(output)
