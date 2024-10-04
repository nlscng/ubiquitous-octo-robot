# The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.
#
# Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).
#
# Analyze the time and space complexities of your solution.
#
# Example:
#
# input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
#
# output: 47 # and given this cap the new grants array would be
#            # [2, 47, 47, 47, 47]. Notice that the sum of the
#            # new grants is indeed 190

def find_grants_cap(grantsArray, newBudget):
    naive_avg = float(newBudget) / len(grantsArray)  # 38
    grantsArray.sort()

    remaining_fund = 0
    new_cap = naive_avg  # 38
    for idx in range(len(grantsArray)):
        if grantsArray[idx] < new_cap:
            remaining_fund = new_cap - grantsArray[idx]
            num_left = len(grantsArray) - idx - 1
            # print("new_cap: {}, idx: {}, num_left: {}".format(new_cap, idx, num_left))
            new_cap += float(remaining_fund) / num_left

    return round(new_cap, 1)


assert find_grants_cap([2, 4], 3) == 1.5
assert find_grants_cap([2, 4, 6], 3) == 1
assert find_grants_cap([2, 100, 50, 120, 167], 400) == 128
assert find_grants_cap([2, 100, 50, 120, 1000], 190) == 47
assert find_grants_cap([21, 100, 50, 120, 130, 110], 140) == 23.8
assert find_grants_cap([210, 200, 150, 193, 130, 110, 209, 342, 117], 1530) == 211
