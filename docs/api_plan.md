# KrishiPrajna API Plan

## Authentication APIs

### POST /auth/register
Create farmer account.

### POST /auth/login
Login farmer account.

### POST /auth/forgot-password
Password recovery.

---

## Farm APIs

### GET /farms
Get all farms for user.

### POST /farms
Create new farm.

### PUT /farms/{id}
Update farm information.

### DELETE /farms/{id}
Delete farm.

---

## Device APIs

### GET /devices
Get all farm devices.

### POST /devices
Register ESP32 device.

### PUT /devices/{id}
Update device information.

---

## Sensor APIs

### POST /sensor-data
Upload sensor readings.

### GET /sensor-data/{device_id}
Get historical sensor data.

---

## Irrigation APIs

### POST /irrigation/start
Start irrigation.

### POST /irrigation/stop
Stop irrigation.

### GET /irrigation/logs
Get irrigation history.

---

## AI APIs

### POST /ai/disease-detection
Analyze crop disease.

### POST /ai/irrigation-prediction
Predict irrigation timing.

### POST /ai/crop-recommendation
Recommend suitable crops.

---

## Notification APIs

### GET /alerts
Get all alerts.

### POST /alerts/send
Send notification alerts.

---

## Weather APIs

### GET /weather/current
Get live weather.

### GET /weather/forecast
Get weather forecast.

---

## Market APIs

### GET /market/prices
Get crop market prices.

### GET /market/demand
Get crop demand analytics.
