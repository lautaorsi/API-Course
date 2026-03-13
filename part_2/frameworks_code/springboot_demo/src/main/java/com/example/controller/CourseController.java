package com.example.controller;

import com.example.repository.CourseRepository;
import com.example.model.Course;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/v1/courses") //Definimos para endpoint de usuarios
public class CourseController {

    @Autowired
    private CourseRepository courseRepository;


    //GET curso individual
    @GetMapping("/{courseId}")
    public Course getCourse(@PathVariable("courseId") Long courseId) {
        return courseRepository.findById(courseId).orElse(null); //Retornamos curso
    }

    //GET todos los cursos
    @GetMapping
    public List<Course> getAllCourses() {
        return courseRepository.findAll(); //Obtiene todos los cursos
    }

    //POST un curso
    @PostMapping
    public Course createCourse(@RequestBody Course course) {
        return courseRepository.save(course); // Guarda un curso
    }

    //PUT un curso
    @PutMapping("/{courseId}")
    public Object updateCourse(@PathVariable("courseId") Long courseId,@RequestBody Course newCourseData){
        //Buscamos curso
        Course course = courseRepository.findById(courseId).orElse(null);
        
        if (course == null) {
            return "NOT FOUND";
        }

        course.setCourseTitle(newCourseData.getCourseTitle());
        course.setCredits(newCourseData.getCredits());
    
        return courseRepository.save(course);
    }

    //DELETE un curso
    @DeleteMapping("/{courseId}")
    public void deleteCourse(@PathVariable("courseId") Long courseId){   //Solo retornamos estado de exito
        courseRepository.deleteById(courseId);  //Borra un curso dado su id
    }   

}