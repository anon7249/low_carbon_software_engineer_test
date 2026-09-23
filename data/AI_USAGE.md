## AI Usage

I used Claude.AI. 

1)  Prompted AI as i was unsure whether to work with the actual dataset or to make a copy, it recommended that I should copy the dataset rather than work with the actual dataset this was to ensure I couldn't accidently alter the actual dataset. 

2)  Used AI in check_for_missing_intervals function to convert the timestamp strings into actual datetimes that pandas can work with, as I could not remember the syntax. 

3)  My first version check_for_missing_temp_online , only checked internal_temp_c, because that's where I had spotted blanks on VM01. When AI reviewed it, it pointed
  out that the other four  columns weren't being checked, so a blank in any of them would have been missed. I asked it to help me rewrite this as check_for_missing_values_online, which loops over a list of all five  columns  and flags any online row with a blank in any of them. I kept this change, as it makes the check cover the whole row rather than one column, and makes it easy to add columns later. I confirmed it still flags the same 20 VM01 rows, so no false positives were introduced. Below was my original code sample.

def check_for_missing_temp_online(readings):
    readings = readings.copy()

    online_missing_temp = readings[
        (readings["connectivity_status"] == "online")
        & (readings["internal_temp_c"].isna())
    ]

    return online_missing_temp


print(check_for_missing_temp_online(readings))


## Assumptions
A duplicate is two rows with the same machine_id and time_stamp. I assumed each machine should report once per hour, so a missing hour counts as a missing reading. Nulls while a machine is offline is an expected result; nulls values whlist online where not expected and were to be flagged. Timestamps are DD/MM/YYYY. For implausible values: temperature outside -20 to 60°C, stock below 0 or above the machine's capacity_units, and negative door counts, transactions or sales. I treated the  30-44°C readings on VM02 as a real anomaly, not an implausible value because they're physically possible.
