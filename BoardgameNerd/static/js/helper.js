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
    let $e = $(e.relatedTarget);
    let idx = $e.index();
    let itemsPerSlide = 5;
    let totalItems = $('.item-hot').length;
    console.log(idx, totalItems, totalItems-(itemsPerSlide-1))
  
    if (idx >= totalItems-(itemsPerSlide-1)) {
        let it = itemsPerSlide - (totalItems - idx);
        for (let i=0; i<it; i++) {
            // append slides to end
            console.log('append', i, it)
            if (e.direction=="left") {
                $('.item-hot').eq(i).appendTo('.carousel-inner-hot');
            }
            else {
                $('.item-hot').eq(0).appendTo('.carousel-inner-hot');
            }
        }
    }
  });
  /* duplicating for old carousel must put this into a fuction */
  $('#carousel-example2').on('slide.bs.carousel', function (e) {
    /*
        CC 2.0 License Iatek LLC 2018 - Attribution required
    */
    let $e = $(e.relatedTarget);
    let idx = $e.index();
    let itemsPerSlide = 5;
    let totalItems = $('.item-old').length;
  
    if (idx >= totalItems-(itemsPerSlide-1)) {
        let it = itemsPerSlide - (totalItems - idx);
        for (let i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.item-old').eq(i).appendTo('.carousel-inner-old');
            }
            else {
                $('.item-old').eq(0).appendTo('.carousel-inner-old');
            }
        }
    }
  });

});