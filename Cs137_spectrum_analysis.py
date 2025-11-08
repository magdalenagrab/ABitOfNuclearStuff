import numpy as np
import matplotlib.pyplot as plt

# --- Load detector data ---
def load_detector_data(filename):
    """Loads detector data from a text file (energy [keV], counts)."""
    data = np.loadtxt(filename)
    energy, counts = data[:, 0], data[:, 1]
    return energy, counts

# --- Generate a synthetic simulation spectrum ---
def simulated_spectrum(energy):
    """Simulates an energy spectrum with 3 peaks (e.g., Cs-137)."""
    # 3 Gaussian peaks: main one at 662 keV + random background
    peak1 = 1200 * np.exp(-0.5 * ((energy - 662) / 30)**2)
    bulk = 100 * np.exp(-energy / 500)
    noise = np.random.poisson(20, len(energy))
    return peak1 + bulk + noise

# --- Main ---
def main():
    # Load real (simulated) detector data
    energy_data, counts_data = load_detector_data("detector_data.txt")

    # Simulate theoretical spectrum
    energy_sim = np.linspace(0, 1000, 1000)
    counts_sim = simulated_spectrum(energy_sim)
# --- Scale simulation to match detector data ---
    counts_sim = counts_sim * 1.7   # scaling

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(energy_data, counts_data, 'o', label="Detector Data", color="red", alpha=0.7)
    plt.plot(energy_sim, counts_sim, label="Simulated Spectrum", color="blue", linestyle="--")
    plt.title("Cs-137 Energy Spectrum")
    plt.xlabel("Energy [keV]")
    plt.ylabel("Counts per 50 keV per day")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("spectrum_analysis.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
