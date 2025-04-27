const express = require('express')
const app = express()
const port = 3000
 
let todo_list_item =  []
app.set("view engine", "ejs")
app.get("/", (req, res) => {
  res.render("index.ejs")
})
app.get("/2", (req, res) => {
  res.render("2.ejs")
})


// simpel api for todo 
app.get("/all", (req, res) => {
    res.send('todo!')
  })
  app.post("/:id", (req, res) => {
    todo_list_item.push("test") 
})
  app.delete("/", (req, res) => {
    todo_list_item.delete("test") 
})

app.listen(port, () => {
  console.log("TODO app listening on port ${port}")
  console.log("http://127.0.0.1:3000/")
})
