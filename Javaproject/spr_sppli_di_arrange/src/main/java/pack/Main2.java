package pack;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main2 {
	public static void main(String[] args) {
		// @Configuratin을 적용한 환경파일 읽기
		AnnotationConfigApplicationContext context =
			 new AnnotationConfigApplicationContext(Config.class);
		
		MessageInter inter = context.getBean("messageImpl", MessageInter.class);
		inter.sayHi();
		
	}
	
}
