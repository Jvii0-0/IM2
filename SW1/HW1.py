# Currency conversion rates (as of current estimation, can be updated)
USD_TO_INR = 83.26
USD_TO_GBP = 0.789
USD_TO_CNY = 7.26

def convert_and_display(dollar_amounts):
    print(f"\n{'Dollar ($)':<15}{'Indian Rupee (₹)':<20}{'British Pound (£)':<20}{'Chinese Yuan (¥)':<20}")
    for amount in dollar_amounts:
        try:
            usd = float(amount)
            inr = usd * USD_TO_INR
            gbp = usd * USD_TO_GBP
            cny = usd * USD_TO_CNY
            print(f"{usd:<15.2f}{inr:<20.2f}{gbp:<20.2f}{cny:<20.2f}")
        except ValueError:
            print(f"Invalid input: {amount}")

# Main loop
while True:
    user_input = input("Enter dollar ($) (* to exit): ")
    if user_input.strip() == '*':
        print("Bye")
        break
    else:
        dollar_list = user_input.strip().split('@')
        convert_and_display(dollar_list)
