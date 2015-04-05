from random  import randint, shuffle

def generate_test(count):
    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]

    result = []

    for name in names:
        result = result + [name] * randint(1, count)
    
    shuffle(result)

    return result

def get_people_count(people):
    count_people = []
    for name in people:
        if name not in count_people:
            count_people += [name]

    return len(count_people)

test = generate_test(5)

print(test)

print(get_people_count(test))
