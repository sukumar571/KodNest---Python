# count = 1
# while count <= 5:
#     print(count)
#     count +=1
# else:
#     print("loop executes successfully")


# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#     if count == 4:
#         break
# else:
#     print("loop doesn't executes because we forcefully break the loop")


number = int(input("Enter a number to (-1 to quit)"))
while number != -1:
    print(number)
    # number = int(input("Enter a number to (-1 to quit)"))
else:
    print("in else block")
print("out from loop")


"""
Note: if you enter -1 then it automatically executes the else block 
it doesn't executes the while loop
"""
