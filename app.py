from flask import Flask, request, jsonify, render_template
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload_transactions', methods=['POST'])
def upload_transactions():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Read CSV into a DataFrame
    df = pd.read_csv(io.StringIO(file.stream.read().decode("utf-8")), sep=None, engine="python")
    
    # Process transactions
    df = df.dropna(subset=['Amount'])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Time of processing"] = pd.to_numeric(df["Time of processing"].str.extract(r'(\d+)')[0], errors="coerce")
    
    total_deposits = df[df["Status"] == "OK"]["Amount"].sum()
    total_withdrawals = df[df["Status"] == "Approved"]["Amount"].sum()
    net_balance = total_deposits - total_withdrawals
    avg_processing_time = df["Time of processing"].mean()
    
    summary = {
        "Total Deposits": total_deposits,
        "Total Withdrawals": total_withdrawals,
        "Net Balance": net_balance,
        "Average Processing Time (seconds)": avg_processing_time
    }
    
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
