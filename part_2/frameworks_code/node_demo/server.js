import sqlite3 from "sqlite3"
import express from "express"
import {open} from 'sqlite'

//SETUP del servidor
const app = express()
const PORT = process.env.PORT || 3000 
app.use(express.json())

const db_path = process.env.DB_PATH || '../db.sqlite3';

//Abrimos database
const db = await open({
  filename: db_path,
  driver: sqlite3.Database
});



//GET para todos los cursos
app.get('/items', async (req,res) => {
    res.json(await db.all('SELECT * FROM courses;'))
})


//GET para cursos especificos
app.get('/items/:id', async (req,res) => {
    const id = parseInt(req.params.id, 10)
    
    const item =  await db.get(`SELECT * FROM courses WHERE course_id = ${id};`)

    if (!item) return res.status(404).json({error: 'Item was not found'})
    
    res.json(item)
})

//POST nuevos cursos
app.post('/items', async (req,res) => {
    const {course_title, credits} = req.body

    //Hacemos un simple chequeo para asegurarnos que tenga ambos campos (esto no contempla "", pero para este proyecto no es necesario)
    if(!course_title || !credits){
        return res.status(500).json({error: "Missing content"})
    }
    const status = await db.run(`INSERT INTO courses (course_title, credits) VALUES (?,?)`, [course_title,credits])

    res.json(status.lastID)
})

//DELETE para cursos (se puede hacer inyección para borrar todo, pero este proyecto no contempla seguridad)
app.delete('/items/:id', async (req,res) =>{
    const id = parseInt(req.params.id, 10);
    
    let status;
    
    try{
        status = await db.run(`DELETE FROM courses WHERE course_id = ?`, [id]);
    }catch (err) {
        res.status(500).json({ error: "Database error", details: err.message });
    }
    
    if(status.changes == 0){res.status(404).json({error: "Course not found"})}

    res.json(status)
})


app.patch('/items/:id', async (req,res) => {
    const id = parseInt(req.params.id, 10)
    
    const {course_title, credits} = req.body

    let status;

    try{
        status = await db.run(`UPDATE courses SET course_title = ?, credits = ? WHERE course_id = ?`, [course_title, credits, id]);
    }catch (err) {
        return res.status(500).json({ error: "Database error", details: err.message });
    }
    
    if(status.changes == 0){res.status(404).json({error: "Course not found"})}

    res.status(200).json({"message":"Course updated successfully"})

})


app.listen(PORT, () => {
    console.log(`Server running http://localhost:${PORT}`)
})