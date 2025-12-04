#!/usr/bin/env python3
"""
Advent of Code Manager
Handles creating new day folders and running solutions
"""

import sys
import os
import urllib.request
import urllib.error
import importlib.util
from pathlib import Path
from typing import Optional
import argparse
from datetime import datetime
import traceback


def get_current_year() -> int:
    """Get the current year."""
    return datetime.now().year


def get_current_day() -> int:
    """Get the current day in December, or 25 if not December."""
    today = datetime.now()
    if today.month == 12:
        return min(today.day, 25)
    return 25


def validate_day(day: int) -> bool:
    """Validate that day is between 1 and 25."""
    return 1 <= day <= 25


def get_session_cookie() -> Optional[str]:
    """
    Get AOC session cookie from environment or .aoc_session file.

    Returns:
        Session cookie string or None
    """
    # Try environment variable first
    session = os.getenv("AOC_SESSION")
    if session:
        return session

    # Try .aoc_session file
    session_file = Path(__file__).parent / ".aoc_session"
    if session_file.exists():
        return session_file.read_text().strip()

    return None


def download_input(day: int, year: Optional[int] = None, silent: bool = False) -> Optional[str]:
    """
    Download AoC input for a specific day.

    Args:
        day: Day number (1-25)
        year: Year (default: current year)
        silent: If True, don't print error messages (default: False)

    Returns:
        Input data as string, or None if download fails
    """
    if year is None:
        year = get_current_year()

    if not validate_day(day):
        if not silent:
            print(f"❌ Error: Day must be between 1 and 25, got {day}")
        return None

    session_cookie = get_session_cookie()
    if not session_cookie:
        if not silent:
            print("⚠️  AOC session cookie not found - skipping input download")
            print("   Set AOC_SESSION environment variable or create .aoc_session file")
        return None

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    try:
        headers = {
            "User-Agent": "aoc-client",
            "Cookie": f"session={session_cookie}"
        }

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8").strip()

    except urllib.error.HTTPError as e:
        if not silent:
            if e.code == 404:
                print(f"❌ Error: Day {day} not found (advent not started yet?)")
            elif e.code == 401:
                print(f"❌ Error: Invalid session cookie")
            else:
                print(f"❌ HTTP Error {e.code}: {e.reason}")
        return None
    except Exception as e:
        if not silent:
            print(f"❌ Error downloading input: {e}")
        return None


def create_day(day: int, year: Optional[int] = None) -> None:
    """Create a new day folder with boilerplate files and auto-download input."""
    if year is None:
        year = get_current_year()

    if not validate_day(day):
        print(f"❌ Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)

    day_folder = Path(__file__).parent / f"aoc{year}" / f"day{day}"

    if day_folder.exists():
        print(f"⚠️  Day {day} already exists at {day_folder}")
        return

    # Create directory
    day_folder.mkdir(parents=True, exist_ok=True)

    # Read boilerplate and replace year placeholder
    boilerplate_path = Path(__file__).parent / "boilerplate.py"
    boilerplate_content = boilerplate_path.read_text()
    boilerplate_content = boilerplate_content.replace("aoc2025", f"aoc{year}")

    # Create dayX.py
    day_file = day_folder / f"day{day}.py"
    day_file.write_text(boilerplate_content)

    # Create test.txt
    test_file = day_folder / "test.txt"
    test_file.touch()

    print(f"✅ Created day {day} for {year}")
    print(f"   - day{day}.py")
    print(f"   - test.txt")

    # Try to download input
    print(f"\n📥 Attempting to download input...")
    input_content = download_input(day, year, silent=False)

    input_file = day_folder / "input.txt"
    if input_content:
        input_file.write_text(input_content)
        print(f"✅ Downloaded and saved input.txt")
    else:
        input_file.touch()
        print(f"⚠️  Created empty input.txt - add your puzzle input manually or set AOC_SESSION")


def run_day(day: int, year: Optional[int] = None, test: bool = False) -> None:
    """Run a specific day's solution."""
    if year is None:
        year = get_current_year()

    if not validate_day(day):
        print(f"❌ Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)

    day_folder = Path(__file__).parent / f"aoc{year}" / f"day{day}"
    day_file = day_folder / f"day{day}.py"

    if not day_file.exists():
        print(f"❌ Day {day} not found. Create it first with: python main.py create {day}")
        sys.exit(1)

    # Load and run the module
    spec = importlib.util.spec_from_file_location(f"aoc{year}.day{day}", day_file)
    if spec is None or spec.loader is None:
        print(f"❌ Failed to load day{day}")
        sys.exit(1)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, 'star1') or not hasattr(module, 'star2'):
        print(f"❌ day{day}.py must contain star1() and star2() functions")
        sys.exit(1)

    print(f"🎄 Running {year} Day {day}:")
    try:
        result1 = module.star1()
        print(f"  ⭐ Star 1: {result1}")
    except Exception as e:
        print(f"  ❌ Star 1 failed: {e}")
        traceback.print_exc()

    try:
        result2 = module.star2()
        print(f"  ⭐ Star 2: {result2}")
    except Exception as e:
        print(f"  ❌ Star 2 failed: {e}")
        traceback.print_exc()




def main() -> None:
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Advent of Code Multi-Year Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py create 5                # Create day 5 for current year
  python main.py create 5 -y 2024        # Create day 5 for 2024 (short form)
  python main.py create 5 --year 2024    # Create day 5 for 2024
  python main.py run                     # Run current day of current year
  python main.py run 3                   # Run day 3 of current year
  python main.py run 3 -y 2024           # Run day 3 of 2024 (short form)
  python main.py run 3 --year 2024       # Run day 3 of 2024
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new day")
    create_parser.add_argument("day", type=int, help="Day number (1-25)")
    create_parser.add_argument("-y", "--year", type=int, default=None,
                              help="Year (default: current year)")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a day's solution")
    run_parser.add_argument("day", nargs="?", default=None,
                           help="Day number (1-25) (default: current day)")
    run_parser.add_argument("-y", "--year", type=int, default=None,
                           help="Year (default: current year)")

    args = parser.parse_args()

    # Handle no arguments (run current day of current year by default)
    if args.command is None:
        current_year = get_current_year()
        current_day = get_current_day()
        run_day(current_day, current_year)
        return

    if args.command == "create":
        create_day(args.day, args.year)
    elif args.command == "run":
        year = args.year if args.year is not None else get_current_year()
        day = args.day if args.day is not None else get_current_day()
        try:
            run_day(int(day), year)
        except ValueError:
            print(f"❌ Error: Day must be a number, got '{args.day}'")
            sys.exit(1)


if __name__ == "__main__":
    main()
