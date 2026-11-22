#!/bin/bash
BASE=${BASE:-http://localhost:5000}

echo "=== 1. Regression ==="
curl -i --max-time 120 -X POST $BASE/api/v1/models/sme-revenue-regressor/predictions \
  -H "Content-Type: application/json" \
  -d '{"sector": "Technology", "county": "Nairobi", "quarter": "Q3", "business_age_years": 4.5, "num_employees": 12, "owner_education_level": "Secondary", "monthly_marketing_spend_kes": 45000, "avg_daily_foot_traffic": null, "online_presence_score": 78.0, "loan_amount_kes": 250000, "interest_rate_pct": 14.5, "inflation_rate_pct": 6.5, "competitor_density": 5, "customer_satisfaction_score": 4.2}'
echo -e "\n"

echo "=== 2. Classification ==="
curl -i --max-time 120 -X POST $BASE/api/v1/models/sme-credit-risk-classifier/predictions \
  -H "Content-Type: application/json" \
  -d '{"sector": "Retail", "county": "Nairobi", "quarter": "Q2", "loan_purpose": "Working Capital", "owner_education_level": "Secondary", "business_age_years": 2.1, "num_employees": 4, "monthly_revenue_kes": 850000, "loan_amount_kes": 150000, "loan_term_months": 12, "interest_rate_pct": 16.5, "collateral_value_kes": null, "debt_to_income_ratio": 0.62, "credit_score": 590, "num_previous_loans": 1, "missed_payments_count": 3, "online_presence_score": 40.0, "customer_satisfaction_score": 3.4, "competitor_density": 6}'
echo -e "\n"

echo "=== 3. Clustering ==="
curl -i --max-time 120 -X POST $BASE/api/v1/models/mall-customer-segmenter/predictions \
  -H "Content-Type: application/json" \
  -d '{"Age": 27, "Annual Income (k$)": 45, "Spending Score (1-100)": 72}'
echo -e "\n"

echo "=== 4. Recommender ==="
curl -i --max-time 120 -X POST $BASE/api/v1/models/ecommerce-recommender/predictions \
  -H "Content-Type: application/json" \
  -d '{"cart": ["H06", "H07"]}'
echo -e "\n"
