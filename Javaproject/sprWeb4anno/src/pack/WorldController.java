package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class WorldController {
	//@RequestMapping("world.do") // get/post 모두 적용됨
	@RequestMapping(value = "world.do", method = RequestMethod.POST) // 하나만 찝어서
	public ModelAndView aaa() {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("view2");
		mv.addObject("message", "헬로우 어노테이션 - POST");
		
		return mv;
		
	}
	
	@RequestMapping(value = {"world","good","nice*"}, method = RequestMethod.GET) // 하나만 찝어서
	public ModelAndView bbb() {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("view2");
		mv.addObject("message", "헬로우 어노테이션 - GET");
		
		return mv;
		
	}
}
