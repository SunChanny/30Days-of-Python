#Credit card validator
card_number = list(input("Please enter your card number: ").strip())

check_digit = card_number.pop()

card_number.reverse()

processed_digits = []

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(digit) * 2

        if doubled_digit > 0:
            doubled_digit = doubled_digit - 9
            
        processed_digits.append(doubled_digit)
    else:
        processed_digits.append(int(digit))

total = int(check_digit) + sum(processed_digits)

if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid")