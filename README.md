# Data Visualization Dashboard

This project is a simple web application built using Flask and D3.js to visualize data from a CSV file. Users can upload a CSV file, and the application generates various charts based on the data.

## Getting Started

### Prerequisites

- Python (version 3.6 or higher)
- Flask (install using `pip install Flask`)

### Installation

1. Clone the repository:

   git clone https://github.com/bethvourc/dataRepresentation.git
   cd dataRepresentation

2. Install dependencies:

   pip install Flank
   pip install Panda


### Usage

1. Run the Flask application:

   python app.py


   The application will be accessible at http://localhost:5000 in your web browser.

2. Upload a CSV file through the web interface to visualize the data.

## Project Structure

data_visualization_dashboard/
|-- static/
|   |-- js/
|       |-- d3.min.js
|-- templates/
|   |-- index.html
|-- app.py
|-- requirements.txt
|-- README.md


- **static/js/d3.min.js:** D3.js library for data visualization.
- **templates/index.html:** HTML template for the web interface.
- **app.py:** Python script for the Flask backend.

## Customization

- **Adding More Charts:** Customize the `prepare_charts_data` function in `app.py` to generate different types of charts based on your specific requirements.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.