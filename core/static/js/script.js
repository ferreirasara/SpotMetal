var thCheck = document.getElementById("thCheck");
var rows = document.getElementById("resultTable").rows;
document.getElementById("").onclick = function () {
    if (thCheck.checked) {
        alert(rows[0].cells[0].childNodes.checked);
        rows[0].cells[0].checked = true;
    } else {
        rows[0].cells[0].checked = false;
    }
};