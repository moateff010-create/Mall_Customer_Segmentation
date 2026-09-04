# Customer Segmentation using K-Means Clustering

## Project Overview
This project aims to segment mall customers based on their annual income and spending score to help the marketing team design targeted marketing strategies.

## Dataset
The dataset contains customer information including:
- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

## Methodology
1. **Data Preprocessing & Scaling**: Normalized features using `StandardScaler` to balance feature influence.
2. **Elbow Method**: Evaluated Within-Cluster Sum of Squares (WCSS) to determine the optimal number of clusters ($K=5$).
3. **K-Means Clustering**: Trained the model on scaled features and extracted cluster centroids.

## Business Insights & Recommendations
- **Cluster 0 (Standard Customers)**: Average income and average spending. Target with standard promotions.
- **Cluster 1 (Target / VIP Customers)**: High income and high spending. Focus on premium services and loyalty programs.
- **Cluster 2 (Careless Spenders)**: Low income but high spending. Offer discount deals and installment plans.
- **Cluster 3 (Sensible Customers)**: High income but low spending. Engage with value-driven marketing and premium quality offers.
- **Cluster 4 (Budget Customers)**: Low income and low spending. Focus on low-cost essential products.

## How to Run
```bash
python "Mall Customer Segmentation.py"