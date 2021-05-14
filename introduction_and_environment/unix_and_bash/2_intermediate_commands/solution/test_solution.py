import solution
from hashlib import sha1

def test_solution():
    def hashed_output(submission):
        return sha1(submission.encode()).hexdigest()

    assert hashed_output(solution.ONE) == "8d90393573522285c5d58b437885ccbb9a9daced"
    assert hashed_output(solution.TWO) == '6862d5dbed79ab65cf70e169232ad10ea4575373'
    assert hashed_output(solution.THREE) == 'a0d69d758be9fd8be90f83bb3c51c3539c105bdf'
    assert hashed_output(solution.FOUR) == 'e31d24b0d08a712dd0c8155c15259958e43dcd04'
    assert hashed_output(solution.FIVE) == 'd07f1559dea4f7fb83c1a2b0c506646542856acb'
