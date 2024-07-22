# 🎓 Student Grades Analysis App

A Streamlit app for analyzing student grades with a FastAPI backend!


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

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License.


