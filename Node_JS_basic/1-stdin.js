var standard_input = process.stdin;
standard_input.setEncoding('utf-8');
console.log("Welcome to Holberton School, what is your name?");
standard_input.on('data', function(data) {
    console.log('Your name is: ' + data);
    console.log("This important software is now closing");
    process.exit();
});
