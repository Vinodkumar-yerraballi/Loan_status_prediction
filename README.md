# Loan Status Prediction Project

## Description
This project predicts loan approval status based on applicant data using machine learning. It includes data preprocessing, model training, and a web interface for predictions.

## Project Structure

### Root Directory
- `loan_prediction.csv`: Dataset containing loan applicant information and approval status.
- `main.py`: Main Python script for running the Flask web application and handling predictions.
- `request.py`: Module for handling API requests or data processing utilities.
- `requirements.txt`: List of Python dependencies required for the project.
- `README.md`: This file, providing project overview and instructions.

### notebook/
- `Loan Prediction Project.ipynb`: Jupyter notebook containing exploratory data analysis, model training, and evaluation.

### templates/
- `index.html`: Home page template for the web application.
- `prediction.html`: Template for displaying prediction results.
- `style.css`: CSS styles for the web interface.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Usage
- Access the web app at `http://localhost:5000` (assuming Flask default port).
- Upload or input applicant data to get loan approval predictions.

## Contributing
Feel free to submit issues or pull requests.