#!/usr/bin/node
//  script that writes a string to a file
// syntax: fs.writeFile(file, data, options, callback)

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (error) => {
    if (error) console.log(error);
});
