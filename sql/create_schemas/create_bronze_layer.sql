CREATE TABLE IF NOT EXISTS bronze_crypto_markets (
    bronze_id  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id     BIGINT NOT NULL REFERENCES pipeline_runs(run_id),
    payload    JSONB NOT NULL
);