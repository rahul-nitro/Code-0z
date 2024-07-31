def BoyerMooreHorspool(pattern, text):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    skip = [m] * 256
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1
    while k < n:
        j, i = m - 1, k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(text[k])]

    return -1

if __name__ == '__main__':
    text = "this is the string to search in"
    pattern = "the"
    s = BoyerMooreHorspool(pattern, text)
    print(f'Text: {text}')
    print(f'Pattern: {pattern}')
    print(f'Pattern "{pattern}" found at position {s}' if s > -1 else f'Pattern "{pattern}" not found')
