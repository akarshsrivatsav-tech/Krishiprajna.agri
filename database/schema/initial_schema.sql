CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE farms (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    farm_name VARCHAR(255),
    location VARCHAR(255),
    crop_type VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    farm_id INTEGER REFERENCES farms(id),
    temperature FLOAT,
    humidity FLOAT,
    soil_moisture FLOAT,
    rain_detected BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
