package aa.bb.advice;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class MyAspectClass {

	@Autowired
	private SecurityClass class1;
	
	@Around("execution(public String procesMsg()) or execution(public String businessMsg()) ")
	public Object aopProcess(ProceedingJoinPoint joinPoint) throws Throwable{
		class1.mySecurity();
		
		
		//===========================================
		Object object = joinPoint.proceed(); // 조인포인트 실행 지점. 여기를 기준으로 위는 핵심메소드 수행전
											// 이 밑으로는 핵심 메소드 수행 후
		// ==========================================
		
		
		
		return object;
	}
}
