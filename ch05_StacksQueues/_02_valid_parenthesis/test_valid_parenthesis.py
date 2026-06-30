import pytest
from ch05_StacksQueues._02_valid_parenthesis.valid_parenthesis import ValidParenthesis
from ch05_StacksQueues._02_valid_parenthesis.solution import ValidParenthesisSolution

@pytest.mark.parametrize("klass", [ValidParenthesis, ValidParenthesisSolution])
def test_valid_parenthesis(klass):
    instance = klass()
    try:
        assert instance.is_valid("([]){}") is True
        assert instance.is_valid("({)}") is False
        assert instance.is_valid("()[]{}") is True
        assert instance.is_valid("(]") is False
    except NotImplementedError:
        pytest.skip("ValidParenthesis is not implemented yet")
