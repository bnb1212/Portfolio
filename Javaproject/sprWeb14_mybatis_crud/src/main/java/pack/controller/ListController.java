package pack.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ListController {

	@RequestMapping("list")
	public ModelAndView listProcess() {
		return new ModelAndView("list");
	}
}
