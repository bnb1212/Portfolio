package aa.bb.cc;

import javax.xml.crypto.Data;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@Service
public class LoginController {

	private String formViewName = "loginform";

	@Autowired
	public LoginCommand loginCommand;

	@ModelAttribute("command")
	public LoginCommand formBack() {
		return loginCommand;
	}

	@RequestMapping(value = "login", method = RequestMethod.GET)
	public String form() {
		return formViewName; // view 파일 명 반환

	}
	/*
	 * @RequestMapping(value = "login", method = RequestMethod.POST) public String
	 * submit(LoginCommand loginCommand) { if (loginCommand.getUserid().equals("aa")
	 * && loginCommand.getPasswd().equals("11")) { return "redirect:/list"; // 목록보기
	 * 
	 * } else { return formViewName; // view 파일 명 반환
	 * 
	 * }
	 * 
	 * }
	 */

	@RequestMapping(value = "login", method = RequestMethod.POST)
	public String submit(@Validated @ModelAttribute("command") LoginCommand loginCommand, BindingResult result) {
		if (loginCommand.getUserid().equals("aa") && loginCommand.getPasswd().equals("11")) {
			return "redirect:/list"; // 목록보기

		} else {
			return formViewName; // view 파일 명 반환

		}
	}

	@InitBinder
	public void initBinder(WebDataBinder binder) {
		binder.setValidator(new DataValidator());		
		}
}

