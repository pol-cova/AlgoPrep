import pytest
from dynamic_programming.generate_parentheses.generate_parenthesis import GenerateParenthesis
from dynamic_programming.generate_parentheses.solution import GenerateParenthesisSolution

@pytest.mark.parametrize("klass", [GenerateParenthesis, GenerateParenthesisSolution])
def test_generate_parenthesis(klass):
    instance = klass()
    try:
        assert instance.generate_parenthesis(1) == ["()"]
        
        res3 = instance.generate_parenthesis(3)
        assert sorted(res3) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    except NotImplementedError:
        pytest.skip("GenerateParenthesis is not implemented yet")
