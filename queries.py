
LOOKUP_BUNDLE_BY_TIME = """
SELECT device_uuid, sensor_type, sensor_value, sensor_reading_time
FROM device_bundles
WHERE device_uuid = '{device_uuid}'
AND sensor_type = '{sensor_type}'
AND sensor_reading_time >= {start_time}
AND sensor_reading_time <= {end_time};
"""


INSERT_BUNDLE = """
INSERT INTO device_bundles(device_uuid, sensor_type, sensor_value, sensor_reading_time)
VALUES
 ('{device_uuid}', '{sensor_type}', {sensor_value}, {sensor_reading_time});
"""