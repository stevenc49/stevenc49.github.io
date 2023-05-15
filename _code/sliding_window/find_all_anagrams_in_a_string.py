from collections import defaultdict
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:


    freq = defaultdict(int)
    res = []

    if (len(p) > len(s)):
        return res

    # build map of freq in p
    for char in p:
        freq[char] +=1

    # start with initial pass (so later pass can include entire slide in/slide out)
    for i in range(0, len(p)-1):
        if s[i] in freq:
            freq[s[i]] -= 1


    for i in range(-1, len(s)-len(p)+1):

        # if slide in, subtract
        if i+len(p)<len(s) and s[i+len(p)] in freq:
            freq[s[i+len(p)]] -= 1

        # if slide out, add
        if i>-1 and s[i] in freq:
            freq[s[i]] += 1

        if not any(freq.values()):
            res.append(i+1)     # because in this iteration, 'i' will be behind by 1 when the slide in char will be p ahead

    return res


# def findAnagrams(s: str, p: str) -> List[int]:
#     char_freqs, indices, len_p, len_s = defaultdict(int), [], len(p), len(s)
#
#     # s cannot have p anangrams if len(p) > len(s)
#     if len_p > len_s:
#         return indices
#
#     # build map of character frequencies in p
#     for char in p:
#         char_freqs[char] += 1
#
#     # initial full pass over the window, except last element which we will pass over later
#     for i in range(len_p - 1):
#         if s[i] in char_freqs:
#             char_freqs[s[i]] -= 1
#
#     # slide the window with stride 1, adding the value "sliding out" and subtracting the value "sliding in"
#     for i in range(-1, len_s - len_p + 1):
#         if i > -1 and s[i] in char_freqs:
#             char_freqs[s[i]] += 1
#         if i + len_p < len_s and s[i + len_p] in char_freqs:
#             char_freqs[s[i + len_p]] -= 1
#
#         # check whether we encountered an anagram by seeing if all frequencies add up to 0
#         if not any(char_freqs.values()):
#             indices.append(i + 1)
#
#     return indices

def main():
    s = "cbaebabacd"
    p = "abc"

    res = findAnagrams(s, p)

    print(res)


if __name__ == "__main__":
    main()