import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import market_indicators

def plot_pe_ratio_trend_from_series(
    pe_series: pd.Series, 
    ticker_symbol: str, 
    period: str = "1y"
):
    """
    Wyświetla historyczny trend wskaźnika P/E, przyjmując dane jako pd.Series.
    
    Parameters
    ----------
    pe_series : pd.Series
        Seria Pandas z historycznymi wskaźnikami P/E (indeks to data).
    ticker_symbol : str
        Symbol akcji (używany tylko do tytułu wykresu).
    period : str
        Okres historyczny (używany tylko do tytułu wykresu).
    """
    
    # Krok 1: Weryfikacja danych (zastępuje pobieranie danych)
    if pe_series.empty:
        print(f"Otrzymana seria P/E jest pusta dla {ticker_symbol}. Nie można stworzyć wykresu.")
        return
        
    # Krok 2: TWORZENIE WYKRESU
    fig, ax = plt.subplots(figsize=(12, 6))

    # Rysowanie linii
    ax.plot(pe_series.index, pe_series.values, 
            label=f'P/E Ratio Trend ({ticker_symbol})',
            color='teal',
            linewidth=2)

    # Krok 3: DODAWANIE OPISÓW I STYLIZACJA
    ax.set_title(f'Trend Wskaźnika P/E dla {ticker_symbol} (Okres: {period})', fontsize=16)
    ax.set_xlabel('Data', fontsize=12)
    ax.set_ylabel('Wskaźnik P/E', fontsize=12)
    
    # Dodanie linii siatki
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Formatowanie dat na osi X dla lepszej czytelności
    fig.autofmt_xdate()

    # Dodanie poziomej linii średniej
    mean_pe = pe_series.mean()
    ax.axhline(mean_pe, color='red', linestyle=':', linewidth=1.5, 
               label=f'Średnia P/E ({mean_pe:.2f})')
    
    # Dodanie legendy
    ax.legend(loc='upper left')
    
    # Krok 4: WYŚWIETLANIE WYKRESU
    plt.tight_layout()
    plt.show()