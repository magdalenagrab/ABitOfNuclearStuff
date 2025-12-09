# isotope.py
import math

class Isotope:
    def __init__(self, name, half_life):
        """Creates an isotope object with its half-life (in years)."""
        self.name = name
        self.half_life = half_life

    def remaining_after_time(self, initial_amount, time):
        """Calculates how much of the substance remains after a given time."""
        remaining = initial_amount * (0.5 ** (time / self.half_life))
        return remaining

    def decay_description(self, initial_amount, time):
        """Returns a description of the decay after a given time."""
        remaining = self.remaining_after_time(initial_amount, time)
        return (f"Isotope {self.name}: after {time} years, "
                f"{remaining:.4f} units remain from the initial {initial_amount}.")

