var selectedItem =[]

function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {

    selected=document.getElementById("selected")
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    if (!selectedItem.includes(data)){
        selectedItem.push(data);
    }

    console.log(selectedItem)

    selected.innerHTML += document.getElementById(data).outerHTML;
}