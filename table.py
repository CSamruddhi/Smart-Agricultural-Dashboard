import pandas as pd

# Load the dataset
df = pd.read_csv('Crop_Recommendation.csv')

# Define the columns for which you want to calculate the ranges
columns = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH_Value', 'Rainfall']

# Initialize an empty dictionary to store the ranges for each crop
crop_ranges = {}

# Iterate over each crop in the dataset
for crop in df['Crop'].unique():
    # Filter the dataset for the current crop
    crop_data = df[df['Crop'] == crop]
    
    # Calculate the min and max values for each column
    ranges = {}
    for col in columns:
        ranges[col] = (crop_data[col].min(), crop_data[col].max())
    
    # Store the ranges in the dictionary
    crop_ranges[crop] = ranges

# Convert the dictionary to a DataFrame for better visualization
ranges_df = pd.DataFrame.from_dict(crop_ranges, orient='index')

# Generate the HTML table rows
html_rows = []
for idx, (crop, ranges) in enumerate(crop_ranges.items(), start=1):
    row = f"""
    <tr>
        <td>{idx}</td>
        <td>{crop}</td>
        <td>{ranges['Nitrogen'][0]}-{ranges['Nitrogen'][1]}</td>
        <td>{ranges['Phosphorus'][0]}-{ranges['Phosphorus'][1]}</td>
        <td>{ranges['Potassium'][0]}-{ranges['Potassium'][1]}</td>
        <td>{ranges['Rainfall'][0]}-{ranges['Rainfall'][1]}</td>
        <td>{ranges['pH_Value'][0]}-{ranges['pH_Value'][1]}</td>
        <td>{ranges['Humidity'][0]}-{ranges['Humidity'][1]}</td>
        <td>{ranges['Temperature'][0]}-{ranges['Temperature'][1]}</td>
    </tr>
    """
    html_rows.append(row)

# Join all rows into a single string
html_table_rows = "\n".join(html_rows)

# Create the full HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Table</title>
    <style>
        header {{
            background-color: rgb(79, 189, 76);
            color: #000000;
            padding: 18px;
            text-align: center;
            font-size: 30px;
            font-style: italic;
        }}
        body {{
            font-family: Arial, sans-serif;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #9a3131;
            text-align: left;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        button {{
            margin-left: 1.9cm;
            background-color: rgb(123, 180, 242);
            color: #000000;
            padding: 10px;
            border: none;
            border-radius: 9px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: rgb(224, 125, 125);
        }}
    </style>
</head>
<body>
<header><b>Standard Crop Data</b></header>
<p>
    According to study and research done by various scientists all over the world, they have given some standard values of required parameters for crop yield.<br>
    Indian Government launched <i>"Farmer.gov.in"</i> website for detailed information of each crop also it provides various services like provision of seeds and an expert opinion.
</p>
<ul style="list-style-type:disc;">
    <li>1 inch rainfall = 25.4 mm</li> <br>
    <li>1% humidity = air is at 1 percent of its water-holding capacity for the present temperature.</li>
</ul>
<table>
    <thead>
        <tr>
            <th>Sr. No</th>
            <th>Crop</th>
            <th>Nitrogen [kg per Hectare]</th>
            <th>Phosphorus [kg per Hectare]</th>
            <th>Potassium [kg per Hectare]</th>
            <th>Rainfall [inches]</th>
            <th>pH</th>
            <th>Humidity [%]</th>
            <th>Temperature [°C]</th>
        </tr>
    </thead>
    <tbody>
        {html_table_rows}
    </tbody>
</table><br>
<a href="{{ url_for('main') }}"><button>BACK</button></a>
<footer>
    <p>&copy; 2023 Agricultural Dashboard Project</p>
</footer>
</body>
</html>
"""

# Save the HTML content to a file
with open("crop_data_table.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully!")