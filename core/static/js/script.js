var thCheck = document.getElementById("thCheck");
var rows = document.getElementById("resultTable").rows;
var rowsLenght = document.getElementById("resultTable").rows.length;

document.getElementById("thCheck").onclick = function () {
    for (var i = 1; i < rowsLenght; i++) {
        if (thCheck.checked == true) {
            rows[i].cells[0].querySelector('input').checked = true;
        } else {
            rows[i].cells[0].querySelector('input').checked = false;
        }
    }
};