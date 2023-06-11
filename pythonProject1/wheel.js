const spinWheel = document.getElementById("spinWheel");
const spinBtn = document.getElementById("spin_btn");
/* --------------- Minimum And Maximum Angle For A value  --------------------- */
const spinValues = [
  { minDegree: 0, maxDegree: 90, value: 100 }, //1
  { minDegree: 271, maxDegree: 360, value: 400 }, //2
  { minDegree: 181, maxDegree: 270, value: 700 }, //4
  { minDegree: 91, maxDegree: 180, value: 1000 },  //3
];
/* --------------- Size Of Each Piece  --------------------- */
const size = [30, 30, 30, 30];
/* --------------- Background Colors  --------------------- */
var spinColors = [
  "#a19c8c",
  "#53534a",
  "#a19c8c",
  "#53534a",
];

let spinChart = new Chart(spinWheel, {
  plugins: [ChartDataLabels],
  type: "pie",
  data: {
    labels: ['Communism', 'Medival Ages', ' Industrial Lodz', 'II World War'],
    datasets: [
      {
        backgroundColor: spinColors,
        data: size,
      },
    ],
  },
  options: {
    responsive: true,
    animation: { duration: 0 },
    plugins: {
      tooltip: false,
      legend: {
        display: false,
      },
      datalabels: {
        rotation: 90,
        color: "#ffffff",
        formatter: (_, context) => context.chart.data.labels[context.dataIndex],
        font: {
    size: 20,
    family: "Arial",
    weight: "bold"
  },
      },
    },
  },
});
/* --------------- Display Value Based On The Angle --------------------- */
const generateValue = (angleValue) => {
  for (let i of spinValues) {
    if (angleValue >= i.minDegree && angleValue <= i.maxDegree) {
      spinBtn.disabled = false;
      break;
    }
  }
};




/* --------------- Spinning Code --------------------- */
let count = 0;
let resultValue = 101;
spinBtn.addEventListener("click", () => {
  spinBtn.disabled = true;
  let randomDegree = Math.floor(Math.random() * (355 - 0 + 1) + 0);
  let rotationInterval = window.setInterval(() => {
    spinChart.options.rotation = spinChart.options.rotation + resultValue;
    spinChart.update();
    if (spinChart.options.rotation >= 360) {
      count += 1;
      resultValue -= 5;
      spinChart.options.rotation = 0;
    } else if (count > 15 && spinChart.options.rotation == randomDegree) {
      generateValue(randomDegree);
      clearInterval(rotationInterval);
      count = 0;
      resultValue = 101;

      // Redirect to specific page based on the drawn labels
      const labels = ['Medival Ages', 'Industrial Lodz', 'II World War', 'Communism'];
      const redirectUrls = ['medival.html', 'industrial.html', 'worldwar.html', 'communism.html'];
      const degreesPerSection = 90;
      const drawnDegree = 360 - spinChart.options.rotation;

      const index = Math.floor(drawnDegree / degreesPerSection);
      if (index >= 0 && index < labels.length) {
        setTimeout(() => {
          window.location.href = redirectUrls[index];
        }, 3000);
      }
    }
  }, 10);
});