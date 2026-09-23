SELECT   r.machine_id,
         r.timestamp,
         r.internal_temp_c,
         r.stock_level_units,
         m.capacity_units,
         r.door_open_count,
         r.transaction_count,
         r.total_sales_gbp,
         CONCAT_WS('; ', CASE WHEN r.internal_temp_c < -20
                                   OR r.internal_temp_c > 60 THEN 'internal_temp_c out of range (-20 to 60)' END, CASE WHEN r.stock_level_units < 0 THEN 'stock_level_units negative' END, CASE WHEN r.stock_level_units > m.capacity_units THEN 'stock_level_units exceeds capacity_units' END, CASE WHEN r.door_open_count < 0 THEN 'door_open_count negative' END, CASE WHEN r.transaction_count < 0 THEN 'transaction_count negative' END, CASE WHEN r.total_sales_gbp < 0 THEN 'total_sales_gbp negative' END) AS reason
FROM     read_csv_auto('readings.csv') AS r
         LEFT OUTER JOIN
         read_csv_auto('machines.csv') AS m
         ON r.machine_id = m.machine_id
WHERE    r.internal_temp_c < -20
         OR r.internal_temp_c > 60
         OR r.stock_level_units < 0
         OR r.stock_level_units > m.capacity_units
         OR r.door_open_count < 0
         OR r.transaction_count < 0
         OR r.total_sales_gbp < 0
ORDER BY r.machine_id, r.timestamp;


--  WORKED EXAMPLE FOR SQL
-- machine.csv example: 
-- machine_id | capacity_units
-- VM01       | 120
-- VM02       | 80
-- readings.csv example: 
-- machine_id | timestamp | internal_temp_c | stock_level_units | door_open_count | transaction_count | total_sales_gbp
-- VM02       | 07/08/2026 15:00 | -999            | 30              | 2               | 1                 | 3.50
-- VM02       | 10/08/2026 20:00 | 4.5             | 108             | 3               | 2                 | 6.00
-- VM01       | 01/08/2026 00:00 | 4.2             | 50              | 1               | -4                | 0.00
-- VM01       | 01/08/2026 01:00 | 4.3             | 50              | 1               | 0                 | 0.00
-- Expected output example:
-- machine_id | timestamp        | reason
--  VM01      | 01/08/2026 00:00 | transaction_count negative
--  VM02      | 07/08/2026 15:00 | internal_temp_c out of range (-20 to 60)
--  VM02      | 10/08/2026 20:00 | stock_level_units exceeds capacity_units
