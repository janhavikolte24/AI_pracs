from tabulate import tabulate
x = 0
y = 0
A = 4
B = 3
# 4,0 1,3 1,0 0,1 4,1 2,3
goal = int(input("Enter goal state for jug A: "))
actions = []
while x != 2:
    rule = int(input("Enter Rule Number: "))
    if(rule == 1):
        x = A
    elif(rule == 2):
        y = B
    elif(rule == 3):
        x = 0
    elif(rule == 4):
        y = 0
    elif(rule == 5):
        x -= B - y
        y = B
    elif(rule == 6):
        y -= A - x
        x = A
    elif(rule == 7):
        y += x
        x = 0
    elif(rule == 8):
        x += y
        y = 0
actions.append(((x, y), rule))
print(tabulate(actions, headers = ["State", "Rule"]))