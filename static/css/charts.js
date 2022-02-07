const ctx = document.getElementById('myChart');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['01.02.2022', '02.02.2022', '03.02.2022', '04.02.2022', '05.02.2022'],
        datasets: [{
            label: 'Au',
            data: [95, 110, 170, 145, 134],
            fill: false,
            borderColor: 'rgb(255, 216, 0)',
            tension: 0.1},{
            label: 'Ag',
            data: [56.04, 61.05, 74, 85, 110],
            fill: false,
            borderColor: 'rgb(170, 170, 170)',
            tension: 0.1},{
            label: 'Pt',
            data: [234, 210, 183, 198, 213],
            fill: false,
            borderColor: 'rgb(229, 228, 226)',
            tension: 0.1},{
            label: 'Pd',
            data: [10, 59, 84, 85, 110],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }]
        },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});