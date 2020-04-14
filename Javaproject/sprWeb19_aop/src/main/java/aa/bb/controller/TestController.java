package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.MyModelInter;

@Controller
public class TestController {
	
	@Autowired
	@Qualifier("myModel")
	private MyModelInter myModelInter;
	
	@RequestMapping("test")
	public ModelAndView abc() {
		String result1 = myModelInter.processMsg();
		String result2 = myModelInter.businessMsg();
		
		ModelAndView view = new ModelAndView();
		view.setViewName("list");
		view.addObject("data1", result1);
		view.addObject("data2", result2);
		return view;
	}
}
