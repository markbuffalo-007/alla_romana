from tricount import calculate_balances, settle_debts


def test_one():
    expenses = [
        ("Antonio", 3, ["Antonio", "Luca"], "Parcheggio (20 €)"),
        ("Antonio", 7, ["Antonio", "Luca"], "Autostrada (10 €)")
    ]

    net = calculate_balances(expenses)
    assert net == {'Antonio': 5.0, 'Luca': -5.0}

    settlements = settle_debts(net)
    assert settlements == [('Luca', 'Antonio', 5.0)]


def test_two():
    expenses = [
        ("Antonio", 3, ["Antonio", "Luca"], "Parcheggio (20 €)"),
        ("Luca", 7, ["Antonio", "Luca"], "Autostrada (10 €)")
    ]

    net = calculate_balances(expenses)
    assert net == {'Antonio': -2.0, 'Luca': 2.0}

    settlements = settle_debts(net)
    assert settlements == [('Antonio', 'Luca', 2.0)]


def test_three():
    expenses = [
        ("Luca", 3.50, ["Antonio", "Luca"], ""),
        ("Luca", 58.0, ["Antonio", "Luca"], ""),
        ("Antonio", 9.0, ["Antonio", "Luca"], ""),
    ]

    net = calculate_balances(expenses)
    assert net == {'Antonio': -26.25, 'Luca': 26.25}

    settlements = settle_debts(net)
    assert settlements == [('Antonio', 'Luca', 26.25)]