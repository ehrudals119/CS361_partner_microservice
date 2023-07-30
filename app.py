from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/risk-free-interest-rate', methods=['GET'])
def get_risk_free_interest_rate():
    year = datetime.today().strftime('%Y')

    first_day_of_current_month = datetime.today().replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)

    last_month = last_day_of_previous_month.strftime("%m")

    filter = f"?fields=security_desc,avg_interest_rate_amt,record_date&filter=record_calendar_year:eq:{year},record_calendar_month:eq:{last_month}&sort=-record_date"

    api_url = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates{filter}"

    data = requests.get(api_url).json()['data']

    t_bonds_obj = data[2]

    rf_rate = float(t_bonds_obj['avg_interest_rate_amt'])

    return jsonify({'rate': rf_rate})

if __name__ == "__main__":
    app.run(debug=True)