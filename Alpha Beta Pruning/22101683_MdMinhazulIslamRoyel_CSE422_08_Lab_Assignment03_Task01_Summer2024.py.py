import random
import math

def mortal_kombat(first_kick):
  rounds_played = 0
  rounds_winner = []
  current_player = first_kick

  def alpha_beta_prunning(depth,alpha,beta,player):
    if depth == 0:
      arr = [1,-1]
      return random.choices(arr)[0]
    if player == 1:
      points = MIN
      for child in range(2):
        points = max(points, alpha_beta_prunning(depth - 1, alpha, beta, 1 - player))
        alpha = max(alpha, points)
        if beta <= alpha:
          break
      return points

    else:
      points = MAX
      for child in range(2):
        points = min(points, alpha_beta_prunning(depth - 1, alpha, beta, 1 - player))
        beta = min(beta, points)
        if beta <= alpha:
          break
      return points
  while rounds_played<3:
    MIN = -math.inf
    MAX = math.inf
    result = alpha_beta_prunning(5, MIN, MAX, current_player)
    if result > 0:
      rounds_winner.append("Sub-Zero")
    else:
      rounds_winner.append("Scorpion")
    rounds_played += 1
    current_player = 1 - current_player
    if rounds_winner.count("Scorpion") >=2 :
      break
    if rounds_winner.count("Sub-Zero") >=2 :
      break
  return rounds_winner

inp = int(input("0 for Scorpion, 1 for Sub-Zero: "))
rounds_winner = mortal_kombat(inp)
if rounds_winner.count("Scorpion") >=2 :
  print("Game Winner: Scorpion")
else:
  print("Game Winner: Sub-Zero")

print("Total Rounds Played:",len(rounds_winner))

for i in range(len(rounds_winner)):
  print(f"Winner of Round {i+1}: {rounds_winner[i]}")