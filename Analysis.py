import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.show()

# Top journals
top_journals = df['journal'].value_counts().head(10)
top_journals.plot(kind='bar', figsize=(8,5), title="Top Journals")

# Word frequency in titles
all_words = " ".join(df['title'].dropna()).lower().split()
common_words = Counter(all_words).most_common(20)
print(common_words)

# Word cloud of titles
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(all_words))
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
