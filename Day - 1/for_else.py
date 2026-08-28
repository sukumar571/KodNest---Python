# tuple1 = (2, 45, 67, 98, 10)
# for i in tuple1:
#     print(i)

# else:
#     print("loop successfully is executed and we are in else block")


# tuple2 = (45, 67, 90, 20, 40)
# for i in tuple2:
#     print(i)
#     if i == 20:
#         break
# else:
#     print("loop successfully is executed and we are in else block")


"""
Note: if the loop is executed the successfully then else block is also executed
if you forcefully break the for loop else block does not executed

"""


tuple3 = (10, 20, 30, 40 ,50)
for i in tuple3:
    if i % 11 == 0:
        print(i)
        break
else:
    print("There is no number divisible by 11 in this square")




