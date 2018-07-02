# Calculate the probability of flipping a balanced coin four times 
# and getting each pattern: HTTH, HHHH and TTHH.
def coin_prob(a):
    return a*a*a*a

print(coin_prob(.5))

# If a list of people has 24 women and 21 men, then the probability of 
# choosing a man from the list is 21/45.
# What is the probability of not choosing a man?
total_women = 24
total_men = 21
total_all = total_women + total_men
def prob_woman(pw):
    return total_women / total_all

print(prob_woman(24))

# The probability that Bernice will travel by plane sometime in the 
# next year is 10%. The probability of a plane crash at any time is 0.005%.
# What is the probability that Bernice will be in a plane crash 
# sometime in the next year?
# Multiplication rule, P(AB) = P(A|B)*P(B)
print(.1 * .0005)
