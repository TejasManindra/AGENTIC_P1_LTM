-- ============================================================
-- Agentic AI for Business Intelligence
-- PostgreSQL Database Schema
-- ============================================================

-- Customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(150),
    customer_segment VARCHAR(50),
    region VARCHAR(100),
    city VARCHAR(100),
    signup_date DATE,
    tenure_months INTEGER,
    lifetime_revenue NUMERIC(14, 2),
    lifetime_profit NUMERIC(14, 2)
);

-- Products
CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    subcategory VARCHAR(100),
    unit_price NUMERIC(14, 2),
    unit_cost NUMERIC(14, 2),
    supplier_lead_days INTEGER
);

-- Orders
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    region VARCHAR(100),
    city VARCHAR(100),
    customer_segment VARCHAR(50),
    order_status VARCHAR(50),
    payment_method VARCHAR(50)
);

-- Order Items
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50) REFERENCES orders(order_id),
    product_id VARCHAR(50) REFERENCES products(product_id),
    quantity INTEGER,
    unit_price NUMERIC(14, 2),
    discount_pct NUMERIC(8, 4),
    gross_sales NUMERIC(14, 2),
    discount_amount NUMERIC(14, 2),
    net_sales NUMERIC(14, 2),
    product_cost NUMERIC(14, 2),
    shipping_cost NUMERIC(14, 2),
    fulfillment_cost NUMERIC(14, 2),
    gross_profit_before_marketing NUMERIC(14, 2),
    profit NUMERIC(14, 2),
    profit_margin_pct NUMERIC(8, 4)
);

-- Marketing Campaigns
CREATE TABLE IF NOT EXISTS marketing_campaigns (
    campaign_id VARCHAR(50) PRIMARY KEY,
    campaign_name VARCHAR(200),
    channel VARCHAR(100),
    start_date DATE,
    end_date DATE,
    target_segment VARCHAR(100),
    marketing_spend NUMERIC(14, 2),
    attributed_revenue NUMERIC(14, 2),
    roi NUMERIC(12, 4)
);

-- Inventory
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id VARCHAR(50) PRIMARY KEY,
    product_id VARCHAR(50) REFERENCES products(product_id),
    snapshot_date DATE,
    opening_stock INTEGER,
    units_received INTEGER,
    units_sold INTEGER,
    closing_stock INTEGER,
    reorder_level INTEGER
);

-- Returns
CREATE TABLE IF NOT EXISTS returns (
    return_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50) REFERENCES orders(order_id),
    product_id VARCHAR(50) REFERENCES products(product_id),
    return_date DATE,
    return_quantity INTEGER,
    return_reason VARCHAR(200),
    refund_amount NUMERIC(14, 2)
);

-- Business Scenarios
CREATE TABLE IF NOT EXISTS business_scenarios (
    scenario_id VARCHAR(50) PRIMARY KEY,
    scenario_name VARCHAR(200),
    scenario_type VARCHAR(100),
    description TEXT,
    expected_business_action TEXT
);

-- Useful indexes for BI queries
CREATE INDEX IF NOT EXISTS idx_orders_date
    ON orders(order_date);

CREATE INDEX IF NOT EXISTS idx_orders_customer
    ON orders(customer_id);

CREATE INDEX IF NOT EXISTS idx_orders_region
    ON orders(region);

CREATE INDEX IF NOT EXISTS idx_order_items_order
    ON order_items(order_id);

CREATE INDEX IF NOT EXISTS idx_order_items_product
    ON order_items(product_id);

CREATE INDEX IF NOT EXISTS idx_inventory_product
    ON inventory(product_id);

CREATE INDEX IF NOT EXISTS idx_inventory_date
    ON inventory(snapshot_date);

CREATE INDEX IF NOT EXISTS idx_returns_order
    ON returns(order_id);

CREATE INDEX IF NOT EXISTS idx_returns_product
    ON returns(product_id);