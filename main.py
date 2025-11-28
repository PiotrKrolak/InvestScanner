import sys

import market_indicators

def main(args):
    """
    Wykonanie głównej logiki programu InvestScanner.
    
    Args:
        args (list): Lista argumentów wiersza poleceń (np. sys.argv[1:]).
    """
    # Główna logika programu idzie tutaj
    if len(args) > 0:
        print(f"Arguments of main() function: {args}")
    else:
        print("Activate without arguments")
    
    return 0

if __name__ == "__main__":
    # Ten blok jest wykonywany TYLKO wtedy, gdy skrypt jest 
    # uruchamiany bezpośrednio (np. python moj_skrypt.py)
    # i nie jest wykonywany, gdy skrypt jest importowany jako moduł.
    
    # Przekazujemy argumenty wiersza poleceń (pomijając nazwę skryptu)
    exit_code = main(sys.argv[1:]) 
    
    # Używamy sys.exit() z kodem wyjścia
    sys.exit(exit_code)