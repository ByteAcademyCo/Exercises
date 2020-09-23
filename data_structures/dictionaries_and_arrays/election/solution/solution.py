def election_winner(clst):
    # create a dict to store the names of candidates as keys
    # and the number of votes for that candidate as the value
    candidate_dict = {}
    # itterate through the votes
    for c in clst:
        # if it is a new candidate we havent seen yet
        # add it to our dict and set the value of votes to 1.
        if c not in candidate_dict:
            candidate_dict[c] = 1
        # otherwise increment the votes for that candidate by 1
        else:
            candidate_dict[c] += 1
    # keep track of maximal votes we've seen so far
    max_votes = 0
    # keep track of winner so far
    winner = ""
    for cname, num_votes in candidate_dict.items():
        # if the current candidate beats the max so far
        # we update the max and set the winner so far 
        # to this candidate.
        if num_votes > max_votes:
            max_votes = num_votes
            winner = cname
        # if this candidate is tied with the max so far
        # we compare the name, if it is less than winners
        # name we update the winner so far.
        elif num_votes == max_votes and cname < winner:
            winner = cname
    return winner
