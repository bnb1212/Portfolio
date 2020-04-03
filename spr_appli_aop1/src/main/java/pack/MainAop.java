package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainAop {
	
	public static void main(String[] args) {
		ApplicationContext context = 
				new ClassPathXmlApplicationContext("aop_init.xml");
		
		// AOP 적용 전
		//MessageInter inter = context.getBean("mimpl", MessageInter.class);
		//inter.sayHi();
		
		// AOP 적용 후
		MessageInter inter = context.getBean("proxy", MessageInter.class);
		inter.sayHi();
	}
}
