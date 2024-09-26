from faker import Faker
fake = Faker()

# print('####################### Female names')
# for i in range(0, 10):
#     print(fake.unique.name_female())

# print('####################### Male names')
# for i in range(0, 10):
#     print(fake.unique.name_male())

# f = open("input/male.txt", "r")
# print(f.read())

def generateMaleNameEndingWith(letter):
    name = ""
    while True:
        name = fake.name_male()
        if(name[-1] == letter):
            # print(name)
            break
    return name

def generateFemaleNameEndingWith(letter):
    name = ""
    N = len(letter)
    while True:
        name = fake.name_female()
        if(name[-N:] == letter):
            # print(name)
            break
    return name

def deduplicate(fileName):
    # Read File
    with open(fileName) as file:
        lines = [line.rstrip() for line in file]
    dedupedList = list(dict.fromkeys(lines))
    
    # Clear file
    with open(fileName,'w') as file:
        file.write("")

    # Write back deduped list to file
    with open(fileName,'a') as file:
        for line in dedupedList:
            file.write(line + "\n")

with open("input/male.txt", "a") as f:
    f.write("\n")
    for i in range(0, 500):
        f.write(generateMaleNameEndingWith('y') + "\n")

deduplicate("input/male.txt")

with open("input/female.txt", "a") as f:
    f.write("\n")
    for i in range(0, 500):
        f.write(generateFemaleNameEndingWith('hy') + "\n")

deduplicate("input/female.txt")