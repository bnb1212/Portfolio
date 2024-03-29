package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MessageMain {
	public static void main(String[] args) {

		// Spring 비사용
		Message1 message1 = new Message1();

		MessageInter inter;
		inter = message1;
		inter.sayHello("홍길동");

		System.out.println("===========");
		
		// Spring을 사용한 경우
		ApplicationContext context = new ClassPathXmlApplicationContext("init.xml");
		MessageInter inter2 = (MessageInter) context.getBean("mes");
		inter2.sayHello("한국인");
	}
}
