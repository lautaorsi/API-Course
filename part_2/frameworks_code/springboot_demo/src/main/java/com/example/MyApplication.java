package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

//Anotacion Stereotype, indica queque la clase tiene un rol especifico
//en este caso es un controlador y por lo tanto Spring lo tiene en cuenta al handlear requests
@RestController
@SpringBootApplication
public class MyApplication {

    //Punto de entrada, delega a la clase SpringApplication que inicializa el servidor web  
	public static void main(String[] args) {
		SpringApplication.run(MyApplication.class, args);
	}

}