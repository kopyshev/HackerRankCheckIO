def conjunction(x,y):
    return x and y

def disjunction(x,y):
    return x or y

def implication(x,y):
    return not x or y

def exclusive(x,y):
    return not (x==y)

def equivalence(x,y):
    return (x==y)


def boolean(x, y, operation):
    boolean_operations = {
        "conjunction": conjunction,
        "disjunction": disjunction,
        "implication": implication,
        "exclusive": exclusive,
        "equivalence": equivalence
    }
    func = boolean_operations.get(operation)
    return int(func(x,y))

print(boolean(0, 1, "equivalence"))
