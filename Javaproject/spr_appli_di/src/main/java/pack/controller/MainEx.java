package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainEx {
	public static void main(String[] args) {
		// spring이 작성한 객체를 읽어서 실행
		ApplicationContext context = new ClassPathXmlApplicationContext("ex_init.xml");

		ExInter inter = (ExInter)context.getBean("exProcess");
		inter.showStudent();
	}
	
}

