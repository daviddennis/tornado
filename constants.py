
DEVICE_FIELDS = [
	"device_uuid",
	"sensor_type",
	"sensor_value",
	"sensor_reading_time",
]

LOOKUP_REQ_FIELDS = [
	"device_uuid",
	"sensor_type",
	"start_time",
	"end_time",
]

SENSOR_TYPES = ['temperature', 'humidity']

TEST_DATA = [{
		"device_uuid": "b21ad0676f26439482cc9b1c7e827de4",
		"sensor_type": "temperature",
		"sensor_value": 50.0,
		"sensor_reading_time": 1510093202
	},
	{
		"device_uuid": "g32ad0676f26439482cc9b1d7e828de4",
		"sensor_type": "temperature",
		"sensor_value": 51.0,
		"sensor_reading_time": 1510099303
	},
]

RESPONSE_TEMPLATE = {
	'status': None,
	'response': None,
}

SUCCESS = 'success'