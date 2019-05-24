// 'let' Keyword

// Using 'var' - will throw an undefined
function logger(){
    console.log(x)
    var x = 'hi'
}
logger()

// Using 'let'  - Will throw an error
function logger2() {
    console.log(y)
    let y = 'hello'
}
//logger2()

// Const will refuse attempts to edit
const myPets = ['dog','cat','rabbit','sea turtle']
//myPets = 'ferret' - throws an error
// but still allow manipulation
console.log('before',myPets)
myPets.pop() //removes last element
console.log('after:',myPets)
console.log('----------------------')

// Basic Plot
var trace1 = {
    x: ["beer", "wine", "martini", "margarita",
      "ice tea", "rum & coke", "mai tai", "gin & tonic"],
    y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
    type: "bar"
  };

var data = [trace1]

var layout = {
      title: "'Bar' Chart",
      xaxis: {title: 'Drinks'},
      yaxis: {title: '% of Drinks Ordered'}
  }

Plotly.newPlot('plot',data,layout)

var eyeColor = ["Brown", "Brown", "Brown", "Brown", "Brown",
  "Brown", "Brown", "Brown", "Green", "Green",
  "Green", "Green", "Green", "Blue", "Blue",
  "Blue", "Blue", "Blue", "Blue"];
var num_eye = [26.8, 27.9, 23.7, 25, 26.3, 24.8,
  25.7, 24.5, 26.4, 24.2, 28, 26.9,
  29.1, 25.7, 27.2, 29.9, 28.5, 29.4, 28.3];

var trace1 = {
    x: eyeColor,
    y: num_eye,
    boxpoints:'all',
    type: 'box'
}

var data = [trace1]
var layout = {
    title: 'Frequency of People By Eye Color',
    xaxis: {title:'Eye Color'},
    yaxis: {title:'# of People'}
}
Plotly.newPlot('bar-plot',data,layout)

// Plotting Multiple Traces

var Greek = {
    x:gods_data.map(row => row.pair),
    y:gods_data.map(row => row.greekSearchResults),
    name: 'Greek',
    text:gods_data.map(row => row.greekName),
    type: 'bar'
}
var Rome = {
    x:gods_data.map(row=>row.pair),
    y:gods_data.map(row => row.romanSearchResults),
    text: gods_data.map(row=>row.romanName),
    name: 'Roman',
    type:'bar'
}

var data = [Greek, Rome]

var layout = {
    title:'Greek vs Roman Gods Search Results',
    barmode: 'group'
}

Plotly.newPlot('anotherone',data,layout)

// Sorting and Slicing

var sorted = gods_data.sort(function compareFunction(a,b){
    const vala = a.greekSearchResults
    const valb = b.greekSearchResults
    let comparison = 0
    if (vala > valb){
        comparison = -1
    }
    else if (vala < valb){
        comparison = 1
    }
    return comparison
})

var top10 = sorted.slice(0,10).reverse()

var trace = [{
    x:top10.map(row => row.greekSearchResults),
    y:top10.map(row => row.greekName),
    type:'bar',
    orientation: 'h'
}]

var layout = {
    title:'Top 10 Search Greek Gods',
    xaxis:{title:'# of Search Results'},
    yaxis:{title:'Greek Gods'}
}

Plotly.newPlot('two',trace,layout)

// Scatter Plots

var long_jump = {
    x:olympic_data.year,
    y:olympic_data.long_jump,
    type:'scatter',
    mode:'markers',
    name:'Long Jump',
    marker:{
        color:'#f3cec9',
        symbol:'hexagram'
    }
}
var high_jump = {
    x:olympic_data.year,
    y:olympic_data.high_jump,
    name:'High Jump',
    type:'line'
}
var discus_throw = {
    x:olympic_data.year,
    name:'Discus Throw',
    y:olympic_data.discus_throw,
    type:'line'
}
data = [long_jump,high_jump,discus_throw]
layout = {
    colorway:['#f3cec9', '#e7a4b6', '#cd7eaf'],
    xaxis: {title:'Temperature'},
    yaxis: {title:'Event Record'},
    title: 'Event Records vs Temperatures'
}
Plotly.newPlot('three',data,layout)