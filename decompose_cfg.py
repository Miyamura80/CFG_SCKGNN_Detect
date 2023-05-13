import os
import re

# Order: 1
# Extract raw nodes and edges from the graph
# Export to: ./binary_graph_data/{vuln}/node/ and ./binary_graph_data/{vuln}/edge/
def write_nodes_and_edges(vuln):
    inputFileDir = f"./binary_cfg_code/{vuln}/"
    dirs = os.listdir(inputFileDir)
    # dirs.sort(key=lambda x: int(x[:-4]))
    print(dirs)
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r")
        lines = f.readlines()
        nodes = f"./binary_graph_data/{vuln}/node/" + str(file)[0:-4] + ".txt"
        edges = f"./binary_graph_data/{vuln}/edge/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, 'w')
        f_edge = open(edges, "w")

        flag = 0

        for line in lines:
            if "block" in line and flag == 0:
                f_node.write(line.strip() + "\n")
            if "block" in line and flag != 0:
                f_edge.write(line.strip() + "\n")
            if "}" in line:
                flag += 1
                continue

# Order: 2
# clean \l
def clean_nodes(vuln):
    inputFileDir = f"./binary_graph_data/{vuln}/node/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        nodes = f"./binary_graph_data/{vuln}/new_node/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        lines = f.readlines()
        for line in lines:
            tt = re.sub(r'\\l', r' ', line)
            f_node.write(tt)

# Order 3:
# reserve '0x' and remove 'block'
def clean_nodes_2(vuln):
    inputFileDir = f"./binary_graph_data/{vuln}/new_node/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        nodes = f"./binary_graph_data/{vuln}/new_node1/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        i = 0
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:2] == "0x":
                    s += i
                if i[0:1].isupper() != 0:
                    s += i
                s += ' '
            s += '\n'
        s = s.replace("  ", " ")
        print(s)
        f_node.write(s)


# extract the pure bytecode
def extractPureBytecode(vuln):
    inputFileDir = "./bytecode/delegatecall/"
    dirs = os.listdir(inputFileDir)
    print(dirs)
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./binary_cfg_code/delegatecall/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        i = 0
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:4] == "6080":
                    s += i
        s = s.replace("  ", " ")
        print(s)
        f_node.write(s)


if __name__ == "__main__":
    vuln_list = ["delegatecall", "integeroverflow", "reentrancy", "timestamp"]
    for vuln in vuln_list:
        write_nodes_and_edges(vuln)
        # clean_nodes(vuln)
