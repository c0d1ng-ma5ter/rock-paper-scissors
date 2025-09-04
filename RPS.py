# Neural networks? What's a neural network? This is just if statemets and random stuff!

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
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

        if abs(rocks - papers) <= 50 and abs(papers - scissorsssss) <= 50:
            # Fight random players with random playing
            guess = random.choice("RPS")
            return guess

        if rocks > scissorsssss and papers > scissorsssss: # Detect Quincy-like players

            # This strat works oddly well against him, but not against other bots  
            memory = random.choice(history)
            if memory == "R":
                guess = "S"
            elif prev_play == "P":
                guess = "R"
            else:
                guess = "P"

        else:
            # This strategy is kinda mediocre, but works against all bots
            if rocks > papers and rocks > scissorsssss:
                guess = "P"
            elif papers > rocks and papers > scissorsssss:
                guess = "S"
            elif scissorsssss > papers and scissorsssss > rocks:
                guess = "R"
    

    return guess