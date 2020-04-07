package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HelloController {
	@RequestMapping("hello.do") // get/post 모두 적용됨
	public ModelAndView abc() {
		
		ModelAndView mv = new ModelAndView();
		mv.setViewName("view1");
		mv.addObject("message", "헬로우 어노테이션");
		
		return mv;
		
	}
}
