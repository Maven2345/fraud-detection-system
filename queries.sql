-- Identifying high-frequency transactions that exceed the average user behavior
-- This helps in detecting potential "card cracking" or bot attacks.

SELECT 
    user_id, 
    COUNT(transaction_id) AS tx_count, 
    AVG(amount) AS avg_amount,
    MAX(amount) AS max_amount,
    merchant_category
FROM transactions
WHERE transaction_status = 'COMPLETED'
GROUP BY user_id, merchant_category
HAVING COUNT(transaction_id) > 10 -- Potential bot activity
   AND AVG(amount) > 5000;       -- Large suspicious volume

-- Flagging transactions from blacklisted or high-risk IP addresses
SELECT * FROM transactions
WHERE ip_address IN (SELECT ip_address FROM high_risk_locations)
OR device_id IN (SELECT device_id FROM flagged_devices);
