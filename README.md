# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) and set up tools/utils.

This year I am doing it again in Python with the hopes of going back and trying it again in go later. 

A rule for myself is I am going to **use no AI besides copilot tab completions** and no hinting what I want to solve with comments. Only after I solve it my self will I go back and see better ways of doing it with an LLM. 

## Progress
- Day 1 ⭐️ ⭐️
- Day 2
- Day 3
- Day 4
- Day 5
- Day 6
- Day 7
- Day 8
- Day 9
- Day 10
- Day 11
- Day 12

## Setup

### Prerequisites
- Python 3.12+
- [UV](https://docs.astral.sh/uv/) (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ItsMacto/Advent-of-Code-2025.git
cd Advent-of-Code-2025
```

2. Sync dependencies with UV:
```bash
uv sync
```

3. (Optional) Set up automatic input downloading:
   - Get your AOC session cookie:
     1. Go to https://adventofcode.com/
     2. Log in
     3. Open browser DevTools (F12)
     4. Go to Application/Storage > Cookies
     5. Find the `session` cookie and copy its value

   - Create `.aoc_session` file in the project root:
     ```bash
     echo "YOUR_SESSION_COOKIE_HERE" > .aoc_session
     ```

   - Or set environment variable:
     ```bash
     export AOC_SESSION="YOUR_SESSION_COOKIE_HERE"
     ```

## Usage

### Create a new day
```bash
python main.py create 1
```
This creates a folder structure:
```
aoc2025/day1/
├── day1.py      (boilerplate with star1() and star2() functions)
├── input.txt    (will have your downloaded input if session cookie is set)
└── test.txt     (empty, for test data)
```


### Run solutions
```bash
# Run all days
python main.py

# Run specific day
python main.py run 1
```

## Project Structure

```
Advent-of-Code-2025/
├── main.py                 # CLI for creating and running days
├── download_input.py       # Download inputs from AoC
├── boilerplate.py          # Template for new days
├── pyproject.toml          # UV/Python configuration
├── .aoc_session            # Session cookie (git-ignored)
├── README.md
├── .gitignore
└── aoc2025/
    ├── __init__.py
    ├── utils/
    │   ├── __init__.py
    │   └── utils.py        # Helper functions (grid, input reading, etc.)
    ├── day1/
    │   ├── day1.py
    │   ├── input.txt
    │   └── test.txt
    ├── day2/
    └── ...
```

## Utilities

The `aoc2025/utils/utils.py` module provides helpful functions:

### Input Reading
```python
from aoc2025.utils.utils import read_input

# Read input.txt as list of lines (default)
data = read_input()

# Read without splitting
data = read_input(split=False)

# Read the test.txt file
data = read_input(test=True)

# Read different file
data = read_input("other.txt")
```

#### Other Utils that I use throughout the challenges will be here also like grid handling, etc.

## Solution Template

Each day follows this template:

```python
from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    # Your solution for part 1
    return result


def star2() -> int:
    data = read_input()
    # Your solution for part 2
    return result


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
```

When you run a day's solution, you'll see output like:
```
🎄 Running Day 1:
  ⭐ Star 1: ####
  ⭐ Star 2: ####
```


