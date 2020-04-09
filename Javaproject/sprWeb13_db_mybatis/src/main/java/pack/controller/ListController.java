package pack.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.model.SangpumDto;
import pack.model.SangpumInter;

@Controller
@ComponentScan("pack.model")
public class ListController {
	
	@Autowired
	@Qualifier("sangpumImpl")
	private SangpumInter sangpumInter;	
	
	@RequestMapping("list") // view 파일명을 따로 지정해주지 않는다면 요청명이 view파일명으로 지정 된다.
	public Model process(Model model) {
		List<SangpumDto>list = sangpumInter.selectList();
		model.addAttribute("datas", list);
		
		return model;
	}
}
