import sys
from solutions.SUM import sum_solution

sys.path.append("/Users/emmanuel/Desktop/accelerate_runner")

# will switch to pycharm will swictch to personal laptop

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3


