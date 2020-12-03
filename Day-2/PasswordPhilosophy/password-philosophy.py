def serializer():
    file = open("input.txt", "r")
    passwords = []
    for line in file:
        password = line.split(": ")[1][0:-1]
        not_serialized_range = line.split(": ")[0]
        letter = not_serialized_range[-1]
        range1, range2 = not_serialized_range[0:-2].split("-")
        passwords.append([int(range1), int(range2), letter, password])
    return passwords

def part_one(passwords):
    correct_passwords = 0
    for password in passwords:
        occurencies = password[3].count(password[2])
        if occurencies >= password[0] and occurencies <= password[1]:
            correct_passwords += 1
    return correct_passwords

def part_two(passwords):
    correct_passwords = 0
    for password in passwords:
        occurencies = 0
        if password[3][password[0] - 1] == password[2]:
            occurencies += 1
        if password[3][password[1] - 1] == password[2]:
            occurencies += 1
        if occurencies == 1:
           correct_passwords += 1
    return correct_passwords

if __name__ == '__main__':
    passwords = serializer()
    print(part_one(passwords))
    print(part_two(passwords))