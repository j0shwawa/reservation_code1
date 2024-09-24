# list for the store reservs
reservations = []

# function to check if a reservation slot is available
def check_availability(date, time):
    for reservation in reservations:
        if reservation['date'] == date and reservation['time'] == time:
            return False  # The slot is already taken
    return True  # The slot is available

# collect user input and make reservation
def create_reservation():
    name = input("Enter your name: ")
    date = input("Enter reservation date (YYYY-MM-DD): ")
    time = input("Enter reservation time (HH:MM): ")
    
    # check availability before creating a reservation
    if check_availability(date, time):
        # dictionary for details
        reservation = {
            "name": name,
            "date": date,
            "time": time
        }
        
        # add reservations to list
        reservations.append(reservation)
        
        # confirmation
        print(f"Reservation created: {reservation}")
    else:
        print(f"Sorry man but {date} at {time} is already booked.")

# function to display all reservations
def view_reservations():
    if not reservations:
        print("No reservations found.")
    else:
        print("Current Reservations:")
        for r in reservations:
            print(f"{r['name']} - {r['date']} at {r['time']}")

# function to cancel a reservation
def cancel_reservation():
    if not reservations:
        print("No reservations found to cancel.")
        return

    name = input("Enter the name for the reservation to cancel: ")
    date = input("Enter the reservation date (YYYY-MM-DD): ")
    time = input("Enter the reservation time (HH:MM): ")

    for reservation in reservations:
        if reservation['name'] == name and reservation['date'] == date and reservation['time'] == time:
            reservations.remove(reservation)
            print(f"Reservation for {name} on {date} at {time} has been canceled.")
            return
    
    print(f"No matching reservation found for {name} on {date} at {time}.")

# main flow
if __name__ == "__main__":
    print("HI! Welcome to the booking reservation that Josh made!")
    
    while True:
        print("\n1. Make a new reservation")
        print("2. View all reservations")
        print("3. Cancel a reservation")
        print("4. Exit (you do NOT want to exit bro trust me)")

        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            create_reservation()
        elif choice == '2':
            view_reservations()
        elif choice == '3':
            cancel_reservation()
        elif choice == '4':
            print("leaving already? alright say goodbye to all your reservations cause i dont have a saving system yet")
            break
        else:
            print("Sorry uhhhhh i think you did something wrong cause i know it's not my code thats wrong.")