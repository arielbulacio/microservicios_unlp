CREATE TABLE IF NOT EXISTS api_keys (
    key VARCHAR(255) PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

INSERT INTO api_keys (key, tipo) VALUES
    ('valid_api_key', 'admin'),
    ('user_key_1', 'user'),
    ('user_key_2', 'user'),
    ('service_key', 'service')
ON CONFLICT (key) DO NOTHING; 