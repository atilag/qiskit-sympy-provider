# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.
"""
Example use of the symbolic simulator backends, which keep precise forms of
amplitudes.
"""

<<<<<<< HEAD
from qiskit import register, load_qasm_file, execute
from qiskit.backends.sympy import SympyProvider
=======
from qiskit_addon_sympy import SympyProvider
>>>>>>> Adding changes



""" Usage examples for the Sympy Provider """

SyQ = SympyProvider()

# prints the symp
print(SyQ.backends())

<<<<<<< HEAD
<<<<<<< HEAD

if __name__ == "__main__":
    use_sympy_backends()
=======
print(SyQ.backends(name='statevector_simulator_sympy'))
>>>>>>> Adding changes
=======
print(SyQ.backends(name='statevector_simulator_sympy'))

backend = SyQ.get_backend('statevector_simulator_sympy')
print(backend)


# gets the name of the backend.
print(backend.name())

# gets the status of the backend.
print(backend.status())

# returns the provider of the backend
print(backend.provider) 

# gets the configuration of the backend.
print(backend.configuration())

# gets the properties of the backend.
print(backend.properties())
>>>>>>> Adding changes
