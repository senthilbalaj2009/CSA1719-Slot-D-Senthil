
rooms = {}

n = int(input("Enter number of rooms: "))

for i in range(n):
    room = input("Enter room name: ")
    status = input("Is the room dirty? (yes/no): ").lower()
    rooms[room] = status

current = input("Enter vacuum cleaner starting room: ")

print("\nVacuum Cleaner Actions:")

for room in rooms:
    if rooms[room] == "yes":
        print("Move to", room)
        print("Clean", room)
        rooms[room] = "no"

print("\nFinal Room Status:")
for room, status in rooms.items():
    print(room, ":", "Clean" if status == "no" else "Dirty")

print("All rooms cleaned!")
