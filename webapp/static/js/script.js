function tabs(evt, tab_name) {
  // Declare all variables
  var i, contents, links;

//   Get all elements with class="links" and remove the class "active"
//  links = document.getElementsByClassName("bottom-nav");
//  for (i = 0; i < links.length; i++) {
//    links[i].className = links[i].className.replace(" nav-active", " ");
//  }

//   Show the current tab, and add an "active" class to the button that opened the tab
//  document.getElementById(tab_name).style.display = "block";
  evt.currentTarget.className += " nav-active";

}


//function keephighlight(event, element_id) {
//
//    var selected_element_id,selected_element_class;
//
//    selected_element_id=document.getElementById(element_id);
//    selected_element_class=document.getElementByClassName(element_class);
//
//}

