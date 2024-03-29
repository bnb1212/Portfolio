package pack.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import pack.model.SangpumInter;

@Controller
public class SearchController {

	@Autowired
	private SangpumInter sangpumInter;
	
	@RequestMapping(value = "search", method = RequestMethod.POST)
	public ModelAndView searchProcess(SangpumBean bean) {
		
		return new ModelAndView("list", "datas",sangpumInter.search(bean));
		
	}
	
}
