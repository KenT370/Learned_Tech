Plotly.d3.json('/api/pals', function(error,data){
    if (error) return console.warn(error)
    var data = [data]
    console.log('Data',data)
    var layout = {
        title:'Pet Locations',
        font:{
            family:'Droid Serif, serif',
            size:15
            },
        height:700,
        width:1080,
        geo:{
            scope:'usa',
            resolution:50,
            showrivers: true,
            rivercolor: '#fff',
            countrywidth:1,
            showlakes: true,
            lakecolor: '#fff',
            showland: true,
            landcolor: '#EAEAAE',
            countrycolor: '#d3d3d3',
            subunitcolor: '#d3d3d3'
            }
        }
    
    Plotly.newPlot('plot',data,layout)
})

