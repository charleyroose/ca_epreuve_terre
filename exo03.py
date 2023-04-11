import sys

def alphabet_from(letter):
    arg = range(ord(letter), ord('z')+1)
    var = letter

    for num in arg:
        print(var, end="")
        if var == "z":
            break
        var = chr(ord(var) + 1)
    print()

letter = sys.argv[1]
alphabet_from(letter)
