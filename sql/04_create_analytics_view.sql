CREATE OR REPLACE VIEW CLAIMS_ANALYTICS AS
SELECT
p.policy_id,
c.claim_amount,
p.risk_score
FROM POLICY_TABLE p
JOIN CLAIMS_TABLE c
ON p.policy_id = c.policy_id;
