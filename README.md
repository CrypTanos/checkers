# checkers

Data formats
- EVM адреси: один рядок = одна адреса, без ком.
- CSV для списків бірж або проєктів, кодування UTF-8.

Usage
- `python src/dedupe_addresses.py`
- Результат у `/out/clean_addresses.txt`.

Conventions
- Лише валідні 0x-адреси.
- Зберігаємо lowercased для стабільності.
