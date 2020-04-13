package aa.bb.cc;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class MemberController {
	
	@RequestMapping(value="member", method = RequestMethod.GET)
	public String form(){
		return "myform";
	}

	@RequestMapping(value="member", method = RequestMethod.POST)
	@ResponseBody
	public String submit(@RequestBody String formData){
		// @RequestBody : HTTP 요청 몸체를 자바 객체로 전달
		// @ResponseBody : 자바 객체를 HTTP 응답 객체로 클라이언트에 전달
		
		System.out.println("formData");
		
		return "return data : " + formData;
	}
	
	
}
