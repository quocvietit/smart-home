function callNameTable(obj){
     while(obj.tagName.toUpperCase() !== "TABLE") {
        obj = obj.parentNode;
    }
    return obj.id;
}
function sortTableInt(n, idTable) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById(idTable);
  switching = true;

  dir = "desc";

  while (switching) {

    switching = false;
    rows = table.getElementsByTagName("TR");

    for (i = 1; i < (rows.length - 1); i++) {

      shouldSwitch = false;

      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];

      if (dir == "asc") {
        if (parseInt(x.innerHTML) > parseInt(y.innerHTML)) {

          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {

          shouldSwitch= true;
          break;
        }
      }
    }
    if (shouldSwitch) {

      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;

      switchcount ++;      
    } else {

      if (switchcount == 0 && dir == "desc") {
        dir = "asc";
        switching = true;
      }
    }
  }
  var id = document.createElement("script");
  id.src = 'identityTable.js';
  identity();
}

function sortTableString(n, idTable) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById(idTable);
  switching = true;

  dir = "desc";

  while (switching) {

    switching = false;
    rows = table.getElementsByTagName("TR");

    for (i = 1; i < (rows.length - 1); i++) {

      shouldSwitch = false;

      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];

      if (dir == "asc") {
        if (x.innerHTML > y.innerHTML) {

          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML < y.innerHTML) {

          shouldSwitch= true;
          break;
        }
      }
    }
    if (shouldSwitch) {

      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;

      switchcount ++;
    } else {

      if (switchcount == 0 && dir == "desc") {
        dir = "asc";
        switching = true;
      }
    }
  }
  identity();
}
