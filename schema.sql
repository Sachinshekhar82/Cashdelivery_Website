DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT NOT NULL UNIQUE,
    user_id TEXT NOT NULL,
    amount REAL NOT NULL,
    address TEXT NOT NULL,
    total_charge REAL NOT NULL,
    otp TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    partner_id TEXT
);