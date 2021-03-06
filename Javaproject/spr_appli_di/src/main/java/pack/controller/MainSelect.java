package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainSelect {
	public static void main(String[] args) {
		// spring이 작성한 객체를 읽어서 실행
		ApplicationContext context = new ClassPathXmlApplicationContext("select_init.xml");
		
		SelectService selectService = (SelectService) context.getBean("selectServiceImpl");
		selectService.selectProcess();
	}
}
