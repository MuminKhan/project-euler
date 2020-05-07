##########################################################
##########################################################
##
##  Spoilers below
##
##########################################################
##########################################################

def sum_find(N, multiples_of):
    N -= 1
    total = 0
    number_of_multiples = len(multiples_of)

    for i in range(0, number_of_multiples):
        total += multiples_of[i] * seq_sum(N//multiples_of[i])

        for j in range(i + 1, number_of_multiples):
            product = multiples_of[i] * multiples_of[j]
            total += 0 - (product * seq_sum(N//product))

    return total


def seq_sum(n):
    return (n*(n+1))/2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_find(n), [3,5])
    