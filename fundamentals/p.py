import pandas as pd


language = {'python':["Easy","Nice",'AI and ML and Software Dev'],'c': ['mother','low level','good for logic building'],'java':["Need Oop","Good for Enterprise","Sprint is a popular framework"],'php':['easy','popular','well known for web development'],'c++':['oop','popular','well known for fast product development like game, AI model, contest']}

df = pd.DataFrame(language)

print(df.columns)

df['html'] = ['easy','well structure','structure of a web page']
# print(df.info())
# df.drop(0,axis=0,inplace=True)
# print(df.info())

# for index, row in df.iterrows():
#     print(index,row)
for value in df['html']:
    print(value)
