package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.context.support.GenericApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Main {
	public static void main(String[] args) {
		//ApplicationContext context = new ClassPathXmlApplicationContext("classpath:arrange.xml");
		//ApplicationContext context = new ClassPathXmlApplicationContext("classpath:pack/arrange.xml");
		
		
		GenericApplicationContext context = new GenericXmlApplicationContext("classpath:pack/arrange.xml");
		
		// 싱글톤이다! 임을 보여주겠따
		/*
		MessageImpl impl1 = (MessageImpl) context.getBean("messageImpl");
		impl1.sayHi();
		MessageImpl impl2 = (MessageImpl) context.getBean("messageImpl");
		impl2.sayHi();
		System.out.println("주소1 : " + impl1);
		System.out.println("주소2 : " + impl2.toString());
		*/
		
		// 다형성
		// MessageInter inter = (MessageImpl)context.getBean("messageImpl"); (1)
		//MessageInter inter = (MessageInter) context.getBean("messageImpl"); (1) 보다 나음
		MessageInter inter = context.getBean("messageImpl", MessageInter.class); // 이렇게 해두 된다.
		inter.sayHi();
	}
}
