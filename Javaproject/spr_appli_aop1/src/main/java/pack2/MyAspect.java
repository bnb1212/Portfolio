package pack2;

import org.aspectj.lang.ProceedingJoinPoint;

public class MyAspect {	//핵심 메소드 수행 전후에 관심사항 코드를 기술
	//ProceedingJoinPoint : 지정된 핵심메소드를 호출 가능
	public Object kbs(ProceedingJoinPoint joinPoint) throws Throwable{	
		//지정된 핵심 메소드 이름 얻기
		String methodName = joinPoint.getSignature().toString();
		System.out.println(methodName + " 시작 전 뭔가를 작업(예: login, security, transaction..");
		
		Object object = joinPoint.proceed();	//이 코드에 의해 인터셉트 대상 핵심 메소드가 수행
		
		System.out.println(methodName + " 처리 후 어떤 작업");
		
		return object;	//null을 리턴할 경우 AOP가 수행되지 않는다.
	}

}
