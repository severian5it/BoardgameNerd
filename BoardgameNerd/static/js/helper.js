/**
 * Jquery function to call search with CR on a search field
 */
$(document).ready(function(){


    $('#toSearch').keypress(function(e){
      if(e.keyCode==13)
      $('.searchButton').click();
    });

    $('.searchButton').click(function(){
        this.href='/search/'+document.getElementById('toSearch').value
        $('.searchButton').submit()
    });

});