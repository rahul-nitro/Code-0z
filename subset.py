from itertools import combinations

def input_set(S, n):
    for i in range(n):
        ele = int(input("Enter element: "))
        S.append(ele)

def subset_sum(size, S, d):
    count = 0
    for i in range(1, size + 1):
        for my_sub_set in combinations(S, i):
            if sum(my_sub_set) == d:
                print(list(my_sub_set))
                count += 1
    if count == 0:
        print(f"No subsets found for the given sum {d}")

# Main module
if __name__ == "__main__":
    S = []
    n = int(input("Enter size of the set: "))
    input_set(S, n)
    print("Set:", S)
    d = int(input("Enter the desired sum: "))
    print("The result is:")
    subset_sum(n, S, d)
