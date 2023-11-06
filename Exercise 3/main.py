import os

file_names = ['1', '2', '3']
file_line_counts = {}

for name in file_names:
    with open(f"{name}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        file_line_counts[f"{name}.txt"] = len(lines)

sorted_files = sorted(file_line_counts.items(), key=lambda x: x[1])

with open("result.txt", "w", encoding="utf-8") as result_file:
    for file_name, line_count in sorted_files:
        result_file.write(f"{file_name}\n{line_count}\n")
        with open(file_name, "r", encoding="utf-8") as source_file:
            result_file.write(source_file.read())