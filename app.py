from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/api/bikes', methods=['GET'])
def get_bikes():
    csv_url = "https://raw.githubusercontent.com/cem1000/DublinBikeAvailability/main/dublinbikes.csv"
    df = pd.read_csv(csv_url)
    
    # Fetch parameters from the query string
    address = request.args.get('address')
    day_of_week = request.args.get('day_of_week')
    
    # Filter based on the address if provided
    if address:
        df = df[df['address'].str.contains(address, case=False, na=False)]
    
    # Filter based on the day of the week if provided
    if day_of_week:
        df = df[df['day_of_week'] == day_of_week]

    # Convert DataFrame to JSON
    result = df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
