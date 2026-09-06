velkost = int(input("Zadaj velkost tojholnika (1-10):"))


if 1 <= velkost <= 10:
    for i in range(1, velkost + 1):
        print("*" * i)

else:
    print("iba cislo od 1 do 10")