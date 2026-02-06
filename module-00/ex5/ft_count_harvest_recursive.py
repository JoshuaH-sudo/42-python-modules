def ft_count_harvest_recursive() -> None:
    def helper(day: int, max_days: int) -> None:
        if day > max_days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1, max_days)

    days_until_harvest = int(input("Days until harvest: "))
    helper(1, days_until_harvest)
