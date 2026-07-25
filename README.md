# CV Template — Miroslav Peček

Dvě jazykové verze, stejný layout A4:

| Soubor | Jazyk | PDF |
|--------|-------|-----|
| `index.html` | EN | `Miroslav_Pecek_CV_EN.pdf` |
| `index-cz.html` | CZ | `Miroslav_Pecek_CV_CZ.pdf` |

Sdílené: `styles.css`, `app.js`, `photo.png`

## Otevření

```bash
open /Users/mircekspace/muj-projekt/cv-template/index.html      # EN
open /Users/mircekspace/muj-projekt/cv-template/index-cz.html   # CZ
```

## PDF

V prohlížeči: **Tisk / PDF** → Uložit jako PDF (okraje: None)

Nebo:

```bash
cd /Users/mircekspace/muj-projekt/cv-template
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --window-size=1200,1700 --print-to-pdf="Miroslav_Pecek_CV_EN.pdf" \
  --virtual-time-budget=10000 "file://$PWD/index.html?pdf=1"

"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --window-size=1200,1700 --print-to-pdf="Miroslav_Pecek_CV_CZ.pdf" \
  --virtual-time-budget=10000 "file://$PWD/index-cz.html?pdf=1"
```
