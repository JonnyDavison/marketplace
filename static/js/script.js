// Variables
// Getting the stars
let one = document.getElementById('first')
let two = document.getElementById('second')
let three = document.getElementById('third')
let four = document.getElementById('fourth')
let five = document.getElementById('fifth')
// Gets the ratings form
let starForm = document.querySelector('.ratings')
// Stars Array
let stars = [one, two, three, four, five]
// Get csrf token
csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)
// Gets confirm box by id
confrim = document.getElementById('confirm')


// Stars array loops as cursour passes over the stars
stars.forEach(item=> item.addEventListener('mouseover', (event)=>{
    starSelect(event.target.id)
}))

// Get numeric value
let getNumericValue = (stringValue) => {
    let numericValue;
    if(stringValue == 'first'){
        numericValue = 1
    } else if (stringValue == 'second') {
        numericValue = 2
    } else if (stringValue == 'third') {
        numericValue = 3
    } else if (stringValue == 'fourth') {
        numericValue = 4
    } else if (stringValue == 'fifth') {
        numericValue = 5
    } else {
        numericValue = 0
    }
    return numericValue
}

stars.forEach(item=> item.addEventListener('click', (event)=>{
    let starValue = event.target.id
    starRating = getNumericValue(starValue)
    console.log(starRating)

    let submitted = false
    starForm.addEventListener('submit', e=>{
        e.preventDefault()
        if (submitted){
            return
        }
        submitted = true
        let starId = e.target.id
    //     console.log(starId)
        $.ajax({
            type: 'POST',
            url: 'market/rate/',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'rate_id': starId,
                'rate_value': starRating
            },
            success: function(response){
                console.log(response)
                confirm.innerHTML = `<h3>Your rating ${response.rating}</h3>`
            },
            error: function(error){
                console.log(error)
                confirm.innerHTML = `<h3>Ohh dear! Try again.</h3>`
            }
        })

    })
}))




// Select stars and add the class 'checked'
let starSelect = (selection) => {
    switch(selection){
        case 'first': {
            addCheckedClass(1)
            return
        }
        case 'second': {
            addCheckedClass(2)
            return
        }
        case 'third': {
            addCheckedClass(3)
            return
        }
        case 'fourth': {
            addCheckedClass(4)
            return
        }
        case 'fifth': {
            addCheckedClass(5)
            return
        }
    }
}

// Adds/removes the checked class from the star button
let addCheckedClass = (size) =>{
    let fromChildren = starForm.children
    for (let i=0; i < fromChildren.length; i++){
        if (i <= size) {
            fromChildren[i].classList.add('checked')
        } else {
            fromChildren[i].classList.remove('checked')
        }
    }
}


