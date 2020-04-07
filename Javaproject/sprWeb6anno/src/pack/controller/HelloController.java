package pack.controller;

import java.util.HashMap;
import java.util.Map;

import javax.print.attribute.HashAttributeSet;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import pack.model.HelloModel;

@Controller
@RequestMapping({"bakemono","abc/world", "h*"}) // GET , POST 모두 허용
public class HelloController {
	@Autowired
	private HelloModel helloModel;
	/* ============== 1번 ===================
	@RequestMapping(method = RequestMethod.GET)
	public ModelAndView abc() {
		String result = helloModel.getGreeting();
		
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("hello");
		modelAndView.addObject("result", result);
		
		return modelAndView;
	}
	*/
	/* ============= 2번 ==============
	@RequestMapping(method = RequestMethod.GET)
	public Map<String, Object> abc() {
		String result = helloModel.getGreeting();
		
		HashMap<String, Object> map = new HashMap();
		map.put("result", result);
		return map;
	}
	*/
	// 위는 ViewFile명이 정해져있고 밑은 정해지지 않음
	// 두번째 요청명은 hello가 아님 (world) 
	// 두번째 메소드는 요청명이 ViewFile이 된다.(HashMap<요청명, 뷰파일> map)
	
	// ================= 3번 ===============
	@RequestMapping(method = RequestMethod.GET)
	public Model abc(Model model) {
		String result = helloModel.getGreeting();
		
		model.addAttribute("result", result);
		return model;
	}
	
	
	
	// =================== 4번 ================
	
	
}
