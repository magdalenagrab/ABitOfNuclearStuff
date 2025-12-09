#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <random>

int main() {
    // --- Parameters ---
    int num_points = 1000;
    std::vector<double> energy;
    std::vector<double> counts;
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::poisson_distribution<> d(20);

    for (int i = 0; i <= num_points; ++i) {
        double e = i; // energy [keV]
        double peak = 1200 * std::exp(-0.5 * std::pow((e - 662)/30, 2));
        double bulk = 100 * std::exp(-e / 500.0);
        double noise = d(gen);
        energy.push_back(e);
        counts.push_back((peak + bulk + noise) * 1.7); // manual scaling
    }

    // --- Save to CSV ---
    std::ofstream outfile("simulated_spectrum.csv");
    outfile << "Energy,Counts\n";
    for (size_t i = 0; i < energy.size(); ++i) {
        outfile << energy[i] << "," << counts[i] << "\n";
    }
    outfile.close();

    std::cout << "Simulation complete. Data saved to simulated_spectrum.csv\n";
    return 0;
}
