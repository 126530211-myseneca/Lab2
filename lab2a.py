#!/usr/bin/env python3

import sys

def show_var():
	s_name = sys.argv[0]
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]

	print("Script name:", s_name)
	print("Arguments:", arg1, arg2)
	print("Script name and arguments:", s_name, arg1, arg2)

def helloWorld():
	print("Hello World")


if __name__ == "__main__":
	show_var()
    helloWorld()
