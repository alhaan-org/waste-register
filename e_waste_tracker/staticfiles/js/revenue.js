document.addEventListener("DOMContentLoaded", function () {
  // Line Chart
  const ctxLine = document.getElementById("revenueLineChart").getContext("2d");
  new Chart(ctxLine, {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
      datasets: [
        {
          label: "Revenue (Rs)",
          data: [12000, 19000, 15000, 22000, 28000, 32000],
          borderColor: "#28a745",
          fill: false,
          tension: 0.3,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: { legend: { display: true } },
      scales: {
        y: { beginAtZero: true },
      },
    },
  });

  // Donut Chart
  const ctxDonut = document.getElementById("profitDonutChart").getContext("2d");
  new Chart(ctxDonut, {
    type: "doughnut",
    data: {
      labels: ["Profit", "Loss"],
      datasets: [
        {
          data: [70, 30],
          backgroundColor: ["#28a745", "#dc3545"],
        },
      ],
    },
    options: {
      plugins: {
        legend: { position: "bottom" },
      },
    },
  });
});
