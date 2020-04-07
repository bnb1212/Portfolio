package www.pack.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

// 방법 1
/*
@Controller
public class LoginController {
	@RequestMapping(value = "login", method = RequestMethod.GET)
	public ModelAndView submit(HttpServletRequest request) {

		// ==신경쓸 POINT==
		String id = request.getParameter("id"); // request 객체 사용
		String pwd = request.getParameter("pwd"); // request 객체 사용
		// ============

		String data = "";
		if (id.equals("aa") && pwd.equals("11")) {
			data = "로그인 성공";
		} else {
			data = "쥐엔장 로그인 실패";
		}

		ModelAndView view = new ModelAndView();
		view.setViewName("result");
		view.addObject("data", data);
		return view;

	}
	*/

//===방법 2
@Controller("login") // type LEVEL 타입 레벨
public class LoginController {
	@RequestMapping(method = RequestMethod.GET) // METHOD LEVEL 메소드 레벨
	public ModelAndView submit(
		// ==신경쓸 POINT==
			@RequestParam("id") String id,
			@RequestParam(value="pwd") int pwd) {
			
		// ============

		String data = "";
		//if (id.equals("aa") && pwd.equals("11")) {
		if(id.equals("aa") && pwd==11) {
			data = "로그인 성공";
		} else {
			data = "쥐엔장 로그인 실패";
		}

		ModelAndView view = new ModelAndView();
		view.setViewName("result");
		view.addObject("data", data);
		return view;

	}
}
