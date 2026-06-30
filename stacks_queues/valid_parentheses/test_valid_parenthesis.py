import pytest
from stacks_queues.valid_parentheses.valid_parenthesis import ValidParenthesis
from stacks_queues.valid_parentheses.solution import ValidParenthesisSolution

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
