#!/usr/bin/python3
import sys

# Initialize variables to hold statistics
file_sizes = []
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            file_sizes.append(file_size)

            if status_code in status_codes:
                status_codes[status_code] += 1

            lines_processed += 1

            if lines_processed % 10 == 0:
                total_file_size = sum(file_sizes)
                print(f"File size: {total_file_size}")
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print(f"{code}: {count}")

        except KeyboardInterrupt:
            total_file_size = sum(file_sizes)
            print(f"File size: {total_file_size}")
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")
            break

except KeyboardInterrupt:
    total_file_size = sum(file_sizes)
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
