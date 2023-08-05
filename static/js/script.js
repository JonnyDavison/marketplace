// Variables

// Getting the stars
let one = document.getElementById('first')
let two = document.getElementById('second')
let three = document.getElementById('third')
let four = document.getElementById('fourth')
let five = document.getElementById('fifth')

let stars = [one, two, three, four, five]

stars.forEach(item=> item.addEventListener('mouseover', (event)=>{
    console.log(event.target)
}))