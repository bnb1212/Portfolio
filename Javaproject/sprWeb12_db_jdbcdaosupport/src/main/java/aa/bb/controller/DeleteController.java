package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.MemberDao;

@Controller
public class DeleteController {
	
	@Autowired
	public MemberDao memberDao;
	
	@RequestMapping(value="delete", method=RequestMethod.GET)
	public String submit(String id) {
		memberDao.delData(id);	
		return "redirect:/list";
	}
	
	/*
	@RequestMapping(value="delete", method =RequestMethod.POST)
		public String submit(String id) {
		memberDao.delData(id);	
		return "redirect:/list";
	}
	*/
}
