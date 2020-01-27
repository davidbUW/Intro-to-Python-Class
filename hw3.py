newlist = "-"
newlist = list(newlist)
oddlist = "-"
oddlist = list(oddlist)

def number_program():
    while True:
        start = int(input("Enter a starting number: "))
        end = int(input("Enter an ending number: "))
        if start < 1:
            print("ERROR: Starting number must be greater than 1")
        elif end < 5*start:
            print("ERROR: Ending number greater than 5 times starting number")
        else:
            for x in range(start,end+1,1):
                newlist.append(x)
            del newlist[0]
            for index, number in enumerate(newlist):
                if number % 2 == 0:
                    print("{} [{}]".format(number, str(index)))
            for y in range(start,end+1,1): #consider using else for this function
                if y % 2 > 0:
                    oddlist.append(y)
            del oddlist[0]
            total = sum(oddlist)
            print(total)
            break
number_program()





