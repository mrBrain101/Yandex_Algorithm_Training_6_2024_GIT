def find_clean_string(s: str, c: int, k: int) -> int:
    l = r = 0
    a = b = 0
    x = 0
    max_len = 0

    while r < c:
        if s[r] == 'a':
            a += 1
        elif s[r] == 'b':
            x += a
            b += 1

        if x > k: 
            if s[l] == 'a':
                l += 1
                x -= b
                a -= 1
            elif s[l] == 'b':
                l += 1
                b -= 1
            else:
                l += 1

        max_len = max(max_len, r - l + 1)
        r += 1

    return max_len

if __name__ == '__main__':
    with open('input.txt') as f:
        c, k = map(int, f.readline().split())
        s = f.readline().strip()
    with open('output.txt', 'w') as f:
        f.write(str(find_clean_string(s, c, k)))