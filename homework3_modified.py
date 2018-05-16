"""
Creates a data frame from a SQL query on video ID, category ID, and language for videos.
See https://tutorials.technology/tutorials/08-How-to-check-that-file-exists-with-Python.html,
 importing Path function from pathlib module is most efficient for checking if file path exists
"""
from pathlib import Path

import sqlite3
import pandas as pd

def create_dataframe(file_path):
    """Checks that a file path is valid, then returns the video ID, category ID,
    and language ID for all videos from all 5 countries in a data frame."""
    filepath = Path(file_path)
    if not filepath.exists():
        raise ValueError
    #From https://www.dataquest.io/blog/python-pandas-databases/
    conn = sqlite3.connect(file_path)
    #Query from HW 1
    return pd.read_sql_query(
        "SELECT video_id, category_id, 'ca' AS language FROM CAvideos \
        UNION SELECT video_id, category_id, 'de' AS language FROM DEvideos \
        UNION SELECT video_id, category_id, 'fr' AS language FROM FRvideos \
        UNION SELECT video_id, category_id, 'gb' AS language FROM GBvideos \
        UNION SELECT video_id, category_id, 'us' AS language FROM USvideos;", conn)
