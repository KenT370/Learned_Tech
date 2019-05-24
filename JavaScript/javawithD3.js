

// var text1 = d3.select('.text1').text()
// console.log(text1)

// var text2 = d3.select('.inner').text()
// console.log(text2)

// var text3 = d3.select('#text2').text()
// console.log(text3)

// d3.select('.text1').text('Hey I changed this')

// var link = d3.select('.my-link').html()
// console.log(link)

// var linkanchor = d3.select('.my-link>a')
// console.log(linkanchor)

// var link = linkanchor.attr('href')
// console.log(link)

// linkanchor.attr('href','https://python.org')

// d3.select('.my-link>a').attr('href','https://nytimes.org').text('This will take you to NY Times')

// d3.selectAll("li").style('color','blue')

// var li1 = d3.select('ul').append('li')
// li1.text('New Thing Added')

// Adding Data to a Table using D3
var newGrade = ["Wash", 79];
console.log(`Using D3 to add [${newGrade}] to the Table`)

//Changing the ID for the Last Row in the Table
d3.selectAll('.grade').append('tr').attr('id','new')
//Adding data to the new row
d3.select('#new').append('td').text(newGrade[0])
d3.select('#new').append('td').text(newGrade[1])
// Making the Table Striped
d3.select('.grades').attr('class','table table-striped')
// Looping through the list of grades and adding them to the table
var grades = [["Malcolm", 80], ["Zoe", 85], ["Kaylee", 99], ["Simon", 99], ["Wash", 79]];
grades.forEach((row) => {
    var newrow = d3.selectAll('.grade').append('tr')
    newrow.append('td').text(row[0])
    newrow.append('td').text(row[1])   
})
console.log('-----------------------------')

// Creating a Table from an Array of Array's
var data = [
    {weekday: "SUN", date: "July 1",high: 76,low: 63
    }, {weekday: "MON", date: "July 2",high: 77,low: 63
    }, {weekday: "TUE",date: "July 3",high: 77, low: 63
    }, {weekday: "WED",date: "July 4",high: 81,low: 65
    }, {weekday: "THU",date: "July 5",high: 87,low: 68
    }, {weekday: "FRI",date: "July 6",high: 91,low: 71
    }, {weekday: "SAT",date: "July 7",high: 91,low: 72
    }
  ];

var tbody = d3.select('.weather_data')

data.forEach(value => {
    console.log(value)
    var row = tbody.append('tr')
    Object.entries(value).forEach((key,value) => {
        console.log(key)
        row.append('td').text(key[1]) })
})

d3.select('.weather').attr('class','table table-striped')
console.log('--------------------------------')


// Using D3 to "listen" to events and change the HTML
function reverse(string){
    return string.split('').reverse().join('')
}
function cal_char(string){
    var split = string.toLowerCase().replace(/\s+/g,'').split('')
    count_int = 0
    var count = Object.entries(split).forEach(key => {
        count_int += 1
    })
    return count_int
}
// Selecting the text box
var input= d3.select('#input-field')

// Create an Action when text is entered
input.on('change',function(){
    // Reversing the Input Text
    console.log(input.node().value)
    var reversed = reverse(input.node().value)
    console.log(reversed)
    d3.select('.output').text(reversed)

    // Counting the Letters in the Input Text and Putting them in a list
    console.log(cal_char(input.node().value))
    
    d3.select('#list').append('li').text(`${input.node().value} has ${cal_char(input.node().value)} letters.`)
})
console.log('----------------------------')

// Button Clicks (Upvote & Downvote)


