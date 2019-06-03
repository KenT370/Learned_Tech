console.log('connected')

Plotly.d3.json('/data',function(err,data) {
    var data = [data]
    layout = {
        title:'BigFoot Sightings Through the Ages',
        xaxis:{
            type:'date'
        },
        yaxis: {
            autorange:true,
            type:'linear'
        }
    }
    Plotly.newPlot('plot',data,layout)
})