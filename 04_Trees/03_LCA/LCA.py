class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None

def form_tree(gen_pairs):
    nodes = {}
    for child, parent in gen_pairs:
        if child not in nodes:
            nodes[child] = Node(child)
        if parent not in nodes:
            nodes[parent] = Node(parent)
        nodes[child].parent = nodes[parent]
    return nodes

def get_LCA(name1, name2, nodes):
    node1 = nodes[name1]
    node2 = nodes[name2]
    ancestors = set()
    while node1:
        ancestors.add(node1)
        node1 = node1.parent
    while node2:
        if node2 in ancestors:
            return node2.name
        node2 = node2.parent
    return None

def main(input):
    lines = input.strip().split('\n')
    n = int(lines[0])
    gen_pairs = [line.split() for line in lines[1:n]]
    query_pairs = [line.split() for line in lines[n:]]
    nodes = form_tree(gen_pairs)
    res = []
    for name1, name2 in query_pairs:
        res.append(get_LCA(name1, name2, nodes))
    return res

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        input = f.read()

    with open('output.txt', 'w') as f:
        f.write('\n'.join(main(input)))