# 📘 Radioactive Decay Simulator (Python Project)

## 🔬 Overview

This project is a modular, extensible Python toolkit for simulating radioactive decay of isotopes.  
It includes:

- a clean object-oriented model (**Isotope class**),
- a mini isotope database (**isotopes_data.py**),
- a numerical decay engine using **numpy** (**decay_sim.py**),
- and a fully functional command-line interface (**cli.py**) with plotting via **matplotlib**.

The goal is to provide a simple but powerful foundation for nuclear-related simulations — useful for educational purposes, engineering tasks, radiation safety, and scientific demonstrations.

---

## 🧪 Why radioactive decay?

Radioactive decay is one of the most fundamental processes in nuclear engineering, radiation protection, medical physics, and environmental studies.  
Simulating decay helps understand:

- long-term activity of waste,
- radiation exposure from isotopes,
- environmental behavior of radionuclides,
- isotope selection in industrial applications,
- decay chains and equilibrium dynamics.

---

## 🧬 Example: Potassium-40 (K-40)

To demonstrate the tool, we use **Potassium-40**, one of the most interesting naturally occurring radioactive isotopes.

**Why K-40?**

- It has an extremely long half-life: ~1.25 billion years.
- It occurs naturally in bananas, potatoes, cocoa, and many other potassium-rich foods.
- Every human body contains ~140g of potassium → which means we all carry radioactive K-40 inside us.
- A human body emits about 4,000 radiation decays per second (4 kBq) purely from K-40 — and this is perfectly natural and harmless.

Using K-40 as the demo isotope highlights how radioactive decay is not only a reactor or lab process — it's part of everyday life.

---

## 🏗️ Project Structure

project/  
├── isotope.py # Isotope class (half-life, decay law, math utilities)  
├── isotopes_data.py # Built-in isotope mini-database  
├── decay_sim.py # Numerical simulation engine (numpy-based)  
├── cli.py # Command-line interface with plotting support  
└── README.md # Documentation  

**isotope.py**  

Defines the Isotope class:  

- stores name and half-life  
- computes decay constant  
- computes remaining mass/activity after time  
- includes helper textual descriptions for CLI output  

**isotopes_data.py**  

A convenient dictionary of common engineering & radiological isotopes:

- Cs-137  
- Co-60  
- Sr-90  
- Am-241  
- U-238  
- I-131  
- Ir-192  
- C-14  
- K-40  
- Th-232  

This database can be easily extended with additional nuclides.

**decay_sim.py**  

Handles simulation of decay using:

- float-friendly `numpy.arange` for time stepping  
- vectorized numerical evaluation  
- returns arrays for plotting / further analysis  

It is designed to be imported both from:

- CLI  
- interactive Python sessions (Jupyter, VS Code, shell)  

**cli.py**  

A user-friendly interface with `argparse`. You can:

✔ choose isotope  
✔ set initial quantity  
✔ set total time  
✔ set step size  
✔ automatically generate a plot  
✔ save the plot to PNG  

---

## ▶️ Possible to run from command line:

**Basic example: K-40 decay**

```bash
python cli.py K-40 --initial 100 --time 1e9 --step 5e7

Example Output:

Isotope K-40: after 1000000000.0 years, 65.0 units remain from the initial 100.
Plot saved as K-40_decay.png

