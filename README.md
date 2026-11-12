# Project 02: Data Visualization with Matplotlib & Seaborn
**InternCircle Learner Guide — Data Science & AI**  
*Level: Beginner | Estimated Time: ~6 Hours*

---

## 📊 Project Overview
This repository contains the complete implementation and test suite for **Project 02: Data Visualization with Matplotlib & Seaborn**. 

The goal of this project is to create a set of clear, honest, and impactful charts from the real-world **Tips dataset** (`sns.load_dataset('tips')`). The visualizations answer distinct business and behavioral questions regarding customer spending, tipping habits, and dining timing using modern visual storytelling principles.

---

## 🎯 Requirements & Standards Achieved
- [x] **Bar charts and scatter plots:** Categorical bill comparisons with confidence intervals and bivariate total-bill-to-tip scatter plots segmented by dining time.
- [x] **Correlation heatmap generation:** Annotated Pearson correlation matrix identifying the strongest statistical drivers.
- [x] **Custom color palettes & plot formatting:** Color-blind safe palettes (`deep`, `Blues`, contrasting blue/orange), readable typography, labeled axes with units (`USD ($)`).
- [x] **Finding-driven titles:** Titles state the insight rather than simply listing variables (e.g., *"Larger Bills Consistently Yield Larger Tips"*).
- [x] **One-line takeaway under every chart:** Explicit summary sentences explaining key takeaways.
- [x] **Honest charting standards:** Zero baseline enforced on bar charts, sensible axes, no 3D or pie charts, and `plt.tight_layout()` to prevent cutoff.
- [x] **Multi-panel dashboard export:** 2x2 dashboard saved at **150 DPI** (`tips_overview.png`), plus an extended executive dashboard (`tips_dashboard.png`).
- [x] **Comprehensive automated testing:** Unit test suite verifying dataset integrity, correlation values, and image file properties.

---

## 📁 Repository Structure
```text
INTER2/
├── README.md                                 # Complete documentation, analysis, and submission guide
├── data_visualization.py                     # Main script generating all individual & dashboard figures
├── data_visualization_tips.ipynb             # Full runnable Jupyter Notebook with executed cells & plots
├── test_visualizations.py                    # Automated test suite (6 passing unit tests)
├── tips_overview.png                         # Primary 2x2 dashboard figure (150 DPI)
├── tips_dashboard.png                        # Extended 5-chart executive dashboard (150 DPI)
├── generate_notebook.py                      # Programmatic notebook builder & runner
└── images/                                   # Individual high-resolution exported charts
    ├── 01_distribution_total_bill_histogram.png
    ├── 02_tips_by_day_boxplot.png
    ├── 03_total_bill_vs_tip_scatterplot.png
    ├── 04_average_bill_by_day_smoker_barchart.png
    └── 05_correlation_matrix_heatmap.png
```

---

## 🔍 Step-by-Step Analysis & Visual Storytelling

### Step 1 & 2: Formulating Questions and Matching Charts
| # | Business / Analytical Question | Chart Selection | Rationale |
|---|---|---|---|
| 1 | **How are total bill amounts distributed across dining parties?** | **Histogram + KDE** | Ideal for continuous univariate distribution, showing right-skewness and density concentration. |
| 2 | **Do tip amounts differ across days of the week?** | **Box Plot** | Displays median, quartiles, and outlier tipping behaviors across discrete categorical days. |
| 3 | **Does a bigger bill mean a bigger tip, and does dining period affect this?** | **Scatter Plot** | Captures bivariate linear association with hue differentiation (`Lunch` vs. `Dinner`). |
| 4 | **How does average bill size compare across days between smoking and non-smoking groups?** | **Bar Chart** | Categorical aggregation displaying mean spend with honest zero baseline and error bars. |
| 5 | **Which numeric variables move together, and what is the strongest relationship?** | **Correlation Heatmap** | Matrix of Pearson correlation coefficients ($r$) with color intensity and numeric annotations. |

---

### Step 3, 4 & 7: Visual Gallery and One-Line Takeaways

#### 1. Distribution of Total Bill Amounts (Histogram)
* **Title:** *Most Dining Bills Range Between $10 and $25 (Right-Skewed Distribution)*
* **Axis Labels:** X: `Total Bill Amount (USD)`, Y: `Number of Meals`
* **Takeaway:** *Most bills fall between $10 and $25 with a median of $17.80; high bills tapering off past $40 create a pronounced right skew.*

