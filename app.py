from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/bikes', methods=['GET'])
def get_bikes():
    csv_url = "https://raw.githubusercontent.com/cem1000/DublinBikeAvailability/main/dublinbikes.csv"
    df = pd.read_csv(csv_url)
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
