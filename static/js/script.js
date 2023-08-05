// Variables

// Getting the stars
let one = document.getElementById('first')
let two = document.getElementById('second')
let three = document.getElementById('third')
let four = document.getElementById('fourth')
let five = document.getElementById('fifth')

// Stars array loops as cursour passes over the stars
let stars = [one, two, three, four, five]
stars.forEach(item=> item.addEventListener('mouseover', (event)=>{
    starSelect(event.target.id)
}))


// Select stars and add the class 'checked'
let starSelect = (selection) => {
    switch(selection){
        case 'first': {
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'second': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'third': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'fourth': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            return
        }
        case 'fifth': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            return
        }
    }
}

let starForm = document.querySelector('.ratings')
let csrf = document.getElementsByName('csrfmiddlewaretoken')


let addCheckedClass = (size) =>{
    let fromChildren = starForm.children
    console.log(fromChildren)
}
addCheckedClass(2)
