import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

fake_df = pd.read_csv("../data/Fake.csv")
true_df = pd.read_csv("../data/True.csv")

fake_df["label"] = "FAKE"
true_df["label"] = "REAL"

df = pd.concat([fake_df, true_df], ignore_index=True)

df.head()

print("Rows, Columns:", df.shape)
print(df["label"].value_counts())
print(df.isnull().sum())

df["text_length"] = df["text"].astype(str).apply(len)
df["title_length"] = df["title"].astype(str).apply(len)
df["word_count"] = df["text"].astype(str).apply(lambda x: len(x.split()))

df[["label", "word_count", "text_length", "title_length"]].describe()

plt.figure(figsize=(12,5))
sns.countplot(data=df, x="subject", hue="label")
plt.title("Subject Distribution by Label")
plt.xlabel("Subject")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../figures/subject_distribution.png", dpi=300)
plt.show()

print(df["subject"].value_counts().head(10))
