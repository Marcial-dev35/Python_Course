game = "Eldeng Ring"
rate = "10/10"
with open("review.txt", "a") as file:
    file.write(f"Game: {game}, Rating: {rate}\n")

with open("review.txt", "r") as file:
    data_list = file.readlines()
total = len(data_list)
print(f"Total entries: {total}")