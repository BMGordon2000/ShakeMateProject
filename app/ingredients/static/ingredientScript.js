var selectedItems = []

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    if (!selectedItems.includes(data)){
        selectedItems.push(data);
    }
    console.log(selectedItems)
}

function getShakes(){
    console.log(selectedItems);

    let ingredients = selectedItems;
    fetch("http://127.0.0.1:5000/ingredients/getshakes", {
        // Adding method type
        method: "POST",

        // Adding body or contents to send
        body: JSON.stringify({
        items: ingredients
        }),

        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    // Converting to JSON
    .then(response => response.json())

    // Displaying results to console
    .then(json => document.getElementById("PossibleShakes").innerHTML = JSON.stringify(json.value));
    //.then(json => setTable(JSON.stringify(json.value)))
    let url = '/recipes/filteredRecipes'
    for (let i = 0; i < selectedItems.length; i++) {
        if (url.indexOf('?') === -1) {
            url = `${url}?array[]=${selectedItems[i]}`
        } else {
            url = `${url}&array[]=${selectedItems[i]}`
        }
    }
    window.location.href = url
}