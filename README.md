# CS361_risk_free_interest_rate_microservice

## How to run the server:

1. Run requirements:
   git install requests, git install flask

2. Run the server:
   python app.py

## How to request the data:
  ### GET /risk-free-interest-rate 
  Returns the most recent risk-free interest rate from the fiscal data API

  Example call: http://localhost:5000/risk-free-interest-rate

## How to receive the data: 
  The API will automatically respond with JSON data with the rate as the key and the risk-free interest rate as the value 

## UML Sequence Diagram
```
User                     Risk-free interest rate Microservice           Fiscal Data API
  |                                        |                                   |
  |----------RequestRiskFreeRate-------->  |                                   |
  |                                        |----------RetrieveData(date)------>|
  |                                        |<---ReturnData(t-bond avg rate)----|
  |<--ReturnRiskFreeRate(rate)------------ |                                   |
  |                                        |                                   |

```




  

