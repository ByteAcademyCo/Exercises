def election_winner(clst):
    candidate_dict = {}
    for r in clst:
        if r not in candidate_dict:
            candidate_dict[r] = 1
        else:
            candidate_dict[r] += 1
    max_votes = 0
    winner =""
    for cname, num_votes in candidate_dict.items():
        if num_votes > max_votes:
            max_votes = num_votes
            winner = cname
        elif num_votes == max_votes and cname < winner:
            winner = cname
    return winner