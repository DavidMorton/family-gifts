import random

names = {
    'David': 3,
    'Jennifer': 3,
    'Jakob': 3,
    'Liam': 3,
    'Daniel': 1,
    'Amanda': 1,
    'Rachel': 1,
    'Joshua': 1,
    'Lucas': 1,
    'Matt': 2,
    'Shannon': 2,
    'Elizabeth': 2,
    'Samuel': 2,
    'Abby': 2,

}

success = False
while not success:
    try:
        assignments = {}

        gifter = list(names.keys())[0]

        while len(assignments) < len(names):
            possible_giftees = [x for x in names if (x not in assignments.values()) and (names[x] != names[gifter])]
            giftee = random.choice(possible_giftees)
            assignments[gifter] = giftee
            gifter = giftee
        success = True
    except:
        pass

for gifter, giftee in assignments.items():
    print(f'{gifter} buys for {giftee}.')