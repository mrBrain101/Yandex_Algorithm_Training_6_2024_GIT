def count_nodes(n, nodes):
    tree = [[] for _ in range(n + 1)]
    for u, v in nodes:
        tree[u].append(v)
        tree[v].append(u)

    count = [0] * (n + 1)

    def dfs(node, parent):
        count[node] = 1
        for neighbor in tree[node]:
            if neighbor != parent:
                count[node] += dfs(neighbor, node)
        return count[node]

    dfs(1, -1)

    return count[1:]

def main(input: str):
    n = int(input.split('\n')[0])
    nodes = [tuple(map(int, line.split())) 
             for line in input.split('\n')[1:] if line.strip()]
    return count_nodes(n, nodes)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(100000)
    
    with open('input.txt', 'r') as f:
        input = f.read()

    with open('output.txt', 'w') as f:
        for i in main(input):
            f.write(str(i) + ' ')