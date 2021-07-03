
input = "Robbie"
def isUnique(word):
    for a in range(len(word)):
        for b in range(len(word)):
            if (a != b):
                if (word[a] == word[b]):
                    return(print(word + " is not unique" + " because of " + word[a]))
    return(word + "is unique")  

#uncomment to run above function
#print(isUnique(input))

def isUnique2(word):
    base_list = []
    duplicate_list = []
    dict = {}

    for i in word:
        base_list.append(i)
        duplicate_list.append(i)

    dict[1] = [base_list]
    dict[2] = [duplicate_list]   


    #dict.insert(2, duplicate_list)
    return(print(dict[2]))

#print(isUnique2("Bob"))