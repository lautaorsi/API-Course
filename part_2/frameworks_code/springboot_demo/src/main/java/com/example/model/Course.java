package com.example.model;

import jakarta.persistence.*;

@Entity
@Table(name = "courses") //Nombre de la tabla en archivo .sqlite

public class Course {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "course_id")
    private Long courseId;

    @Column(name = "course_title")    
    private String courseTitle;

    private Double credits;

    public Course() {}

    // Getters and Setters
    public Long getCourseId() { return courseId; }
    public void setCourseId(Long courseId) { this.courseId = courseId; }
    public String getCourseTitle() { return courseTitle; }
    public void setCourseTitle(String courseTitle) { this.courseTitle = courseTitle; }
    public Double getCredits() { return credits; }
    public void setCredits(Double credits) { this.credits = credits; }
}