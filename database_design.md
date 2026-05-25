# KrishiPrajna Database Design

## Main Database Tables

### users
Stores farmer account information.

Fields:
- id
- name
- email
- password_hash
- phone_number
- language
- created_at

---

### farms
Stores farm details.

Fields:
- id
- user_id
- farm_name
- location
- crop_type
- soil_type
- created_at

---

### devices
Stores ESP32 device information.

Fields:
- id
- farm_id
- device_name
- device_status
- firmware_version
- created_at

---

### sensor_data
Stores live sensor readings.

Fields:
- id
- device_id
- temperature
- humidity
- soil_moisture
- rain_detected
- timestamp

---

### irrigation_logs
Stores irrigation activity.

Fields:
- id
- device_id
- irrigation_status
- irrigation_duration
- water_usage
- timestamp

---

### alerts
Stores notification and alert data.

Fields:
- id
- user_id
- alert_type
- message
- alert_status
- created_at

---

### disease_reports
Stores crop disease detection results.

Fields:
- id
- farm_id
- image_path
- disease_name
- confidence_score
- recommendation
- created_at

---

### weather_data
Stores weather information.

Fields:
- id
- farm_id
- temperature
- humidity
- rainfall
- wind_speed
- timestamp

---

## Database Technology
- PostgreSQL

---

## Future Expansion
- Satellite data tables
- AI prediction tables
- Community posts
- Marketplace integration
