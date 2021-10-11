import random

print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

print(f"abs(-12.5) є рівним {abs(-12.5)}")
print(bin(5))

A = random.randint(0,1)
print("Значить А=True" if A else "Значить А=False")

mas = []
for x in range(1,10):
    mas.append(random.randint(1,10))
print("Масив:", mas)

try:
    print("Що буде якщо", 2/b, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

with open("hi.txt", "r+") as f:
    for line in f:
        if line=="hello world":
            print("hi there")
        else:
            f.write("would  u say hi?")
            print("successfully added some text")

a_lambda = lambda first, last: f'Цей код написав: {last} {first}'
print("Це просто функція:", a_lambda)
print("Це її виклик:", a_lambda('Олег','Чабак'))