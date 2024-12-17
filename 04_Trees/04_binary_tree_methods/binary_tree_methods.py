class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def search(self, value):
        if self.value is None:
            return False
        if self.value == value:
            return True
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        if value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)
        
        return False
    
    def add(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)

    def get_tree(self, level=0):
        tree_printout = []
        if self.left:
            tree_printout.extend(self.left.get_tree(level+1))
        tree_printout.append(f"{'.'*level}" + f'{str(self.value)}')
        if self.right:
            tree_printout.extend(self.right.get_tree(level+1))

        return tree_printout

def main(input):
    tree = BinaryTree()
    res = []
    for line in input:
        if line.startswith('ADD'):
            if tree.search(int(line.split()[1])):
                res.append('ALREADY')
                continue
            tree.add(int(line.split()[1]))
            res.append('DONE')
        elif line.startswith('SEARCH'):
            if tree.search(int(line.split()[1])):
                res.append('YES')
            else:
                res.append('NO')
        elif line.startswith('PRINTTREE'):
            res.append('\n'.join(tree.get_tree()))

    return res

if __name__ == "__main__":
    with open('input.txt') as f:
        input = [line.strip() for line in f.readlines()]
        
    with open('output.txt', 'w') as f:
        f.write('\n'.join(main(input)))