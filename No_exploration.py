user_name = input("Enter your name: ")
fav_no1 = int(input("Enter your first favourite number: "))
fav_no2 = int(input("Enter your second favourite number: "))
fav_no3 = int(input("Enter your third favourite number: "))

print(f"Hello, {user_name}! Let's explore your favorite numbers:")

numbers = [fav_no1, fav_no2, fav_no3]
new_list = []

if fav_no1 % 2 == 0:
    new_list.append((fav_no1, "even"))
else:
    new_list.append((fav_no1, "odd"))

if fav_no2 % 2 == 0:
    new_list.append((fav_no2, "even"))
else:
    new_list.append((fav_no2, "odd"))

if fav_no3 % 2 == 0:
    new_list.append((fav_no3, "even"))
else:
    new_list.append((fav_no3, "odd"))

for item in new_list:
    print(f"The number {item[0]} is {item[1]}.")

squares_list = []
for num in numbers:
    squares_list.append((num, num ** 2))

for item in squares_list:
    print(f"The number {item[0]} and its square: {item}")

total_sum = fav_no1 + fav_no2 + fav_no3
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

is_prime = True
if total_sum > 1:
    for i in range(2, total_sum):
        if total_sum % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
