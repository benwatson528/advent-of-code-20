from typing import Set


def solve(data: str, required: Set[str], optional: Set[str]) -> int:
    passports = data.split("\n\n")
    valid_passports = 0
    for passport in passports:
        extracted_fields = {}
        for parsed in passport.replace("\n", " ").split(" "):
            if ":" not in parsed:
                continue
            key, value = parsed.split(":")
            extracted_fields[key] = value
        if required.issubset(extracted_fields.keys()):
            valid_passports += 1
    return valid_passports
