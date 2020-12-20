import random

number_of_nodes = int(input("Enter number of nodes: "))
list_nodes = []
edges = number_of_nodes + 1

# Generate nodes 0-99
for i in range(number_of_nodes):
    node = random.randint(0, number_of_nodes - 1)
    while node in list_nodes:  # If node exists in list, regenerate until does not exist
        node = random.randint(0, number_of_nodes - 1)
    else:
        list_nodes.append(node)
        # print(node)

# Create text file
file = "test_random.txt"
temp_open = open(file, "w+")
temp_open.write("#" + "\n")
temp_open.write("# Random Graph" + "\n")
temp_open.write("# Nodes: " + str(number_of_nodes) + " Edges: " + str(edges) + "\n")
temp_open.write("# FromNodeId	ToNodeId" + "\n")

# Generate 2 edges for each node
for j in range(0, number_of_nodes):
    if j == number_of_nodes - 1:  # For the last node
        temp_open.write(str(list_nodes[0]) + "\t" + str(list_nodes[number_of_nodes - 1]) + "\n")
        temp_open.write(str(list_nodes[number_of_nodes - 1]) + "\t" + str(list_nodes[0]) + "\n")
    else:
        temp_open.write(str(list_nodes[j]) + "\t" + str(list_nodes[j + 1]) + "\n")
        temp_open.write(str(list_nodes[j + 1]) + "\t" + str(list_nodes[j]) + "\n")

print("Random graph generated, File name: " + file)
temp_open.close()
