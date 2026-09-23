from pathlib import Path

import pandas as pd

from data_qualiy_checks import (
    check_duplicates,
    check_for_missing_intervals,
    check_for_missing_values_online,
)

ROOT = Path(__file__).parent


def print_summary(title, flagged):
    """Print the total count, then how many of those belong to each machine."""
    print(f"{title}: {len(flagged)}")
    if len(flagged) > 0:
        print(flagged["machine_id"].value_counts().sort_index().to_string())
    print()


def main():
    readings = pd.read_csv(ROOT / "readings.csv")

    print_summary("Duplicate rows", check_duplicates(readings))
    print_summary("Missing hourly intervals", check_for_missing_intervals(readings))
    print_summary(
        "Rows with missing telemetry while online",
        check_for_missing_values_online(readings),
    )


if __name__ == "__main__":
    main()
