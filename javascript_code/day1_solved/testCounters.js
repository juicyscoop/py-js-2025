function countHello(maxCount) {
  if (typeof maxCount !== 'number' || maxCount < 1 || maxCount > 10) {
    throw new Error('countHello: parameter must be an integer between 1 and 10');
  }

  let counter = 0;
  const intervalId = setInterval(() => {
    counter += 1;
    console.log(`Hello (${counter})`);

    if (counter >= maxCount) {
      clearInterval(intervalId);
      console.log('Done!');
    }
  }, 1000); // runs every 1 second; adjust delay as needed
}

// Example usage:
countHello(5);
// → After 1s: "Hello (1)"
// → After 2s: "Hello (2)"
// …
// → After 5s: "Hello (5)"
// → then logs: "Done!" and stops
