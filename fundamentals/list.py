#there are two types of list - 1D and 2D => D for dimension

product = ['p1','p22','p333']



# print(product[1])

#loop using range function
#loop using without range function
#loop using list comprehension

#for #while

#start, end, step => default = 0, step = 1, end = 5 => loop iterate  <5

# for i in product:
#     print(i) 
#     for j in i:
#         print(j)



# for i in product:
#     for j in range(20):
#         print(i,j)


product_price = [20,30,40,50,60]

discount_list = []
# discount_list_10 = []

# for i in product_price:
#     if(i>30):

#         discount_price = i - (i*15)/100
#         discount_list.append(discount_price)
#     else:
#         discount_price = i - (i*10)/100
#         discount_list.append(discount_price)

discount_list = [i - (i*15)/100 if i>30 else i - (i*10)/100  for i in product_price]

print(discount_list)

#list methods

#append, #insert, copy, find, clear(), count(),sort(), rsort(),reverse(),extend()

list_2_d = [['AB','BACA','CDADAD'],['DADADAD','EADADA','FaDa'],['Gadasdasd','Hadasd','I','J']]

print(len(list_2_d[2]))

for row in list_2_d:
    for col in row:
        print(col)



#[12,17,20]
#49

