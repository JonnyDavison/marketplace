// Variables
// Getting the stars
let five = document.getElementById('rate10')
let four_half = document.getElementById('rate9')
let four = document.getElementById('rate8')
let three_half = document.getElementById('rate7')
let three = document.getElementById('rate6')
let two_half = document.getElementById('rate5')
let two = document.getElementById('rate4')
let one_half = document.getElementById('rate3')
let one = document.getElementById('rate2')
let half = document.getElementById('rate1')

// Stars Array
let stars = [five, four_half, four, three_half, three, two_half, two, one_half, one, half]

// Get numeric value
let getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue == 'rate10'){
        numericValue = 5
    } else if (stringValue == 'rate9') {
        numericValue = 4.5
    } else if (stringValue == 'rate8') {
        numericValue = 4
    } else if (stringValue == 'rate7') {
        numericValue = 3.5
    } else if (stringValue == 'rate6') {
        numericValue = 3
    } else if (stringValue == 'rate5') {
        numericValue = 2.5
    } else if (stringValue == 'rate4') {
        numericValue = 2
    } else if (stringValue == 'rate3') {
        numericValue = 1.5
    } else if (stringValue == 'rate2') {
        numericValue = 1
    } else if (stringValue == 'rate1') {
        numericValue = 0.5
    } else {
        numericValue = 0
    }
    rates = document.getElementById('rated');
    rates.innerHTML = numericValue;
    return numericValue
}

stars.forEach(item=> item.addEventListener('click', (event)=>{
    let starValue = event.target.id
    starRating = getNumericValue(starValue)
    console.log(starRating)
}))
