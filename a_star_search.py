n = int(input("Enter number of nodes:"))
print("\n")

adj_matrix = []

open = []
closed = []

nodes = []

for i in range(n):
    temp = []
    temp.append(chr(i+65))    
    temp.append(-1)
    temp.append(int(input("Enter heuristic value for node %s:"%chr(i+65))))
    nodes.append(temp)

adj_matrix = [[-1, 2, -1, -1, -1, 3],
         [2, -1, 1, 9, -1, -1],
         [-1, 1, -1, -1, -1, -1],
         [-1, 9, -1, -1, 1, -1],
         [-1, -1, -1, 1, -1, 6],
         [3, 2, -1, -1, 6, -1]
        ]

# for i in range(n):
#     temp = []
#     for j in range(n):
#             temp.append(int(input("Enter cost between node %s and node %s:" %(chr(i+65),chr(j+65)))))
#     adj_matrix.append(temp)

def create_path(nodes,dest,source):
    path = []
    path.append(chr(dest+65))
    curr = dest
    while curr!=source:
        curr = nodes[curr][1]
        path.append(nodes[curr][0])
    
    path.reverse()
    print(path)

source = ord(input("Enter source:")) - 65
dest = ord(input("Enter destination:")) - 65

open.append(nodes[source])
nodes[source].append(0)

curr = []

while len(open):
    min = 99999
    for i in open:
        if (i[2]+i[3]<min):
            min = i[2] + i[3]
            curr = i

    if(curr[0] == chr(dest+65)):
        create_path(nodes,dest,source)
        break

    curr_index = ord(curr[0])-65

    for i in range(n):
        if adj_matrix[curr_index][i] != -1:
            successor_curr_cost = curr[3] + adj_matrix[curr_index][i]
            if nodes[i] in open:
                if nodes[i][3] <= successor_curr_cost:
                    continue
            elif nodes[i] in closed:
                if nodes[i][3] <= successor_curr_cost:
                    continue
                open.append(nodes[i])
                closed.remove(nodes[i])
            else:
                open.append(nodes[i])
            nodes[i].append(successor_curr_cost)
            nodes[i][1] = curr_index
    closed.append(curr)
    open.remove(curr)






            
    



        

    
    


    


