import re

required = {"byr": r"^([1][9][2-9][0-9])|([2][0][0][0-2])$",
            "iyr": "^([2][0][1][0-9])|([2][0][2][0])$",
            "eyr": r"^([2][0][2][0-9])|([2][0][3][0])$",
            "hgt": r"^([1]([5-8][0-9]|[9][0-3])cm)|(([5][9]|[6][0-9]|[7][0-6])in)$",
            "hcl": r"^#(\d|[a-f]){6}$",
            "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
            "pid": r"^\d{9}$"}

optional = {"cid"}


def solve(data: str, validate=False) -> int:
    passports = data.split("\n\n")
    valid_passports = 0
    for passport in passports:
        extracted_fields = extract_fields(passport)
        if set(required.keys()).issubset(extracted_fields.keys()) and validate_values(extracted_fields,
                                                                                      validate):
            valid_passports += 1
    return valid_passports


def extract_fields(passport):
    extracted_fields = {}
    for parsed in passport.replace("\n", " ").split(" "):
        if ":" not in parsed:
            continue
        key, value = parsed.split(":")
        extracted_fields[key] = value
    return extracted_fields


def validate_values(extracted_fields, validate):
    if not validate:
        return True
    else:
        for extracted_field, value in extracted_fields.items():
            if extracted_field not in optional and not re.match(required[extracted_field], value):
                return False
        return True
