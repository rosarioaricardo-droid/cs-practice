# main.py
# Читает таблицу и печатает статистику, сохраняет summary.csv.

from tablestats import read_rows, count_types, total_minutes, to_csv

filename = input().strip()

with open(filename, encoding="utf-8") as table:
    rows = read_rows(table)

types = count_types(rows)

print(len(rows))
print(len(types))
print(total_minutes(rows, "ошибка"))

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(types))
