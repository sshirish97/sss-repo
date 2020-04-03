command = ""
stopped = True
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car 
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if stopped:
            print("Car started. Ready to go!!")
            stopped = False
        else:
            print("Car is already started")
    elif command == "stop":
        if not stopped:
            print("Car stopped.")
            stopped = True
        else:
            print("Car is already stopped")
    elif command == "quit":
        break
    else:
        print("Type something meaningful")