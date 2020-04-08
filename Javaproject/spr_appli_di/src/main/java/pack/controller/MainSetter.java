package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainSetter {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("setter_init.xml");
		
		SetterProcess process = (SetterProcess) context.getBean("setterProcess");
		process.showData();
		
	}
}