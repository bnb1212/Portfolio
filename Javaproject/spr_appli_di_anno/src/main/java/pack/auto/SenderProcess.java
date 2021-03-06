package pack.auto;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

//@Component("senderProcess") //아래와 뜻은 같다
//@Component
@Service// 비즈니스 로직이 실행되고 있는 클래스에서는 서비스 어노테이션을 넣어준다 가독성을 위해. @Component와 객체를 만든다는 역할은 비슷하다.
@Scope("singleton")
@ComponentScan("pack.auto")
public class SenderProcess {
	//@Autowired(required = true)
	@Autowired // 내부적으로 setter 메소드를 만들어서 운영. type에 의한 매핑(mapping)
	private Sender sender;
	
	/*
	public void setSender(Sender sender) {
		this.sender = sender;
		
	}
	*/
	
	public Sender getSender() {
		return sender;
	}
	public void dispData() {
		sender.show();
	}
}
