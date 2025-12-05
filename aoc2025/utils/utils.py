"""
Utility functions for Advent of Code 2025
"""

import inspect
from pathlib import Path
from typing import Any, List, Optional, Union


def read_input(filename: str = "input.txt", split: bool = True, split_by: str = "\n", test: bool = False) -> Union[str, List[str]]:
    """
    Read input file relative to the calling script.

    Args:
        filename: Name of the file to read (default: input.txt)
        split: Whether to split by newlines (default: True)
        test: If True, read test.txt instead (default: False)

    Returns:
        String or list of strings depending on split parameter
    """
    # Get the calling frame's file path
    frame = inspect.currentframe()
    if frame is None or frame.f_back is None:
        raise RuntimeError("Unable to determine caller's file path")

    caller_file = frame.f_back.f_globals.get("__file__")
    if caller_file is None:
        raise RuntimeError("Unable to determine caller's file path")

    caller_dir = Path(caller_file).parent

    # If test=True, override filename to test.txt
    if test:
        filename = "test.txt"

    file_path = caller_dir / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    content = file_path.read_text().strip()

    if split:
        return content.split(split_by)
    return content


def to_grid(data: Union[str, List[str]], to_int: bool = False) -> List[List[Union[str, int]]]:
    """
    Convert string or list of strings to a 2D grid.

    Args:
        data: String or list of strings to convert
        to_int: If True, convert each character to int (default: False)

    Returns:
        2D list representing the grid
    """
    if isinstance(data, str):
        lines = data.split("\n")
    else:
        lines = data

    if to_int:
        return [[int(char) for char in line] for line in lines]
    return [list(line) for line in lines]


def grid_rotate(grid: List[List[Any]], times: int = 1) -> List[List[Any]]:
    """
    Rotate grid 90 degrees clockwise.

    Args:
        grid: 2D list to rotate
        times: Number of times to rotate (default: 1)

    Returns:
        Rotated grid
    """
    times = times % 4  # Only need to rotate 0-3 times
    result = [row[:] for row in grid]  # Copy grid

    for _ in range(times):
        result = [list(row) for row in zip(*reversed(result))]

    return result


def grid_get(grid: List[List[Any]], row: int, col: int, default: Any = None) -> Any:
    """
    Safely get a value from the grid with boundary checking.

    Args:
        grid: 2D list to access
        row: Row index
        col: Column index
        default: Value to return if out of bounds (default: None)

    Returns:
        Value at grid[row][col] or default if out of bounds
    """
    if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
        return grid[row][col]
    return default


def grid_find(grid: List[List[Any]], target: Any) -> Optional[tuple[int, int]]:
    """
    Find the first occurrence of target in grid.

    Args:
        grid: 2D list to search
        target: Value to find

    Returns:
    """
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                return (x, y)
    return None


def grid_find_all(grid: List[List[Any]], target: Any) -> List[tuple[int, int]]:
    """
    Find all occurrences of target in grid.

    Args:
        grid: 2D list to search
        target: Value to find

    Returns:
        List of (x, y) tuples where target is found
    """
    results = []
    for y, row_data in enumerate(grid):
        for x, cell in enumerate(row_data):
            if cell == target:
                results.append((x, y))
    return results


def grid_print(grid: List[List[Any]]) -> None:
    """
    Print a formatted grid to stdout.

    Args:
        grid: 2D list to print
    """
    for row in grid:
        print("".join(str(cell) for cell in row))
