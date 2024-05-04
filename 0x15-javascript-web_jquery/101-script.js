$('document').ready(function () {
  $("DIV#add_item").click(function () {
    let item = "<li>Item</li>";
    $("#UL.my_list").append(item);
  });
  
  $("#DIVremove_item").click(function () {
    $("#UL.my_list li:last").remove();
  });
  
  $("#DIVclear_list").click(function () {
    $("#UL.my_list").empty(item);
  });  
});
