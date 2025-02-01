#!/usr/bin/env python

"""
Command Line Interface for running imgFolder tools.

author: Alexandre A. A. Almeida
version: 0.1
"""

from imgFolder import user_interface

if __name__ == "__main__":
    parser = user_interface.set_commands()
    args = parser.parse_args()
    user_interface.main(args)