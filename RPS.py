# Neural networks? What's a neural network? This is just if statemets and random stuff!

import random

def player(prev_play, opponent_history=[], counter=[0], kris_counter=[0], player_history=[]):
    opponent_history.append(prev_play)
    ideal_response = {"R": "P", "P": "S", "S": "R"}
    counter[0] += 1
    guess = "P"

    if random.random() > 0.7:
        guess = random.choice("RPS")
    elif random.random() > 0.5 and len(opponent_history) > 1:
        history = ""
        total = 0
        rocks = 0
        papers = 0
        scissorsssss = 0

        for play in opponent_history:
            history = history + play

            if play == "R":
                rocks += 1
            elif play == "P":
                papers += 1
            else:
                scissorsssss += 1

        #print(rocks, papers, scissorsssss)

        if opponent_history[:10] == ['', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S'] and rocks > scissorsssss: # Detect when Quincy is playing
            
            choices = ["P", "P", "S", "S", "R"] # Perfect anti-Quincy counterplay
            guess = choices[counter[0] % len(choices)]

        elif len(player_history) > 1 and prev_play == ideal_response[player_history[-1]]: # Detect if Kris is playing
            kris_counter[0] += 1 # Raise our suspicions it's Kris
            if kris_counter[0] > 3: # IT'S KRIS
                guess = ideal_response[ideal_response[player_history[-1]]]
        else:
            # This strategy is kinda mediocre, but works against all bots consistently
            if rocks > papers and rocks > scissorsssss:
                guess = "P"
            elif papers > rocks and papers > scissorsssss:
                guess = "S"
            elif scissorsssss > papers and scissorsssss > rocks:
                guess = "R"
    
    player_history.append(guess)
    return guess