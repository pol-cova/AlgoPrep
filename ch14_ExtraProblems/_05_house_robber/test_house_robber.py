import pytest
from ch14_ExtraProblems._05_house_robber.house_robber import HouseRobber
from ch14_ExtraProblems._05_house_robber.solution import HouseRobberSolution

@pytest.mark.parametrize("klass", [HouseRobber, HouseRobberSolution])
def test_house_robber(klass):
    instance = klass()
    try:
        assert instance.rob([1, 2, 3, 1]) == 4
        assert instance.rob([2, 14, 8, 3, 4]) == 18
    except NotImplementedError:
        pytest.skip("HouseRobber is not implemented yet")
