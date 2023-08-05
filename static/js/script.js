// Variables
// Getting the stars
let one = document.getElementById('first')
let two = document.getElementById('second')
let three = document.getElementById('third')
let four = document.getElementById('fourth')
let five = document.getElementById('fifth')
// Gets the ratings form
let starForm = document.querySelector('.ratings')


// Stars array loops as cursour passes over the stars
let stars = [one, two, three, four, five]
stars.forEach(item=> item.addEventListener('mouseover', (event)=>{
    starSelect(event.target.id)
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


