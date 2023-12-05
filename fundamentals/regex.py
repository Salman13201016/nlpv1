#regular expression

import re

# str1 = "you service is fantastic"

# # text_case1 = str1.lower()

# pattern = r'fantastic'

# match = re.search(pattern,str1,re.IGNORECASE)

# if match:
#     print("found", match.group())
# else:
#     print("note found")



# str2 = "The price is $500 $500"
# pattern2 = r'\d+'

# match2 = re.findall(pattern2,str2,re.IGNORECASE)

# if match2:
#     print("found digit", len(match2))
# else:
#     print("not found")

#salman_sultan@gmai.com
#email part
#1 = A-Z or a-z or 0-9 or ._
#2 = @
#3 = A-Z or a-z
#4 = TLD = Top Level Domain = A-Z or a-z -> minimum 2

str2 = "contact us at salmanmdsultan92@gmail.c innovative@innovativeskillsbd.com"
pattern2 = r'\b[A-Za-z0-9._]+@[A-Za-z]+\.[A-Z|a-z]{0,}\b'

match2 = re.findall(pattern2,str2,re.IGNORECASE)

if match2:
    print("found digit", (match2))
else:
    print("not found")