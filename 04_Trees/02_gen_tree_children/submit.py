class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def form_tree(gen_pairs):
    children = {}
    parents = set()
    
    for child, parent in gen_pairs:
        if parent not in children:
            children[parent] = Node(parent)
        if child not in children:
            children[child] = Node(child)
        
        children[parent].children.append(children[child])
        parents.add(child)
    
    root = None
    for node in children.values():
        if node.name not in parents:
            root = node
            break
            
    return root

def get_num_desc(node, desc):
    if node not in desc:
        desc[node.name] = 1
        for child in node.children:
            desc[node.name] += get_num_desc(child, desc)
    return desc[node.name]

def main(input):
    lines = input.strip().split('\n')
    n = int(lines[0])
    gen_pairs = [line.split() for line in lines[1:n + 1]]

    root = form_tree(gen_pairs)
    desc = {}
    get_num_desc(root, desc)
    for name in sorted(desc.keys()):
        yield(f"{name} {desc[name] - 1}")

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(100000)

    with open('input.txt', 'r') as f:
        input = f.read()

    with open('output.txt', 'w') as f:
        f.write('\n'.join(main(input)))