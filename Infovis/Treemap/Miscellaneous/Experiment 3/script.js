document.getElementById("fileInput").addEventListener("change", handleFileSelect);
document.getElementById("backButton").addEventListener("click", generateInitialTreemap);

let csvData = [];
let attributes = [];

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
            generateCountryTreemap(clickedAttribute);
        }
    });
}

// Generate treemap for top 15 countries based on the selected attribute
function generateCountryTreemap(attribute) {
    document.getElementById("backButton").style.display = "block"; // Show back button

    const values = csvData.map(row => ({
        country: row['country'], // Replace with your actual column name for country
        value: parseFloat(row[attribute])
    }));

    const topValues = values
        .filter(item => !isNaN(item.value))
        .sort((a, b) => b.value - a.value)
        .slice(0, 15);

    const labels = topValues.map(item => `${item.country} (${item.value})`);
    const counts = topValues.map(item => item.value);

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
        title: `Top 15 Countries for ${attribute}`,
        margin: { t: 50, l: 0, r: 0, b: 0 }
    };

    Plotly.newPlot("treemap", dataTrace, layout);
}
