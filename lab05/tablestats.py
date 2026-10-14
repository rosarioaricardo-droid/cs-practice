# tablestats.py
# Разбор CSV-таблиц без использования модуля csv.


def read_rows(lines):
    """Разбирает CSV с заголовком в список словарей.
    Пустые и короткие строки пропускаются.
    """
    rows = []
    header = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        if header is None:
            header = parts
            continue
        if len(parts) != len(header):
            continue
        row = {}
        for i in range(len(header)):
            row[header[i]] = parts[i]
        rows.append(row)
    return rows


def count_types(rows):
    """Сколько записей каждого типа."""
    counts = {}
    for row in rows:
        kind = row.get("тип", "")
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows, kind):
    """Суммарная длительность записей одного типа, округлённая до десятых."""
    total = 0.0
    for row in rows:
        if row.get("тип") != kind:
            continue
        value = row.get("минуты", "").replace(",", ".")
        try:
            total += float(value)
        except ValueError:
            continue
    return round(total, 1)


def to_csv(counts):
    """Сводка «тип,количество» с заголовком, строки по алфавиту типа."""
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
