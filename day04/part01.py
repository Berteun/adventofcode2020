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
    mandatory = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional = {"cid"}
    known = mandatory | optional
    valid = 0
    for passport in passports:
        fields = set(passport.keys())
        valid += mandatory.issubset(fields) # and fields.issubset(known)
    return valid

def main():
    passports = read_passports()
    valid = count_valid(passports)
    print(valid)

if __name__ == '__main__':
    main()
