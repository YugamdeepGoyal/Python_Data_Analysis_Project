# Movies Dataset — Exploratory Data Analysis

A data analysis project that explores patterns and trends in movies released between 1980 and 2020, using a dataset of 7,668 films sourced from IMDb.

---

## Dataset Overview

**Source:** [Kaggle — danielgrijalvas/movies](https://www.kaggle.com/datasets/danielgrijalvas/movies)
**File:** `movies.csv`  
**Rows:** 7,668 movies  
**Time period:** 1980 – 2020

| Column | Description |
|---|---|
| `name` | Title of the movie |
| `rating` | MPAA rating (R, PG, PG-13, G, etc.) |
| `genre` | Primary genre |
| `year` | Year of release |
| `released` | Full release date and country |
| `score` | IMDb rating (out of 10) |
| `votes` | Number of IMDb votes |
| `director` | Director's name |
| `writer` | Writer's name |
| `star` | Lead actor/actress |
| `country` | Country of production |
| `budget` | Production budget (USD) |
| `gross` | Box office gross revenue (USD) |
| `company` | Production company |
| `runtime` | Runtime in minutes |

**Genres covered:** Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Family, Fantasy, History, Horror, Music, Musical, Mystery, Romance, Sci-Fi, Sport, Thriller, Western

---

## What This Project Does

### 1. Data Cleaning
- Drops rows missing critical fields: `score`, `votes`, `writer`, `country`, `runtime`, `rating`, `star`
- Fills missing `budget` and `gross` with their **median** values (chosen because both columns are highly right-skewed)
- Fills missing `company` with `"UNKNOWN"` to retain the row without guessing the value
- Removes duplicate rows
- Adds a derived `profit` column (`gross - budget`)
- Adds a `decade` column grouped by 10-year periods
- Converts `votes` and `runtime` from float to int

### 2. Analysis & Visualizations

**Genre analysis**
- Which genre has the highest average IMDb score?
- Which genre earns the most money on average?

**Director analysis**
- Top 20 directors by average IMDb score, filtering to only those with more than 3 movies (to avoid one-hit wonders skewing the results)

**Correlation studies**
- Does runtime affect IMDb score? (~0.4 correlation — weak but positive)
- Does bigger budget lead to higher gross revenue? (strong positive correlation)
- Scatter plot with regression line for budget vs gross

**Country analysis**
- Top 15 countries by number of movies produced (US leads by a large margin)

**Decade analysis**
- Which decade had the best average IMDb scores?

**Best and worst movies**
- Biggest flop (lowest profit)
- Most successful movie (highest profit)

---

## How to Run

**Requirements**
```
pip install numpy pandas matplotlib seaborn
```

**Run**
```bash
python app.py
```

Make sure `movies.csv` is in the same directory as the script.

---

## Project Structure

```
├── app.py   # Main analysis script
├── app.ipynb   # Main analysis script in .ipynb format
├── movies.csv           # Dataset
└── README.md
```

---

## Key Findings

- **Budget and gross** are strongly correlated — studios that spend more tend to earn more
- **Runtime and score** have a weak positive correlation (~0.4) — longer films score slightly higher but it's not a strong rule
- **United States** dominates production volume, followed by United Kingdom and France
- Directors with consistent output across multiple films tend to score more reliably than one-film wonders
