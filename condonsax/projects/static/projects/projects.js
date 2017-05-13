function projectParallax(){
    var scrolled = $(window).scrollTop();
    console.log(scrolled)
    $('#header-image').css('top', (0+(scrolled * 0.5)) + 'px');
    $('#header-image').css('opacity', 1-(scrolled / 400));
}

$(document).ready(function(){
    $(window).scroll(function(){
        projectParallax();
    });
})