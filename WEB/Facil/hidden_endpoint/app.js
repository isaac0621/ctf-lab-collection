const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/api/flag_hidden_92a', (req,res)=>{
  res.send("CTF{hidden_js123}");
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
