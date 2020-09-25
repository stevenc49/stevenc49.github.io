def helper(listt):
    prod = 1
    for val in listt:
      prod = prod*val
    return prod

print(helper([1,2,3]))