def ft_harvest_total():
    max_days = 3
    day = 1
    total_harvest = 0
    while day <= max_days:
        daily_harvest = input(f"Day {day} harvest: ")
        total_harvest += int(daily_harvest)
        day += 1
    print(f"Total harvest: {total_harvest}")
