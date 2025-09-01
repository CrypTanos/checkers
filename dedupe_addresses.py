import re
from pathlib import Path

ADDR_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")

def load_addresses(path: Path) -> list[str]:
    return [l.strip() for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]

def clean(addresses: list[str]) -> list[str]:
    valid = [a for a in addresses if ADDR_RE.match(a)]
    return sorted(set(a.lower() for a in valid))

if __name__ == "__main__":
    src = Path("data/addresses.txt")
    dst = Path("out/clean_addresses.txt")
    if not src.exists():
        raise SystemExit("Put raw addresses into data/addresses.txt")
    cleaned = clean(load_addresses(src))
    dst.write_text("\n".join(cleaned) + "\n", encoding="utf-8")
    print(f"OK - input: {sum(1 for _ in load_addresses(src))}, unique valid: {len(cleaned)} -> {dst}")
