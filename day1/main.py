# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online
def getValue(x):
    x = x.replace("oneight", "18")
    x = x.replace("twone", "21")
    x = x.replace("threeight", "38")
    x = x.replace("fiveight", "58")
    x = x.replace("sevenine", "79")
    x = x.replace("eightwo", "82")
    x = x.replace("eighthree", "83")
    x = x.replace("nineight", "98")

    x = x.replace("one", "1")
    x = x.replace("two", "2")
    x = x.replace("three", "3")
    x = x.replace("four", "4")
    x = x.replace("five", "5")
    x = x.replace("six", "6")
    x = x.replace("seven", "7")
    x = x.replace("eight", "8")
    x = x.replace("nine", "9")

    num = int(''.join(filter(str.isdigit, x)))

    if num < 10:
        return num + num * 10
    return int(str(num)[:1]) * 10 + num % 10


f = open("input.txt", "r")
val = 0
for x in f:
    print(x + " " + str(getValue(x)))
    val += getValue(x)
print(val)


