from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):

    days_range = tuple((date.today() + timedelta(days=i)) for i in range(7))

    # If today is Sunday or Monday next weekend's birthday persons
    # should be congratulated next Monday but not this one
    sat2mon = "Monday" if date.today().weekday() not in (0, 6) else "Next Monday"
    sun2mon = "Monday" if date.today().weekday() != 0 else "Next Monday"

    output = defaultdict(list)

    for user in users:
        user_date = user["birthday"].strftime("%m.%d")
        for day in days_range:
            day_str = day.strftime("%m.%d")
            if day_str == user_date or (user_date == "02.29" and day_str == "03.01"):  # who were born on February 29 celebrate March 1
                output[day.strftime("%A").replace("Saturday", sat2mon).replace("Sunday", sun2mon)].append(user["name"])
                break

    return output


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
