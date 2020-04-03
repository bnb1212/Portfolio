package pack3;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Aspect	//원래 이것만 적어도 된다.
@Component	//두개 줘도 상관없다.
public class MyAspect {	//핵심 메소드 수행 전후에 관심사항 코드를 기술
	//ProceedingJoinPoint : 지정된 핵심메소드를 호출 가능
	//public에 pack2패키지의 하위패키지를 모두 포함하고 파라메터가 0개  이상인 모든 메소드 선택
	//@Around("execution(public * pack3..*(..))")
	
	@Around("execution(public void selectDataProcess())")	//메소드 하나만 지정하고 싶을 경우
	public Object kbs(ProceedingJoinPoint joinPoint) throws Throwable{	
		//지정된 핵심 메소드 이름 얻기
		String methodName = joinPoint.getSignature().toString();
		System.out.println(methodName + " 시작 전 뭔가를 작업(예: login, security, transaction..");
		
		Object object = joinPoint.proceed();	//이 코드에 의해 인터셉트 대상 핵심 메소드가 수행
		
		System.out.println(methodName + " 처리 후 어떤 작업");
		System.out.println("-------------------------");
		
		return object;	//null을 리턴할 경우 AOP가 수행되지 않는다.
	}

	//핵심 메소드 실행 전 처리 - Object object = joinPoint.proceed(); 이전에 처리
	@Before("execution(public void updateDataPart())")
	public void mbc(){
		System.out.println("해당 메소드 처리 전 작업합니다");
	}
}
