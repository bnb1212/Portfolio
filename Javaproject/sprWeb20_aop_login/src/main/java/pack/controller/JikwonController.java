package pack.controller;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.model.JikwonDto;
import pack.model.JikwonInter;

@Controller
public class JikwonController {
	@Autowired
	@Qualifier("jikwonImpl")
	private JikwonInter jikwonInter;
	
	
	@RequestMapping("jikwonlist")
	public ModelAndView abc(HttpServletRequest request, HttpServletResponse response) {
	// AOP 할때는 매개변수 HttpServletRequest, HttpServletResponse를 명시적으로 적어주어야한다.
		
		ModelAndView view = new ModelAndView();
		List<JikwonDto> list = jikwonInter.jikwonList();
		view.setViewName("list");
		view.addObject("list", list);
		
		return view;
		
	}
	
}
