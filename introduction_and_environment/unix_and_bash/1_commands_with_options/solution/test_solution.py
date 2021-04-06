import solution
from hashlib import sha1

def test_solution():
    def hashed_output(submission):
        return sha1(submission.encode()).hexdigest()

    assert hashed_output(solution.ONE) == '8f7096f862f1c01437d435b1440612fc5907d76c'
    assert hashed_output(solution.TWO) == '37fa265330ad83eaa879efb1e2db6380896cf639'
    assert hashed_output(solution.THREE) == 'aa2ba3db8235609f178bac463e31eb01c1a9e711'
    assert hashed_output(solution.FOUR) == 'e52fb413040572fbc243c74e29760dd3c9867aea'
    assert hashed_output(solution.FIVE) == 'fda17aa65051cb574d5f9f1cc4c7f3ddbc931735'
    assert hashed_output(solution.SIX) == '3441d7e6e51f18f214ae7f2ca9c6a87fe14deea8'
    assert hashed_output(solution.SEVEN) == 'e120eb80c4d1bc2976a2176f8dd83d0a795725b6'
