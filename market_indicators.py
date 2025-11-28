import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

"""
Minimalna wersja do implementacji w pierwszej kolejności:
P/E
P/B
EV/EBITDA
EPS
ROE
ROA
D/E (Debt-to-Equity)
Current Ratio
Free Cash Flow
Net Profit Margin



Wskaźniki fundamentalne do implementacji w InvestScanner:

1. P/E (Price/Earnings Ratio)
Relacja ceny do zysku.
Najpopularniejszy wskaźnik wyceny.
Pozwala ocenić, czy akcja jest droga/tania względem zysku.

2. P/B (Price/Book Ratio)
Cena akcji do wartości księgowej.
Dobre dla spółek kapitałowych (np. banki).

3. P/S (Price/Sales Ratio)
Cena do przychodów.
Użyteczne gdy firma ma mały lub zerowy zysk.

4. EV/EBITDA
Kluczowy wskaźnik do wyceny przedsiębiorstw (bardziej kompletny niż P/E).
Uwzględnia dług.

5. EPS (Earnings Per Share)
Zysk na akcję.
Często wykorzystywany także do obliczeń P/E.

6. ROE (Return on Equity)
Zwrot na kapitale własnym.
Pokazuje efektywność wykorzystania kapitału.

7. ROA (Return on Assets)
Zwrot na aktywach.
Wskaźnik efektywności majątku spółki.

8. Debt-to-Equity (D/E)
Stosunek zadłużenia do kapitału własnego.
Podstawowy wskaźnik ryzyka finansowego.

9. Current Ratio
Wskaźnik płynności podstawowej: aktywa obrotowe / zobowiązania krótkoterminowe.

10. Quick Ratio (Acid Test)
Jak wyżej, ale wyłącza zapasy.

11. Gross Margin
Marża brutto.
Pokazuje efektywność produkcji / usług.

12. Operating Margin
Marża operacyjna (EBIT margin).
Bardzo istotna przy analizie rentowności.

13. Net Profit Margin
Marża zysku netto.
Ostateczna rentowność biznesu.

14. Free Cash Flow (FCF)
Najważniejszy wskaźnik zdrowia finansowego i możliwości inwestycyjnych spółki.

15. Dividend Yield
Dla spółek dywidendowych.
Stosunek dywidendy do ceny akcji.

"""