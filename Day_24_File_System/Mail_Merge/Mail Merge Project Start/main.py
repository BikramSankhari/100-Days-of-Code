with open("./Input/Names/Invited_names.txt") as input_file:
    names = input_file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as body:
    body = body.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        temp = body.replace("[name]", name)
        file.write(temp)
