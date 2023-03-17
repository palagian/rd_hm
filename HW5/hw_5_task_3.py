# Завдання:
# 1. (необов'язкове виконання) Надрукувати наступний патерн, використовуючи цикл в циклі:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for a in range(1, 2):
    print(f"{a}")
    for b in range(2, 3):
        print(f"{a} {b}")
        for c in range(3, 4):
            print(f"{a} {b} {c}")
            for d in range(4, 5):
                print(f"{a} {b} {c} {d}")
                for e in range(5, 6):
                    print(f"{a} {b} {c} {d} {e}")