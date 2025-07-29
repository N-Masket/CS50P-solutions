"""
prompt user forinput

validate input to see if its in fmrt:
year,month,day

9/8/2025

split input split('\')





for list i can use enumarte
"""
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def iso_date(date):
    date = date.strip()
    parts = date.split('/')
    if len(parts) != 3:
        raise ValueError("Incorrect format")

    month = int(parts[0])
    day = int(parts[1])
    year = parts[2].strip()

    # Basic validation
    if not (1 <= month <= 12) or not (1 <= day <= 31) or len(year) < 4:
        raise ValueError("Invalid ISO values")

    print(f'{year}-{month:02}-{day:02}')

def annon_Domini(date):
    date = date.strip().title()
    parts = date.split(',')
    if len(parts) != 2:
        raise ValueError("Missing comma")

    month_day = parts[0].strip()
    year = parts[1].strip()

    sub_parts = month_day.split(' ')
    if len(sub_parts) != 2:
        raise ValueError("Invalid month-day structure")

    month = sub_parts[0]
    try:
        day = int(sub_parts[1])
    except:
        raise ValueError("Invalid day")

    if month not in months:
        raise ValueError("Invalid month name")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day number")

    print(f'{year}-{months.index(month)+1:02}-{day:02}')

# Main loop
while True:
    date = input("Date: ")
    try:
        iso_date(date)
        break
    except:
        try:
            annon_Domini(date)
            break
        except:
            pass  # reprompt until valid
