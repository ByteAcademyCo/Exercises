import solution
from hashlib import sha1

def test_solution():
    def hashed_output(submission):
        return sha1(submission.encode()).hexdigest()

    assert hashed_output(solution.ONE) == '1efc27c5f639a389de478c3d2572063bf0b303f0'
    assert hashed_output(solution.TWO) == '649b0028d6ad29d4b0099e6cd227551c19e75c68'
    assert hashed_output(solution.THREE) == '3c8f2856c8f42eb101b62632788173107a857a88'
    assert hashed_output(solution.FOUR) == 'e6e017e01c6c83091049d013bfad653f3fb75d27'
    assert hashed_output(solution.FIVE) == '034778198a045c1ed80be271cdd029b76874f6fc'
    assert hashed_output(solution.SIX) == '2c98f52bc8dc4272160f7ee35acfff3aa3f63676'
