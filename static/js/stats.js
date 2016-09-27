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
            var statusChart = new Chart($('#applicationsStatus'), {
                type: 'pie',
                data: {
                    labels: ['Finished', 'Lost'],
                    datasets: [
                        {
                            data: [
                                Math.round(response.progress.finished_proportion),
                                100 - Math.round(response.progress.finished_proportion)
                            ],
                            backgroundColor: [
                                '#141414',
                                '#fb1855'
                            ]
                        }   
                    ]
                }
            });
            var stepsChart = new Chart($('#stepsStatus'), {
                type: 'pie',
                data: {
                    labels: ['1st', '2nd', '3rd', '4th'],
                    datasets: [
                        {
                            data: [
                                Math.round(response.steps['1_proportion']),
                                Math.round(response.steps['2_proportion']),
                                Math.round(response.steps['3_proportion']),
                                Math.round(response.steps['4_proportion'])
                            ],
                            backgroundColor: [
                                '#141414',
                                '#fb1855',
                                '#4af16d',
                                '#01ffd5'
                            ]
                        }   
                    ]
                },
            });
        }
    });

    $.ajax({
        url: 'api/stats/education/',
        success: function (response) {
            var schools = response;
            var container = $('#schools');
            var template = $('.school-template');
            schools.forEach(function (school) {
                school_element = template.clone();
                school_element.show();
                school_element.removeClass('school-template');
                school_element.find('.school-name').text('#' + school.id + ' - ' + school.name);
                school_element.find('.school-applications').text(school.totals.total);
                school_element.find('.school-finished').text(school.totals.finished);
                school_element.find('.school-accepted').text(school.totals.accepted);

                school_pie_id = 'school-pie-' + school.id;
                school_pie = school_element.find('.school-pie-canvas');
                school_pie.attr('id', school_pie_id);

                container.append(school_element);

                var schoolPieChart = new Chart($('#' + school_pie_id), {
                    type: 'pie',
                    data: {
                        labels: ['Finished', 'Lost',],
                        datasets: [
                            {
                                data: [
                                    school.totals.finished,
                                    school.totals.total - school.totals.finished
                                ],
                                backgroundColor: [
                                    '#141414',
                                    '#fb1855'
                                ]
                            }   
                        ]
                    },
                });

                school_campus = school.campus;
                campus_template = $('.school-table-row-template');
                campus_container = school_element.find('tbody');

                campus_bars_id = 'school-bars-' + school.id;
                school_campus_bars = school_element.find('.school-campus-bars');
                school_campus_bars.attr('id', campus_bars_id);

                var campus_labels = [];
                var campus_applications = {
                    data: [],
                    label: 'Applications',
                    backgroundColor: '#141414',
                };
                var campus_finished = {
                    data: [],
                    label: 'Finished',
                    backgroundColor: '#fb1855',
                };
                var campus_accepted = {
                    data: [],
                    label: 'Accepted',
                    backgroundColor: '#4af16d',
                };
                var campus_lost = {
                    data: [],
                    label: 'Lost',
                    backgroundColor: '#01ffd5',
                };

                school_campus.forEach(function (campus) {
                    campus_element = campus_template.clone();
                    campus_element.show();
                    campus_element.removeClass('school-table-row-template');

                    campus_element.find('.campus-id').text(campus.id);

                    campus_element.find('.campus-name').text(campus.name);
                    campus_labels.push(campus.name);

                    campus_element.find('.campus-applications').text(campus.totals.total);
                    campus_applications.data.push(campus.totals.total);

                    campus_element.find('.campus-finished').text(campus.totals.finished);
                    campus_finished.data.push(campus.totals.finished);
                    
                    campus_element.find('.campus-accepted').text(campus.totals.accepted);
                    campus_accepted.data.push(campus.totals.accepted);

                    campus_element.find('.campus-lost').text(campus.totals.total - campus.totals.finished);
                    campus_lost.data.push(campus.totals.total - campus.totals.finished);

                    campus_container.append(campus_element);
                });

                var campusBarChart = new Chart($('#' + campus_bars_id), {
                    type: 'bar',
                    data: {
                        labels: campus_labels,
                        datasets: [
                            campus_applications,
                            campus_finished,
                            campus_accepted,
                            campus_lost
                        ]
                    }
                });

            });
        }
    });

});