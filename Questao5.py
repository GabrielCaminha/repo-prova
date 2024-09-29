string = "O rato roeu a roupa do rei de Roma"
# Usando [::-1]

print(f"{string[::-1]}")

# Usando for

for letra in range(len(string)):
    print(string[-letra-1], end="")
