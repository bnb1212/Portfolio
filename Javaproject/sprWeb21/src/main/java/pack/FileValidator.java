package pack;

import org.springframework.stereotype.Service;
import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

@Service
public class FileValidator implements Validator { // 파일 유무 검사용
	
	
	@Override
	public boolean supports(Class<?> clazz) {
		
		return false;
	}

	@Override
	public void validate(Object uploadFile, Errors errors) {
		UploadFile file = (UploadFile)uploadFile;
		
		if(file.getFile().getSize()==0) {
			errors.rejectValue("file", "","업로드할 파일을 선택하세요");
		}

	}
}
