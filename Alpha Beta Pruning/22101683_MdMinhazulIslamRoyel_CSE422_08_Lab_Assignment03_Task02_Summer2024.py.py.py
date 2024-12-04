import math
def minimax(depth, idx, maximizingPlayer, arr, alpha, beta): 
    if depth == 3: 
        return arr[idx] 
    if maximizingPlayer: 
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, idx * 2 + i, False, arr, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best) 
            if beta <= alpha: 
                break
        return best 
    else:
        best = MAX
        for i in range(0, 2): 
            val = minimax(depth + 1, idx * 2 + i, True, arr, alpha, beta) 
            best = min(best, val) 
            beta = min(beta, best) 
            if beta <= alpha: 
                break
        return best 
    
values = [3,6,2,3,7,1,2,0]  
MAX, MIN = math.inf, -math.inf
final = minimax(0, 0, True, values, MIN, MAX)
c = int(input())
if (max(values) - c) > final:
  print(f"The new minimax value is {max(values) - c}. Pacman goes right and uses dark magic")
else:
  print(f"The minimax values is {final}. Pacman does not use dark magic")