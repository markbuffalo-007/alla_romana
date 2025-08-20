from typing import List, Tuple, Dict

from tricount import Expense, calculate_balances, settle_debts

_DB = {
    '69': [
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
    ],
    'trip_puglia_13_17_august_2025': [
        ("Antonio", 19.20, ["Antonio", "Luca"], "Pedaggio (19,20 €)"),
        ("Antonio", 15.60, ["Antonio", "Luca"], "Pedaggio (15,60 €)"),
        ("Antonio", 40.00, ["Antonio", "Luca"], "Panino con pesce (40,00 €)"),
        ("Antonio", 5.00, ["Antonio", "Luca"], "Parcheggio (5,00 €)"),
        ("Luca", 37.50, ["Antonio", "Luca"], "Pranzo festa 18 anni (37,50 €)"),
        ("Antonio", 3.00, ["Antonio", "Luca"], "Caffè (3,00 €)"),
        ("Antonio", 26.00, ["Luca"], "Cena (26,00 €) — Luca paga tutto"),
        ("Antonio", 5.00, ["Antonio", "Luca"], "Parcheggio (5,00 €)"),
        ("Luca", 10.00, ["Antonio"], "Mojito aperitivo sera (10,00 €) — Antonio paga tutto"),
        ("Luca", 12.90, ["Antonio", "Luca"], "Colazione Martinucci (12,90 €)"),
        ("Luca", 10.00, ["Antonio"], "Cena quota pizza di Antonio con coperto (10,00 €) — Antonio paga tutto"),
        ("Antonio", 40.10, ["Antonio", "Luca"], "Campeggio (40,10 €)"),
        ("Antonio", 8.50, ["Antonio", "Luca"], "Parcheggio Monopoli (8,50 €)"),
        ("Antonio", 41.50, ["Luca"], "Cena Monopoli quota Luca (41,50 €)"),
        ("Luca", 7.50, ["Antonio", "Luca"], "Limone e acqua frizzante a Monopoli (7,50 €)"),
        ("Antonio", 5.00, ["Antonio", "Luca"], "Parcheggio Monopoli discoteca (5,00 €)"),
        ("Antonio", 10.00, ["Antonio", "Luca"], "Parcheggio Gargano (10,00 €)"),
        ("Antonio", 36.50, ["Antonio", "Luca"], "Pranzo domenica (36,50 €)"),
        ("Antonio", 27.00, ["Antonio", "Luca"], "Aperitivo (27,00 €)"),
    ],
    'trip_puglia_13_17_august_2025_extra': [
        ("Luca", 71.00, ["Antonio", "Luca"], "Benzina Avezzano–Brindisi (71,00 €)"),
        ("Luca", 60.00, ["Antonio", "Luca"], "Benzina Lecce giorno 1 (60,00 €)"),
        ("Luca", 45.04, ["Antonio", "Luca"], "Benzina Lecce sabato 16 agosto — 27,99 litri (45,04 €)"),
        ("Luca", 6.10, ["Antonio", "Luca"], "Pedaggio (6,10 €)"),
        ("Luca", 74.00, ["Antonio", "Luca"], "Benzina Avezzano finale (74,00 €)"),
    ]
}


def get_bucket(name: str) -> Tuple[List[Expense], Dict[str, float], List[Tuple[str, str, float]]]:
    if _DB.get(name):
        expenses = _DB.get(name)
        net = calculate_balances(expenses)
        settlements = settle_debts(net)
        return expenses, net, settlements
    raise KeyError(f'No bucket found for {name}')
