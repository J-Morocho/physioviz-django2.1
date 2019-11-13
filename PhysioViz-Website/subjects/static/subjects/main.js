
var temp = document.getElementById('temp').innerText;
var temperature_array = JSON.parse(temp);
var eda = document.getElementById('eda').innerText;
var eda_array = JSON.parse(eda);
var hr = document.getElementById('hr').innerText;
var hr_array = JSON.parse(hr);

console.log(temperature_array)
console.log(eda_array)
console.log(hr_array)

//document.getElementById('temp').innerText = "";
//document.getElementById('eda').innerText = "";

// Adding data points into the chart

function addData(chart, label, data){
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
        
    });
    chart.update();
}


//iterating temperature data
var i = 0;
var func = setInterval(function(){
        i++;
        document.getElementById('temp').innerText = temperature_array[i];
        if(i === temperature_array.length - 1) {
            clearInterval(func);
        };
}, 20)


//iterating eda data
var j = 0;
var func2 = setInterval( function(){
    j++;
    document.getElementById('eda').innerText = eda_array[j];
    if (j === eda_array.length - 1){
        clearInterval(func2)
    };
}, 20)


// iterating hr data
var k = 0;
var func3 = setInterval( function(){
    k++;
    document.getElementById('hr').innerText = hr_array[k];
    if (k === hr_array.length - 1){
        clearInterval(func3)
    };

    addData(myChart, k, hr_array[k]);

}, 20)
//This gives us a bar chart.

var ctx = document.getElementById('my-chart');

var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            data: [],
            backgroundColor: ['rgba(255,255,255)'],
            fill: false,
            spanGaps: true,
            borderColor: 'rgba(255,255,255)',
            pointRadius: 1,
            borderWidth: 1,
        }]
    },



    options: {
        scales: {
            yAxes: [{
                ticks: {
                    fontColor: 'rgba(255,255,255)',
                    beginAtZero: false
                }
            }]
        },

        maintainAspectRatio: true,
    }
    
});

