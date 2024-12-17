def socks_and_shirts(input : str) -> list[int]:
    A, B, C, D = map(int, input.split())
    
    if A == B == C == D and A != 0:
        return [A + 1, 1]
    elif A == B == C == D == 0:
        return [0, 0]
    else:
        res = []
        #blue pair
        if A > 0 and C > 0 :
            res.append([B + 1, D + 1])
        # red pair
        if B > 0 and D > 0 :
            res.append([A + 1, C + 1])
        # guaranteed answers
        if A > 0 and B > 0 :
            res.append([max(A , B) + 1, 1])
        if C > 0 and D > 0 :
            res.append([1, max(C ,D) + 1])
        return min(res, key=sum)
    
if __name__ == '__main__':
    with open("input.txt", "r") as file:
        input = file.read().strip()

    result = socks_and_shirts(input)
    with open("output.txt", "w") as file:
        file.write(f'{result[0]} {result[1]}')