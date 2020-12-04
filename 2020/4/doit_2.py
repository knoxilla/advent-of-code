#!/usr/bin/env python3

from collections import defaultdict
import re

from falala import tada

with open("data", "r") as f:
    raw = f.read()

# one line per password, please
data = raw.replace("\n\n", "|").replace("\n", " ").split("|")

required_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

valid_hgts = re.compile("^[0-9]{1,3}[incm]{2}$")
valid_hcls = re.compile("^#[0-9a-f]{6}$")
valid_ecls = "amb blu brn gry grn hzl oth".split()
valid_pids = re.compile("^[0-9]{9}$")

# so we can count 'em up
invalid_reasons = defaultdict(int)


def fully_valid(pport):
    # already checked that all required keys exist

    valid = True

    try:
        byr = int(pport["byr"])
        if byr < 1920 or byr > 2002:
            invalid_reasons["byr"] += 1
            valid = False

        iyr = int(pport["iyr"])
        if iyr < 2010 or iyr > 2020:
            invalid_reasons["iyr"] += 1
            valid = False

        eyr = int(pport["eyr"])
        if eyr < 2020 or eyr > 2030:
            invalid_reasons["eyr"] += 1
            valid = False
    except:
        invalid_reasons["yearparsing"] += 1
        valid = False

    hgt = pport["hgt"]
    if hgt[-2:] in ["in", "cm"]:
        hgt, unit = (int(hgt[:-2]), hgt[-2:])
        # print(hgt,unit)
        if unit == "in":
            if hgt < 59 or hgt > 76:
                invalid_reasons["hgt"] += 1
                valid = False
        if unit == "cm":
            if hgt < 150 or hgt > 193:
                invalid_reasons["hgt"] += 1
                valid = False
    else:
        valid = False

    if pport["ecl"] not in valid_ecls:
        invalid_reasons["ecl"] += 1
        valid = False

    if not valid_hcls.match(pport["hcl"]):
        invalid_reasons["hcl"] += 1
        valid = False

    if not valid_pids.match(pport["pid"]):
        invalid_reasons["pid"] += 1
        valid = False

    return valid


def looks_validish(fields):
    return len(fields) == 8 or (len(fields) == 7 and "cid" not in fields)


def check_passports(data):
    valid = 0
    for row in data:
        pport_parts = row.split(" ")
        pport = {k: v for (k, v) in [tuple(p.split(":")) for p in pport_parts]}
        fields = set(pport.keys())

        if not looks_validish(fields):
            invalid_reasons["notenoughfields"] += 1
            continue

        # if not fields_complete(fields):
        #     invalid_reasons["wrongfields"] += 1
        #     continue

        if fully_valid(pport):
            valid += 1

    tada(f"{valid} out of {len(data)} passports are fully valid.")


if __name__ == "__main__":
    check_passports(data)

    # print("\nInvalid reasons:")
    # for entry in invalid_reasons.items():
    #     print(entry)
