user = input("enter the answer to the Great Question of Life, the Universe and Everything: ")

if user.replace(" ", "") == "42" or user.lower() == "forty-two" or user.lower() == "forty two":
    print ("Yes")
else:
    print ("No")