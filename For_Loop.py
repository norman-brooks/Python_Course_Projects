# for loop

heroes = ["Superman", "Batman", "Spider-Man"]
for x in heroes:
    print(x)


# Break Statement

heroes = ["Superman", "Batman", "Spider-Man"]
for x in heroes:
    print(x)
    if x == "Batman":
        break

# Continue Statement

heroes = ["Superman", "Batman", "Spider-Man", "Wolverine"]
for x in heroes:
    print(x)
    if x == "Spider-Man":
        continue

# Range Function

for x in range(21):
    print(x)

# Else Keyword

for x in range (2, 10, 2):
    print(x)
else:
    print("We made it!")

