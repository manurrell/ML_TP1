import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Dataprocessor:
    def __init__(self, df):
        self.df = df
        self.mean_std = []
    def handle_missing_values(self):
        # self.df = self.df.dropna()
        # return self.df
        for column in self.df.columns:
            if self.df[column].nunique() == 2:  # Verifica si es binaria y asi dejar las columnas binarias como binarias usando la mediana
                median_value = self.df[column].median()
                self.df[column] = self.df[column].fillna(median_value)
            else:
                mean_value = self.df[column].mean()
                self.df[column] = self.df[column].fillna(mean_value)
        return self.df
    
    def set_area_units(self):
        self.df.loc[self.df["area_units"] == "sqft", "area"] *= 0.092903
        self.df = self.df.drop(columns=["area_units"])
        return self.df

    def normalize(self):
        #reg
        # Z-score
        for col in self.df.columns:
            if col != "price":
                self.mean_std.append((self.df[col].mean(), self.df[col].std()))
                self.df[col] = (self.df[col] - self.df[col].mean()) / self.df[col].std()
                
            
    def normalize_new_data(self, X):
        i = 0
        for col in X.columns:
            if col != "price":
                X[col] = (X[col] - self.mean_std[i][0]) / self.mean_std[i][1]
                i += 1
        return X
        
    def get_data(self):
        return self.df
    def get_means_std(self):
        return self.mean_std
