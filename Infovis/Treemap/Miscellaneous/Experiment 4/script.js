document.getElementById("fileInput").addEventListener("change", handleFileSelect);
document.getElementById("generateTreemap").addEventListener("click", generateTreemap);

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
            populateAttributeOptions();
        };
        reader.readAsText(file);
    }
}

// Parse CSV text and extract attributes
function parseCSV(text) {
    const rows = text.split("\n").map(row => row.split(","));
    attributes = rows[0];  // Assuming first row has headers
    csvData = rows.slice(1).map(row => {
        const obj = {};
        attributes.forEach((attr, index) => {
            obj[attr] = row[index];
        });
        return obj;
    });
}

// Populate dropdowns with CSV attributes and range options
function populateAttributeOptions() {
    const select = document.getElementById("attributeSelect");
    const rangeSelect = document.getElementById("rangeSelect");

    select.innerHTML = "";
    attributes.forEach(attr => {
        const option = document.createElement("option");
        option.value = attr;
        option.textContent = attr;
        select.appendChild(option);
    });
    select.style.display = "inline-block";
    document.getElementById("generateTreemap").style.display = "inline-block";

    // Add range options
    rangeSelect.innerHTML = "";
    for (let i = 0; i < 100; i += 10) {  // Creating ranges 0-10, 10-20, etc.
        const option = document.createElement("option");
        option.value = `${i}-${i + 10}`;
        option.textContent = `Top ${i + 1} - ${i + 10}`;
        rangeSelect.appendChild(option);
    }
    rangeSelect.style.display = "inline-block";
}

// Generate Treemap based on selected attribute and range
function generateTreemap() {
    const attribute = document.getElementById("attributeSelect").value;
    const range = document.getElementById("rangeSelect").value.split("-").map(Number);
    const start = range[0];
    const end = range[1];

    // Extract individual countries and their values for the selected attribute
    const values = csvData.map(row => ({
        country: row["country"],  // Assuming "country" column holds country names
        value: parseFloat(row[attribute])
    }));

    // Sort by attribute values in descending order, then select the specified range
    const sortedValues = values
        .filter(item => !isNaN(item.value))
        .sort((a, b) => b.value - a.value)
        .slice(start, end);

    const labels = sortedValues.map(item => `${item.country} (${item.value})`);
    const counts = sortedValues.map(item => item.value);

    const data = [{
        type: "treemap",
        labels: labels,
        parents: labels.map(() => ""),
        values: counts,
        textinfo: "label+value",
        hoverinfo: "label+value+percent parent",
        marker: {
            colors: counts,
            colorscale: [
                [0, "rgba(255, 204, 204)"],
                [0.2, "rgba(255, 153, 153)"],
                [0.4, "rgba(255, 102, 102)"],
                [0.6, "rgba(255, 204, 51)"],
                [0.8, "rgba(102, 255, 102)"],
                [1, "rgba(0, 204, 0)"]
            ],
            colorbar: {
                title: "Value",
                thickness: 15,
                tickvals: [Math.min(...counts), Math.max(...counts)],
                ticktext: ["Low", "High"],
            }
        }
    }];

    const layout = {
        title: `Treemap for Top ${start + 1} to ${end} ${attribute} Values`,
        margin: { t: 50, l: 0, r: 0, b: 0 }
    };

    Plotly.newPlot("treemap", data, layout);
}
