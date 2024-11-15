def get_date(day_index):
    day_index_to_date = {
        236: "25-08-2005",
        238: "27-08-2005",
        239: "28-08-2005",
        240: "29-08-2005",
        241: "30-08-2005",
        242: "31-08-2005",
        243: "01-09-2005",
    }
    return day_index_to_date.get(day_index)
