package pack;

import java.util.Scanner;

import org.aopalliance.intercept.Joinpoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class LoginAspect {
	@Autowired
	private JikwonInter jikwoninter;
	
	@Around("execution(public void dataList())")
	public Object trace(ProceedingJoinPoint joinPoint) throws Throwable{
		System.out.println("AOP로 로긴");
		System.out.println("사번 : ");
		Scanner scanner = new Scanner(System.in);
		String no = scanner.nextLine();
		System.out.println("이름 : ");
		String name = scanner.nextLine();
		for(JikwonDto s:jikwoninter.selectList()) {
			if(no.equals(s.getJikwon_no()) && name.equals(s.getJikwon_name())) {
				System.out.println("로그인 성공");
				Object object = joinPoint.proceed();
				return object;
			}
		}
		
		System.out.println("로그인 실패");
		return null;
	
	}
}
