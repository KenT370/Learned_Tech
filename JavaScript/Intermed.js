// Using forEach to Iterate
console.log('Iterating through an Array via forEach')
movieScores = [3,4,5,6,2]
good = []
bad = []
movieScores.forEach(function(num){
    if (num>5){
        good.push(num)
    }
    else if (num <5){
        bad.push(num)
    }
})

console.log(good)
console.log(bad)
console.log('----------------------')


// Using JavaScript Objects 
console.log('Creating a Word Counter')

function wordCounter(sent){
    var sentence = sent.split(" ")
    var dictionary = {}
    for (var i = 0; i < sentence.length;i ++){
        if (sentence[i] in dictionary){
            dictionary[sentence[i]] += 1
        }
        else{
            dictionary[sentence[i]] = 1
        }
    }
    return dictionary
}
var string = "I yam what I yam and always will be what I yam"
console.log(wordCounter(string))
console.log('-----------------------')


// Map Function
console.log('Using the forEach function')
var princesses = [
    { name: "Rapunzel", age: 18 },
    { name: "Mulan", age: 16 },
    { name: "Anna", age: 18 },
    { name: "Moana", age: 16 }
  ];

princesses.forEach(function(value,index){
    console.log(`${value.name}: ${value.age}`)
})
console.log('Using the map function')
var names = princesses.map(function(row){
    return row.name
})
console.log(names)
console.log('------------------------------')


// Arrow Functions
console.log('Using the Arrow Function')
var mapred = princesses.map((item, index) => `Stage ${index + 1}: ${item.name}, ${item.age}`);
console.log(mapred)
var names = princesses.map(item => item.name)
console.log(names)
var ages = princesses.map(item => item.age)
console.log(ages)
console.log('-------------------------------')


// Object Iteration
console.log('Iterating over an Object')
dishes = []
spices = []
var recipes = [
    { dish: "Fried fish", spice: "Dorrigo" },
    { dish: "Crab Rangoon", spice: "Akudjura" },
    { dish: "Pickled Okra", spice: "Chili pepper" },
    { dish: "Macaroni salad", spice: "Pepper" },
    { dish: "Apple butter", spice: "Avens" },
    { dish: "Pepperoni Pizza", spice: "Asafoetida" },
    { dish: "Hog fry", spice: "Peppermint" },
    { dish: "Corn chowder", spice: "Akudjura" },
    { dish: "Home fries", spice: "Celery leaf" },
    { dish: "Hot chicken", spice: "Boldo" }];

console.log('Created Using forEach and Object.entries')
Object.entries(recipes).forEach(([key,value]) => {
    dishes.push(value.dish)
    spices.push(value.spice)})
console.log(dishes)
console.log(spices)

console.log('Created using Map')
var dishes = recipes.map(value => value.dish)
var spices = recipes.map(value => value.spice)
console.log(dishes)
console.log(spices)
console.log('---------------------')


// Filter Method
console.log('Using the Filter Method')
var roster = [{
      name: "Doug", position: "Quarterback", madeTeam: true
    },
    {
      name: "Antonio", position: "Tight End", madeTeam: true
    },
    {
      name: "Nick", position: "Kicker", madeTeam: false
    },
    {
      name: "Ereck", position: "Offensive Live", madeTeam: false
    },
    {
      name: "AJ", position: "Line Backer", madeTeam: true
    }];

function madeTeam(person) {
    return person.madeTeam === true
}
function notmade(person){
    return person.madeTeam === false
}
var madeTheTeam = roster.filter(madeTeam)
var notmadeteam = roster.filter(notmade)

console.log(`${madeTheTeam.length} Players made the Team!`)
console.log(`${notmadeteam.length} Players did NOT make the Team!`)