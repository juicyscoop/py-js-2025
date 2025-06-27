// testTimers.js

// 1. setInterval: runs repeatedly every 10 seconds
const intervalId = setInterval(() => {
  console.log("Generated from setInterval");
}, 10_000); // 10 000 ms = 10 s

// 2. setTimeout: runs once after 4 seconds
const timeoutId = setTimeout(() => {
  console.log("JavaScript Rules");
}, 4_000); // 4 000 ms = 4 s

// (Optional) If you want to stop the interval at some point, e.g. after 35s:
setTimeout(() => {
  clearInterval(intervalId);
  console.log("Interval cleared");
}, 35_000);
