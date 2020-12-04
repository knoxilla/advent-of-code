#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from random import choice

doodads = ["❄️ ", "🎅", "🛷", "🎄", "☃️ "]


def tada(message):
    pick = choice(doodads)
    print(f"{pick*3}\n{message}\n{pick*3}")


if __name__ == "__main__":
    tada("hello my old friend")
