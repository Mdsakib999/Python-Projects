from collections import defaultdict


def anagrams(x):
    d_dict = defaultdict(list)
    for i in x:
        sort_item = " ".join(sorted(i))
        d_dict[sort_item].append(i)

    return d_dict.values()


word = ["sakib", "act", "cat", "xio", "dog"]

print(anagrams(word))