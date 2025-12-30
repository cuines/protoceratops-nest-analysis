#!/usr/bin/env python3
"""
Analysis script for Protoceratops nest measurements.
Calculates descriptive statistics and visualizes size distribution.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Load nest measurement data from CSV."""
    df = pd.read_csv('nest_data.csv')
    return df

def compute_statistics(df):
    """Compute mean, standard deviation, and coefficient of variation."""
    stats = {}
    for col in ['femur_length_mm', 'skull_width_mm']:
        mean = df[col].mean()
        std = df[col].std()
        cv = (std / mean) * 100 if mean != 0 else np.nan
        stats[col] = {'mean': mean, 'std': std, 'cv': cv}
    return stats

def plot_distribution(df, column, save_path=None):
    """Plot histogram of a measurement column."""
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=10, kde=True, color='steelblue')
    plt.title(f'Distribution of {column.replace("_", " ").title()}')
    plt.xlabel('Millimeters (mm)')
    plt.ylabel('Frequency')
    if save_path:
        plt.savefig(save_path, dpi=150)
    else:
        plt.show()

def main():
    print("Protoceratops Nest Data Analysis")
    print("=" * 40)
    df = load_data()
    print(f"Loaded {len(df)} specimens.")
    print()
    
    stats = compute_statistics(df)
    for col, vals in stats.items():
        print(f"{col.replace('_', ' ').title()}:")
        print(f"  Mean = {vals['mean']:.2f} mm")
        print(f"  Standard deviation = {vals['std']:.2f} mm")
        print(f"  Coefficient of variation = {vals['cv']:.2f} %")
        print()
    
    # Plot femur length distribution
    plot_distribution(df, 'femur_length_mm', save_path='femur_length_distribution.png')
    print("Saved femur length distribution plot as 'femur_length_distribution.png'.")
    
    # Plot skull width distribution
    plot_distribution(df, 'skull_width_mm', save_path='skull_width_distribution.png')
    print("Saved skull width distribution plot as 'skull_width_distribution.png'.")

if __name__ == '__main__':
    main()