package pack.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import pack.model.JikwonDto;
import pack.model.JikwonInter;

@Controller
public class LoginController {
	@Autowired
	private JikwonInter inter;
	
	@RequestMapping(value = "login", method=RequestMethod.GET)
	public String goLogin() {
		return "login";
		
	}

	@RequestMapping(value = "login", method=RequestMethod.POST)
	public String goSubmit(HttpSession session,
			@RequestParam("no") String no,
			@RequestParam("name") String name) {
		JikwonDto dto = inter.getLoginInfo(no);
		
		if(dto != null) {
			String resultName = dto.getJikwon_name();
			if(resultName.equals(name)) {
				session.setAttribute("name", name);
			}
		}
		return "redirect:/jikwonlist";
		
	}
	
	@RequestMapping(value = "logout", method=RequestMethod.GET)
	public String goLogout(HttpSession session) {
		session.invalidate();
		return "redirect:/index.jsp";
		
	}
}
