# FINDINGS


1. VM06 is missing a whole day

My missing intervals check showed 24 missing hours, and they're all VM06. When I looked at the timestamps they're every hour of 10 Aug (00:00 to 23:00), so I concluded that these are not random gaps but a full day with no data.

python
missing = check_for_missing_intervals(readings)
missing.groupby("machine_id")["timestamp"].agg(["min", "max", "count"])

Anyone looking at VM06's daily sales or uptime would get the wrong picture unless they know that day is missing.

2. VM05 has 30 "offline" rows that still have data

There are 98 offline rows. 68 of them have all five telemetry values blank, which is what I would expect if the machine can't connect. The other 30 are all VM05, and they have every value filled in. This could either mean that the status is wrong or the values are old readings which have been stored late, would require further clarification to what they are.

python
offline = readings[readings["connectivity_status"] == "offline"]
offline[TELEMETRY_COLUMNS].isna().all(axis=1).value_counts()
offline[offline["internal_temp_c"].notna()]["machine_id"].value_counts()

3. Some duplicates don't match

There are 26 pairs of rows with the same machine and timestamp. 18 pairs are identical, so one copy can be dropped. The other 8 pairs differ, and the only difference in all of them is stock_level_units. For these we can't just drop one, as we don't know which stock level is right.

python
dupelicate = readings[readings.duplicated(subset=["machine_id", "timestamp"], keep=False)]
dupelicate.groupby(["machine_id", "timestamp"]).nunique()[TELEMETRY_COLUMNS].gt(1).sum()

4. VM02 had high internal_temp_c for 3 days

Every VM02 reading from 11 Aug 00:00 to 13 Aug 23:00 (72 hours) is between 36°C and 44°C. The rest of the time, VM02 and all the other machines sit between about 1.4°C and 7.5°C. These temperatures are possible, so my implausible values check  doesn't catch them on purpose. This could mean that the machine is either broken or the sensor is faulty.

python
readings[readings["internal_temp_c"] > 30].groupby("machine_id")["internal_temp_c"].agg(["count", "min", "max"])

The -999 temperatures are a separate thing, this seems like a sensor error and was flagged in implausible data 

How I found these findings were by reviewing the CSV and subsequently running short python snippets as shown above.
