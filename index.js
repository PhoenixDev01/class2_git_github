function greet(name) {
    return `Hello, ${name}!`;
}

function calculateArea(radius) {
    return Math.PI * radius ** 2;
}

const userName = "World";
const circleRadius = 5;
console.log(`${greet(userName)} Circle area: ${calculateArea(circleRadius)}`);
