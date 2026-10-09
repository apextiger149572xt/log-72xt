"""Log parsing helper: simple parser for logs with format
YYYY-MM-DD HH:MM:SS [LEVEL] message."""

import re
import argparse
import sys

LOG_RE = re.compile(
    r'^(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<msg>.*)$'
)

def parse_line(line):
    m = LOG_RE.match(line.strip())
    return m.groupdict() if m else None

def main():
    parser = argparse.ArgumentParser(description="Simple log parser")
    parser.add_argument("file", help="Log file to parse")
    parser.add_argument("-l", "--level", help="Filter by level (e.g., ERROR)")
    args = parser.parse_args()

    try:
        with open(args.file) as f:
            for line in f:
                entry = parse_line(line)
                if not entry:
                    continue
                if args.level and entry["level"] != args.level:
                    continue
                print(f'{entry["datetime"]} [{entry["level"]}] {entry["msg"]}')
    except FileNotFoundError:
        sys.exit(f'File not found: {args.file}')

if __name__ == "__main__":
    main()