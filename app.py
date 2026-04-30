import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies.csv")

print(df.head())

print("Getting info of the dataset")
print(df.info())

print("Printing total null values of each column")
print(df.isna().sum())

# Dropping the rows with null values of score, votes, writer, country, runtime
df.dropna(subset=["score", "votes", "writer", "country", "runtime"], inplace=True)

print("Printing how many types of rating are there and how many of each of them is there")
print(df["rating"])
print(df["rating"].value_counts())

# First I thought that I will fill it with mode but then it might cause some problems as some movies might be restricted for some audience even if they are not incorrect then now I thought of dropping the rows
# Dropping the rows with null values of rating
df.dropna(subset=["rating"], inplace=True)

print("Checking how many null values are still there")
print(df.isna().sum())

# First checking whether there are any rows with budget or gross as zero
print("Checking whether budget has any zero value")
print(df[df["budget"] == 0])
print("Checking whether gross has any zero value")
print(df[df["gross"] == 0])

# Now filling the missing values in the dataset for budget
# First checking the distribution of the data
print("Printing the skewness of budget and then plotting budget")
print(df["budget"].skew())
sns.histplot(df["budget"].dropna(), kde=True)
plt.show()

# As the graph and the skew function suggest the data in the budget column so we will use median to fill it
df["budget"] = df["budget"].fillna(df["budget"].median())
print("Printing skewness of gross and plotting gross")
print(df["gross"].skew())
sns.histplot(df["gross"].dropna(), kde=True)
plt.show()

# Same case here that it is highly skewed data
# So now filling the gross with the median
df["gross"] = df["gross"].fillna(df["gross"].median())

# For the text data like company we cannot fill it with any data from our side as it is not a rule that which company might have produced this content
# So to handle these null values I will fill it with UNKNWON
# I cannot leave these values as it is as if I do so they will not be used during plotting or groupby. I don't want to loose data so I will not delete them as well.
df["company"] = df["company"].fillna("UNKNOWN")

print("Again printing to see how many null values are still left")
print(df.isna().sum())
print("Column of stars")
print(df["star"])

print("\n")
print("Checking if there are any duplicated rows")
print(df.duplicated().sum())

# As only 1 row is missing so we can drop it
df = df.dropna(subset=["star"])

print("Finally printing that if all null values are fixed")
print(df.isna().sum())

# Adding new columns
df["profit"] = df["gross"] - df["budget"]
# As votes cannot be a float so I will convert them to integers to save memory
df["votes"] = df["votes"].astype("int")
df["runtime"] = df["runtime"].astype("int")

print("Printing dtypes of all columns")
print(df.dtypes)
decades = (df["year"] // 10) * 10
df.insert(loc=4, column="decade", value=decades)
print("Printing info of the dataframe")
print(df.info())
print("Printing decades column")
print(df["decade"])

# Now I am going to get the genre with highest IMDB average score
average_genre_score = df.groupby("genre")["score"].mean()
print("Getting the genre which has maximum IMDb score")
print(average_genre_score.idxmax())
sns.barplot(average_genre_score)
plt.xticks(rotation=45)
plt.show()

print(f"The category with highest average IMDb score is {average_genre_score.idxmax()}")

# Top 10 Directors by Average Score
# I am doing this because I don't want any director with only one movie which is super-hit to be classified as top director
movie_count = df["director"].value_counts()
qualified_directors = movie_count[movie_count > 3].index
average_director_score = df[df["director"].isin(qualified_directors)].groupby("director")["score"].mean()
print("Printing top director")
print(average_director_score.idxmax())
plt.figure(figsize=(10, 8))
sns.barplot(average_director_score.sort_values(ascending=False).head(20))
plt.xticks(rotation=45)
plt.show()

print(f"The top director with highest average IMDb score is {average_director_score.idxmax()}")

# Does runtime affect scores?
corelation = df["runtime"].corr(df["score"])
print("Correaltion between runtime and scroe")
print(corelation)

# As we got 0.4 corr that means correlation is not very strong but still runtime and score are positively correlated
# sns.regplot(x=df["runtime"], y=df["score"], line_kws={"color": "red", "lw": 4})
# plt.show()

# Do bigger budgets earn more gross?
print("Correaltion between budget and gross")
print(df["budget"].corr(df["gross"]))

# This value of corr suggests that they are highly and positively co-related
sns.regplot(x=df["budget"], y=df["gross"], color="green", line_kws={"color": "red", "lw": 4})
plt.show()

# Which genre makes the most money on average?
average_genre_gross = df.groupby("genre")["gross"].mean() / 1e6
print("Data is in millions")
print(average_genre_gross)

plt.figure(figsize=(10, 8))
sns.barplot(x=average_genre_gross.head(30).values, y=average_genre_gross.head(30).index)
plt.xlabel("Millions")
plt.ylabel("genre")
plt.show()

# Which country produces most movies?
movie_count_per_country = df["country"].value_counts().head(15)  # I am using head although all countries can be displayed but on scale count will not be visible as the count of movies is very less

plt.figure(figsize=(10, 10))
sns.barplot(y=movie_count_per_country.index, x=movie_count_per_country.values)
plt.xlabel("movie count")
plt.ylabel("country")
plt.show()

# Biggest flop
flop_movie = df.loc[df["profit"].idxmin()]

print(f"The biggest flop movie is {flop_movie['name']}")

# Most successful movie
success_movie = df.loc[df["profit"].idxmax()]

print(f"The most successful movie is {success_movie['name']}")

# Best decade quality by highest average score
score_mean_per_decade = df.groupby("decade")["score"].mean()

print(f"The best decade quality by highest average score is {score_mean_per_decade.idxmax()}")

sns.barplot(score_mean_per_decade)
plt.show()
