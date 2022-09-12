const PromptSync = require("prompt-sync");

console.log("First javascript code ");
let a=900
let b=33
console.log(a+b);

const prompt=require("prompt-sync")({sigint:true});
let V1=parseInt(prompt('Enter fruit name'))
let V2=parseInt(prompt('cost per kg'))
let V3=parseInt(prompt('Quantity'))
console.log('you selected ' + V1 + ' having a cost of ' + V2 + ' per kg' );