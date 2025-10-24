
# TRDES (Python)

Modern, portable CLI edition of legacy TRDES utilities.

**Note:** This build ignores legacy `.DAT`, `.MRS`, and barcode/label-printing paths.
It focuses on text utilities inferred from the historical codebase: combine, split,
search, sort, date/time helpers, simple accumulation, and tokenized command parsing.

## Quick start

```bash
# Option A: run in-place without installing
python -m trdes.cli --help

# Option B: install editable
pip install -e .
trdes --help
```

## Examples

```bash
# Combine all *.log under input/ into combined.txt
trdes combine input --pattern "*.log" --out combined.txt

# Split big.txt into 1000-line chunks under out/
trdes split big.txt --lines 1000 --out out

# Search for ALL tokens (case-insensitive) across tree
trdes search src --tokens "error,timeout" --mode all --ignore-case

# Sort unique lines (numeric by column 2 delimited by ,)
trdes sort data.csv --unique --numeric --key-col 2 --delimiter , --out sorted.csv

# Accumulate sum of column 3 grouped by column 1
trdes accum data.csv --value-col 3 --group-col 1 --delimiter , --out totals.csv

# Date helpers
trdes weekday 2025-10-24
trdes date add 2025-10-24 --days -30

# Parse a command template with tokens
trdes parsecmd "run --port {COM} --user {USER}" --var COM COM3 --var USER gary
```

## License
MIT
