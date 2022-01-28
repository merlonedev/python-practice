def bigger_name(names):
    bigger=''
    for name in names:
        if len(name) > len(bigger):
            bigger = name
        else:
            bigger = bigger
    return bigger

print(bigger_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
