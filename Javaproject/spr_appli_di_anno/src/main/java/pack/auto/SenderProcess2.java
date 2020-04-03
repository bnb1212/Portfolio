package pack.auto;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

@Service
@Scope("singleton")
@ComponentScan("pack.auto2")
public class SenderProcess2 {
	//클래스의 부모 클래스를 setter injection
	// @Autowired
	// private SenderInter inter; // type에 의한 매핑이기때문에 SenderInter를 implement하는 클래스가 두개 있어서
							   // 에러가 남
	
	@Autowired 			//위의 문제로 Qualifier와 함께 쓰는 경우가 많다
	@Qualifier("s2")
	private SenderInter inter;
	
	public void dispData() {
		inter.show();
	}
}
