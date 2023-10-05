#!/usr/bin/python3
import sys

def main():
    if len(sys.argv) == 1:
        print(0)
    else:
        total = 0
        for arg in sys.argv[1:]:
            try:
                total += int(arg)
            except ValueError:
                pass

        # Print the total sum
        print(total)

if __name__ == "__main__":
    main()
