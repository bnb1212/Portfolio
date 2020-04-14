package aa.bb.model;


import org.springframework.stereotype.Repository;

@Repository
//@Component
public class MyModel implements MyModelInter{
	@Override
	public String processMsg() {
		System.out.println("processMsg 핵심메소드 수행");
		return "Spring AOP 만세";
	}

	@Override
	public String businessMsg() {
		System.out.println("businessMsg 핵심 메소드 처리");
		return "Spring AOP 나이수으";
	}
	
}
