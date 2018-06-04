CREATE TYPE sensor_type_enum AS ENUM ('temperature', 'humidity');

CREATE TABLE IF NOT EXISTS device_bundles(
	id bigserial PRIMARY KEY     NOT NULL,
	device_uuid VARCHAR(32)       NOT NULL,
	sensor_type sensor_type_enum NOT NULL,
	sensor_value numeric(3,1) NOT NULL,
	sensor_reading_time bigserial NOT NULL
	CHECK (sensor_value BETWEEN 0 AND 100)
);

CREATE INDEX device_uuid_index
ON device_bundles (device_uuid);

CREATE INDEX sensor_reading_time_index
ON device_bundles (sensor_reading_time);