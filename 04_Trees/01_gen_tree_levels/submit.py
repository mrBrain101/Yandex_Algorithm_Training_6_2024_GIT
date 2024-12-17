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

def get_gens(node, gen, gens):
    if node is None:
        return
    
    gens[node.name] = gen
    for child in node.children:
        get_gens(child, gen + 1, gens)

def main(input):
    lines = input.strip().split('\n')
    n = int(lines[0])
    gen_pairs = [line.split() for line in lines[1:n + 1]]

    root = form_tree(gen_pairs)
    gens = {}
    get_gens(root, 0, gens)
    
    for name in sorted(gens.keys()):
        yield(f"{name} {gens[name]}")

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        input = f.read()

    with open('output.txt', 'w') as f:
        f.write('\n'.join(main(input)))