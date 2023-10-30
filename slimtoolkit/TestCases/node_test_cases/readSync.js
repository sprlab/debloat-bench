
// Include fs module
const fs = require('fs');

// Calling the readFileSync() method
const data = fs.readFileSync('./correct.js',
			{encoding:'utf8', flag:'r'});

console.log(data);
