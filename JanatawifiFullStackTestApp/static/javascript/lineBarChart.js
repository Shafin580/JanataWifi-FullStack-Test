const ctx = document.getElementById("myChart").getContext("2d");
const mixedChart = new Chart(ctx, {
  data: {
      datasets: [{
          type: 'bar',
          label: 'Bar Dataset',
          data: [10, 20, 30, 40],
          backgroundColor: [
            'rgba(252, 57, 37, 0.69)'
          ],
          order: 2
      }, {
          type: 'line',
          label: 'Line Dataset',
          data: [10, 15, 35, 45],
          backgroundColor: [
            'rgba(0, 70, 192, 0.69)'
          ],
          order: 1
      }],
      labels: ['January', 'February', 'March', 'April']
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});
