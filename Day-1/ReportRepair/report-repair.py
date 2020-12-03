from numbers import numbers

def part_one():
    for numb1 in numbers:
        for numb2 in numbers:
            if numb1 + numb2 == 2020:
                return numb1 * numb2


def part_two():
    for numb1 in numbers:
        for numb2 in numbers:
            for numb3 in numbers:
                if numb1 + numb2 + numb3 == 2020:
                    return numb1 * numb2 * numb3

if __name__ == '__main__':
    print(part_two())