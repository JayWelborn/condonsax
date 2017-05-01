$(document).ready(function(){
    
    // expand card on button clock
    $('.button').click(function(){
        // find related write-up sibling
        var parent = $(this).parent();
        var write_up = parent.find('.write-up');

        // add 'visible' class to write-up
        write_up.toggleClass( 'visible' );

        console.log(write_up.height());

        // change button text from read more to read less
        $( this ).text(function(i, text){
            return text === "Read More" ? "Read Less" : "Read More";
        })
    });
});