document.getElementById('file-input').addEventListener('change', handleFile);
document.getElementById('plot-btn').addEventListener('click', plotPCP);

let csvData = [];
let attributeList = [];

// Country mappings (example mappings)
// const countryMappings = {
//     1: "China",
//     2: "United States",
//     3: "India",
//     4: "Russian Federation",
//     5: "Japan",
//     6: "Germany",
//     7: "Korea, Rep.",
//     8: "Iran, Islamic Rep.",
//     9: "Canada",
//     10: "United Kingdom",
//     11: "Mexico",
//     12: "Saudi Arabia",
//     13: "South Africa",
//     14: "Indonesia",
//     15: "Italy",
//     16: "Brazil",
//     17: "Australia",
//     18: "France",
//     19: "Poland",
//     20: "Turkiye",
//     21: "Spain",
//     22: "Ukraine",
//     23: "Thailand",
//     24: "Kazakhstan",
//     25: "Egypt, Arab Rep.",
//     26: "Malaysia",
//     27: "Netherlands",
//     28: "Argentina",
//     29: "Venezuela, RB",
//     30: "United Arab Emirates",
//     31: "Viet Nam",
//     32: "Pakistan",
//     33: "Uzbekistan",
//     34: "Algeria",
//     35: "Czechia",
//     36: "Iraq",
//     37: "Belgium",
//     38: "Nigeria",
//     39: "Greece",
//     40: "Philippines",
//     41: "Romania",
//     42: "Israel",
//     43: "Austria",
//     44: "Chile",
//     45: "Colombia",
//     46: "Finland",
//     47: "Belarus",
//     48: "Syrian Arab Republic",
//     49: "Qatar",
//     50: "Libya"
// };

// const countryMappings = {
//     1: "China",
//     2: "United States",
//     3: "India",
//     4: "Russian Federation",
//     5: "Japan",
//     6: "Germany",
//     7: "Korea, Rep.",
//     8: "Iran, Islamic Rep.",
//     9: "Canada",
//     10: "United Kingdom"
// };

const countryMappings = {
    11: "Mexico",
    12: "Saudi Arabia",
    13: "South Africa",
    14: "Indonesia",
    15: "Italy",
    16: "Brazil",
    17: "Australia",
    18: "France",
    19: "Poland",
    20: "Turkiye",
    21: "Spain",
    22: "Ukraine",
    23: "Thailand",
    24: "Kazakhstan",
    25: "Egypt, Arab Rep.",
    26: "Malaysia",
    27: "Netherlands",
    28: "Argentina",
    29: "Venezuela, RB",
    30: "United Arab Emirates",
    31: "Viet Nam",
    32: "Pakistan",
    33: "Uzbekistan",
    34: "Algeria",
    35: "Czechia",
    36: "Iraq",
    37: "Belgium",
    38: "Nigeria",
    39: "Greece",
    40: "Philippines",
};


// Column name mappings
const columnNameMappings = {
    CountryIndex: "Country ID",
    population: "Population",
    other_greenhouse_emisions: "Other greenhouse emissions",
    CO2_emisions: "CO2 emissions",
    electric_power_consumption: "Electric power consumption"
};

// Handle file upload
function handleFile(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const text = e.target.result;
            csvData = parseCSV(text);
            populateAttributeCheckboxes(csvData);
        };
        reader.readAsText(file);
    }
}

// Parse CSV into JSON with renamed columns
function parseCSV(text) {
    const rows = text.trim().split('\n');
    const headers = rows[0].split(',');
    
    // Map original headers to new headers based on columnNameMappings
    const renamedHeaders = headers.map(header => columnNameMappings[header.trim()] || header.trim());
    
    const data = rows.slice(1).map(row => {
        const values = row.split(',');
        const obj = {};
        headers.forEach((header, index) => {
            const renamedHeader = columnNameMappings[header.trim()] || header.trim();
            obj[renamedHeader] = parseFloat(values[index]) || values[index];
        });
        return obj;
    });
    
    attributeList = renamedHeaders;
    return data;
}

// Populate attribute checkboxes
function populateAttributeCheckboxes(data) {
    const container = document.getElementById('checkbox-container');
    container.innerHTML = ''; // Clear previous checkboxes

    attributeList.forEach((attribute, index) => {
        const checkboxItem = document.createElement('div');
        checkboxItem.className = 'checkbox-item';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `attr-${index}`;
        checkbox.value = attribute;

        const label = document.createElement('label');
        label.htmlFor = `attr-${index}`;
        label.innerText = attribute;

        checkboxItem.appendChild(checkbox);
        checkboxItem.appendChild(label);
        container.appendChild(checkboxItem);
    });
}

