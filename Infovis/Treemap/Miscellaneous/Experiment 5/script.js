document.getElementById("fileInput").addEventListener("change", handleFileSelect);
document.getElementById("backButton").addEventListener("click", generateInitialTreemap);

let csvData = [];
let attributes = [];
let selectedAttribute = "";

// Function to read and parse CSV file
function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const text = e.target.result;
            parseCSV(text);
            generateInitialTreemap();
        };
        reader.readAsText(file);
    }
}

// Parse CSV text and extract attributes
function parseCSV(text) {
    const rows = text.split("\n").map(row => row.split(","));
    attributes = rows[0]; // Assuming the first row has headers
    csvData = rows.slice(1).map(row => {
        const obj = {};
        attributes.forEach((attr, index) => {
            obj[attr] = row[index];
        });
        return obj;
    });
}

// Generate initial treemap with column names
function generateInitialTreemap() {
    document.getElementById("backButton").style.display = "none"; // Hide back button

    const labels = attributes;
    const dataTrace = [{
        type: "treemap",
        labels: labels,
        parents: labels.map(() => ""),
        textinfo: "label",
        hoverinfo: "label",
        marker: {
            colorscale: "Viridis"
        }
    }];

    const layout = {
        title: "Treemap of Attributes",
        margin: { t: 50, l: 0, r: 0, b: 0 }
    };

    Plotly.newPlot("treemap", dataTrace, layout);

    document.getElementById("treemap").on('plotly_click', function(data) {
        const clickedAttribute = data.points[0].label;
        if (attributes.includes(clickedAttribute)) {
            selectedAttribute = clickedAttribute;
            generateRangeTreemap(clickedAttribute);
        }
    });
}

// Generate range treemap (1-10, 10-20, etc.) for the selected attribute, limited to top 250 countries
function generateRangeTreemap(attribute) {
    document.getElementById("backButton").style.display = "block"; // Show back button

    const values = csvData.map(row => ({
        country: row['country'], // Replace with your actual column name for country
        value: parseFloat(row[attribute])
    }));

    // Sort in descending order, take the top 250, and divide into ranges of 10
    const sortedValues = values
        .filter(item => !isNaN(item.value))
        .sort((a, b) => b.value - a.value)
        .slice(0, 250);

    const rangeLabels = [];
    const rangeStartIndices = [];
    for (let i = 0; i < sortedValues.length; i += 10) {
        const rangeStart = i + 1;
        const rangeEnd = Math.min(i + 10, sortedValues.length);
        rangeLabels.push(`${rangeStart}-${rangeEnd}`);
        rangeStartIndices.push(i);
    }

    const dataTrace = [{
        type: "treemap",
        labels: rangeLabels,
        parents: rangeLabels.map(() => ""),
        textinfo: "label",
        hoverinfo: "label",
        marker: {
            colorscale: "Cividis"
        }
    }];

    const layout = {
        title: `Select Range for ${attribute}`,
        margin: { t: 50, l: 0, r: 0, b: 0 }
    };

    Plotly.newPlot("treemap", dataTrace, layout);

    document.getElementById("treemap").on('plotly_click', function(data) {
        const clickedRange = data.points[0].label;
        const rangeIndex = rangeLabels.indexOf(clickedRange);
        if (rangeIndex !== -1) {
            const start = rangeStartIndices[rangeIndex];
            const end = Math.min(start + 10, sortedValues.length);
            generateCountryTreemap(attribute, sortedValues.slice(start, end));
        }
    });
}

// Generate treemap for specific countries within a selected range
function generateCountryTreemap(attribute, countryData) {
    document.getElementById("backButton").style.display = "block"; // Show back button

    const labels = countryData.map(item => `${item.country} (${item.value})`);
    const counts = countryData.map(item => item.value);

    const dataTrace = [{
        type: "treemap",
        labels: labels,
        parents: labels.map(() => ""),
        values: counts,
        textinfo: "label+value",
        hoverinfo: "label+value+percent parent",
        marker: {
            colors: counts,
            colorscale: "Blues"
        }
    }];

    const layout = {
        title: `Top Countries for ${attribute} (Selected Range)`,
        margin: { t: 50, l: 0, r: 0, b: 0 }
    };

    Plotly.newPlot("treemap", dataTrace, layout);
}
