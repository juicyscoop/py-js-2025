

function countHello(maxCount) {
    if (maxCount < 1 || maxCount > 10) {
        throw new Error("maxCount must be between 1 and 10");
    }

    let counter = 0;
    
    const intervalId = setInterval(() => {
        console.log('Hello');
        counter++;
        // counter = counter + 1;
        if (counter >= maxCount) {
            clearInterval(intervalId);
            console.log('Finished!')
        }
    }, 1000);

}

countHello(5);
console.log(counter)
let a = 5;