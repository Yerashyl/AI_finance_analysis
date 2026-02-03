import pandas as pd
import matplotlib.pyplot as plt
import io

def generate_charts(df: pd.DataFrame) -> dict[str, io.BytesIO]:
    """
    Generates analysis charts from the dataframe.
    Returns a dictionary of {chart_name: image_bytes}.
    """
    charts = {}
    
    # 1. Category Distribution (Pie Chart)
    if "category" in df.columns and "total_sum" in df.columns:
        plt.figure(figsize=(10, 6))
        category_sum = df.groupby("category")["total_sum"].sum()
        
        # Filter out very small categories for cleaner chart
        limit = category_sum.sum() * 0.02
        category_sum_filtered = category_sum[category_sum >= limit]
        other_sum = category_sum[category_sum < limit].sum()
        if other_sum > 0:
            category_sum_filtered["Other"] = other_sum

        category_sum_filtered.plot(kind="pie", autopct="%1.1f%%", startangle=140)
        plt.title("Budget Distribution by Category")
        plt.ylabel("")
        
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        charts["category_dist"] = buf
        plt.close()

    # 2. Top 5 Most Expensive Items (Bar Chart)
    if "name" in df.columns and "total_sum" in df.columns:
        plt.figure(figsize=(10, 6))
        top_items = df.nlargest(5, "total_sum")
        
        # Truncate long names
        names = top_items["name"].astype(str).apply(lambda x: x[:20] + "..." if len(x) > 20 else x)
        
        plt.bar(names, top_items["total_sum"], color='skyblue')
        plt.title("Top 5 Most Expensive Items")
        plt.xlabel("Item")
        plt.ylabel("Total Sum")
        plt.xticks(rotation=45)
        
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        charts["top_items"] = buf
        plt.close()

    return charts
