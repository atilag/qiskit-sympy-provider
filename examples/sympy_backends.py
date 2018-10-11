# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.
"""
Example use of the symbolic simulator backends, which keep precise forms of
amplitudes.
"""

from qiskit_addon_sympy import SympyProvider



""" Usage examples for the Sympy simulators """

SyQ = SympyProvider()

print(SyQ.backends())

print(SyQ.backends(name='statevector_simulator_sympy'))