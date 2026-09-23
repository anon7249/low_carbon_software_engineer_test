import pandas as pd
import pytest

from data_qualiy_checks import (
    check_duplicates,
    check_for_missing_intervals,
    check_for_missing_values_online,
)


def test_check_duplicates_flags_only_the_duplicated_rows():
    readings = pd.DataFrame(
        {
            "machine_id": ["VM01", "VM01", "VM02"],
            "timestamp": [
                "01/08/2026 00:00",
                "01/08/2026 00:00",
                "01/08/2026 00:00",
            ],
            "internal_temp_c": [4.0, 4.0, 5.0],
        }
    )

    result = check_duplicates(readings)

    assert len(result) == 2
    assert set(result["machine_id"]) == {"VM01"}


def test_check_duplicates_returns_empty_when_no_duplicates_exist():
    readings = pd.DataFrame(
        {
            "machine_id": ["VM01", "VM02"],
            "timestamp": ["01/08/2026 00:00", "01/08/2026 00:00"],
            "internal_temp_c": [4.0, 5.0],
        }
    )

    result = check_duplicates(readings)

    assert len(result) == 0


def test_check_for_missing_intervals_flags_the_missing_hour():

    readings = pd.DataFrame(
        {
            "machine_id": ["VM01", "VM01", "VM01"],
            "timestamp": [
                "01/08/2026 00:00",
                "01/08/2026 01:00",
                "01/08/2026 03:00",
            ],
        }
    )

    result = check_for_missing_intervals(readings)

    assert len(result) == 1


def test_check_for_missing_intervals_returns_empty_for_a_complete_sequence():
    readings = pd.DataFrame(
        {
            "machine_id": ["VM01", "VM01", "VM01"],
            "timestamp": [
                "01/08/2026 00:00",
                "01/08/2026 01:00",
                "01/08/2026 02:00",
            ],
        }
    )

    result = check_for_missing_intervals(readings)

    assert len(result) == 0


def test_check_for_missing_values_online_flags_null_while_online():
    readings = pd.DataFrame(
        {
            "machine_id": ["VM01", "VM02", "VM03"],
            "timestamp": ["01/08/2026 00:00"] * 3,
            "connectivity_status": ["online", "online", "offline"],
            "internal_temp_c": [None, 4.0, None],
            "stock_level_units": [50, 60, None],
            "door_open_count": [1, 2, None],
            "transaction_count": [0, 1, None],
            "total_sales_gbp": [0.0, 3.5, None],
        }
    )

    result = check_for_missing_values_online(readings)

    assert len(result) == 1
    assert result.iloc[0]["machine_id"] == "VM01"


def test_check_for_missing_values_online_ignores_expected_offline_nulls():
    readings = pd.DataFrame(
        {
            "machine_id": ["VM03"],
            "timestamp": ["01/08/2026 00:00"],
            "connectivity_status": ["offline"],
            "internal_temp_c": [None],
            "stock_level_units": [None],
            "door_open_count": [None],
            "transaction_count": [None],
            "total_sales_gbp": [None],
        }
    )

    result = check_for_missing_values_online(readings)

    assert len(result) == 0


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v"]))
