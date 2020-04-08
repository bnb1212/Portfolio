package pack4;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main4 {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("aop4_init.xml");
				
		LogicInter logicInter = (LogicInter) context.getBean("logicImpl");
		logicInter.startProcess();
	}
}