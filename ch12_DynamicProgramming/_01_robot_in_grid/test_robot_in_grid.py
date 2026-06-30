import pytest
from ch12_DynamicProgramming._01_robot_in_grid.cell import Cell
from ch12_DynamicProgramming._01_robot_in_grid.robot_in_grid import RobotInGrid
from ch12_DynamicProgramming._01_robot_in_grid.solution import RobotInGridSolution

@pytest.mark.parametrize("klass", [RobotInGrid, RobotInGridSolution])
def test_robot_in_grid(klass):
    instance = klass()
    try:
        grid1 = [
            [True, True, True, True],
            [False, False, False, True],
            [True, True, False, True],
            [True, True, False, True]
        ]
        expected1 = [Cell(0,0), Cell(0,1), Cell(0,2), Cell(0,3), Cell(1,3), Cell(2,3), Cell(3,3)]
        assert instance.get_path(grid1) == expected1

        grid2 = [
            [True, True, True, True],
            [False, True, True, True],
            [True, True, False, False],
            [True, True, True, True]
        ]
        expected2 = [Cell(0,0), Cell(0,1), Cell(1,1), Cell(2,1), Cell(3,1), Cell(3,2), Cell(3,3)]
        assert instance.get_path(grid2) == expected2
    except NotImplementedError:
        pytest.skip("RobotInGrid is not implemented yet")
