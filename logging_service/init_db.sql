CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    endpoint VARCHAR(255) NOT NULL,
    api_key VARCHAR(255),
    duration FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO logs (endpoint, api_key, duration) VALUES
    ('/auth', 'valid_api_key', 0.12),
    ('/service', 'user_key_1', 0.34),
    ('/auth', 'user_key_2', 0.09)
ON CONFLICT DO NOTHING; 