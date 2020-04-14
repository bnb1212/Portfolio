package pack.controller;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class LoginController {

	@RequestMapping(value = "login", method = RequestMethod.GET)
	public String login(HttpSession session) {
		if (session.getAttribute("id") == null) {
			return "login";

		} else {
			return "redirect:/index.jsp";
		}
	}

	@RequestMapping(value = "login", method = RequestMethod.POST)
	public String login(HttpSession session, @RequestParam("id") String id, @RequestParam("pwd") String pwd) {
		if (id.equals("aa") && pwd.equals("11")) {
			session.setAttribute("id", id);
			return "redirect:/index.jsp";
		} else {
			return "redirect:/err.jsp";
		}
	}

	@RequestMapping(value = "logout", method = RequestMethod.GET)
		public String logout(HttpSession session) {
			session.invalidate();
			return "redirect:/index.jsp";
		}
}