// Plot the PCP
function plotPCP() {
    const selectedAttributes = Array.from(document.querySelectorAll('#checkbox-container input:checked')).map(
        checkbox => checkbox.value
    );

    if (selectedAttributes.length !== 5) {
        alert('Please select exactly 5 attributes.');
        return;
    }

    const dimensions = selectedAttributes.map(attribute => ({
        label: attribute,
        values: csvData.map(row => row[attribute]),
        labelFont: {
            size: 12  // Adjust this value to control axis label font size
        }
    }));

    // Calculate color scale tick values and labels
    const colorValues = csvData.map(row => row[selectedAttributes[0]]);
    const minValue = Math.min(...colorValues);
    const maxValue = Math.max(...colorValues);
    const numTicks = 8;  // Number of ticks you want along the color scale
    
    // Generate tick values and labels
    const tickVals = Array.from({ length: numTicks }, (_, i) => minValue + (i * (maxValue - minValue) / (numTicks - 1)));
    const tickText = tickVals.map(val => val.toFixed(0));  // Format to two decimal places or adjust as needed


    const trace = {
        type: 'parcoords',
        dimensions: dimensions,
        line: {
            color: csvData.map(row => row[selectedAttributes[0]]), // Color by the first attribute for variety
            colorscale: 'Viridis',  // Change color scheme for visual effect
            showscale: true,
            width: 16,
            opacity: 0.6,
            colorbar: {
                title: {
                    text: selectedAttributes[0],// Adjust if you want a title for the color scale
                    font: {
                        size: 10 // Adjust this for a smaller title size
                    }
                },
     
                tickvals: tickVals,            // Set calculated tick values
                ticktext: tickText,            // Set corresponding labels
                tickmode: 'array',              // Use array mode to define specific tick positions
                tickfont: {
                    size: 9  // Adjust this for a smaller label size
                }
            }
        }
    };

    const layout = {
        title: {
            text: 'Global emissions Parallel Coordinate Plot',
            y: 4.0, // Moves the title up; increase this value if more space is needed
            font: {
                size: 16 // Adjust title font size if needed
            }
        },
        height: 480,   // for 10 countries

        // height: 600, // for 50 or more countries
        margin: {
            l: 60,
            r: 60,
            t: 100, // Increase top margin if needed to avoid clipping
            b: 60
        },
        font: {
            size: 15
        }
    };
    

    Plotly.newPlot('plot', [trace], layout);

    // Display country mappings below the plot
    displayCountryMappings();
}

// Display country mappings in two columns
function displayCountryMappings() {
    const mappingContainer = document.getElementById('country-mappings');
    // mappingContainer.innerHTML = '<h4>Country ID Mappings:</h4>';
    mappingContainer.innerHTML = '<div style="font-size: 15px;">Country ID Mappings:</div>';

    
    // Split mappings into two arrays for two columns
    const mappingsArray = Object.entries(countryMappings);
    // const halfwayIndex = Math.ceil(mappingsArray.length / 2);
    // const column1Mappings = mappingsArray.slice(0, halfwayIndex);
    // const column2Mappings = mappingsArray.slice(halfwayIndex);

    const segmentLength = Math.ceil(mappingsArray.length / 3);

    // Create five columns by slicing the mappingsArray
    const column1Mappings = mappingsArray.slice(0, segmentLength);
    const column2Mappings = mappingsArray.slice(segmentLength, segmentLength * 2);
    const column3Mappings = mappingsArray.slice(segmentLength * 2, segmentLength * 3);
    // const column4Mappings = mappingsArray.slice(segmentLength * 3, segmentLength * 4);
    // const column5Mappings = mappingsArray.slice(segmentLength * 4);


    // Create two columns for displaying mappings
    const column1 = document.createElement('div');
    column1.className = 'mapping-column';
    column1Mappings.forEach(([key, value]) => {
        const listItem = document.createElement('div');
        listItem.style.fontSize = '12px';  // Set font size for each item
        listItem.style.marginBottom = '6px';
        listItem.textContent = `${key} - ${value}`;
        column1.appendChild(listItem);
    });

    const column2 = document.createElement('div');
    column2.className = 'mapping-column';
    column2Mappings.forEach(([key, value]) => {
        const listItem = document.createElement('div');
        listItem.style.fontSize = '12px';  // Set font size for each item
        listItem.style.marginBottom = '6px';
        listItem.textContent = `${key} - ${value}`;
        column2.appendChild(listItem);
    });

    const column3 = document.createElement('div');
    column3.className = 'mapping-column';
    column3Mappings.forEach(([key, value]) => {
        const listItem = document.createElement('div');
        listItem.style.fontSize = '12px';  // Set font size for each item
        listItem.style.marginBottom = '6px';
        listItem.textContent = `${key} - ${value}`;
        column3.appendChild(listItem);
    });

    // const column4 = document.createElement('div');
    // column4.className = 'mapping-column';
    // column4Mappings.forEach(([key, value]) => {
    //     const listItem = document.createElement('div');
    //     listItem.style.fontSize = '12px';  // Set font size for each item
    //     listItem.style.marginBottom = '6px';
    //     listItem.textContent = `${key} - ${value}`;
    //     column4.appendChild(listItem);
    // });

    // const column5 = document.createElement('div');
    // column5.className = 'mapping-column';
    // column5Mappings.forEach(([key, value]) => {
    //     const listItem = document.createElement('div');
    //     listItem.style.fontSize = '12px';  // Set font size for each item
    //     listItem.style.marginBottom = '6px';
    //     listItem.textContent = `${key} - ${value}`;
    //     column5.appendChild(listItem);
    // });


    // Add columns to the container
    mappingContainer.appendChild(column1);
    mappingContainer.appendChild(column2);

    
    mappingContainer.appendChild(column3);

    // mappingContainer.appendChild(column4);

    // mappingContainer.appendChild(column5);

}
