package pack.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.model.JikwonDto;
import pack.model.JikwonInter;

@Controller
@ComponentScan("pack.model")
public class ListController {
	
	@Autowired
	@Qualifier("jikwonImpl")
	private JikwonInter jikwonInter;	
	
	@RequestMapping("list") // view 파일명을 따로 지정해주지 않는다면 요청명이 view파일명으로 지정 된다. list라는 요청을 받음
	public Model process(Model model) { 
		List<JikwonDto> list = jikwonInter.selectList(); // selectList를 실행하구 list 반환
		model.addAttribute("datas", list); // 해서 model에 더한후 ("key", value)
		return model; // 반환
	}
}
