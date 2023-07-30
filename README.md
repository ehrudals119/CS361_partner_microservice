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
  |                                        |<---ReturnData(avg rate object)----|
  |<--ReturnRiskFreeRate(rate)------------ |                                   |
  |                                        |                                   |

```

1. User sends a GET request to /risk-free-interest-rate
2. Microservice gets today's date and uses that to get the last month and current year
3. Microservice calls fiscal data API to get avg interest rates data with the last month and current year as the filter value
4. Microservice returns treasury bond's average interest rate as JSON object




  

