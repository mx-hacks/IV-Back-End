$(function() {

    $.ajax({
        url: 'api/stats/applications/',
        success: function (response) {
            labels = response.map(function(obj) {return obj.day});
            data = response.map(function(obj) {return obj.applications});
            var scatterChart = new Chart($('#applicationsChart'), {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Applications',
                        data: data
                    }]
                },
                options: {
                    defaultFontFamily: 'Open Sans',
                    legend: {
                        display: false
                    },
                    elements: {
                        line: {
                            tension: .8,
                            backgroundColor: 'rgba(39, 39, 39, .5)',
                            borderWidth: 1,
                            borderColor: 'rgba(236, 25, 91, 1)',
                        },
                        point: {
                            radius: 1
                        }
                    },
                    scales: {
                        xAxes: [{
                            display: false,
                            gridLines: {
                                display: false
                            }
                        }],
                        yAxes: [{
                            gridLines: {
                                display: false
                            }
                        }]
                    }
                }
            });
        }
    });

});