package aa.bb.cc;

import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

public class DataValidator implements Validator {
	
	
	@Override
	public boolean supports(Class<?> clazz) {
		return LoginCommand.class.isAssignableFrom(clazz);
	}

	@Override
	public void validate(Object target, Errors errors) {
		//target에 대한 검증 지원. 에러 발생 시 Errors에 저장
		LoginCommand command = (LoginCommand)target;
		System.out.println(command.getUserid() + " " + command.getPasswd());
	
		// 자료 검증
		// 방법 1
		if(command.getUserid() == null || command.getUserid().trim().isEmpty()){
			errors.rejectValue("userid", "err.userid");
		}
		
		// 방법 2
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "passwd", "err.passwd");
	}
}
