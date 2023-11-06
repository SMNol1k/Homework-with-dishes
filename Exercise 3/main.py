import os

# Список имен файлов (указать имена всех файлов без расширения)
file_names = ['1', '2', '3']  # Пример: 1.txt, 2.txt, 3.txt

# Словарь для хранения количества строк в каждом файле
file_line_counts = {}

# Получение количества строк в каждом файле и сохранение в словаре
for name in file_names:
    with open(f"{name}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        file_line_counts[f"{name}.txt"] = len(lines)

# Сортировка файлов по количеству строк
sorted_files = sorted(file_line_counts.items(), key=lambda x: x[1])

# Запись содержимого файлов в результирующий файл с предварительной служебной информацией
with open("result.txt", "w", encoding="utf-8") as result_file:
    for file_name, line_count in sorted_files:
        result_file.write(f"{file_name}\n{line_count}\n")
        with open(file_name, "r", encoding="utf-8") as source_file:
            result_file.write(source_file.read())