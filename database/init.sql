CREATE TABLE test_runs (
    id SERIAL PRIMARY KEY,
    run_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_tests INT,
    passed INT,
    failed INT
);

CREATE TABLE defects (
    id SERIAL PRIMARY KEY,
    test_name TEXT,
    error_log TEXT,
    ai_category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
