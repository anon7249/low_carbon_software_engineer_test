## Data Quality checks for a vending machine telemetry 

Checking for 3 kinds of data quality issues from readings.csv:
duplicate readings, missing readings, and implausible values, I have also provided tests and
a small script (run_checks.py), to run everything and print a summary. 

## Files

- `data_qualiy_checks.py` - Checks for duplicates and missing readings. 
- `implausible_values.sql` – SQL check for implausible values
- `tests.py` – pytest tests for the Python checks
- `run_checks.py` – runs the Python checks and provides a summary
- `FINDINGS.md` – Other issues which stood out but was not included in `data_qualiy_checks.py`


## How checks work in `data_qualiy_checks.py`

1) Duplicated 
- check_duplicates function flags rows which are the same machine and have the same timestamp, both
rows are returned so you can compare the findings. 

2) Missing Readings 
- check_for_missing_intervals function which builds the full list of hours it is then compared against the actual dataset
any hour missing is stored in a missing list then subsequently returned, this provides all the missing hours in the dataset. 

- check_for_missing_values_online function checks for rows in the machine which are online but have any of the 5 telemetry columns as blank. 
Offline readings are expected to be blank, these findings are not flagged. 

3) implausible Values 
- SQL flags rows where: 
Temperature is below -20 or above 60 degrees. 
Stock is below 0 or above the machines capacity. 
door_open_count/transaction_count/total_sales_gbp are negative values.  

## How to test
python run_checks.py
python -m pytest tests.py -q

For the SQL, open `duckdb.exe` in the same folder and paste in the query found in implausible_values.sql

## Known limitations

- Only flagging the issues, nothing is fixed or removed. 
- VM02's 36–44°C readings are not flagged on purpose as they may be legitimate readings,
issue is flagged in FINDING.md 
