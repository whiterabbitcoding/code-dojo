from collections import namedtuple
from typing import List

import arrow

import matplotlib.pyplot as plt

import pandas as pd

input_dataframe = pd.read_csv("./reservation_data_sample.csv")


def rows_from_night_of_stay(df, date):
    return df.loc[df["NIGHT_OF_STAY"] == date]


def is_occupied(room):
    room.sort(key=lambda x: x.get("DATE_LAST_MODIFIED"))
    if room[0]["RPG_STATUS"] == 2:
        return False
    return True


def daily_occupancy(reservations: pd.DataFrame) -> int:
    total_rooms = input_dataframe["ROOM_ID"].nunique()
    rooms_occupied = 0

    grouped_by_res_id = {}

    for i in reservations.to_dict("records"):
        if i["ROOM_RESERVATION_ID"] not in grouped_by_res_id.keys():
            grouped_by_res_id[i["ROOM_RESERVATION_ID"]] = [i]
        else:
            grouped_by_res_id[i["ROOM_RESERVATION_ID"]].append(i)

    for room in grouped_by_res_id.values():
        if is_occupied(room):
            rooms_occupied += 1

    occupancy = (rooms_occupied / total_rooms) * 100
    return occupancy


# If changing lookback number could refactor to have it as an argument, as opposed to hardcoded 100
def calculate_occupancy_last_100_days(dataframe: pd.DataFrame, date: str) -> List:
    rows_for_night_of_stay = rows_from_night_of_stay(dataframe, date)
    Occupancy = namedtuple("Occupancy", ["date", "occupancy"])
    arrow_date = arrow.get(date)
    output_data = []
    for i in range(100):
        all_reservations_by_date = rows_for_night_of_stay.loc[
            rows_for_night_of_stay["DATE_OF_RESERVATION"] <= str(arrow_date)
        ]
        output_data.append(
            Occupancy(
                arrow_date.format("YYYY-MM-DD"),
                daily_occupancy(all_reservations_by_date),
            )
        )

        arrow_date = arrow_date.shift(days=-1)

    output_data.reverse()

    # can be useful having axis separately
    # x = [x.date for x in output_data]
    # y = [x.occupancy for x in output_data]
    return [x.occupancy for x in output_data]


def generate_line_graph(date: str) -> int:
    arrow_date = arrow.get(date)
    from_original = calculate_occupancy_last_100_days(input_dataframe, date)
    one_year_back = calculate_occupancy_last_100_days(
        input_dataframe,
        arrow_date.shift(days=-364).format("YYYY-MM-DD"),
    )

    plt.plot(from_original, label=date)
    plt.plot(one_year_back, label=arrow_date.shift(days=-364).format("YYYY-MM-DD"))
    plt.title("Occupancy Curve")
    plt.legend(loc="upper left", title="Plots")
    plt.grid(True)
    plt.show()

    return 0


if __name__ == "__main__":
    assert isinstance(
        calculate_occupancy_last_100_days(input_dataframe, "2022-07-16"), List
    )
    generate_line_graph("2022-07-16")
