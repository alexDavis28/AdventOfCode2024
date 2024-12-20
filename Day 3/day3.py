import re

with open("input.txt", "r") as file:
    text = file.read()

mul_match = r"mul\(\d+,\d+\)"
muls = re.findall(mul_match, text)
num_match = r"\d+"
mul_pairs = [[int(i) for i in re.findall(num_match, mul)] for mul in muls]
mul_products = [a*b for [a,b] in mul_pairs]
print(sum(mul_products))

# Still want to do the second part in a regex but this works
print(text)
text_mod = "do()" + text
print(text_mod)

dosplit = text_mod.split("do()")[1:]
activetext = "".join([i.split("don't()")[0] for i in dosplit])

muls = re.findall(mul_match, activetext)
num_match = r"\d+"
mul_pairs = [[int(i) for i in re.findall(num_match, mul)] for mul in muls]
mul_products = [a*b for [a,b] in mul_pairs]
print(sum(mul_products))
