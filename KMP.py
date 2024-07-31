def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
    initial_point = []
    m, n = 0, 0

    while m < a:
        if text[m] == pattern[n]:
            m += 1
            n += 1
        if n == b:
            initial_point.append(m - n)
            n = prefix_arr[n - 1]
        elif m < a and text[m] != pattern[n]:
            if n != 0:
                n = prefix_arr[n - 1]
            else:
                m += 1
    return initial_point

def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n, m = 0, 1

    while m < b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
            n = prefix_arr[n - 1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr

if __name__ == '__main__':
    string = "ABABDABACDABABCABABCABAB"
    pat = "ABABCABAB"
    initial_index = KMP_String(pat, string)
    print("String:", string)
    print("Pattern:", pat)
    for i in initial_index:
        print('Pattern is found in the string at index number', i)
