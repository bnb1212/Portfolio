package aa.bb.cc;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class Sub1Controller {
	
	@RequestMapping(value= "/sub1", method=RequestMethod.GET)
	public ModelAndView abc() {
		String msg = "스프링 실습방법 점검";
		
		return new ModelAndView("sub_list1", "msg", msg);
		
	}
}
