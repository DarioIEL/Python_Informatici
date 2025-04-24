// Questo è un commento in JS

/**
* Anche questo è un commento in JS, solo che questo è un commento multiriga
*/

// Dichiaro una variabile utilizzando la parola chiave let

let mioNome = "Dario"; //String
let mioCognome = "Mennillo"; //String
let miaEta = 36; //Number 

//Chiedo di che tipo sono le mie variabili

console.log(typeof mioNome);
console.log(typeof miaEta);


//Per poter vedere lo script e la relativa console devo usare il browser
console.log("Ciao " + mioNome + " " + mioCognome); 

//dimostro come Javascript sia un linguaggio DEBOLMENTE TIPIZZATO

let numero1 = "10"; 
let numero2 = 8.5;

// let somma = numero1 + numero2; //erroneamente verrebbe 108.5
//posso, anche in questo caso, fare il cast del dato forzando la variabile numero1 da stringa a number
let somma = Number(numero1) + numero2;

//Tutte le altre sono operazioni tipo matematico quindi non fa altro che svolgerle come sempre
let diff = numero1 - numero2; 
let prod = numero1 * numero2;
let quoz = numero1 / numero2;

console.log(somma);
console.log(diff);
console.log(prod);
console.log(quoz);

//COSTRUTTI - PARADIGMI FONDAMENTALI della PROGRAMMAZIONE
if(miaEta >= 18){
    //body dell'IF
    console.log("Benvenuto");
}else{
    console.log("Mi spiace, non puoi accedere");
}


for(let i = 0; i < 10; i++){
    console.log("Ciao " + i);
}
