import pyperclip

DAYS = ["ponedjeljak", "utorak", "srijeda", "četvrtak", "petak"]
out_lines = []

input = pyperclip.paste()
lines = input.split("\n")

for line in lines:
    line = line.strip()
    if not line:
        continue
    elif line.lower() in DAYS:
        out_lines.append("*{}*".format(line.upper()))
    else:
        params = line.split()
        food = " ".join(params[:-1])
        price = float(params[-1])
        out_lines.append("* {0} - *{1:0.2f}*".format(food.capitalize(), price))

out =  "\n".join(out_lines)
pyperclip.copy(out)
print(out)
