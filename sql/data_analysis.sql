--Total orders and total revenue by month
SELECT 
    COUNT(*) AS total_orders,
    SUM(quantity* unit_price) AS total_revenue,
    DATE_TRUNC('month', order_date) AS month
FROM orders
GROUP BY month
ORDER BY month;


-- products wise revenue analysis
SELECT
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_revenue
FROM orders
GROUP BY product
ORDER BY total_revenue DESC;