# Note the messy spacing and casing
data = """  john smith - 1990
SARAH CONNOR - 1984
  kylo REN - 1995
LARA croft - 1992"""

with open("raw_users.txt", "w") as f:
    f.write(data)
with open("raw_users.txt", "r") as file:
    for line in file:
        small = line.lower().split()
        for word in small:
            upper = word[0].upper()
            formatted = upper + word[1:]
            new_sentences = ''.join(formatted)
            print(new_sentences)