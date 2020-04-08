package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import aa.bb.model.MemberDao;

@Controller
public class InsertController {
	@Autowired
	private MemberDao memberDao;
	
	@ModelAttribute("command")
	public MemberBean formBack() {
		return new MemberBean();
		
	}
	
	private String forName = "insform";
	
	@RequestMapping(value = "insert", method = RequestMethod.GET)
	public String form() {
		return forName;
	}
	
	@RequestMapping(value = "insert", method = RequestMethod.POST)
	public String form(MemberBean bean) {
		memberDao.insData(bean);
		return "redirect:/list";
	}
	
}
