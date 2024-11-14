# Optimized-Machine-Learning-Pipeline-with-Cython
Optimized Machine Learning Pipeline with Cython 
## Version: 0.0.3

## Overview

The **Optimized Machine Learning Pipeline with Cython** project integrates advanced technologies like Cython, C++, Rust, and Bayesian Optimization to create a highly efficient machine learning pipeline. This pipeline includes modules for data preprocessing, model training, evaluation, and advanced ML calculations, along with a Bayesian optimizer to fine-tune hyperparameters and improve model performance.

## Project Structure

The project is organized as follows:

```
Optimized Machine Learning Pipeline with Cython/
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── preprocessing.py       # Data preprocessing
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   ├── training.py            # Model training
│   │   └── evaluation.py          # Model evaluation
│   │   ├── model_training.py      # Model training function
│   │   └── hyperparameter_search.py # Bayesian optimizer integration
│   │
│   ├── calculations/
│   │   ├── __init__.py
│   │   ├── ml_calculations.pyx    # Cython interface for C++
│   │   ├── ml_calculations.cpp    # C++ backend for advanced calculations
│   │   ├── rust_calculations.rs   # Rust backend for intensive calculations
│   │   ├── bayesian_optimizer.pyx # Cython for Bayesian Optimization
│   │   ├── gauss_process.py       # Gaussian process implementation
│   │   └── acquisition_function.py # Acquisition function
│   │   └── setup.py               # Compilation setup for C++/Cython modules
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── setup_database.py      # SQLite database setup
│   │   └── results.db             # SQLite database for storing results
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── main_pipeline.py       # Main pipeline that runs the full process
│   │
│   └── utils/
│       ├── __init__.py
│       └── helper_functions.py    # Auxiliary functions and utilities
│
├── rust/
│   ├── Cargo.toml                 # Rust project configuration
│   ├── src/
│   │   ├── lib.rs                 # Main Rust code for calculations
│   │   └── utils.rs               # Rust utility functions
│   └── target/                    # Rust build output files
│
├── tests/
│   ├── test_preprocessing.py      # Tests for the preprocessing module
│   ├── test_training.py           # Tests for the training module
│   ├── test_evaluation.py         # Tests for the evaluation module
│   ├── test_calculations.py       # Tests for advanced calculations module
│   ├── test_rust_calculations.py  # Tests for Rust calculations module
│   ├── test_bayesian_optimizer.py # Tests for the Bayesian optimizer
│
├── docs/
│   ├── README.md                  # Project description and instructions
│   └── architecture.md            # Documentation about the architecture and design
│
├── setup.py                       # Project installation script
├── requirements.txt               # Project dependencies
└── .gitignore                     # Git ignore file

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
<br>
C++ compiler (for compiling the C++ code)
<br>
Cython (for Cython integration)
<br>
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




