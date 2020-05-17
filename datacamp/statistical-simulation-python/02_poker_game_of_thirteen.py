# Pre-set constant variables
deck, sims, coincidences = np.arange(1, 14), 10000, 0

for _ in range(sims):
    # Draw all the cards without replacement to simulate one game
    draw = np.random.choice(deck, size=len(deck), replace=False)
    # Check if there are any coincidences
    coincidence = (draw == list(np.arange(1, 14))).any()
    if coincidence == True: 
        coincidences += 1

# Calculate probability of winning (or without coincidences = 1 - probability coincidences)
prob_of_winning = 1 - np.sum(coincidences) / 10000
print("Probability of winning = {}".format(prob_of_winning))
