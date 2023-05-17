var floor = 3;
var floor_math = 2 * floor + 1;

for (let i = 0; i < floor_math ; i++){
    if (i % 2 === 1){
        console.log(" ".repeat((floor_math - i) / 2) + "*".repeat(i) + " ".repeat((floor_math - i) / 2))
    }
}

