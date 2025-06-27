// 1) Function Declaration

// Call it BEFORE its definition
hello(); // ✅ Logs "Hello"
// Observation: this works because function declarations are hoisted.
// The entire function definition is moved to the top by the JS engine.

function hello() {
  console.log("Hello");
}

// Call it AFTER its definition
hello(); // ✅ Logs "Hello"
// Observation: of course this also works—normal function call.

// ----------------------------------------------------------

// 2) Function Expression

// Call it BEFORE its definition
try {
  hi(); // ❌ ReferenceError or TypeError
} catch (e) {
  console.log("Error calling hi() before definition:", e.message);
  // Observation: hi is in the temporal-dead-zone (if let/const) or undefined (if var),
  // so you cannot invoke it before its assignment.
}

const hi = function() {
  console.log("Hi");
};

// Call it AFTER its definition
hi(); // ✅ Logs "Hi"
// Observation: works because now hi refers to the function expression.

