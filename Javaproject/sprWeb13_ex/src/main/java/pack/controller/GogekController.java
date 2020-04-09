package pack.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import pack.model.GogekDto;
import pack.model.GogekInter;


@Controller
@ComponentScan("pack.model")
public class GogekController {

	@Autowired
	@Qualifier("gogekImpl")
	private GogekInter gogekInter;

	@RequestMapping("gogeklist")
	public ModelAndView gogekProcess(@RequestParam("no") String no) {
		List<GogekDto> list = gogekInter.selectGogek(no);

		return new ModelAndView("gogeklist", "gogeks", list);

		/*
		 * List<JikwonDto>list = jikwonInter.selectList(); model.addAttribute("datas",
		 * list); return model;
		 */
	}
}