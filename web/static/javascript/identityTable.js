function identity() {
  var table, rows, i, x, id = 1;
  table = document.getElementById("rating_table");
  rows = table.getElementsByTagName("TR");

    for (i = 1; i < rows.length; i++) {
      rows[i].getElementsByTagName("TD")[0].innerHTML = id;
      id=id+1
    }
}