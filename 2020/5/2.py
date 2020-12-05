#!/usr/bin/env python3

from falala import tada

with open("input", "r") as f:
    data = f.read().splitlines()

tests = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
answers = [
    "row 44, column 5, seat ID 357",
    "row 70, column 7, seat ID 567",
    "row 14, column 7, seat ID 119",
    "row 102, column 4, seat ID 820",
]

seat_id_data = []

for code in data:
    rowcode, seatcode = code[:7], code[7:]

    row = seat = 0

    for idx, val in enumerate(rowcode):
        half = 2 ** (7 - idx - 1)
        if val == "B":
            row = row + half  # move to the top half

    for idx, val in enumerate(seatcode):
        half = 2 ** (3 - idx - 1)
        if val == "R":
            seat += half  # move to the top half

    seat_id_data.append([row, seat, row * 8 + seat])

seat_ids = sorted([s[2] for s in seat_id_data])

# tada(f"Maximum seat id seen in our data is {max(seat_ids)}")

for idx, id in enumerate(seat_ids):
    next_id = seat_ids[idx + 1]
    if next_id != id + 1:
        my_seat_id = id + 1
        break

tada(f"My seat id is {my_seat_id}")
