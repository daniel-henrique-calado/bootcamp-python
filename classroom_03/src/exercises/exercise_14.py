"""
Simulate attempts to reconnect to a service with a maximum number of attempts.
"""

connection_limit = 5
num_connection = 1

while num_connection <= connection_limit:
    print(f"Attempt to connect to service ({num_connection} of {connection_limit}).")
    connection_status = input("Do you want to proceed (y/n)? ")

    if connection_status.lower() == "y":
        print("Connected.")
        break

    num_connection += 1
else:
    print("Failure to connect.")