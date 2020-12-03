
def serializer():
    numbers = []
    file = open("numbers.txt", "r")
    for x in file:
        numbers.append(int(x))
    return numbers

def part_one(numbers):
    for numb1 in numbers:
        for numb2 in numbers:
            if numb1 + numb2 == 2020:
                return numb1 * numb2


def part_two(numbers):
    for numb1 in numbers:
        for numb2 in numbers:
            for numb3 in numbers:
                if numb1 + numb2 + numb3 == 2020:
                    return numb1 * numb2 * numb3

if __name__ == '__main__':
    numbers = serializer()
    print(part_one(numbers))
    print(part_two(numbers))