CREATE TABLE IF NOT EXISTS pipeline_runs(
    run_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    extracted_at TIMESTAMPTZ NOT NULL,
    total_data INT,
    accepted_rows INT ,
    rejected_rows INT 
)