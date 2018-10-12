[![Build Status](https://travis-ci.com/Qiskit/qiskit-addon-sympy.svg?branch=master)](https://travis-ci.com/Qiskit/qiskit-addon-sympy)

# Qiskit Sympy Provider

This module contains [Qiskit](https://www.qiskit.org/) simulators with Qiskit Sympy Provider. This provider adds to Qiskit two symbolic quantum circuit simulators using [Sympy](https://www.sympy.org/en/index.html). The two types of simulators are:
* Statevector simulator - returns the statevector of a quantum circuit 
* Unitary simulator - returns the unitary representation of a quantum circuit 

## Installation


```
git clone git@github.com:Qiskit/qiskit-sympy-provider.git
cd qiskit-sympy-provider
pip install -e .
```

PIP will handle all dependencies automatically.

## Usage

We recommend to follow the [usage example](examples/sympy_statevector.py). More general information and education on running quantum simulation can be found in the [Qiskit instructions page](https://github.com/Qiskit/qiskit-core) and the Qiskit tutorials.

## Authors 

The Qiskit Sympy Provider was originally authored by Peng Liu, Yael Ben-Haim, and Marco Pistoia. It continues to grow with the help and work of [many people](https://github.com/Qiskit/qiskit-sympy-provider/graphs/contributors) who contribute to the project at different levels.

## License

This project uses the [Apache License Version 2.0 software license](https://www.apache.org/licenses/LICENSE-2.0).
