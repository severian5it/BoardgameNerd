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

    $('#hotCarousel').carousel({
      interval: 5000
    })
    
    $('.carousel .carousel-item').each(function(){
        var minPerSlide = 3;
        var next = $(this).next();
        if (!next.length) {
        next = $(this).siblings(':first');
        }
        next.children(':first-child').clone().appendTo($(this));
        
        for (var i=0;i<minPerSlide;i++) {
            next=next.next();
            if (!next.length) {
              next = $(this).siblings(':first');
            }
            
            next.children(':first-child').clone().appendTo($(this));
          }
    });

});