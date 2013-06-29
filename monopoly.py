# problem 84
# ugly, but beautiful :)
import random
import numpy as np

die_range = 4
squares = 40

def roll(dice=1):
  return sum(random.choice(die_range) for _ in range(dice))

dice_prob = [0. for _ in xrange(die_range * 2 + 1)]
for i in xrange(1, die_range + 1):
  for j in xrange(1, die_range + 1):
    dice_prob[i + j] += 1./(die_range**2)

prob = [[0. for _ in xrange(squares)] for _ in xrange(squares)]

CC = [2, 17, 33]
CC1, CC2, CC3 = tuple(CC)
CH = [7, 22, 36]
CH1, CH2, CH3 = tuple(CH)
GO = 0
JAIL = 10
G2J = 30
C1 = 11
E3 = 24
H2 = 39
R1 = 5
R2 = 15
R3 = 25
U1 = 12
U2 = 28
next_R = {CH1: R2, CH2: R3, CH3: R1}
next_U = {CH1: U1, CH2: U2, CH3: U1}

def CH_vector(current, CH):
  return [GO, JAIL, C1, E3, H2, R1, next_R[CH], next_R[CH], next_U[CH], current - 3]

def CC_vector():
  return [GO, JAIL]

def process_next(square, next_square, val=1.):
  if val < 1./16**5: return
  if next_square in CC:
    for card_square in CC_vector():
      prob[square][card_square] += val * 1./16
    prob[square][next_square] += val * 14./16
  elif next_square in CH:
    for card_square in CH_vector(square, next_square):
      #prob[card_square] += val * 1./16
      process_next(square, card_square, val=val * 1./16)
    prob[square][next_square] += val * 6./16
  elif next_square is G2J:
    prob[square][JAIL] += val
  else:
    prob[square][next_square] += val

for square in xrange(squares):
  for i in xrange(1, die_range + 1):
    for j in xrange(1, die_range + 1):
      next_square = (square + i + j) % squares
      process_next(square, next_square)

prob_sums = [sum(prob_j) for prob_j in prob]
probs_norm = [[p / prob_sums[j] for p in prob[j]] for j in xrange(len(prob))]
prob_sums = [sum(prob_j) for prob_j in probs_norm]
prob_matrix = np.array(probs_norm).T
#print prob_matrix
w, v= np.linalg.eig(prob_matrix)
prob_flat = [float(x) for x in v[:,0].real]

sum_prob = sum(prob_flat)
norm_prob = [p / sum_prob * (1 - 1./die_range**3) for p in prob_flat]
norm_prob[JAIL] += 1./(die_range ** 3)
sort_indices = sorted(range(len(norm_prob)), key=lambda x: norm_prob[x], reverse=True)
print sort_indices
print [norm_prob[i] for i in sort_indices]
