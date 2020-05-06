function slideCustom(carousel, suffix) {
    /** 
     *  code for carousel adapted from this link here:  https://azmind.com/bootstrap-carousel-multiple-items 
     *  check number of items and connect the next one
     * @param {carousel} carousel on which implement the method 
     * @param {string} string to compose the item to attach when sliding
     */
    let $e = $(carousel.relatedTarget);
    let idx = $e.index();
    let itemsPerSlide = 5;
    let totalItems = $('.item-'.concat(suffix)).length;

    if (idx >= totalItems - (itemsPerSlide - 1)) {
        let it = itemsPerSlide - (totalItems - idx);
        for (let i = 0; i < it; i++) {
            // append slides to end
            if (carousel.direction == "left") {
                $('.item-'.concat(suffix)).eq(i).appendTo('.carousel-inner-'.concat(suffix));
            } else {
                $('.item-'.concat(suffix)).eq(0).appendTo('.carousel-inner-'.concat(suffix));
            }
        }
    }
};

$(document).ready(function () {

    $("#warningToast").toast('show');



    $('#toSearch').keypress(function (e) {
        /**
         * Jquery function to call search with CR on a search field
         */
        if (e.keyCode == 13)
            $('.searchButton').click();
    });

    $('.searchButton').click(function () {
        /**
         * submitting search query
         */
        this.href = '/search/' + document.getElementById('toSearch').value
        $('.searchButton').submit()
    });

    $('#carousel-hot').on('slide.bs.carousel', function (e) {
        
        slideCustom(e, 'hot')
    });

    $('#carousel-old').on('slide.bs.carousel', function (e) {
        slideCustom(e, 'old')
    });

});
