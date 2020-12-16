def test_solution():
    from solution import election_winner

    clst1 = ["Trump", "Bernie", "Bernie", "Oprah", "Biden", "Bernie", "Trump"]
    assert election_winner(clst1) == "Bernie"

    clst2 = ["Trump", "Bernie", "Bernie", "Trump"]
    assert election_winner(clst2) == "Bernie"

    assert election_winner(["Oprah"]) == "Oprah"


