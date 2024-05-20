def pre_sell_tickets():
    available_tickets = 160
    num_tickets_sold = 0
    curr_buyers_count = 0

    while num_tickets_sold < available_tickets:
        try:
            requested_tickets = int(input("How many tickets would you like to buy? (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 1 <= requested_tickets <= 4:
            if num_tickets_sold + requested_tickets > available_tickets:
                print(f"Sorry, we can only sell {available_tickets - num_tickets_sold} more tickets.")
            else:
                num_tickets_sold += requested_tickets
                curr_buyers_count += 1
                print(f"{requested_tickets} tickets sold. {available_tickets - num_tickets_sold} tickets remaining.")
        else:
            print("Please enter a number between 1 and 4.")

    print(f"All tickets sold out. Total number of buyers: {curr_buyers_count}")


pre_sell_tickets()
