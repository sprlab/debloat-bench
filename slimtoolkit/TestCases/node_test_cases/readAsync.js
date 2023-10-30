const fs = require('fs');

fs.readFile('./correct.js',
		{encoding:'utf8', flag:'r'},
		function(err, data) {
	if(err)
		console.log(err);
	else
		console.log(data);
});

console.log("I'm called Synchronously")
