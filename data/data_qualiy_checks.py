import pandas as pd

# machines = pd.read_csv("machines.csv")
# readings = pd.read_csv("readings.csv")


# readings = readings.merge(
#     machines[["machine_id", "capacity_units"]], on="machine_id", how="left"
# )


def check_duplicates(readings):
    duplicates = readings[
        readings.duplicated(subset=["machine_id", "timestamp"], keep=False)
    ]
    return duplicates


def check_for_missing_intervals(readings):
    readings = readings.copy()
    readings["timestamp"] = pd.to_datetime(
        readings["timestamp"], format="%d/%m/%Y %H:%M"
    )

    missing = []

    for machine_id, machine_data in readings.groupby("machine_id"):
        machine_data = machine_data.sort_values("timestamp")

        expected = pd.date_range(
            machine_data["timestamp"].min(), machine_data["timestamp"].max(), freq="h"
        )

        actual = machine_data["timestamp"]

        missing_times = expected.difference(actual)

        for timestamp in missing_times:
            missing.append({"machine_id": machine_id, "timestamp": timestamp})

    return pd.DataFrame(missing)


TELEMETRY_COLUMNS = [
    "internal_temp_c",
    "stock_level_units",
    "door_open_count",
    "transaction_count",
    "total_sales_gbp",
]


def check_for_missing_values_online(readings, columns=TELEMETRY_COLUMNS):

    readings = readings.copy()
    online = readings[readings["connectivity_status"] == "online"]

    flagged = online[online[columns].isna().any(axis=1)]

    return flagged
