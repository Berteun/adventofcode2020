import re

def read_passports():
    f = open('input')
    passports = []
    passport = {}
    for line in f:
        if not line.strip():
            passports.append(passport)
            passport = {}
        else:
            pairs = [p.split(":", 2) for p in line.split()]
            passport.update(dict(pairs))
    if passport:
        passports.append(passport)
    return passports

def count_valid(passports):
    def valid_height(v):
        if v.endswith("in"):
            h = v[:-2]
            return h.isdigit() and 59 <= int(h) <= 76
        elif v.endswith("cm"):
            h = v[:-2]
            return h.isdigit() and 150 <= int(h) <= 193
        else:
            return False

    validators =  {
            "byr": lambda v: len(v) == 4 and v.isdigit() and 1920 <= int(v) <= 2002,
            "iyr": lambda v: len(v) == 4 and v.isdigit() and 2010 <= int(v) <= 2020,
            "eyr": lambda v: len(v) == 4 and v.isdigit() and 2020 <= int(v) <= 2030,
            "hgt": lambda v: valid_height(v),
            "hcl": lambda v: re.match("#[0-9a-f]{6}", v),
            "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
            "pid": lambda v: len(v) == 9 and v.isdigit(),
            "cid": lambda v: True
    }

    mandatory = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional = {"cid"}
    known = mandatory | optional
    valid = 0
    for passport in passports:
        fields = set(passport.keys())
        if mandatory.issubset(fields):
            valid += all(validators[k](v) for (k, v) in passport.items())
    return valid

def main():
    passports = read_passports()
    valid = count_valid(passports)
    print(valid)

if __name__ == '__main__':
    main()
