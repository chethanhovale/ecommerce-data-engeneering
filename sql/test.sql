CREATE VIEW analytics.vw_payment_method_usage AS
SELECT
    payment_method,
    COUNT(*) AS total_orders
FROM analytics.fact_orders
GROUP BY payment_method;
SELECT * FROM analytics.vw_payment_method_usage
ORDER BY total_orders DESC;
