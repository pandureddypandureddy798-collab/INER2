"""
Project 02: Data Visualization with Matplotlib & Seaborn
InternCircle Learner Guide Implementation

This script loads the 'tips' dataset, generates informative, honest data visualizations
(histogram, box plot, scatter plot, bar chart, and correlation heatmap), and exports
high-resolution figures (150 DPI) following data storytelling best practices.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set consistent, color-blind friendly aesthetic theme
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.titlesize": 16,
    "figure.autolayout": False
})

def load_data() -> pd.DataFrame:
    """Load the tips dataset from seaborn."""
    df = sns.load_dataset("tips")
    return df

def generate_individual_plots(df: pd.DataFrame, output_dir: str = "images") -> None:
    """Generate and save individual high-resolution plots with takeaways."""
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Histogram: Distribution of Total Bill
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["total_bill"], bins=20, kde=True, color="#2b5c8f", ax=ax)
    ax.set_title("Most Dining Bills Range Between $10 and $25 (Right-Skewed Distribution)", 
                 fontsize=13, pad=12, fontweight="bold")
    ax.set_xlabel("Total Bill Amount (USD)", fontsize=11)
    ax.set_ylabel("Number of Meals", fontsize=11)
    # Adding takeaway annotation text at the bottom of the figure
    fig.text(0.5, 0.01, 
             "Takeaway: Most bills fall between $10 and $25 with a median of $17.80; high bills past $40 create a right skew.",
             ha="center", fontsize=9.5, style="italic", color="#333333")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(os.path.join(output_dir, "01_distribution_total_bill_histogram.png"), dpi=150)
    plt.close()

    # 2. Box Plot: Tips across Days
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="day", y="tip", hue="day", palette="deep", legend=False, ax=ax)
    ax.set_title("Weekend Meals Show Higher Median Tips and Greater Spending Variance", 
                 fontsize=13, pad=12, fontweight="bold")
    ax.set_xlabel("Day of the Week", fontsize=11)
    ax.set_ylabel("Tip Amount (USD)", fontsize=11)
    fig.text(0.5, 0.01, 
             "Takeaway: Sunday and Saturday produce higher median tips (~$3.00) and upper outliers reaching $10.00.",
             ha="center", fontsize=9.5, style="italic", color="#333333")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(os.path.join(output_dir, "02_tips_by_day_boxplot.png"), dpi=150)
    plt.close()

    # 3. Scatter Plot: Total Bill vs Tip by Meal Time
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", palette=["#2b5c8f", "#d95f02"], 
                    alpha=0.85, s=60, ax=ax)
    ax.set_title("Larger Bills Consistently Yield Larger Tips Across Both Lunch and Dinner", 
                 fontsize=13, pad=12, fontweight="bold")
    ax.set_xlabel("Total Bill Amount (USD)", fontsize=11)
    ax.set_ylabel("Tip Amount (USD)", fontsize=11)
    ax.legend(title="Dining Time", loc="upper left", frameon=True)
    fig.text(0.5, 0.01, 
             "Takeaway: A strong positive linear correlation exists between bill size and tip amount across lunch and dinner.",
             ha="center", fontsize=9.5, style="italic", color="#333333")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(os.path.join(output_dir, "03_total_bill_vs_tip_scatterplot.png"), dpi=150)
    plt.close()

    # 4. Bar Chart: Average Bill by Day & Smoking Status
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df, x="day", y="total_bill", hue="smoker", palette=["#4575b4", "#f46d43"], 
                errorbar=("ci", 68), ax=ax)
    ax.set_title("Average Total Bill Peaks on Weekends for Both Smokers and Non-Smokers", 
                 fontsize=13, pad=12, fontweight="bold")
    ax.set_xlabel("Day of the Week", fontsize=11)
    ax.set_ylabel("Average Total Bill (USD)", fontsize=11)
    ax.set_ylim(bottom=0)  # Honest charting rule: zero baseline for bar chart
    ax.legend(title="Smoker", loc="upper left", frameon=True)
    fig.text(0.5, 0.01, 
             "Takeaway: Sunday bills average highest for non-smokers ($21.41) while Saturday peaks for smokers ($21.28).",
             ha="center", fontsize=9.5, style="italic", color="#333333")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(os.path.join(output_dir, "04_average_bill_by_day_smoker_barchart.png"), dpi=150)
    plt.close()

    # 5. Correlation Heatmap
    fig, ax = plt.subplots(figsize=(7, 5))
    corr_matrix = df.select_dtypes("number").corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="Blues", vmin=0, vmax=1,
                cbar_kws={"label": "Pearson Correlation Coefficient"}, ax=ax)
    ax.set_title("Total Bill and Tip Exhibit the Strongest Linear Correlation (r = 0.68)", 
                 fontsize=13, pad=12, fontweight="bold")
    fig.text(0.5, 0.01, 
             "Takeaway: Strongest relationship is between total bill and tip (r = 0.68), followed by total bill and party size (0.60).",
             ha="center", fontsize=9.5, style="italic", color="#333333")
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(os.path.join(output_dir, "05_correlation_matrix_heatmap.png"), dpi=150)
    plt.close()

def generate_2x2_overview(df: pd.DataFrame, output_path: str = "tips_overview.png") -> None:
    """
    Generate the 2x2 dashboard figure matching the learner guide requirements.
    Saved at 150 DPI with clear titles, labeled axes, units, and takeaway notes.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle("Restaurant Tipping Dynamics: Exploratory Data Overview", 
                 fontsize=18, fontweight="bold", y=0.98)

    # Subplot [0, 0]: Histogram
    sns.histplot(df["total_bill"], bins=20, kde=True, color="#2b5c8f", ax=axes[0, 0])
    axes[0, 0].set_title("Most Bills Are Concentrated Under $25", fontweight="bold", pad=8)
    axes[0, 0].set_xlabel("Total Bill (USD)")
    axes[0, 0].set_ylabel("Number of Meals")
    axes[0, 0].text(0.5, -0.22, "Takeaway: Distribution is right-skewed; majority of bills lie between $10 and $25.",
                    transform=axes[0, 0].transAxes, ha="center", fontsize=9, style="italic", color="#333333")

    # Subplot [0, 1]: Boxplot
    sns.boxplot(data=df, x="day", y="tip", hue="day", palette="deep", legend=False, ax=axes[0, 1])
    axes[0, 1].set_title("Tips Vary Modestly by Day with Higher Weekend Spreads", fontweight="bold", pad=8)
    axes[0, 1].set_xlabel("Day of Week")
    axes[0, 1].set_ylabel("Tip Amount (USD)")
    axes[0, 1].text(0.5, -0.22, "Takeaway: Median tip hovers near $3.00, with top tipping outliers appearing on Sat & Sun.",
                    transform=axes[0, 1].transAxes, ha="center", fontsize=9, style="italic", color="#333333")

    # Subplot [1, 0]: Scatter plot
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", palette=["#2b5c8f", "#d95f02"], 
                    alpha=0.85, s=55, ax=axes[1, 0])
    axes[1, 0].set_title("Bigger Bills Consistently Bring Bigger Tips", fontweight="bold", pad=8)
    axes[1, 0].set_xlabel("Total Bill (USD)")
    axes[1, 0].set_ylabel("Tip Amount (USD)")
    axes[1, 0].legend(title="Time of Day", loc="upper left")
    axes[1, 0].text(0.5, -0.22, "Takeaway: Positive linear trend; dinner accommodates higher overall bills and top tips.",
                    transform=axes[1, 0].transAxes, ha="center", fontsize=9, style="italic", color="#333333")

    # Subplot [1, 1]: Correlation Heatmap
    corr = df.select_dtypes("number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues", vmin=0, vmax=1,
                cbar_kws={"label": "Pearson Correlation"}, ax=axes[1, 1])
    axes[1, 1].set_title("Total Bill Has Strongest Correlation with Tip (r = 0.68)", fontweight="bold", pad=8)
    axes[1, 1].text(0.5, -0.22, "Takeaway: Total bill & tip show strongest positive link (0.68); size & tip show moderate (0.49).",
                    transform=axes[1, 1].transAxes, ha="center", fontsize=9, style="italic", color="#333333")

    plt.tight_layout(rect=[0, 0.04, 1, 0.95])
    plt.savefig(output_path, dpi=150)
    plt.close()

