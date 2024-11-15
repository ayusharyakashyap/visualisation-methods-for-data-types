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

// Populate dropdown with CSV attributes and layout methods
function populateAttributeOptions() {
    const select = document.getElementById("attributeSelect");
    const layoutSelect = document.getElementById("layoutSelect");

    select.innerHTML = "";
    layoutSelect.innerHTML = "";

    attributes.forEach(attr => {
        const option = document.createElement("option");
        option.value = attr;
        option.textContent = attr;
        select.appendChild(option);
    });

    // Add options for different treemap layouts
    const layouts = ["squarify", "slice", "dice"];
    layouts.forEach(layout => {
        const option = document.createElement("option");
        option.value = layout;
        option.textContent = layout.charAt(0).toUpperCase() + layout.slice(1);
        layoutSelect.appendChild(option);
    });

    select.style.display = "inline-block";
    layoutSelect.style.display = "inline-block";
    document.getElementById("generateTreemap").style.display = "inline-block";
}

// Generate Treemap based on selected attribute and layout method
function generateTreemap() {
    const attribute = document.getElementById("attributeSelect").value;
    const layoutMethod = document.getElementById("layoutSelect").value;

    // Extract individual countries and their values for the selected attribute
    const values = csvData.map(row => ({
        country: row["country"],  // Assuming "country" column holds country names
        value: parseFloat(row[attribute])
    }));

    // Sort by the attribute values in descending order and take the top 10 entries
    const topValues = values
        .filter(item => !isNaN(item.value))
        .sort((a, b) => b.value - a.value)
        .slice(0, 10);

    const labels = topValues.map(item => `${item.country} (${item.value})`);  // Country name with attribute value
    const counts = topValues.map(item => item.value);  // Use individual values for color encoding

    const data = [{
        type: "treemap",
        labels: labels,
        parents: labels.map(() => ""),  // Root node for all
        values: counts,
        textinfo: "label+value",
        hoverinfo: "label+value+percent parent",
        tiling: {
            packing: layoutMethod  // Specify the layout method here
        },
        marker: {
            colors: counts,
            colorscale: [
                [0, "rgba(255, 204, 204)"],  // Light red
                [0.2, "rgba(255, 153, 153)"], // Red
                [0.4, "rgba(255, 102, 102)"], // Darker red
                [0.6, "rgba(255, 204, 51)"],   // Yellow
                [0.8, "rgba(102, 255, 102)"],  // Light green
                [1, "rgba(0, 204, 0)"]         // Dark green
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
        title: `Treemap for ${attribute} (Top 10 countries)`,
        margin: { t: 50, l: 0, r: 0, b: 0 }
    };

    Plotly.newPlot("treemap", data, layout);
}
