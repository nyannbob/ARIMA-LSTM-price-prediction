# ARIMA-LSTM price prediction
<table>
    <tr>
        <td><img src="https://github.com/nyannbob/ARIMA-LSTM-price-prediction/blob/main/plots/Hybrid_sensex.png" alt="Image 1" width="400"></td>
        <td><img src="https://github.com/nyannbob/ARIMA-LSTM-price-prediction/blob/main/plots/LSTM_sensex.png" alt="Image 2" width="400"></td>
    </tr>
    <tr>
        <td  style="text-align: center;">Hybrid ARIMA-LSTM model predicting on Sensex</td>
        <td  style="text-align: center;">LSTM model predicting on Sensex</td>
    </tr>
</table>

This repository contains code to analyze stock price predictions using a hybrid Long Short-Term Memory (LSTM) and AutoRegressive Integrated Moving Average (ARIMA) model, referred to as the **LSTM-ARIMA** model. This hybrid approach combines the strengths of both models, with LSTM capturing non-linear patterns and ARIMA addressing linear components, enhancing predictive accuracy for financial time series. The model has been evaluated on key Indian equity indices: Nifty, NiftyBank, and Sensex.

## Project Overview

Stock price prediction is a challenging task due to the non-linear and volatile nature of financial markets. Traditional ARIMA models are effective for linear patterns, while LSTMs excel at modeling non-linear dependencies. This project merges these approaches, where residuals from ARIMA predictions serve as inputs for LSTM, thus integrating linear and non-linear forecasting capabilities. The hybrid model’s performance is evaluated using metrics such as Mean Squared Error (MSE) and Directional Accuracy, demonstrating its superiority over standalone ARIMA and LSTM models.

## Repository Contents

The repository includes the following files:
1. **`LSTM.ipynb`** - Notebook implementing the standalone LSTM model for stock price prediction.
2. **`ARIMA.ipynb`** - Notebook implementing the standalone ARIMA model, including preprocessing steps to ensure data stationarity.
3. **`LSTM_ARIMA.ipynb`** - Notebook that combines LSTM and ARIMA models, with ARIMA residuals passed into the LSTM for hybrid forecasting.
4. **`runner.py`** - A Python script that executes the hybrid model (`LSTM_ARIMA`) and optionally the standalone models for comparison.

## Methodology

1. **ARIMA Modeling**:
   - The ARIMA model is trained to capture the linear components in stock price data. The stationarity of the data is checked and achieved via differencing. Model parameters are optimized using the Akaike Information Criterion (AIC) to minimize error.

2. **Residual Extraction**:
   - Residuals (i.e., the errors in ARIMA predictions) are extracted to capture non-linear components that ARIMA alone cannot model.

3. **LSTM Modeling**:
   - The residuals are input into an LSTM model to predict non-linear trends, allowing the hybrid model to address both linear and non-linear dependencies.

4. **Hybrid Forecasting**:
   - The combined predictions of ARIMA and LSTM yield improved forecast accuracy, providing valuable signals for investment strategies.

5. **Model Evaluation**:
   - Performance is assessed via Walk-Forward Validation to ensure adaptability to changing market conditions, using metrics such as RMSE, MAPE, and R².

## Results

The hybrid LSTM-ARIMA model consistently outperformed standalone LSTM and ARIMA models, achieving lower error rates and higher R² scores. For instance, on the Nifty index, the hybrid model achieved an RMSE of 370.23, a R² of 0.9715, and a MAPE of 1.78%. These results underscore the model's ability to capture complex patterns in financial time series data.

## Requirements

- Python 3.x
- Jupyter Notebook
- Required packages listed in `requirements.txt`

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the runner module
   ```bash
   python runner.py
   ```
3. Or run the Jupyter notebooks separately
   
