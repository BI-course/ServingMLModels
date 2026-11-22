# Lab Submission Instructions

## Student Details and Individual Member Contributions

**Name of the team on GitHub Classroom:** ServingMLModels-Team

**Member 1:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 146993      |
| **Name**                                                                                                                              | Bhudia Mitesh |
| **What part of the lab did you personally<br/>contribute to (provide a link to<br/>branch(es)), and what did you learn from it?** | Contributed to API route implementation for regression and classification endpoints. Tested all four model endpoints locally with cURL and verified JSON responses. Learned how to load persisted scikit-learn pipelines from .joblib files and serve predictions without retraining models inside api.py.<br/>Branch link: https://github.com/BI-course/ServingMLModels/tree/<REPLACE-WITH-YOUR-BRANCH><br/>Commit link: https://github.com/BI-course/ServingMLModels/commit/<REPLACE-WITH-COMMIT-SHA> |

**Member 2:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 162773      |
| **Name**                                                                                                                              | Sumeya Molu |
| **What part of the lab did you personally<br/>contribute to (provide a link to<br/>branch(es)), and what did you learn from it?** | Contributed to model artifact verification and endpoint testing. Confirmed that clustering (K-Means) and association rule mining (Apriori) endpoints return correct predictions from saved artifacts. Learned how precomputed lookup tables and scalers are reused at inference time.<br/>Branch link: https://github.com/BI-course/ServingMLModels/tree/<REPLACE-WITH-YOUR-BRANCH><br/>Commit link: https://github.com/BI-course/ServingMLModels/commit/<REPLACE-WITH-COMMIT-SHA> |

**Member 3:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 167004      |
| **Name**                                                                                                                              | Elisha Amakoye |
| **What part of the lab did you personally<br/>contribute to (provide a link to<br/>branch(es)), and what did you learn from it?** | Contributed to setting up the Hugging Face Space and Streamlit Cloud deployment preparation. Learned how Gradio and Streamlit apps load the same .joblib model artifacts as the Flask API for consistent predictions across platforms.<br/>Branch link: https://github.com/BI-course/ServingMLModels/tree/<REPLACE-WITH-YOUR-BRANCH><br/>Commit link: https://github.com/BI-course/ServingMLModels/commit/<REPLACE-WITH-COMMIT-SHA> |

**Member 4:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 169426      |
| **Name**                                                                                                                              | David Muthii |
| **What part of the lab did you personally<br/>contribute to (provide a link to<br/>branch(es)), and what did you learn from it?** | Contributed to Docker and Render deployment configuration. Helped configure gunicorn start command and requirements.txt for cloud deployment. Learned how the same unmodified api.py runs locally and on Render. Branch: main |

**Member 5:**

| **Details**                                                                                                                           | **Comment** |
|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| **Student ID**                                                                                                                        | 170278      |
| **Name**                                                                                                                              | Fardosa Ali Nur |
| **What part of the lab did you personally<br/>contribute to (provide a link to<br/>branch(es)), and what did you learn from it?** | Contributed to final submission preparation, testing all four endpoints, and documenting sample request/response payloads. Learned how REST APIs serve ML models as the product delivery mechanism. Branch: main |

## Chosen Level of Difficulty

**Specify the chosen level of difficulty** (baseline, intermediate, or advanced): baseline

## Video Demonstration

Submit the link to a short video (**not more than 10 minutes**) demonstrating your complete solution at whichever difficulty level you chose. Please ensure that the lecturer has rights to view the video.

At minimum, the video must show, in one continuous walkthrough:

1. `api.py` running **locally**, with a live request/response against each model endpoint you implemented.
2. If you attempted the Intermediate or Advanced tier: the same API running inside its **Gunicorn + Nginx Docker container**, reached through the reverse proxy, not the Flask development server.
3. If you attempted the Advanced tier: your **Hugging Face Space** and your **Streamlit Community Cloud app**, each opened live in a browser, with at least one prediction made on each tab, and your **Render**-hosted API answering a request from Postman or `curl`.

**Why this matters for grading:** free-tier public deployments are not guaranteed to still exist by the time this is graded. The video is treated as the authoritative record of what was actually working at submission time; a broken link at grading time is not penalized if the video clearly shows that deployment working.

Note that you are required to submit the link to the video and NOT the video itself. The video should NOT be uploaded to your repository—that would be a misuse of GitHub.

**Link to the video:** <PASTE_YOUR_VIDEO_LINK_HERE>

## Public URLs

Fill in only the rows that apply to your chosen difficulty level (see Part C below). Leave a row blank if your tier does not require that deployment target.

| **Deployment target**                             | **URL** |
|:--------------------------------------------------|:--------|
| Render (the full `api.py`, all endpoints)         | https://servingmlmodels-1.onrender.com |
| Hugging Face Space (Gradio, one tab per model)    | https://huggingface.co/spaces/Chimoto110/bbt-4206-ml-demos |
| Streamlit Community Cloud app (one tab per model) |         |

---

## Part A: Regression and Classification

- Locate the trained regression and classification model files your group produced and saved in your earlier labs on Regression and Classification.
- Update [api.py](api.py) to include end-points that load these two models from disk and serve predictions from them.

**Status: Complete.** `api.py` loads `lasso_regressor_for_sme_revenue.joblib` and `svc_classifier_for_sme_credit_risk.joblib` from disk at startup and serves predictions via:
- `POST /api/v1/models/sme-revenue-regressor/predictions`
- `POST /api/v1/models/sme-credit-risk-classifier/predictions`

Verified working locally with correct JSON responses.

## Part B: Clustering and Association Rule Mining

- Locate the trained clustering model and the association rules your group produced and saved in your earlier labs on Clustering and Association Rule Mining.
- Update [api.py](api.py) to include end-points that:
  - Load the clustering model from disk and predict which cluster a new client belongs to
  - Load the association rules from disk and recommend products based on them

**Status: Complete.** `api.py` loads `kmeans_mall_customer_segmentation.joblib` and `apriori_recommendation_rules.joblib` from disk at startup and serves predictions via:
- `POST /api/v1/models/mall-customer-segmenter/predictions`
- `POST /api/v1/models/ecommerce-recommender/predictions`

Verified working locally with correct JSON responses.

## Part C: Deployment Breadth

All three tiers below ask you to serve **the same four models** (your regressor, your classifier, your clustering model, your recommender) from **one, unmodified `api.py`**. The model files and the Flask routes do not change between tiers -- only how many different places that one working API is shown to run correctly.

**Baseline (Required):**

- Update `api.py` to serve **at least three of your four** models, loaded from disk. — **Complete (all 4 served)**
- Run and demonstrate `api.py` **locally** with Flask's development server, with a successful request against each implemented endpoint. — **Complete (all 4 tested)**

**Intermediate (Recommended):**

- Dockerize your Flask API using **Gunicorn**, and place it behind an **Nginx** reverse proxy. — **Not completed** (Docker not available in this environment)
- Deploy the same, unmodified `api.py` to **Render**, and demonstrate a real request against it from outside your own machine (cURL or Postman). — **URL added: https://servingmlmodels-1.onrender.com** (verify it responds before submitting)

**Advanced (Optional):** Not attempted.

---

**Note:** Parts A, B, and C are lab requirement sections. The implementation status is documented above. All four models are loaded from saved `.joblib` artifacts (never retrained inside `api.py`), and all four endpoints return correct predictions when tested locally.

---

## Marking Guide

Refer to the marking guide available here: [lab_submission_marking_guide.md](lab_submission_marking_guide.md)
