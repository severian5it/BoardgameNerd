    /** 
     *  code for carousel adapted from this link here:  https://azmind.com/bootstrap-carousel-multiple-items 
     *  check number of items and connect the next one
     * @param {object} carousel on which implement the method 
     * @param {string} string to compose the item to attach when sliding
     */
    function slideCustom(carousel, suffix) {

        let $e = $(carousel.relatedTarget);
        let idx = $e.index();
        let itemsPerSlide = 5;
        let totalItems = $('.item-'.concat(suffix)).length;

        if (idx >= totalItems - (itemsPerSlide - 1)) {
            let it = itemsPerSlide - (totalItems - idx);
            for (let i = 0; i < it; i++) {
                if (carousel.direction == "left") {
                    $('.item-'.concat(suffix)).eq(i).appendTo('.carousel-inner-'.concat(suffix));
                } else {
                    $('.item-'.concat(suffix)).eq(0).appendTo('.carousel-inner-'.concat(suffix));
                }
            }
        }
    };

    function passFormId(id) {
        $('#form-delete').val(id);
    }

    $(document).ready(function () {

        $("#warningToast").toast('show');

        $(window).on("load", function () {
            $(".spinner").hide();
        });


        $('#carousel-hot').on('slide.bs.carousel', function (e) {
            slideCustom(e, 'hot')
        });

        $('#carousel-old').on('slide.bs.carousel', function (e) {
            slideCustom(e, 'old')
        });

        $('#confirm-deletion').click(function () {
            let id = $('#form-delete').val()
            $('#delete-collectionform' + id).submit();
        });

        $('.card-header').hover(
            function () {
                $(this).addClass('hover')
            },
            function () {
                $(this).removeClass('hover')
            }
        )

        let className = 'text-truncate';

        $('.card-header h5').on('mouseenter', function (e) {
            $(this).removeClass(className);
        }).on('mouseleave', function (e) {
            $(this).addClass(className);
        });

    });