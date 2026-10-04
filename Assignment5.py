import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the taxis dataset
df = sns.load_dataset("taxis")

# # Convert pickup column to datetime
# df["pickup"] = pd.to_datetime(df["pickup"])

# # Sort by pickup time
# df = df.sort_values("pickup")

# # Line Chart
# plt.figure(figsize=(10, 5))

# plt.plot(df["pickup"], df["fare"])

# plt.xlabel("Pickup Time")
# plt.ylabel("Fare")
# plt.title("Fare Over Time")

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



# total_fare = df.groupby("pickup_borough")["fare"].sum()

# print(total_fare)

# plt.figure(figsize=(8, 5))

# total_fare.plot(kind="bar")

# plt.xlabel("Pickup Borough")
# plt.ylabel("Total Fare")
# plt.title("Total Fare by Pickup Borough")

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# #pie chart
# payment_counts = df["payment"].value_counts()
# print(payment_counts)

# plt.figure(figsize=(7, 7))

# plt.pie(
#     payment_counts,
#     labels=payment_counts.index,
#     autopct="%1.1f%%",
#     startangle=90
# )

# plt.title("Distribution of Trips by Payment Method")

# plt.show()

# # Histogram
# plt.figure(figsize=(8, 5))

# plt.hist(
#     df["distance"],
#     bins=20,
#     edgecolor="black"
# )

# plt.xlabel("Distance")
# plt.ylabel("Frequency")
# plt.title("Distribution of Taxi Trip Distance")

# plt.tight_layout()
# plt.show()

# #Box Plot
# plt.figure(figsize=(8, 5))

# df.boxplot(
#     column="tip",
#     by="pickup_borough"
# )

# plt.xlabel("Pickup Borough")
# plt.ylabel("Tip Amount")
# plt.title("Distribution of Tip Amount by Pickup Borough")

# plt.suptitle("")

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# #Countplot
# sns.countplot(data=df, x="pickup_borough")

# plt.xlabel("Pickup Borough")
# plt.ylabel("Number of Trips")
# plt.title("Number of Trips by Pickup Borough")

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# #Scatter Plot
# sns.scatterplot(
#     data=df,
#     x="distance",
#     y="fare",
#     hue="pickup_borough"
# )

# plt.xlabel("Distance")
# plt.ylabel("Fare")
# plt.title("Relationship Between Distance and Fare")

# plt.tight_layout()
# plt.show()

# #Heatmap
# correlation_matrix = df[
#     ["distance", "fare", "tip", "tolls", "total"]
# ].corr()

# sns.heatmap(
#     correlation_matrix,
#     annot=True,
#     cmap="coolwarm"
# )

# plt.title("Correlation Heatmap")

# plt.tight_layout()
# plt.show()

# # Pairplot
# sns.pairplot(
#     df,
#     vars=["distance", "fare", "tip", "total"],
#     hue="pickup_zone"
# )

# plt.show()

# Violin Plot
sns.violinplot(
    data=df,
    x="payment",
    y="fare"
)

plt.xlabel("Payment Method")
plt.ylabel("Fare")
plt.title("Distribution of Fare by Payment Method")

plt.tight_layout()
plt.show()