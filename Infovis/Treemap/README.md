# TreeViz - Interactive Treemap Visualization

TreeViz is a web-based application for visualizing CSV data in the form of treemaps. This tool allows users to upload a CSV file, choose an attribute, and view the data interactively by exploring it across different levels and ranges.

## Table of Contents
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Instructions for Use](#instructions-for-use)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)

## Features
- **CSV File Upload:** Import any CSV file and visualize its data.
- **Interactive Attribute Selection:** Select any attribute from the uploaded file to explore the data.
- **Data Range Selection:** View data within specified ranges for easier analysis of top entries.
- **Treemap for Selected Ranges and Countries:** Drill down from attribute ranges to country-specific treemaps.

## Folder Structure
- `index.html`: The main HTML file defining the application's layout and structure.
- `style.css`: Stylesheet file that customizes the look and feel of the application.
- `script.js`: JavaScript file that manages CSV parsing, attribute selection, and treemap visualization.
- `processed.csv`: A pre-processed CSV file that contains a single row per country, with attribute values averaged across the years 1960 to 2022. This allows for a simplified, high-level view of each country’s data. The date column has been removed since it's not relevant to this averaged data.
- `README.md`: This README file, which includes documentation and usage instructions.

## Instructions for Use
1. **Open `index.html`** in a web browser (Chrome, Firefox, or other modern browsers are recommended).
   
2. **Upload a CSV File:**
   - Click on the "Select CSV File" button to upload your CSV file.
   - The CSV should contain a `country` column to ensure proper data visualization across countries.

3. **Choose an Attribute:**
   - The treemap will initially display the list of attributes (columns) in your CSV file.
   - Click on an attribute to analyze it within ranges.

4. **Explore Data by Range:**
   - After selecting an attribute, choose a range to view specific data segments.
   - The treemap will display data for the selected range, showing the top entries within that range.

5. **Country-Level Visualization:**
   - Click on any range to drill down further into the top 10 countries or entries within that segment.
   - Each country or entry is displayed with a color-coded legend indicating the attribute value.

6. **Back Navigation:**
   - Use the "Back" button to navigate to previous views, allowing for easy exploration.

## How It Works

### `index.html`
- Defines the layout of the page, with sections for file upload, back navigation, and treemap visualization.
- Includes Plotly.js via CDN for rendering interactive treemaps.

### `style.css`
- Provides a visually engaging dark theme for the application.
- Styles the container, buttons, and treemap area for a consistent look.

### `script.js`
- **File Upload & Parsing:** Listens for file upload, reads the CSV, and parses it into JavaScript objects.
- **Attribute and Range Selection:** Allows users to choose an attribute from the parsed CSV data and view it within ranges.
- **Treemap Generation:** Uses Plotly.js to create treemaps at each level, including attribute, range, and country-specific views.
- **Color Coding:** Applies a color scale to visually indicate high and low values for each attribute.

### `processed.csv`
- This file provides simplified data for visualization, containing only one row per country. Each row represents the average values of all attributes for that country over the years from 1960 to 2022, making the dataset easier to interpret in a single view. The date column has been excluded as it is not applicable to this averaged dataset.

## Dependencies
TreeViz requires Plotly.js to generate treemaps. If you’re using the provided `index.html` file, the Plotly library is already included via CDN.

### How to Get Plotly.js
- **CDN Option (Recommended)**: Plotly.js is loaded directly from a CDN in `index.html`. No additional steps are needed if you’re connected to the internet.
- **Offline Option**: 
   1. Download Plotly.js from the [official Plotly GitHub repository](https://github.com/plotly/plotly.js).
   2. Link the downloaded file in `index.html`:
      ```html
      <script src="path/to/plotly-latest.min.js"></script>
      ```

For styling and layout, make sure to keep `style.css` and `script.js` in the same directory as `index.html` for a smooth setup.

## Customization
- **Color Scheme:** To adjust colors, modify the color scales in `script.js` under `marker.colorscale`.
- **Range Segmentation:** The default segmentation is set in ranges of 10; this can be modified in the `generateRangeTreemap` function in `script.js`.
- **Plot Layout:** Customize layout settings, including margin and title font, within the layout objects in `script.js`.

## Troubleshooting
- **CSV Format:** Ensure your CSV file is well-formatted and contains a `country` column.
- **File Not Loading:** Check if the file format is correct (only `.csv` files are supported).
- **Plotly Issues:** If treemaps don't render, ensure that you have a stable internet connection for loading Plotly from the CDN.
