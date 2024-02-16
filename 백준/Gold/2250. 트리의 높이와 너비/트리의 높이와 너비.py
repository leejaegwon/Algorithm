import sys
lines = [i.strip() for i in sys.stdin.readlines()]

class Node():
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
    
tree = {}

info = lines[1:]
for line in info:
    num,left,right = line.split(' ')
    if left == '-1':
        left = None
    if right == '-1':
        right = None
    tree[num] = Node(num,left,right)

nodes = [] 
def in_order(node,order):
    order += 1
    if node.left != None:
        in_order(tree[node.left],order)
    # print(node.data, end=' ')
    nodes.append([node.data,order])
    if node.right != None:
        in_order(tree[node.right],order)

tree_keys = set(tree.keys())
lefts = set(i.left for i in tree.values())
rights = set(i.right for i in tree.values())

unmatched_keys = tree_keys - lefts - rights
root = str(list(unmatched_keys)[0])
(in_order(tree[root],0))

# print(nodes)

level = {}

for i,node in enumerate(nodes):
    depth = node[1]
    level.setdefault(depth,[])
    level[depth].append(i)
# print(level)
w_h = {}

for key,values in level.items():
    width = values[-1]-values[0]+1
    w_h.setdefault(width,[])
    w_h[width].append(key)
# print(w_h)
largest_key = max(w_h.keys())
corresponding_list = w_h[largest_key]
smallest_value = min(corresponding_list)
print(smallest_value,largest_key)