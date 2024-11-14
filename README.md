# Optimized-Machine-Learning-Pipeline-with-Cython
Optimized Machine Learning Pipeline with Cython 
## Version: 0.0.1

## Overview

The **Optimized Machine Learning Pipeline with Cython** project integrates advanced technologies like Cython, C++, Rust, and Bayesian Optimization to create a highly efficient machine learning pipeline. This pipeline includes modules for data preprocessing, model training, evaluation, and advanced ML calculations, along with a Bayesian optimizer to fine-tune hyperparameters and improve model performance.

## Project Structure

The project is organized as follows:

```
Optimized_Machine_Learning_Pipeline_with_Cython/
├── src/
│   ├── data/                       # Data preprocessing module
│   ├── model/                      # Model training and evaluation
│   ├── calculations/               # Advanced ML calculations (Cython, C++, Rust)
│   ├── database/                   # Database setup for storing results
│   ├── pipeline/                   # Main pipeline to execute the complete process
│   └── utils/                      # Helper functions and utilities
├── rust/                           # Rust implementation for high-performance calculations
├── tests/                          # Unit tests for various modules
├── docs/                           # Documentation and architecture
├── setup.py                        # Installation script for the project
├── requirements.txt                # List of dependencies
└── .gitignore                      # Git ignore file
```

# Key Features
Data Preprocessing: The data/preprocessing.py module handles data cleaning, transformation, and feature engineering.

Model Training & Evaluation: The model/training.py and model/evaluation.py files define model training, hyperparameter optimization, and performance evaluation.

Bayesian Optimization: The calculations/bayesian_optimizer.pyx module implements Bayesian Optimization using Cython to efficiently tune model hyperparameters.

C++ Backend for ML Calculations: calculations/ml_calculations.cpp provides high-performance ML calculations using C++ for computational efficiency, called via Cython.

Rust Backend: The rust/ directory contains Rust code for handling complex calculations and intensive tasks.

Database Integration: The database/setup_database.py sets up an SQLite database to store results, providing a mechanism to track experiments and outcomes.

Pipeline Execution: The main pipeline is managed through pipeline/main_pipeline.py, which orchestrates the workflow from data preprocessing to model evaluation.

# Installation
### Prerequisites
Before running this project, ensure that the following tools are installed on your system:

Python 3.x
Rust (for Rust-based backend)
C++ compiler (for compiling the C++ code)
Cython (for Cython integration)
SQLite (for database functionality)

# Install Dependencies
Clone the repository:
```
git clone https://github.com/guilhermesob/Optimized-Machine-Learning-Pipeline-with-Cython/
```

```
cd Optimized-Machine-Learning-Pipeline-with-Cython
```
## Install Python dependencies:

```bash
pip install -r requirements.txt
```
Install Rust dependencies by navigating to the rust/ directory:
```
cd rust
cargo build --release
```

## Cython Setup
To build the Cython extension that interfaces with C++, navigate to the src/calculations folder and run:

```
python setup.py build_ext --inplace
```

# Running the Project
You can execute the main pipeline through the following command:
```
python src/pipeline/main_pipeline.py
```

Testing
Unit tests are included to ensure the correctness of each module. Run the tests with:
```
pytest
```

# Documentation
For more details on the architecture and design of the project, refer to the Architecture Documentation.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.




