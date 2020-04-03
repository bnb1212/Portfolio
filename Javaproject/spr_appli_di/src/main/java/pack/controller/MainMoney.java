package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainMoney {
	public static void main(String[] args) {
		// spring이 작성한 객체를 읽어서 실행
		ApplicationContext context = new ClassPathXmlApplicationContext("money_init.xml");

		MyInter inter = (MyInter) context.getBean("myProcess");
		inter.inputMoney();
		inter.showResult();
	}
}
