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
    return selectedItems
}

function getShakes(){
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

// function getShakes() {
//     const request = new XMLHttpRequest()
//     request.open('POST', `/filter/${(selectedItems)}`)
//     request.onload = () => {
//         const flaskMessage = request.responseText
//         console.log(flaskMessage)
//     }
//     request.send()
// }