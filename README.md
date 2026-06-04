# E-Commerce Customer Segmentation Matrix

## 📌 Project Overview
This repository implements an unsupervised machine learning pipeline to perform behavioral market segmentation on retail consumers. By utilizing an RFM (Recency, Frequency, Monetary) data framework combined with a K-Means clustering algorithm, the project maps abstract transaction data arrays into distinct consumer profiles to drive targeted marketing strategies.

## 🛠️ Tech Stack & Libraries
* **Environment:** Jupyter Notebook (`customer_segmentation.ipynb`)
* **Libraries:** Scikit-Learn (KMeans, StandardScaler), Pandas, NumPy, Seaborn, Matplotlib

## ⚙️ Machine Learning Pipeline
1. **Feature Extraction:** Aggregates a raw relational sales transaction sheet into distinct metrics tracking purchase currency totals and day inactivity gaps per user.
2. **Feature Scaling:** Implements standard normal scaling via `StandardScaler` to balance units before feeding features into distance-based models.
3. **Clustering Engine:** Executes K-Means clustering utilizing the Elbow Method to identify optimal data grouping parameters.
4. **Dynamic Persona Assignment:** Benchmarks cluster averages directly against global population sample means to map users to distinct marketing groups.

## 📊 Segmentation Archetypes
The algorithm splits the e-commerce shopper distribution into three clean operational profiles:
* **VIP High-Spenders (317 Customers):** Low recency gaps, maximum order frequencies, and highly elevated monetary spend.
* **Active General Shoppers (477 Customers):** Steady interaction history matching global operational baseline averages.
* **Slipping/At-Risk Customers (198 Customers):** High isolation tracking days with minimal purchase frequencies, indicating clear churn signals.
