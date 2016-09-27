$(function() {

    $.ajax({
        url: 'api/stats/applications/',
        success: function (response) {
            var labels = response.map(function(obj) {return obj.day});
            var data = response.map(function(obj) {return obj.applications});
            var applicationsChart = new Chart($('#applicationsChart'), {
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
                            tension: .2,
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

    $.ajax({
        url: 'api/stats/applications/pie/',
        success: function (response) {
            var finished = response.progress.finished;
            var total = response.progress.total;
            var statusChart = new Chart($('#applicationsStatus'),{
                type: 'pie',
                data: {
                    labels: ['Finished', 'Lost'],
                    datasets: [
                        {
                            data: [
                                Math.round(response.progress.finished_proportion, 2),
                                100 - Math.round(response.progress.finished_proportion)
                            ],
                            backgroundColor: [
                                '#141414',
                                '#fb1855',
                            ]
                        }   
                    ]
                },
            });
        }
    });

});