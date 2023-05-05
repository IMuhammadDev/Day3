print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N ")

final_sum = 0

if size == 'L':
    final_sum += 25
    if add_pepperoni == 'Y':
        final_sum += 3
    if extra_cheese == 'Y':
        final_sum += 1

elif size == 'M':
    final_sum +=20
    if add_pepperoni == 'Y':
        final_sum += 3
    if extra_cheese == 'Y':
        final_sum += 1

elif size == 'S':
    final_sum += 15
    if add_pepperoni == 'Y':
        final_sum += 2
    if extra_cheese == 'Y':
        final_sum += 1

print(f"Your final bill is: ${final_sum}.")