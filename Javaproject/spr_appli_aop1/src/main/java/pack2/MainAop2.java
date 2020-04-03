package pack2;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainAop2 {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("aop2_init.xml");
		
		LogicInter inter= (LogicInter) context.getBean("logicImpl");
		inter.selectDataProcess();
		inter.updateDataPart();
	}
}