def generate_comprehensive_dashboard(df: pd.DataFrame, output_path: str = "tips_dashboard.png") -> None:
    """
    Generate an expanded 5-chart dashboard integrating the required bar chart alongside
    the histogram, boxplot, scatterplot, and correlation heatmap.
    """
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1], hspace=0.45, wspace=0.25)
    fig.suptitle("Restaurant Performance & Customer Tipping Patterns: Executive Dashboard", 
                 fontsize=18, fontweight="bold", y=0.98)

    # 1. Histogram (Row 0, Col 0)
    ax0 = fig.add_subplot(gs[0, 0])
    sns.histplot(df["total_bill"], bins=20, kde=True, color="#2b5c8f", ax=ax0)
    ax0.set_title("1. Distribution of Total Bill Amounts (Skewed Right)", fontweight="bold")
    ax0.set_xlabel("Total Bill (USD)")
    ax0.set_ylabel("Meal Count")
    ax0.text(0.5, -0.24, "Takeaway: 75% of customer bills are $24.13 or lower; median bill is $17.80.",
             transform=ax0.transAxes, ha="center", fontsize=8.5, style="italic", color="#333333")

    # 2. Box Plot (Row 0, Col 1)
    ax1 = fig.add_subplot(gs[0, 1])
    sns.boxplot(data=df, x="day", y="tip", hue="day", palette="deep", legend=False, ax=ax1)
    ax1.set_title("2. Tip Distribution Across Days of the Week", fontweight="bold")
    ax1.set_xlabel("Day")
    ax1.set_ylabel("Tip (USD)")
    ax1.text(0.5, -0.24, "Takeaway: Sunday and Saturday show wider variance and maximum tips reaching $10.00.",
             transform=ax1.transAxes, ha="center", fontsize=8.5, style="italic", color="#333333")

    # 3. Scatter Plot (Row 1, Col 0)
    ax2 = fig.add_subplot(gs[1, 0])
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", palette=["#2b5c8f", "#d95f02"], 
                    alpha=0.85, s=60, ax=ax2)
    ax2.set_title("3. Total Bill vs. Tip Amount by Dining Period", fontweight="bold")
    ax2.set_xlabel("Total Bill (USD)")
    ax2.set_ylabel("Tip (USD)")
    ax2.legend(title="Time", loc="upper left")
    ax2.text(0.5, -0.24, "Takeaway: Clear upward trend confirms tips scale directly with total spend across lunch and dinner.",
             transform=ax2.transAxes, ha="center", fontsize=8.5, style="italic", color="#333333")

    # 4. Bar Chart (Row 1, Col 1)
    ax3 = fig.add_subplot(gs[1, 1])
    sns.barplot(data=df, x="day", y="total_bill", hue="smoker", palette=["#4575b4", "#f46d43"], 
                errorbar=("ci", 68), ax=ax3)
    ax3.set_title("4. Mean Bill by Day and Smoking Status (Honest Zero Baseline)", fontweight="bold")
    ax3.set_xlabel("Day")
    ax3.set_ylabel("Average Total Bill (USD)")
    ax3.set_ylim(bottom=0)
    ax3.legend(title="Smoker", loc="upper left")
    ax3.text(0.5, -0.24, "Takeaway: Weekend spending is highest; Sunday non-smokers and Saturday smokers generate top bills.",
             transform=ax3.transAxes, ha="center", fontsize=8.5, style="italic", color="#333333")

    # 5. Heatmap (Row 2, Spanning Both Columns)
    ax4 = fig.add_subplot(gs[2, :])
    corr = df.select_dtypes("number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues", vmin=0, vmax=1,
                cbar_kws={"label": "Pearson Correlation Coefficient"}, ax=ax4)
    ax4.set_title("5. Correlation Matrix: Strongest Relationship Between Total Bill and Tip (r = 0.68)", 
                  fontweight="bold")
    ax4.text(0.5, -0.22, "Takeaway: Total bill is the primary linear driver of tip size (r = 0.68); party size has secondary influence (r = 0.49).",
             transform=ax4.transAxes, ha="center", fontsize=9, style="italic", color="#333333")

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.08, right=0.95, hspace=0.45, wspace=0.25)
    plt.savefig(output_path, dpi=150)
    plt.close()

def main():
    print("Loading tips dataset...")
    df = load_data()
    print(f"Dataset successfully loaded: {df.shape[0]} rows, {df.shape[1]} columns.")
    
    print("Generating individual figures with takeaways...")
    generate_individual_plots(df)
    
    print("Generating 2x2 overview dashboard (tips_overview.png)...")
    generate_2x2_overview(df, "tips_overview.png")
    
    print("Generating comprehensive executive dashboard (tips_dashboard.png)...")
    generate_comprehensive_dashboard(df, "tips_dashboard.png")
    
    print("All visualizations successfully created at 150 DPI.")

if __name__ == "__main__":
    main()