#### 2. Tip Amounts Across Days of the Week (Box Plot)
* **Title:** *Weekend Meals Show Higher Median Tips and Greater Spending Variance*
* **Axis Labels:** X: `Day of the Week`, Y: `Tip Amount (USD)`
* **Takeaway:** *Saturday and Sunday generate higher median tips (~$3.00) and upper outliers reaching $10.00 compared to Thursday and Friday.*

#### 3. Total Bill vs. Tip Amount by Meal Time (Scatter Plot)
* **Title:** *Larger Bills Consistently Yield Larger Tips Across Both Lunch and Dinner*
* **Axis Labels:** X: `Total Bill Amount (USD)`, Y: `Tip Amount (USD)`, Hue: `Dining Time`
* **Takeaway:** *A strong positive linear correlation exists between bill size and tip amount across lunch and dinner; dinner accounts for top spending parties.*

#### 4. Average Total Bill by Day and Smoker Status (Bar Chart)
* **Title:** *Average Total Bill Peaks on Weekends for Both Smokers and Non-Smokers*
* **Axis Labels:** X: `Day of the Week`, Y: `Average Total Bill (USD)`, Hue: `Smoker`
* **Honest Charting Rule:** Y-axis zero baseline enforced (`ax.set_ylim(bottom=0)`).
* **Takeaway:** *Sunday bills average highest for non-smokers ($21.41) while Saturday peaks for smokers ($21.28).*

#### 5. Correlation Heatmap
* **Title:** *Total Bill and Tip Exhibit the Strongest Linear Correlation (r = 0.68)*
* **Matrix Output:**
  ```text
              total_bill       tip      size
  total_bill    1.000000  0.675734  0.598315
  tip           0.675734  1.000000  0.489299
  size          0.598315  0.489299  1.000000
  ```
* **Takeaway:** *The strongest linear relationship in the dataset is between total bill and tip ($r = 0.68$), confirming customer spend is the primary predictor of gratuity.*

---

### Step 6: Combined Dashboard Images
Two high-resolution (150 DPI) dashboard graphics are generated:
1. **`tips_overview.png`**: The exact 2x2 multi-panel layout matching the Learner Guide specification.
2. **`tips_dashboard.png`**: An expanded executive dashboard incorporating the categorical bar chart alongside the other 4 figures.

---

## 🛡️ Review for Honesty Checklist
- [x] **Sensible Baselines:** Bar charts start strictly at zero, avoiding exaggerated relative difference illusions.
- [x] **No 3D or Pie Charts:** No distorted perspective angles or hard-to-read slices.
- [x] **Color-Blind Accessible:** Avoided red-green combinations; utilized Seaborn `deep` and `Blues` with high contrast.
- [x] **Layout & Margins:** Checked with `plt.tight_layout()` to guarantee no axes, tick values, or legends are clipped.
- [x] **Self-Contained Understanding:** Every figure contains finding-driven headers, units of measurement, and takeaway subtitles.

---

## 🚀 How to Run and Test

### 1. Prerequisites
Ensure Python 3.10+ is installed:
```powershell
python -m pip install pandas numpy matplotlib seaborn scikit-learn pillow nbformat nbclient
```

### 2. Generate Visualizations & Dashboards
```powershell
python data_visualization.py
```
*Output: Generates `tips_overview.png`, `tips_dashboard.png`, and individual chart files in `images/`.*

### 3. Run Automated Test Suite
```powershell
python -m unittest -v test_visualizations.py
```
*Expected Result:*
```text
test_01_dataset_integrity ... ok
test_02_correlation_calculations ... ok
test_03_dashboard_images_exist_and_valid ... ok
test_04_individual_images_exist ... ok
test_05_notebook_exists_and_executed ... ok
test_06_honest_charting_standards ... ok

Ran 6 tests in 1.3s - OK
```

### 4. Interactive Jupyter Notebook
Open the notebook in Jupyter Lab, Notebook, or VS Code:
```powershell
jupyter notebook data_visualization_tips.ipynb
```
*(All cells have already been pre-executed with rich interactive outputs).*

---

## 📤 Submission Deliverables
As requested in **What to Submit** (Page 3 of Learner Guide):
1. **Notebook and Script Code:** [`data_visualization_tips.ipynb`](data_visualization_tips.ipynb) and [`data_visualization.py`](data_visualization.py)
2. **Saved Chart Images:** [`tips_overview.png`](tips_overview.png) and [`images/`](images/)
3. **Written Takeaways:** Provided under every chart and documented in this [`README.md`](README.md).
