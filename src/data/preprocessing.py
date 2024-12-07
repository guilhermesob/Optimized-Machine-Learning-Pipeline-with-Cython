import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Limpeza de dados:
    - Remove valores ausentes
    - Corrige inconsistências
    """
    df = df.dropna()  # Remove linhas com valores ausentes
    # Exemplo: corrigir tipos de dados inconsistentes
    # df['column'] = df['column'].astype(int)
    return df

def transform_data(df, numerical_features, categorical_features):
    """
    Transforma dados:
    - Escalona variáveis numéricas
    - Codifica variáveis categóricas
    """
    num_transformer = StandardScaler()
    cat_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_transformer, numerical_features),
            ('cat', cat_transformer, categorical_features)
        ]
    )

    return preprocessor

def split_data(df, target_column, test_size=0.2, random_state=42):
    """
    Divide os dados em treino e teste.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test

def preprocess_pipeline(file_path, target_column, numerical_features, categorical_features):
    """
    Pipeline completo de preprocessamento.
    """
    df = load_data(file_path)
    df = clean_data(df)
    preprocessor = transform_data(df, numerical_features, categorical_features)
    
    X_train, X_test, y_train, y_test = split_data(df, target_column)
    
    # Ajustar o pipeline apenas no conjunto de treino
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)
    
    return X_train, X_test, y_train, y_test
