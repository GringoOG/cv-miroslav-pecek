#!/usr/bin/env python3
"""Vygeneruje 1-stránkové A4 PDF přesně podle HTML (screenshot → PDF)."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"
OUT = ROOT / "Miroslav_Pecek_CV.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# A4 @ 2× (150 dpi ≈ 2× 96dpi CSS px for 210×297 mm)
W, H = 1588, 2246  # 794*2 × 1123*2


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "cv.png"
        url = HTML.as_uri() + "?pdf=1"
        cmd = [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={W},{H}",
            "--force-device-scale-factor=1",
            f"--screenshot={png}",
            "--virtual-time-budget=10000",
            "--run-all-compositor-stages-before-draw",
            url,
        ]
        subprocess.run(cmd, check=True, capture_output=True)

        # Ořízni přesně na A4 poměr z viewportu (Chrome může přidat okraje)
        # Vlož screenshot na A4 PDF stránku
        doc = fitz.open()
        page = doc.new_page(width=595.28, height=841.89)  # A4 pt
        # použij celý screenshot — Chrome window = A4 CSS px
        # Převzorkuj okno na přesné A4: screenshot má velikost viewportu
        rect = page.rect
        page.insert_image(rect, filename=str(png), keep_proportion=False)
        doc.save(OUT)
        doc.close()

    print(f"OK → {OUT}")


if __name__ == "__main__":
    main()
