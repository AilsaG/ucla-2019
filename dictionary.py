dictionary = {
    "wanker":"jerk",
    "knackered":"tired",
    "chuffed":"pleased",
    2: "even"
}
# print(dictionary["wanker"])
# print(dictionary["knackered"])
# print(dictionary["chuffed"])

sentence = "i am totally chuffed and tired"
wordlist = sentence.split(" ") 
print(wordlist) # ['i', 'am', 'totally', 'chuffed', 'and', 'tired']

# print(dictionary.keys())

for word in wordlist:
    if word in dictionary.keys():
        print(word) #chuffed
        print(dictionary[word]) #pleased     # dictionary[word] is like dictionary["chuffed"]




b = {
    "hi": "hello",
    100: "one hundred"
}

b[100]   # "one hundred"




a = input("what's your name?")
print("hi" + a)






# for word in dictionary:
#     print(word)



# print(dictionary.values())

# print(dictionary[2]) # will print the value "even"
# print(dictionary["chuffed"])