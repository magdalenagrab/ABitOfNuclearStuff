import argparse
from isotopes_data import ISOTOPES
from decay_sim import simulate_decay, plot_decay

def main():
    parser = argparse.ArgumentParser(description="Simulate radioactive decay of isotopes.")
    parser.add_argument("isotope", type=str, choices=ISOTOPES.keys(), help="Name of the isotope")
    parser.add_argument("--initial", type=float, default=100.0, help="Initial amount of substance")
    parser.add_argument("--time", type=float, default=50.0, help="Total time to simulate (years)")
    parser.add_argument("--step", type=float, default=1.0, help="Time step (years)")
    parser.add_argument("--save", type=str, default=None, help="Filename to save the plot (optional)")
    args = parser.parse_args()

    isotope = ISOTOPES[args.isotope]
    times, values = simulate_decay(isotope, args.initial, args.time, args.step)

    print(isotope.decay_description(args.initial, args.time))

    plot_decay(times, values, isotope, save_path=args.save)

if __name__ == "__main__":
    main()
