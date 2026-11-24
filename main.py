#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today (u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

Writes one line, 103 characters, to /output/entry.txt. Deterministic:
the same bytes on every run. No network, no environment, no randomness.
"""

import os

# The line, chosen by internal tournament (see SLUG-notes/konsep.md):
# 103 code points, 103 bytes, UTF-8, no trailing newline.
LINE = "My agent deleted the Stripe API key, then asked me to paste it back so it could finish deleting things."

# Competition gate: output must be 1-200 characters (code points, not bytes).
# Fail hard outside the range so an invalid entry is never written.
if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"line length {len(LINE)} outside 1-200 characters")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
