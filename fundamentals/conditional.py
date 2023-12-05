

first_name = "sal"
last_name = 'salman'
user_name = 'salman'
phone_number ="0170564408"


size_name = len(first_name)

if(first_name=="" or last_name=='' or user_name==''): #indentation case senstive #0 | 1 = 1

    print("the field can not be empty")
else:
    if(size_name<3):
        print("The size must be minimum 3")
    elif(len(phone_number)!=11):
        print("the phone number must be 11 digit")
    else:
        print("success")