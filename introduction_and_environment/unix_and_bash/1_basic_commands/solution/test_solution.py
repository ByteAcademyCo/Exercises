import solution
from hashlib import sha1

def test_solution():
    def hashed_output(submission):
        return sha1(submission.encode()).hexdigest()

    assert hashed_output(solution.ONE) == '8175e3c8753aeb1696959f72ede260ebf3ea14c5'
    assert hashed_output(solution.TWO) == 'ebfdec641529d4b59a54e18f8b0e9730f85939fb'
    assert hashed_output(solution.THREE) == '90868ffdfa3a8bd99cfa9f642349e60cf84e057a'
    assert hashed_output(solution.FOUR) == 'f4d1f0193879cba82d65c5752c4ba5cbb43a7188'
    assert hashed_output(solution.FIVE) == '3f81e91d69a8a61ffbf19297eb0791ad54ce5690'
    assert hashed_output(solution.SIX) == '362d60cb3f6f8e96c37edac670b7618963233e07'
    assert hashed_output(solution.SEVEN) == '5cd7e29c88170aa3f16281e0dbf5772c137f6d8d'
