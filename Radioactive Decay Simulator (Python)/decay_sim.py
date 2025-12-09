import numpy as np
import matplotlib.pyplot as plt

def simulate_decay(isotope, initial_amount, total_time, step):
    """Simulate decay using numpy arange for float steps."""
    times = np.arange(0, total_time + step, step)  # float-friendly
    values = [isotope.remaining_after_time(initial_amount, t) for t in times]
    return times, values


def plot_decay(times, values, isotope, save_path=None):
    """Plot decay for use both in CLI and standalone."""
    plt.figure(figsize=(8, 5))
    plt.plot(times, values, marker='o', linestyle='-', color='teal')
    plt.title(f"{isotope.name} Decay Over Time")
    plt.xlabel("Time (years)")
    plt.ylabel("Remaining units")
    plt.grid(True)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)
        print(f"Plot saved as: {save_path}")

    plt.show()


if __name__ == "__main__":
    from isotopes_data import ISOTOPES

    isotope = ISOTOPES["Cs-137"]
    initial = 100
    total_time = 50
    step = 2

    times, values = simulate_decay(isotope, initial, total_time, step)
    plot_decay(times, values, isotope, save_path="standalone_plot.png")
