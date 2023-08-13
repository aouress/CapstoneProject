def code(rs):
    letterCode = {0: "R", 1: "I", 2: "A", 3: "S", 4: "E", 5: "C"}
    threeLetters = ""
    n = 0

    while len(threeLetters) < 3:
        print(max(rs))
        if rs[n] == max(rs):
            threeLetters = threeLetters + str(letterCode[n])
            rs[n] = 0
        n = n + 1
        if n > 5:
            n = 0
        if len(threeLetters) >= 4:
            threeLetters = threeLetters[0:3]
            break
        print(rs)
        print(threeLetters)
def main():
    riasecscore = [18, 12, 8, 8, 2, 15]
    code(riasecscore)



main()