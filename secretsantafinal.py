"""
This file accepts a list of names of a chosen lengths and pairs each name to another in the list.
Each name is chosen to be the Secret Santa once.
The number of people participating in the Secret Santa must be chosen first and input as an integer.
Each name must be different, so if two people have the same name amek sure there is a way of
distinguising between the two.
"""

from random import shuffle

#Enter the number of people you want in the secret santa.
total = input("How many people involved in the Secret Santa?")
names_to_pair = []

#Input each name involved in the secret santa. This creates a list of all the names.
while len(names_to_pair) < int(total):
    name = input("Add a name to be added to the Secret Santa: ")
    names_to_pair.append(name)
    print(names_to_pair)

#This function copies the list twice and shuffles the two lists.
def secret_santa_pairing(names):
    list_a = names_to_pair.copy()
    list_b = names_to_pair.copy()

    shuffle(list_a)
    shuffle(list_b)

#Loop through each index. If the names at each index are not the same, then they are paired together.
#If the names are the same then list_b is shuffled.
    i = 0
    while i < len(names_to_pair):
        if list_a[i] != list_b[i]:
            print(list_a[i],"is buying for",list_b[i],"for Secret Santa 2021.")
            i += 1
        else:
            shuffle(list_b)

secret_santa_pairing(names_to_pair)

