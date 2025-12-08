import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


def get_ticker_info(ticker_symbol: str) -> dict:
    """
    Fetches the full info dictionary for a given stock ticker.

    Parameters
    ----------
    ticker_symbol : str
        Stock ticker symbol (e.g., "AAPL").

    Returns
    -------
    dict
        A dictionary containing company fundamental data returned by yfinance.
    """
    return yf.Ticker(ticker_symbol).info


def get_pe_ratio(info: dict):
    """
    Returns the Price/Earnings (P/E) ratio.

    Parameters
    ----------
    info : dict
        Ticker.info dictionary.

    Returns
    -------
    float or None
        Trailing P/E ratio if available.
    """
    return info.get("trailingPE")


def get_historical_pe_ratio(ticker_symbol: str, period: str = "1y") -> pd.Series:
    """
    Returns calculated historical Price/Earnings (P/E) ratio.
    
    Parameters
    ----------
    ticker_symbol : str
        Stock ticker symbol (e.g., "AAPL").
    period : str
        Okres historyczny (np. "1y", "6mo", "3mo").

    Returns
    -------
    pd.Series
        Seria Pandas z historycznymi wskaźnikami P/E (indeks to data).
    """
    ticker = yf.Ticker(ticker_symbol)
    
    # 1. Pobierz historyczne ceny zamknięcia (Close)
    hist = ticker.history(period=period)
    
    if hist.empty:
        print(f"Brak danych historycznych dla {ticker_symbol}.")
        return pd.Series()

    # 2. Pobierz ostatni dostępny Zysk na Akcję (EPS) (Trailing EPS)
    # Jest to wartość aktualna. Yfinance nie udostępnia łatwo historycznej serii EPS.
    info = ticker.info
    trailing_eps = info.get("trailingEps")
    
    if trailing_eps is None or trailing_eps <= 0:
        print(f"Brak lub zerowy trailingEps dla {ticker_symbol}. Nie można obliczyć P/E.")
        return pd.Series(index=hist.index)
        
    # 3. Oblicz P/E dla każdego dnia: Cena zamknięcia / EPS
    # Zakładamy, że trailing_eps jest stały w danym okresie.
    historical_pe = hist['Close'] / trailing_eps
    
    # Zmień nazwę serii na 'Historical PE Ratio'
    historical_pe.name = 'Historical PE Ratio'
    
    return historical_pe



def get_pb_ratio(info: dict):
    """
    Returns the Price/Book (P/B) ratio.
    """
    return info.get("priceToBook")


def get_ps_ratio(info: dict):
    """
    Returns the Price/Sales (P/S) ratio.
    """
    return info.get("priceToSalesTrailing12Months")


def get_ev_ebitda(info: dict):
    """
    Calculates the EV/EBITDA ratio.

    Returns
    -------
    float or None
        EV/EBITDA if both enterprise value and EBITDA are available.
    """
    ev = info.get("enterpriseValue")
    ebitda = info.get("ebitda")

    if ev is not None and ebitda not in (None, 0):
        return ev / ebitda
    return None


def get_eps(info: dict):
    """Returns Earnings Per Share (EPS)."""
    return info.get("trailingEps")


def get_roe(info: dict):
    """Returns Return on Equity (ROE)."""
    return info.get("returnOnEquity")


def get_roa(info: dict):
    """Returns Return on Assets (ROA)."""
    return info.get("returnOnAssets")


def get_de_ratio(info: dict):
    """Returns the Debt-to-Equity (D/E) ratio."""
    return info.get("debtToEquity")


def get_current_ratio(info: dict):
    """Returns the Current Ratio."""
    return info.get("currentRatio")


def get_quick_ratio(info: dict):
    """Returns the Quick Ratio (Acid Test)."""
    return info.get("quickRatio")


def get_gross_margin(info: dict):
    """Returns the Gross Margin."""
    return info.get("grossMargins")


def get_operating_margin(info: dict):
    """Returns the Operating Margin."""
    return info.get("operatingMargins")


def get_net_profit_margin(info: dict):
    """Returns the Net Profit Margin."""
    return info.get("profitMargins")


def get_free_cash_flow(info: dict):
    """Returns the Free Cash Flow."""
    return info.get("freeCashflow")


def get_dividend_yield(info: dict):
    """Returns the Dividend Yield."""
    return info.get("dividendYield")