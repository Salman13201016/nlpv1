
#variable take globally declare kora
#return kora
def custom_len(x):
    count = 0
    for i in x:
        count = count+1
    return count


language = {'python':["Easy","Nice","Begineer Friendly"],'c': ['mother','low level','good for logic building']}

data = ["salman"]
size = custom_len(language,data)

print(size)

#function based polymorphism