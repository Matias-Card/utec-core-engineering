#!/usr/bin/env python3
print("".join("{:c}".format(letter) for letter in range(97, 123) if letter != 101 and letter != 113))
