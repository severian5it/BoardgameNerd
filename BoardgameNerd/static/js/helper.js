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

    
/*
   code for carousel from here:  https://azmind.com/bootstrap-carousel-multiple-items 

*/
$('#carousel-example').on('slide.bs.carousel', function (e) {
  /*
      CC 2.0 License Iatek LLC 2018 - Attribution required
  */
  var $e = $(e.relatedTarget);
  var idx = $e.index();
  var itemsPerSlide = 5;
  var totalItems = $('.carousel-item').length;

  if (idx >= totalItems-(itemsPerSlide-1)) {
      var it = itemsPerSlide - (totalItems - idx);
      for (var i=0; i<it; i++) {
          // append slides to end
          if (e.direction=="left") {
              $('.carousel-item').eq(i).appendTo('.carousel-inner');
          }
          else {
              $('.carousel-item').eq(0).appendTo('.carousel-inner');
          }
      }
  }
});

});