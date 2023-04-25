0x14. JavaScript - Web scraping

Node.js fs module basics:
The fs module provides an API for interacting with the file system in a Node.js application. It allows you to perform various operations on files, such as reading from or writing to them.
To use the fs module, you first need to import it using the require() function:

const fs = require('fs');

1. fs.readFile(path, options, callback) - reads the contents of a file at the specified path and calls the callback function with any error or the contents of the file as the second argument. The options argument is an object that can specify things like the file encoding or flag options.

2. fs.writeFile(file, data, options, callback) - writes data to the file at the specified file path, overwriting any existing data, and calls the callback function with any error as the first argument.

3. fs.appendFile(file, data, options, callback) - appends data to the file at the specified file path, creating the file if it doesn't exist, and calls the callback function with any error as the first argument

e. fs.mkdir(path, options, callback) - creates a directory at the specified path and calls the callback function with any error as the first argument.

5. fs.readdir(path, options, callback) - reads the contents of a directory at the specified path and calls the callback function with any error or an array of the names of the files and directories in the directory as the second argument.

const fs = require('fs');

// Read a file with default encoding (utf8)
fs.readFile('/path/to/file.txt', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Read a file with specified encoding
fs.readFile('/path/to/file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Read a file with options
fs.readFile('/path/to/file.txt', { encoding: 'utf8', flag: 'r' }, (err, data) => {
  if (err) throw err;
  console.log(data);
});

==========================================================================
Command Line Arguments
==========================================================================

In JavaScript, command line arguments are available through the process.argv array. This array contains the command line arguments passed to the program, with the first two elements being the path to the node executable and the path to the JavaScript file being run.

Here's an example to demonstrate how to access command line arguments using process.argv:

// example.js
console.log(process.argv);

// run the program with arguments
// node example.js arg1 arg2 arg3

When you run node example.js arg1 arg2 arg3 in the terminal, you should see the following output:

[  '/usr/local/bin/node',  '/path/to/example.js',  'arg1',  'arg2',  'arg3']

In the above example, the process.argv array contains five elements, with the first two being the path to the node executable and the path to the example.js file. The remaining three elements are the command line arguments passed to the program.

To access individual command line arguments, you can use array indexing on the process.argv array. For example, process.argv[2] would give you the first command line argument (in this case, 'arg1').

============================================================================Error Handling
============================================================================ In JavaScript, errors can occur due to a variety of reasons, such as syntax errors, runtime errors, or logic errors. Error handling involves detecting and responding to these errors in a way that allows the program to continue running smoothly.
One of the primary ways to handle errors in JavaScript is to use try-catch blocks. A try-catch block is used to wrap a block of code that might throw an error. If an error is thrown within the try block, the catch block is executed, which allows you to handle the error gracefully.

try {
  // code that might throw an error
  const result = someFunction();
} catch (error) {
  // code to handle the error
  console.error('An error occurred:', error);
}

In the above example, the try block contains the code that might throw an error, which is the someFunction() call. If an error is thrown within this block, the catch block is executed, and the error object is passed to it as the error parameter. You can then use this object to handle the error in a way that makes sense for your program.

Another important aspect of error handling in JavaScript is throwing your own errors. You can use the throw statement to create and throw a new error object with a custom message. This can be useful for detecting and responding to errors in your own code.

function divide(a, b) {
  if (b === 0) {
    throw new Error('Division by zero');
  }
  return a / b;
}

try {
  const result = divide(10, 0);
  console.log(result);
} catch (error) {
  console.error('An error occurred:', error);
}

In the above example, the divide() function checks if the second argument is zero and throws a new Error object with a custom message if it is. When the function is called with divide(10, 0), the throw statement is executed, which immediately stops the function execution and throws the error object. The catch block then handles the error and logs it to the console.

============================================================================request module
============================================================================The request module in JavaScript is a popular module used for making HTTP requests in Node.js. It provides an easy-to-use API for making HTTP requests, handling cookies, following redirects, and more.
To use the request module, you first need to install it using npm. You can do this by running the following command in your terminal:

npm install request

Once you have installed the request module, you can use it to make HTTP requests in your code. Here's an example of making a simple HTTP GET request using the request module:

const request = require('request');

request('https://api.example.com/users', (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(body);
});

In the above example, we require the request module using the require function. We then use the request function to make an HTTP GET request to the specified URL. The callback function is called when the response is received, and it takes three arguments: error, response, and body. If there is an error during the request, the error argument will be set to a non-null value. If the request is successful, the body argument will contain the response body.

The request module provides many options that you can use to customize your HTTP requests. Here's an example of making an HTTP POST request with a JSON payload using the request module:

const request = require('request');

const options = {
  url: 'https://api.example.com/users',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'John Doe', email: 'john.doe@example.com' })
};

request(options, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(body);
});

In the above example, we specify the request options in an object and pass them as the first argument to the request function. The options include the URL, the HTTP method (in this case, POST), headers, and body. We also use the JSON.stringify() function to convert the payload to a JSON string.



