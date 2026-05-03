const express = require('express');
const app = express();

app.get('/admin', (req,res)=>{
  const role = req.headers.cookie?.includes("role=admin");
  if(role) return res.send("CTF{cookie_pwned}");
  res.send("nope");
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
