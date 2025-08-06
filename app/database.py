from typing import List, Tuple, Dict

from tricount import Expense, calculate_balances, settle_debts


def get_bucket(name: str) -> Tuple[List[Expense], Dict[str, float], List[Tuple[str, str, float]]]:
    if name == '69':
        expenses = [
            ("Antonio", 20.0, ["Antonio", "Luca"], "Parcheggio (20 €)"),
            ("Antonio", 10.0, ["Antonio", "Luca", "Valentino"], "Autostrada (10 €)"),
            ("Antonio", 23.0, ["Antonio", "Luca", "Valentino"], "Benzina (23 €)"),
            ("Antonio", 40.0, ["Antonio", "Luca", "Valentino"], "Pedaggio andata (40 €)"),
            ("Antonio", 5.0, ["Antonio", "Luca", "Valentino"], "Parcheggio (5 €)"),
            ("Luca", 24.0, ["Antonio", "Luca"], "Pranzo in spiaggia (24 €)"),
            ("Luca", 4.0, ["Antonio", "Luca"], "Caffè leccese (4 €)"),
            ("Antonio", 163.0, ["Antonio", "Luca", "Valentino"], "Cena (163 €)"),
            ("Antonio", 18.0, ["Antonio", "Luca", "Valentino"], "Birra (18 €)"),
            ("Valentino", 15.6, ["Antonio", "Luca", "Valentino"], "Colazione (15,60 €)"),
            ("Antonio", 8.4, ["Antonio", "Luca", "Valentino"], "Spesa varia (8,40 €)"),
            ("Valentino", 75.0, ["Antonio", "Luca", "Valentino"], "Noleggio barca (75 €)"),
            ("Luca", 24.0, ["Antonio", "Luca", "Valentino"], "Stracetti (24 €)"),
            ("Luca", 8.0, ["Luca", "Valentino"], "Birra (8 €)"),
            ("Valentino", 16.0, ["Antonio", "Luca", "Valentino"], "Bombette (16 €)"),
            ("Luca", 16.0, ["Antonio", "Luca", "Valentino"], "Bruschette con capocollo (16 €)"),
            ("Antonio", 13.5, ["Antonio", "Valentino"], "Birra e patatine Porto Cesario"),
            ("Antonio", 18.5, ["Antonio", "Luca", "Valentino"], "Aperitivo Skafè al Casotto (frutta pessima)"),
            ("Antonio", 65, ["Antonio", "Luca", "Valentino"], "Benzina andata/ritorno"),
            ("Antonio", 47, ["Antonio", "Valentino"], "Pranzo Punta Prosciutto"),
            ("Antonio", 38.8, ["Antonio", "Luca", "Valentino"], "Pedaggio ritorno (38,80 €)"),
        ]
        net = calculate_balances(expenses)
        settlements = settle_debts(net)
        return expenses, net, settlements
    raise KeyError(f'No bucket found for {name}')