#!/usr/bin/env python3
"""
Download Advent of Code input for a specific day.

Requires AOC_SESSION environment variable or .aoc_session file.
Usage:
    python download_input.py 1      # Download day 1 input
    python download_input.py 5 2025 # Download day 5 input for 2025
"""

import sys
import os
import urllib.request
from pathlib import Path
from typing import Optional


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


def download_input(day: int, year: int = 2025) -> Optional[str]:
    """
    Download AoC input for a specific day.

    Args:
        day: Day number (1-25)
        year: Year (default: 2025)

    Returns:
        Input data as string, or None if download fails
    """
    if not 1 <= day <= 25:
        print(f"❌ Error: Day must be between 1 and 25, got {day}")
        return None

    session_cookie = get_session_cookie()
    if not session_cookie:
        print("❌ Error: AOC session cookie not found!")
        print("   Set AOC_SESSION environment variable or create .aoc_session file")
        print("   See README.md for instructions on getting your session cookie")
        return None

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    try:
        headers = {
            "User-Agent": "aoc-client (https://github.com/user/Advent-of-Code-2025)",
            "Cookie": f"session={session_cookie}"
        }

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8").strip()

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Error: Day {day} not found (advent not started yet?)")
        elif e.code == 401:
            print(f"❌ Error: Invalid session cookie")
        else:
            print(f"❌ HTTP Error {e.code}: {e.reason}")
        return None
    except Exception as e:
        print(f"❌ Error downloading input: {e}")
        return None


def save_input(day: int, content: str) -> bool:
    """
    Save input to day folder.

    Args:
        day: Day number
        content: Input content

    Returns:
        True if successful, False otherwise
    """
    day_folder = Path(__file__).parent / f"aoc2025" / f"day{day}"
    input_file = day_folder / "input.txt"

    if not day_folder.exists():
        print(f"❌ Error: day{day} folder not found")
        print(f"   Create it first with: python main.py create {day}")
        return False

    try:
        input_file.write_text(content)
        print(f"✅ Downloaded input for day {day}")
        print(f"   Saved to: {input_file}")
        return True
    except Exception as e:
        print(f"❌ Error saving input: {e}")
        return False


def main() -> None:
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python download_input.py <day> [year]")
        print("Example: python download_input.py 5")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        year = int(sys.argv[2]) if len(sys.argv) > 2 else 2025
    except ValueError:
        print("❌ Error: day and year must be integers")
        sys.exit(1)

    print(f"📥 Downloading input for Day {day} ({year})...")
    content = download_input(day, year)

    if content is not None:
        if save_input(day, content):
            sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()
