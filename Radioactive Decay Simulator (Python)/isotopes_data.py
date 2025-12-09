# isotopes_data.py
# Słownik popularnych izotopów z half-life w latach lub dniach (dla krótkiego życia)
from isotope import Isotope

ISOTOPES = {
    "Cs-137": Isotope("Cs-137", 30.17),        # lata
    "Co-60": Isotope("Co-60", 5.27),           # lata
    "I-131": Isotope("I-131", 8/365),          # dni → lata
    "Am-241": Isotope("Am-241", 432.2),        # lata
    "Sr-90": Isotope("Sr-90", 29),             # lata
    "U-238": Isotope("U-238", 4.47e9),         # lata
    "Ir-192": Isotope("Ir-192", 73.8/365),     # dni → lata
    "C-14": Isotope("C-14", 5730/365),         # dni → lata
    "K-40": Isotope("K-40", 1.248e9),          # lata
    "Th-232": Isotope("Th-232", 1.405e10)      # lata
}
