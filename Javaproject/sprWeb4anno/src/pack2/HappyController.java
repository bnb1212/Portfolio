package pack2;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
//@RequestMapping("happy")
public class HappyController {
	@RequestMapping(value = "happy", method=RequestMethod.POST) // 클래스 밖에다 써도 잘 작동함
	public ModelAndView happy() {
		ModelAndView modelAndView = new ModelAndView("view2");
		modelAndView.addObject("message", "웃자");
		
		return modelAndView;
	}

}
