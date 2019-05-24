// Loan Approval Process
var income = 25000;
var debtIncomeRatio = .5;
var yearsInJob = 3;
var criminalRecord = false;
var creditScore = 780;

console.log('---------------------------')
console.log('Loan Approval Process')
console.log(`Applicant has an Income: ${income}, Debt to Income Ration: ${debtIncomeRatio}.`)
console.log(`On the job: ${yearsInJob} years, and Criminal Record: ${criminalRecord}, Credit Score: ${creditScore}.`)
if (income <= 30000){
    if (debtIncomeRatio >= .5){
        console.log('No Loan')
    }
    else{
        console.log('Loan Approved')
    }

}
else if (income > 30000 && income < 75000){
    if (yearsInJob <= 1 || creditScore <= 600){
        console.log('No Loan')
    }
    else if (yearsInJob > 5 || creditScore >600){
        console.log('Loan Approved')
    }

}
else {
    if (criminalRecord === false){
        console.log('Loan Approved')
    }
    else{
        console.log('No Loan')
    }

}

// Looping through an Array
console.log('-----------------------------------')
console.log('Looping Through an Array of Movie Scores')
var movieScores = [4.4,3.3,5.9,8.8,1.2,5.2,7.4,7.5,7.2,9.7,4.2,6.9];
var sum = 0;
var goodmovies = []
var okmovies = []
var badmovies = []

for (var i = 0; i < movieScores.length; i++){
    sum = sum + movieScores[i]
    if (movieScores[i] >= 7){
        goodmovies.push(movieScores[i])
    }
    else if (movieScores[i] > 5 && movieScores[i] < 7){
        okmovies.push(movieScores[i])
    }
     else {
        badmovies.push(movieScores[i])
    }
}

console.log(`Good: ${goodmovies}`)
console.log(`OK: ${okmovies}`)
console.log(`Bad: ${badmovies}`)
var average = Math.floor(sum / movieScores.length)
console.log(`Avg: ${average}`)

// Simple Function Creation
console.log('---------------------------------------')
console.log('Creating Simple Statistical Functions')
var movieScores = [4.4,3.3,5.9,8.8,1.2,5.2,7.4,7.5,7.2,9.7,4.2,6.9];
var monthlyAvgRainFall = [3.03, 2.48, 3.23, 3.15, 4.13, 3.23]
var mileRunTimes = [5.06, 4.54, 5.56, 4.40, 7.10]

function mean(numbers) {
    var sum = numbers.reduce(function(a,b){return a +b},0)
   var mean = sum/numbers.length
   return mean
}

function variance(numbers) {
    var variance = 0
    var all_nums = 0
    for(var i = 0;i < numbers.length;i++){
        var num = numbers[i]
        all_nums += Math.pow(num - mean(numbers), 2)
    }
    var variance = all_nums/numbers.length
    return variance
}

function standardDev(numbers){
    var stnddev = Math.sqrt(variance(numbers))
    return stnddev
}

console.log('Values for Movie Ratings')
console.log(`The Mean is ${mean(movieScores).toFixed(2)} `)
console.log(`The Variance is ${variance(movieScores).toFixed(2)}`)
console.log(`The Standard Deviation is ${standardDev(movieScores).toFixed(2)}`)
console.log('--------')
console.log('Values for Monthly Average Rainfall')
console.log(`The Mean is ${mean(monthlyAvgRainFall).toFixed(2)} `)
console.log(`The Variance is ${variance(monthlyAvgRainFall).toFixed(2)}`)
console.log(`The Standard Deviation is ${standardDev(monthlyAvgRainFall).toFixed(2)}`)
console.log('---------')
console.log('Values for Mile Run Times')
console.log(`The Mean is ${mean(mileRunTimes).toFixed(2)} `)
console.log(`The Variance is ${variance(mileRunTimes).toFixed(2)}`)
console.log(`The Standard Deviation is ${variance(mileRunTimes).toFixed(2)}`)



