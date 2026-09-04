import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn.cluster import KMeans
df = pd.read_csv(r"D:/datasets/Mall_Customers.csv")
x = df[["Annual Income (k$)","Spending Score (1-100)"]]
scalar = StandardScaler()
x_scaled = scalar.fit_transform(x)
kmeans = KMeans(n_clusters=5,random_state=42,n_init=10)
df["Cluster"] = kmeans.fit_predict(x_scaled)
plt.figure(figsize=(10,6))
sns.scatterplot(
    x= "Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Cluster",
    data=df,
    palette="Set1",
    size=100 
)

centroids = scalar.inverse_transform(kmeans.cluster_centers_)
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    s = 250,
    c = "black",
    marker = "X",
    label = "Centroids"
)
plt.title("Customer Segments With Centroids")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.legend(title = "Cluster")
plt.grid(True)
plt.show()
