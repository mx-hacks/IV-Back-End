$(function() {

    $.ajax({
        url: $('#reviews-url').text(),
        success: function (response) {
            console.log(response);
            var container = $('#hacker-data');

            container.find('.first-name').text(response.first_name);
            container.find('.last-name').text(response.last_name);

            if (response.male)
                container.find('.gender').text('Male');
            else
                container.find('.gender').text('Female');

            container.find('.age').text(response.age);

            container.find('.school').text(response.school.name);
            container.find('.campus').text(response.campus.name);
            container.find('.major').text(response.major);

            container.find('.country').text(response.country);
            container.find('.state').text(response.state);

            container.find('.f_t_h').text(response.first_time_hacker);  
            container.find('.f_t_e').text(response.first_time_event);
            container.find('.c_working').text(response.currently_working);

            container.show();

            $.ajax({
                url: 'http://api.giphy.com/v1/gifs/random',
                data: {
                    api_key: 'dc6zaTOxFJmzC',
                    tag: 'meme'
                },
                success: function (response) {
                    var avatar = $('#hacker-avatar');
                    avatar.attr('src', response.data.image_original_url);
                }
            });
        }
    });

});