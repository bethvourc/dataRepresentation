from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            df = pd.read_csv(file)
            charts_data = prepare_charts_data(df)
            return jsonify({'success': True, 'charts_data': charts_data})
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}'})

def prepare_charts_data(df):
    # Customize this function based on the charts you want to generate
    # For simplicity, let's assume we are creating a bar chart for each column
    charts_data = {}
    for column in df.columns:
        charts_data[column] = {
            'type': 'bar',
            'data': df[column].tolist(),
            'labels': df.index.tolist(),
        }
    return charts_data

if __name__ == '__main__':
    app.run(debug=True)
