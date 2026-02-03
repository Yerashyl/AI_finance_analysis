import pandas as pd
import io
import sys
import os

# Ensure app is in path
sys.path.append(os.getcwd())

from app.services.visualizer import generate_charts
from app.ml.nlp import analyze_comments

def test_visualization():
    print("Testing Visualization...")
    df = pd.DataFrame({
        "category": ["A", "A", "B", "C"],
        "name": ["Item 1", "Item 2", "Item 3", "Item 4"],
        "total_sum": [100, 200, 300, 400]
    })
    charts = generate_charts(df)
    assert "category_dist" in charts
    assert "top_items" in charts
    print("Charts generated successfully: ", list(charts.keys()))

def test_nlp():
    print("\nTesting NLP with Transformers...")
    df = pd.DataFrame({
        "comment": [
            "нужно проверить цену",  # should match "проверить"
            "какая-то ошибка здесь", # should match "ошибка"
            "non-relevant comment",   # should match nothing
            "доставка слишком дорогая" # should match "доставка"
        ]
    })
    
    # Run analysis
    df = analyze_comments(df)
    
    print("NLP Results:")
    print(df[['comment', 'comment_tags']])
    
    # Check if tags were assigned
    assert "проверить" in df.iloc[0]['comment_tags']
    assert "ошибка" in df.iloc[1]['comment_tags']
    assert "доставка" in df.iloc[3]['comment_tags']

if __name__ == "__main__":
    try:
        test_visualization()
        test_nlp()
        print("\n✅ Verification Passed!")
    except Exception as e:
        print(f"\n❌ Verification Failed: {e}")
        # Print traceback
        import traceback
        traceback.print_exc()
