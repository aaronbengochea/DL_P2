import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# Set the base directory containing the experiment subdirectories
base_dir = "experiments"

# Define the path for the output PDF files
loss_pdf = "experiment_loss_charts.pdf"
acc_pdf = "experiment_acc_charts.pdf"

# Get only subdirectories that begin with 'r' followed by a number and are non-empty
subdirs = [d for d in os.listdir(base_dir)
           if os.path.isdir(os.path.join(base_dir, d)) 
           and re.match(r"r\d+", d)
           and os.listdir(os.path.join(base_dir, d))]


# Sort subdirectories in descending order based on the numeric part (modify reverse=True for descending)
sorted_subdirs = sorted(subdirs, key=lambda x: int(x[1:2]), reverse=False)

# Create a PdfPages object to write multiple pages to one PDF file
with PdfPages(loss_pdf) as pdf:
    # Iterate over the sorted subdirectories
    for subdir in sorted_subdirs:
        subdir_path = os.path.join(base_dir, subdir)
        csv_path = os.path.join(subdir_path, "processed_log_history.csv")
        if os.path.exists(csv_path):
            # Load the CSV data into a DataFrame
            df = pd.read_csv(csv_path)

            # Create a new figure for the chart
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Plot "Train Loss" and "Test Loss" vs "Step" on the left y-axis
            l1, = ax.plot(df["Step"], df["Train Loss"], label="Train Loss", color='blue')
            l2, = ax.plot(df["Step"], df["Test Loss"], label="Test Loss", color='orange')
            ax.set_xlabel("Step")
            ax.set_ylabel("Loss")
            
            # Create a secondary y-axis for the learning rate
            ax2 = ax.twinx()
            l3, = ax2.plot(df["Step"], df["Learning Rate"], label="Learning Rate", color='green')
            ax2.set_ylabel("Learning Rate")

            # Combine legends from both axes
            lines = [l1, l2, l3]
            labels = [line.get_label() for line in lines]
            ax.legend(lines, labels, loc='upper right')
            
            ax.set_title(f"{subdir}")
            plt.tight_layout()

            # Save the figure to the PDF
            pdf.savefig(fig)
            plt.close(fig)
        else:
            print(f"CSV file not found in {subdir_path}")

print(f"Charts saved to {loss_pdf}")


with PdfPages(acc_pdf) as pdf:
    # Iterate over the sorted subdirectories
    for subdir in sorted_subdirs:
        subdir_path = os.path.join(base_dir, subdir)
        csv_path = os.path.join(subdir_path, "processed_log_history.csv")
        if os.path.exists(csv_path):
            # Load the CSV data into a DataFrame
            df = pd.read_csv(csv_path)

            # Create a new figure for the chart
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Plot "Train Loss" and "Test Loss" vs "Step" on the left y-axis
            l1, = ax.plot(df["Step"], df["Train Acc"], label="Train Acc", color='blue')
            l2, = ax.plot(df["Step"], df["Test Acc"], label="Test Acc", color='orange')
            ax.set_xlabel("Step")
            ax.set_ylabel("Acc")
            
            # Create a secondary y-axis for the learning rate
            ax2 = ax.twinx()
            l3, = ax2.plot(df["Step"], df["Learning Rate"], label="Learning Rate", color='green')
            ax2.set_ylabel("Learning Rate")

            # Combine legends from both axes
            lines = [l1, l2, l3]
            labels = [line.get_label() for line in lines]
            ax.legend(lines, labels, loc='upper right')
            
            ax.set_title(f"{subdir}")
            plt.tight_layout()

            # Save the figure to the PDF
            pdf.savefig(fig)
            plt.close(fig)
        else:
            print(f"CSV file not found in {subdir_path}")

print(f"Charts saved to {acc_pdf}")