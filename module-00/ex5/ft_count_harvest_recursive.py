def ft_count_harvest_recursive():
    def helper(day, max_days):
        if day > max_days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1, max_days)
    days_until_harvest = int(input("Days until harvest: "))
    helper(1, days_until_harvest)
