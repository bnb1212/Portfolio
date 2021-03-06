package pack.auto;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {

	public static void main(String[] args) {
		String[] metas = new String[] {"anno2.xml"};
		
		
		ApplicationContext context = new ClassPathXmlApplicationContext(metas[0]);

		SenderProcess process = context.getBean("senderProcess", SenderProcess.class);
		process.dispData();
		// process.getSender().show();
		
		System.out.println();
		SenderProcess2 process2 = context.getBean("senderProcess2", SenderProcess2.class);
		process2.dispData();
	}
}
