
# ----------------------------------------
# HOTEL MANAGEMENT SYSTEM - DSA PROJECT
# Author: (Your Name)
# ----------------------------------------

class Guest:
    """Class to hold guest details"""
    def __init__(self, name, room_no, days):
        self.name = name
        self.room_no = room_no
        self.days = days
        self.next = None  # for linked list structure


class Hotel:
    """Hotel system using Data Structures"""
    def __init__(self):
        self.head = None         # Linked list head for active guests
        self.waiting_queue = []  # Queue for guests waiting for rooms
        self.checkout_stack = [] # Stack for recently checked-out guests

    # ----------------------------
    # Add guest (Linked List)
    def check_in(self, name, room_no, days):
        new_guest = Guest(name, room_no, days)

        if self.head is None:
            self.head = new_guest
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_guest

        print(f"✅ {name} checked into Room {room_no} for {days} days.\n")

    # ----------------------------
    # Display all checked-in guests
    def display_guests(self):
        if self.head is None:
            print("⚠️ No guests currently checked in.\n")
            return
        print("\n🏨 Current Guests in Hotel:")
        current = self.head
        while current:
            print(f"Name: {current.name}, Room: {current.room_no}, Stay: {current.days} days")
            current = current.next
        print()

    # ----------------------------
    # Search guest by name (Linear Search)
    def search_guest(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                print(f"🔍 Guest Found → {current.name} in Room {current.room_no}, {current.days} days stay.\n")
                return
            current = current.next
        print("❌ Guest not found.\n")

    # ----------------------------
    # Sort guests alphabetically by name (Bubble Sort)
    def sort_guests(self):
        if self.head is None:
            print("⚠️ No guests to sort.\n")
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.name.lower() > current.next.name.lower():
                    current.name, current.next.name = current.next.name, current.name
                    current.room_no, current.next.room_no = current.next.room_no, current.room_no
                    current.days, current.next.days = current.next.days, current.days
                    swapped = True
                current = current.next
        print("✅ Guest list sorted alphabetically!\n")

    # ----------------------------
    # Guest checkout (Stack for history)
    def check_out(self, name):
        prev = None
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.checkout_stack.append(current)
                print(f"🏁 {name} has checked out. Added to history stack.\n")
                return
            prev = current
            current = current.next
        print("❌ Guest not found for checkout.\n")

    # ----------------------------
    # Show last checkout (Top of stack)
    def last_checkout(self):
        if not self.checkout_stack:
            print("⚠️ No checkouts recorded yet.\n")
        else:
            guest = self.checkout_stack[-1]
            print(f"🧾 Last checkout: {guest.name} from Room {guest.room_no}\n")

    # ----------------------------
    # Add to waiting list (Queue)
    def add_to_waiting(self, name):
        self.waiting_queue.append(name)
        print(f"⏳ {name} added to the waiting list.\n")

    # ----------------------------
    # Assign room to next waiting guest
    def assign_room(self, room_no, days):
        if not self.waiting_queue:
            print("✅ No guests in waiting list.\n")
            return
        name = self.waiting_queue.pop(0)
        self.check_in(name, room_no, days)
        print(f"🛏️ Room {room_no} assigned to {name} from waiting list.\n")


# ----------------------------------------
# MAIN MENU SECTION
# ----------------------------------------
hotel = Hotel()

while True:
    print("========= HOTEL MANAGEMENT MENU =========")
    print("1. Check In Guest")
    print("2. Display All Guests")
    print("3. Search Guest")
    print("4. Sort Guests by Name")
    print("5. Check Out Guest")
    print("6. Show Last Checkout")
    print("7. Add to Waiting List")
    print("8. Assign Room to Waiting Guest")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter guest name: ")
        room = input("Enter room number: ")
        days = int(input("Enter number of days: "))
        hotel.check_in(name, room, days)

    elif choice == '2':
        hotel.display_guests()

    elif choice == '3':
        name = input("Enter guest name to search: ")
        hotel.search_guest(name)

    elif choice == '4':
        hotel.sort_guests()

    elif choice == '5':
        name = input("Enter guest name to check out: ")
        hotel.check_out(name)

    elif choice == '6':
        hotel.last_checkout()

    elif choice == '7':
        name = input("Enter name to add to waiting list: ")
        hotel.add_to_waiting(name)

    elif choice == '8':
        room = input("Enter room number to assign: ")
        days = int(input("Enter number of days: "))
        hotel.assign_room(room, days)

    elif choice == '9':
        print("👋 Exiting Hotel Management System. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.\n")
