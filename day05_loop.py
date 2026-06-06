# #while loop
# count = 1
# while count<=5:
#     print(count, end ="")
#     count+=1

# # Input validation pattern
# while True:
#     age = int(input("Age:"))
#     if age>0:
#         break
#     print("Must be positive!")

           #break.continue.pass
#break-exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i, end ="")

    #continue - skip this iteration
    for i in range(6):
        if i%2 == 0:
            continue
        print(i, end ="")

# pass — do nothing (placeholder)
    for i in range(3):
     pass # fill in logic later
