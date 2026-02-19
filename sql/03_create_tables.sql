CREATE OR REPLACE TABLE CUSTOMER_TABLE(
customer_id INT,
name STRING,
email STRING,
country STRING
);

CREATE OR REPLACE TABLE POLICY_TABLE(
policy_id INT,
customer_id INT,
policy_type STRING,
premium_amount INT,
risk_score INT
);

CREATE OR REPLACE TABLE CLAIMS_TABLE(
claim_id INT,
policy_id INT,
claim_amount INT,
claim_status STRING
);
