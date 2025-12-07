import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import market_indicators

# Wizualizacja
def plot_pe_ratio_trend(ticker_symbol: str, period: str = "1y"):
    """
    Pobiera i wyświetla historyczny trend wskaźnika P/E.
    """
    print(f"Pobieranie historycznego P/E dla {ticker_symbol} z okresu {period}...")
    
    # 1. POBIERANIE DANYCH
    try:
        pe_series: pd.Series = get_historical_pe_ratio(ticker_symbol, period=period)
    except Exception as e:
        print(f"Błąd podczas pobierania danych: {e}")
        return

    if pe_series.empty:
        print("Nie udało się pobrać danych P/E do wykresu.")
        return
        
    # 2. TWORZENIE WYKRESU
    fig, ax = plt.subplots(figsize=(12, 6))

    # Rysowanie linii
    ax.plot(pe_series.index, pe_series.values, 
            label=f'P/E Ratio Trend ({ticker_symbol})',
            color='teal',
            linewidth=2)

    # 3. DODAWANIE OPISÓW I STYLIZACJA
    ax.set_title(f'Trend Wskaźnika P/E dla {ticker_symbol} (Okres: {period})', fontsize=16)
    ax.set_xlabel('Data', fontsize=12)
    ax.set_ylabel('Wskaźnik P/E', fontsize=12)
    
    # Dodanie linii siatki
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Formatowanie dat na osi X dla lepszej czytelności
    fig.autofmt_xdate()

    # Dodanie legendy
    ax.legend(loc='upper left')

    # Dodanie poziomej linii średniej (opcjonalnie)
    mean_pe = pe_series.mean()
    ax.axhline(mean_pe, color='red', linestyle=':', linewidth=1.5, 
               label=f'Średnia P/E ({mean_pe:.2f})')
    
    # Dodanie legendy ponownie, aby uwzględnić linię średnią
    ax.legend()
    
    # 4. WYŚWIETLANIE WYKRESU
    plt.tight_layout() # Dopasowuje elementy, aby się nie nakładały
    plt.show()