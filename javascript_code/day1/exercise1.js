

const generatedFromjs = setInterval(
    function() {
        console.log("Generated from setInterval");
    }, 10_000
);

const jsRules = setTimeout(
    function() {
        console.log("JavaScript Rules");
    }, 4_000
);
