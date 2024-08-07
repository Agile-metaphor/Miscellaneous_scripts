# Hycacinth

def twosum(string):
    return string.replace(" ", "_").lower()

# Remove numbers from string

def numberRemover(string):
    return "".join([i for i in string if not i.isdigit()])

inpul = input("Enter a string: ")

print(twosum(inpul))
print(numberRemover(inpul))