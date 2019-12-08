min = 284639
max = 748759

passwords = []
strict_passwords = []

for i in range(min, max):
    is_consecutive = False
    is_decreasing = True

    stringed = str(i)

    for k in range(6):
        if k < 5 and stringed[k] == stringed[k+1]:
            is_consecutive = True

    if is_consecutive:
        for k in range(6):
            if k < 5 and stringed[k] > stringed[k+1]:
                is_decreasing = False
                break

        if is_decreasing:
            passwords.append(i)
    else:
        continue

print(len(passwords))

for i in passwords:
    stringed = str(i)

    groups = []

    for k in range(6):
        if (k < 5 and stringed[k] == stringed[k+1]) or (stringed[k-1] == stringed[k]):
            added = False
            for group in groups:
                if stringed[k] in group:
                    group.append(stringed[k])
                    added = True

            if not added:
                groups.append([stringed[k]])

    for group in groups:
        if len(group) == 2:
            strict_passwords.append(i)
            break

print(len(strict_passwords))


