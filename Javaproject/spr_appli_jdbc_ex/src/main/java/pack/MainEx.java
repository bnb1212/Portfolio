package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainEx {

	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("ex_init.xml");
		
		BusinessInter inter = context.getBean("businessImpl", BusinessInter.class);
		inter.dataList();
	}
}
