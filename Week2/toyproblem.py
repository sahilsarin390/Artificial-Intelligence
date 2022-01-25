total = int(input('Enter no. of bananas at starting: '))
distance = int(input('Enter the distance you want to cover: '))
capacity = int(input('Enter the Maximum capacity of your camel: '))
lose = 0
start = total
for i in range(distance):
    while start > 0:
        start = start-capacity

        if start == 1:
            lose = lose-1
        lose = lose+2

    lose = lose-1
    start = total-lose
    if start == 0:
        break

print(
    f"The maximum number of bananas that can be transferred to the destination using only camel: {start}")
