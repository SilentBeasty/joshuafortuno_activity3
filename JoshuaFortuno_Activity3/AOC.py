import math

def cca(radius):
    area = math.pi * radius ** 2
    return area

def aoc():
    io = False

    while True:
        if not io:
            r = float(input("Enter radius: "))
            print("Area of circle:", cca(r))

        ta = str(input("\nTry again? (y/n): "))

        if ta.strip().lower() == "y":
            io = False
            continue
        elif ta.strip().lower() == "n":
            break
        else:
            io = True
            print("Invalid option.")

aoc()