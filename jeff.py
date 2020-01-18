# opening the file
with open("c_medium.in") as f:
    data = f.readlines()  # read the text file
    infoline = data[0].strip().split(" ")  # get a list containing all the numbers in the file
    pizzaline = data[1].strip().split(" ")  # get a list containing all the numbers in the file
    maxslices = int(infoline[0])
    numofpizza = infoline[1]
    pizzaline = [int(value) for value in pizzaline]

    print("max slices:")
    print(maxslices)
    print("Number of pizzas:")
    print(numofpizza)
    print("pizza sizes:")
    print(pizzaline)
    print("......................")

# adding to the max
nextbiggestpizza = []
nextbiggestpizzaindex = []
order = []
totalslices = 0
for value in range(0, len(pizzaline)):
    totalslices += pizzaline[value]
    if totalslices < maxslices:
        order.append(pizzaline[value])
    else:
        nextbiggestpizza = pizzaline[value]
        nextbiggestpizzaindex = value
        break

print("order:")
print(order)
print("......................")


# calculating remaining and min to remove for next biggest pizza
remainingslices = maxslices - sum(order)
print("Remaining slices:")
print(remainingslices)

minremove = nextbiggestpizza - remainingslices
print("min to remove:")
print(minremove)

# trying to fit next biggest pizza
answers = []
for value in range(0, len(order)):
    answers.append(value)

for value in range(0, len(order)):
    if order[value] > minremove:
        del order[value]
        answers.remove(value)
        order.append(nextbiggestpizza)
        answers.append(nextbiggestpizzaindex)
        break

print("final order:")
print(order)
print("answer for file:")
print(answers)


