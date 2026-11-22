import os
import json
import requests

# Defaults to the live Render deployment; override with API_BASE_URL=http://localhost:5000 for local testing
BASE_URL = os.getenv("API_BASE_URL", "https://servingmlmodels-1.onrender.com").rstrip("/")

ENDPOINTS = [
    {
        "name": "1. Regression (SME Revenue Regressor)",
        "path": "/api/v1/models/sme-revenue-regressor/predictions",
        "payload": {
            "sector": "Technology",
            "county": "Nairobi",
            "quarter": "Q3",
            "business_age_years": 4.5,
            "num_employees": 12,
            "owner_education_level": "Secondary",
            "monthly_marketing_spend_kes": 45000,
            "avg_daily_foot_traffic": None,
            "online_presence_score": 78.0,
            "loan_amount_kes": 250000,
            "interest_rate_pct": 14.5,
            "inflation_rate_pct": 6.5,
            "competitor_density": 5,
            "customer_satisfaction_score": 4.2,
        },
    },
    {
        "name": "2. Classification (SME Credit Risk Classifier)",
        "path": "/api/v1/models/sme-credit-risk-classifier/predictions",
        "payload": {
            "sector": "Retail",
            "county": "Nairobi",
            "quarter": "Q2",
            "loan_purpose": "Working Capital",
            "owner_education_level": "Secondary",
            "business_age_years": 2.1,
            "num_employees": 4,
            "monthly_revenue_kes": 850000,
            "loan_amount_kes": 150000,
            "loan_term_months": 12,
            "interest_rate_pct": 16.5,
            "collateral_value_kes": None,
            "debt_to_income_ratio": 0.62,
            "credit_score": 590,
            "num_previous_loans": 1,
            "missed_payments_count": 3,
            "online_presence_score": 40.0,
            "customer_satisfaction_score": 3.4,
            "competitor_density": 6,
        },
    },
    {
        "name": "3. Clustering (Mall Customer Segmenter)",
        "path": "/api/v1/models/mall-customer-segmenter/predictions",
        "payload": {
            "Age": 27,
            "Annual Income (k$)": 45,
            "Spending Score (1-100)": 72,
        },
    },
    {
        "name": "4. Recommender (E-Commerce Association Rules)",
        "path": "/api/v1/models/ecommerce-recommender/predictions",
        "payload": {
            "cart": ["H06", "H07"],
        },
    },
]


def run_demo_tests():
    print(f"Running automated endpoint verification against: {BASE_URL}\n")
    passed = 0

    for item in ENDPOINTS:
        url = f"{BASE_URL}{item['path']}"
        print(f"=== {item['name']} ===")
        try:
            response = requests.post(url, json=item["payload"], timeout=120)
            print(f"Status Code : {response.status_code}")
            try:
                print(f"Prediction  : {json.dumps(response.json(), indent=2)}")
            except ValueError:
                print(f"Raw Body    : {response.text}")

            if response.status_code == 200:
                passed += 1

            # Verify empty-payload error handling (expects 400 Bad Request)
            empty_resp = requests.post(url, json={}, timeout=60)
            print(f"Empty Input : HTTP {empty_resp.status_code}\n")
        except requests.RequestException as err:
            print(f"Request Error: {err}\n")

    print(f"Summary: {passed}/{len(ENDPOINTS)} endpoints returned HTTP 200 OK.")


if __name__ == "__main__":
    run_demo_tests()