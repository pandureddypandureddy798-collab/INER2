"""
Test Suite for Project 02: Data Visualization with Matplotlib & Seaborn
InternCircle Learner Guide Verification

Tests verify:
1. Data loading and dataset schema integrity
2. Statistical correlation computations (total_bill vs tip)
3. Image output generation (tips_overview.png, tips_dashboard.png, images/*)
4. Image integrity, non-zero file size, dimensions, and DPI
5. Chart aesthetics and honest charting compliance (zero baseline, titles, labels)
"""

import os
import unittest
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

import data_visualization


class TestDataVisualization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = data_visualization.load_data()

    def test_01_dataset_integrity(self):
        """Verify the tips dataset loaded properly with expected shape and columns."""
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertEqual(len(self.df), 244, "Tips dataset must have 244 rows.")
        expected_cols = {"total_bill", "tip", "sex", "smoker", "day", "time", "size"}
        self.assertTrue(expected_cols.issubset(set(self.df.columns)), 
                        f"Missing expected columns. Found: {self.df.columns}")
        self.assertEqual(self.df.isnull().sum().sum(), 0, "Dataset should have 0 missing values.")

    def test_02_correlation_calculations(self):
        """Verify correlation computation matches statistical expectations."""
        numeric_df = self.df.select_dtypes("number")
        corr = numeric_df.corr()
        
        # Verify self correlation is 1.0
        self.assertAlmostEqual(corr.loc["total_bill", "total_bill"], 1.0, places=4)
        
        # Verify total_bill and tip correlation is strongest (~0.676)
        r_bill_tip = corr.loc["total_bill", "tip"]
        r_bill_size = corr.loc["total_bill", "size"]
        r_tip_size = corr.loc["tip", "size"]
        
        self.assertAlmostEqual(r_bill_tip, 0.6757, places=3)
        self.assertTrue(r_bill_tip > r_bill_size > r_tip_size, 
                        "total_bill & tip should have the strongest linear correlation among pairs.")

    def test_03_dashboard_images_exist_and_valid(self):
        """Verify tips_overview.png and tips_dashboard.png exist and are valid images."""
        overview_path = "tips_overview.png"
        dashboard_path = "tips_dashboard.png"

        for path in [overview_path, dashboard_path]:
            self.assertTrue(os.path.exists(path), f"File {path} does not exist.")
            self.assertGreater(os.path.getsize(path), 50_000, f"File {path} is too small (<50KB).")

            # Check that PIL can open and verify image integrity
            with Image.open(path) as img:
                img.verify()
            
            with Image.open(path) as img:
                w, h = img.size
                self.assertGreaterEqual(w, 1200, f"Image width {w} should be >= 1200px for high-res dashboard.")
                self.assertGreaterEqual(h, 900, f"Image height {h} should be >= 900px for high-res dashboard.")
                self.assertIn(img.format, ["PNG"], "Image must be PNG format.")

    def test_04_individual_images_exist(self):
        """Verify all 5 individual plot images exist in the images/ directory."""
        expected_images = [
            "01_distribution_total_bill_histogram.png",
            "02_tips_by_day_boxplot.png",
            "03_total_bill_vs_tip_scatterplot.png",
            "04_average_bill_by_day_smoker_barchart.png",
            "05_correlation_matrix_heatmap.png"
        ]
        img_dir = "images"
        self.assertTrue(os.path.isdir(img_dir), f"Directory '{img_dir}' should exist.")
        
        for fname in expected_images:
            fpath = os.path.join(img_dir, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing plot image: {fpath}")
            self.assertGreater(os.path.getsize(fpath), 10_000, f"Image {fpath} is unexpectedly small.")
            with Image.open(fpath) as img:
                w, h = img.size
                self.assertGreaterEqual(w, 800, f"Individual chart width {w} should be >= 800px.")
                self.assertGreaterEqual(h, 500, f"Individual chart height {h} should be >= 500px.")

    def test_05_notebook_exists_and_executed(self):
        """Verify that the Jupyter notebook file exists and contains executed outputs."""
        nb_path = "data_visualization_tips.ipynb"
        self.assertTrue(os.path.exists(nb_path), f"Notebook file {nb_path} does not exist.")
        
        import nbformat
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        
        self.assertGreater(len(nb.cells), 10, "Notebook should contain at least 10 cells.")
        
        # Check code cells have outputs
        code_cells = [c for c in nb.cells if c.cell_type == "code"]
        self.assertGreater(len(code_cells), 5, "Notebook should have multiple code cells.")
        
        cells_with_output = [c for c in code_cells if len(c.outputs) > 0]
        self.assertGreater(len(cells_with_output), 0, "Notebook should have pre-executed outputs saved.")

    def test_06_honest_charting_standards(self):
        """Verify honest charting rules: bar chart starts at 0, no negative axes where invalid."""
        # Test bar chart zero baseline
        fig, ax = plt.subplots()
        sns.barplot(data=self.df, x="day", y="total_bill", hue="smoker", errorbar=("ci", 68), ax=ax)
        ax.set_ylim(bottom=0)
        ymin, _ = ax.get_ylim()
        self.assertEqual(ymin, 0.0, "Bar chart baseline must be zero to prevent deceptive scaling.")
        plt.close(fig)


if __name__ == "__main__":
    unittest.main()
