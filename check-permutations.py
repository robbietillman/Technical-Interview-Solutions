


def check_permutations(base, second):
    new_base = base
    new_second = second
    for a in base:
        for b in second:
            print("loop " + b + " ")
            if ((new_base != base) and (new_base != "")):
                print(new_base)
                print(new_second)
                return(print("not a perm"))
            if b == a:
                print(new_base)
                new_base = base.replace(a, "")
                print(new_base)
                new_second = second.replace(b, "")
            if ((new_base == "") & (new_second == "")):
                return(print("string is a permutation"))

print(check_permutations("hio", "hio"))