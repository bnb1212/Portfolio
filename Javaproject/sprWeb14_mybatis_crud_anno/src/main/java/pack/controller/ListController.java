package pack.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.model.MemDaoInter;

@Controller
public class ListController {

	@Autowired
	@Qualifier("memDaoImple")
	private MemDaoInter daoInter;
	
	@RequestMapping("list")
	public ModelAndView listProcess() {
		return new ModelAndView("list", "list", daoInter.getDataAll());
	}
}
