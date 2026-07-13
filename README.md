**Students Placement Dashboard**

A Streamlit-based interactive dashboard for exploring and visualizing student placement data. The application allows users to filter numeric attributes using a range slider, inspect the filtered dataset, and generate bar and scatter plots for quick insights.

### Features

* Displays dataset dimensions.
* Interactive column selection and filtering.
* Range-based filtering for numeric columns.
* Dynamic bar and scatter visualizations using Altair.
* View of the filtered data table.

### Requirements

* Python 3.8+
* Streamlit
* Pandas
* Altair

Install dependencies with:

```bash
pip install streamlit pandas altair
```

### Running the Application

1. Place your dataset file (e.g., `dataset.csv`) in the project directory and update the file path in the script if necessary.
2. Start the app:

```bash
streamlit run dashboard.py
```

### Notes

The selected column for filtering and visualization must contain numeric data. Adjust the chart scale or file path in the code as needed for your dataset and environment.

Feel free to customize the dashboard further with additional charts, filters, or placement-specific metrics.
