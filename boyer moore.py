def badchar_heuristic(pat):
    bdchar = [-1] * 256
    for i, char in enumerate(pat):
        bdchar[ord(char)] = i
    return bdchar

def patternsearch(text, pat):
    m, n = len(pat), len(text)
    bdchar = badchar_heuristic(pat)
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1

        if j < 0:
            print(f"Pattern occurs at position = {s}")
            s += m - bdchar[ord(text[s + m])] if s + m < n else 1
        else:
            s += max(1, j - bdchar[ord(text[s + j])])

text = input("Enter the text: ").rstrip()
pat = input("Enter the pattern: ").rstrip()

patternsearch(text, pat)
