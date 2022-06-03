function tabs(evt, tab_name) {
  // Declare all variables
  var i, contents, links;

  // Get all elements with class="contents" and hide them
  contents = document.getElementsByClassName("contents");
  for (i = 0; i < contents.length; i++) {
    contents[i].style.display = "none";
  }

  // Get all elements with class="links" and remove the class "active"
  links = document.getElementsByClassName("table-links");
  for (i = 0; i < links.length; i++) {
    links[i].className = links[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tab_name).style.display = "block";
  evt.currentTarget.className += " btn btn-light btn-lg active";

}

document.getElementById("defaultOpen").click();
document.getElementById('percent_change').classList.add('positive')
