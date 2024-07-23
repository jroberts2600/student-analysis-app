# 🎓 Student Grades Analysis Streamlit App

This Streamlit application serves as the frontend for interacting with the FastAPI backend to analyze student grades. Users can input their queries and receive responses from the backend.


## Features

- 📊 Query and analyze student grade data
- 🔗 Real-time interaction with FastAPI backend
- 👥 User-friendly interface for easy querying

## How to run it on your own machine

1. Clone the repository

   ```
   $ git clone https://github.com/yourusername/student-grades-analysis.git
   $ cd student-grades-analysis
   ```

2. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

3. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## Backend Configuration

The app connects to a FastAPI backend. Update the `api_url` in `streamlit_app.py` if your backend location changes:

```python
api_url = "https://<render> or <ngrok>/query"
```
## Google Colab

You can also interact with the backend through Google Colab. Click the link below to open the Colab notebook:
[Open in Google Colab](https://colab.research.google.com/drive/1vYXAJGlHQu9nC7Dyw9kgkZ_y2Khvacli?usp=sharing)

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License.


