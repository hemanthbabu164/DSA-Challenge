import datetime

# Get the current time
current_time = datetime.datetime.now()

# Input the time you want to compare (in HH:MM:SS format)
given_time_str = input("Enter the time (HH:MM:SS): ")


try:
    # Convert the given time string to a datetime object
    given_time = datetime.datetime.strptime(given_time_str, "%H:%M:%S")
    
    # Calculate the time difference
    time_difference = current_time - given_time
    
    # Extract hours, minutes, and seconds from the time difference
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"Time difference: {hours} hours, {minutes} minutes, {seconds} seconds")
except ValueError:
    print("Invalid time format. Please use HH:MM:SS format.")
