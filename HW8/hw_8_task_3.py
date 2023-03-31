# 3. (необов'язкове виконання) Перетворити всі елементи списку типу string в верхній регістр, використовуючи map.

names = ['Andrii', 'anastasiia', 'fedir', 'Marina']

def caps(name):
    return name.upper()

for name in map(caps, names):
    print(name)