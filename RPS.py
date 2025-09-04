# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "P"

    if random.random() > 0.5:
        guess = random.choice("RPS")
    elif random.random() > 0.5 and len(opponent_history) > 1:
        history = ""
        rocks = random.random() * 2
        papers = random.random() * 2
        scissorsssss = random.random() * 2

        for play in opponent_history:
            history = history + play

            if play == "R":
                rocks += 1
            elif play == "P":
                papers += 1
            else:
                scissorsssss += 1

        if random.random() > 0.1:
            if rocks > papers and rocks > scissorsssss:
                guess = "P"
            elif papers > rocks and papers > scissorsssss:
                guess = "S"
            elif scissorsssss > papers and scissorsssss > rocks:
                guess = "R"
        else:
            memory = random.choice(history)
            if memory == "R":
                guess = "S"
            elif prev_play == "P":
                guess = "R"
            else:
                guess = "P"
    

    return guess
