from typing import List, Tuple

# (tuple of keywords ⟶ matching emoji)
_ICON_MAP: List[Tuple[Tuple[str, ...], str]] = [
    (("grocery", "groceries", "supermarket",
      "spesa", "supermercato", "alimentari"),            "🛒"),  # 1  Groceries
    (("meal", "restaurant", "dinner", "lunch", "food",
      "dining", "breakfast",
      "pasto", "ristorante", "cena", "pranzo", "cibo", "colazione"), "🍽️"), # 2  Dining / Food
    (("coffee", "tea", "café", "cafe",
      "caffè", "bar", "tè"),                             "☕"),   # 3  Coffee & Tea
    (("rent", "housing", "lease",
      "affitto", "casa", "locazione", "alloggio"),       "🏠"),  # 4  Rent / Housing
    (("utilities", "electric", "water bill", "gas bill",
      "internet", "wifi",
      "utenze", "luce", "acqua", "gas", "bollette"),     "💡"),  # 5  Utilities & Bills
    (("bus", "train", "metro", "ticket",
      "public transport",
      "autobus", "treno", "biglietto", "trasporto pubblico"), "🚌"), # 6  Public Transport
    (("taxi", "uber", "lyft", "cab", "rideshare",
      "ncc"),                                            "🚕"),  # 7  Taxi / Ride-share
    (("fuel", "gasoline", "petrol",
      "carburante", "benzina", "gasolio"),               "⛽"),  # 8  Fuel
    (("parking", "toll",
      "parcheggio", "pedaggio"),                         "🅿️"),  # 9  Parking & Tolls
    (("flight", "plane", "airfare", "airport",
      "volo", "aereo", "biglietto aereo", "aeroporto"),  "✈️"),  # 10 Flights
    (("hotel", "motel", "inn", "bnb", "accommodation",
      "alloggio", "locanda"),                            "🏨"),  # 11 Hotels / Lodging
    (("movie", "cinema", "netflix", "concert",
      "show", "entertainment",
      "film", "concerto", "spettacolo", "intrattenimento"), "🎬"), # 12 Entertainment
    (("subscription", "spotify", "prime", "membership",
      "app store", "icloud",
      "abbonamento", "iscrizione"),                      "🎧"),  # 13 Subscriptions
    (("clothes", "clothing", "apparel", "shirt",
      "pants", "shopping",
      "vestiti", "abbigliamento", "camicia",
      "pantaloni"),                                      "👗"),  # 14 Shopping & Clothes
    (("laptop", "phone", "tablet", "electronics",
      "gadget",
      "portatile", "telefono", "elettronica"),           "💻"),  # 15 Electronics
    (("pharmacy", "medicine", "doctor", "health",
      "hospital",
      "farmacia", "medicina", "dottore", "salute",
      "ospedale"),                                       "💊"),  # 16 Health & Pharmacy
    (("gift", "present", "wedding", "birthday",
      "regalo", "matrimonio", "compleanno"),             "🎁"),  # 17 Gifts
    (("book", "tuition", "course", "education",
      "study",
      "libro", "tasse universitarie", "corso",
      "istruzione"),                                     "📚"),  # 18 Education / Books
    (("camp", "tent", "outdoor", "gear",
      "campeggio", "tenda", "escursionismo",
      "attrezzatura"),                                   "⛺"),  # 19 Camping & Outdoor
    (("misc", "other",
      "varie", "altro"),                                 "💸"),  # 20 Miscellaneous
]

def icon_for(description: str) -> str:
    """
    Return an emoji that matches the expense description.
    Falls back to 💸 if nothing matches.
    """
    desc = description.lower()
    for keywords, emoji in _ICON_MAP:
        if any(k in desc for k in keywords):
            return emoji
    return "💸"