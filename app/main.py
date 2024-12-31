import sys

from dataclasses import dataclass
import sqlparse

database_file_path = sys.argv[1]
command = sys.argv[2]

if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:        
        database_file.seek(16)  # Skip the first 16 bytes of the header
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        num_tables = sum(line.count(b"CREATE TABLE") for line in database_file)
        print(f"database page size: {page_size}")
        print(f"number of tables: {num_tables}")

else:
    print(f"Invalid command: {command}")
