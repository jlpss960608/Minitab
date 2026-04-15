import pandas as pd
import numpy as np
import os

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        ext = os.path.splitext(self.file_path)[-1]
        if ext == '.csv':
            return pd.read_csv(self.file_path)
        elif ext in ['.xls', '.xlsx']:
            return pd.read_excel(self.file_path)
        # Add support for Numbers file if needed

    def clean_data(self, df):
        df.dropna(inplace=True)
        # Additional cleaning logic
        return df

    def parse(self):
        data = self.read_data()
        return self.clean_data(data);
