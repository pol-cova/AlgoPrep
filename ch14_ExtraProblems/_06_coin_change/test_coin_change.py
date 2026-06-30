import pytest
from ch14_ExtraProblems._06_coin_change.coin_change import CoinChange
from ch14_ExtraProblems._06_coin_change.solution import CoinChangeSolution

@pytest.mark.parametrize("klass", [CoinChange, CoinChangeSolution])
def test_coin_change(klass):
    instance = klass()
    try:
        assert instance.coin_change([1, 2, 5], 11) == 3
        assert instance.coin_change([2], 3) == -1
    except NotImplementedError:
        pytest.skip("CoinChange is not implemented yet")
