// Using a dropdown menu to showcase different datasets
function init() {
    var data = [{
        values: [19,26,55,88],
        labels: ['Spotify','Soundcloud','Pandora','ITunes'],
        type: 'pie'
    }]
    var layout = {
        height: 600,
        width: 800
    }
    Plotly.plot('one',data,layout)
}

function restyle(values,labels) {
    Plotly.restyle('one','values',[values])
    Plotly.restyle('one','labels',[labels])
}

function getData(dataset){
    var values = []
    var labels = []
    switch(dataset){
        case 'Streaming':
        values = [15,25,34,54]
        labels = ['Netflix','Hulu','Amazon','Cable']
        break
        case 'coding':
        values = [34,53,23,78]
        labels = ['R','Python','Javascript','C++']
        break
        case 'podcast':
        values = [56,34,23,12]
        labels = ['Joe Rogan','Sam Harris','Bill Burr','Joey Diaz']
        break
        default:
        values: [19,26,55,88]
        labels: ['Spotify','Soundcloud','Pandora','ITunes']
    }
    restyle(values,labels)
}

init()

// Grabbing Data from an API and Displaying it with a Range Slider

apiKey = 'nyPY2xrybx65mxXP_xJm'

function unpack(data, index) {
    return data.map(row => row[index]);
    };

function BuildPlot(url) {
    d3.json(url).then(function(data){
        var name = data.dataset.name
        var stock_symbol = data.dataset.dataset_code
        var end_date = data.dataset.end_date
        var start_date = data.dataset.start_date
       
        var trace1 = [{
            x: unpack(data.dataset.data, 0),
            y: unpack(data.dataset.data,1),
            type:'scatter',
            mode:'lines',
            name: name
        }]

        var layout = {
            title: `Stock Price for ${stock_symbol}`,
            xaxis: {
                range:[start_date,end_date],
                type:'date',
                rangeslider:{}
            },
            yaxis: {autorange:true,
            type:'linear'}
        }
        Plotly.newPlot('two',trace1,layout)
    })}

    
function stockpick(stock){
    var stock = stock.toUpperCase()
    url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`
    BuildPlot(url)
        }


function searchKeyPress(e)
        {
            // look for window.event in case event isn't passed in
            e = e || window.event;
            if (e.keyCode == 13)
            {
                document.getElementById('stockbox').click();
                return false;
            }
            return true;
        }


// Creating Same Stock Viewer but with Candle Sticks and Rolling Average
// This Chart is also using event listeners vs in-line HTML
// functions as the previous chart did


apiKey = 'nyPY2xrybx65mxXP_xJm'

function get_data(){
    d3.event.preventDefault()
    var stock = d3.select('#stock2').node().value.toUpperCase()
    console.log(stock)
    url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`
    return plot_chart(url,stock)
}
function rolling_average(arr){
    var averages = [];
    var windowPeriod = 10
  for (var i = 0; i < arr.length - windowPeriod + 1; i++) {
    var sum = 0;
    for (var j = 0; j < windowPeriod; j++) {
      sum += arr[i + j];
    }
    averages.push(sum / windowPeriod);
    } 
     return averages }

function plot_chart(url,stock){

    d3.json(url).then( value => {
        var end_date = value.dataset.end_date
        var start_date = value.dataset.start_date
        var date = value.dataset.data.map(obj => obj[0])
        var open = value.dataset.data.map(obj => obj[1])
        var high = value.dataset.data.map(obj => obj[2])
        var low = value.dataset.data.map(obj => obj[3])
        var close = value.dataset.data.map(obj => obj[4])
        var roll_avg = rolling_average(close)
        
        // Filling the Table With Data
        for (var i = 0;i<date.length;i++){
            row = d3.selectAll('#table').append('tr')
            row.append('td').text(date[i])
            row.append('td').text(open[i])
            row.append('td').text(high[i])
            row.append('td').text(low[i])
            row.append('td').text(close[i])
        }

        var trace3 = {
            name:`Rolling Average for ${stock} Closing Price`,
            x:date,
            y:roll_avg,
            mode:'lines',
            type:'scatter'
        }

        var trace1 = {
            name:`Candlestick for ${stock}`,
            x: date,
            close: close,
            high: high,
            low: low,
            open: open,
            type: 'candlestick'
        }

        var trace2 = {
            type: "scatter",
            mode: "lines",
            name: `Stock Line for ${stock}`,
            x: date,
            y: close,
            line: {
              color: "#F5F5F5"
            }
          };

        var data = [trace1,trace2,trace3]

        var layout = {
            title: `Stock Prices for ${stock}`,
            dragmode: 'zoom',
            xaxis: {
                autorange:true,
                range: [`${start_date}`,`${end_date}`],
                title: 'Date',
                type: 'date',
                rangeslider: {range: [`${start_date}`,`${end_date}`]}
            },
            yaxis: {
                autorange: true,
                type: 'linear',
                title: 'Stock Price'
            }
        }

        Plotly.newPlot('three',data,layout)

    })
}
d3.select("#stockbutton2").on("click", get_data);
