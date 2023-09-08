from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = dict()
    name_list = []
    weekday_day_dict = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",
        6: "Monday"
    }
    # оприділяєм сьогоднішню дату 
    current_datetime_date = date.today()

    # оприділяєм дату через теждень
    one_weeks_interval = timedelta(weeks=1)
    current_datetime_plus_seven_days_date = current_datetime_date + one_weeks_interval
    
    for user in users:

        # оприділяємо чи відбулась подія в цьому році чи ні 
        if current_datetime_date.year == current_datetime_plus_seven_days_date.year:
        
            if current_datetime_date <= user["birthday"] <= current_datetime_plus_seven_days_date:
                weekday_day_now = user["birthday"].weekday()
                name_list = result.get(weekday_day_dict[weekday_day_now], [])
                name_list.append(user["name"])
                result[weekday_day_dict[weekday_day_now]] = name_list
        
        else:
        
            if user["birthday"].month == 12:
                user["birthday"] = datetime(year=current_datetime_date.year, month=user["birthday"].month, day=user["birthday"].day).date()
            if user["birthday"].month == 1:
                user["birthday"] = datetime(year=current_datetime_plus_seven_days_date.year, month=user["birthday"].month, day=user["birthday"].day).date()
            
            if current_datetime_date <= user["birthday"] <= current_datetime_plus_seven_days_date:
                weekday_day_now = user["birthday"].weekday()
                name_list = result.get(weekday_day_dict[weekday_day_now], [])
                name_list.append(user["name"])
                result[weekday_day_dict[weekday_day_now]] = name_list
    
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
