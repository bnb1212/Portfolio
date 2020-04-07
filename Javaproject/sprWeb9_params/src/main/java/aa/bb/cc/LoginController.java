package aa.bb.cc;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class LoginController {
	@RequestMapping(value = "kbs/login", params = "type=admin")
	public ModelAndView aaa() {
		ModelAndView view = new ModelAndView("show");
		view.addObject("message", "관리자입니다.");
		return view;
	}

	@RequestMapping(value = "kbs/login", params = "type=user")
	public ModelAndView bbb() {
		ModelAndView view = new ModelAndView("show");
		view.addObject("message", "일반고객 입니다.");
		return view;
	}

	@RequestMapping(value = "kbs/login", params = "!type")
	public ModelAndView ccc() {
		ModelAndView view = new ModelAndView("show");
		view.addObject("message", "파라미터 없음!");
		return view;
	}

//== 요청 url 일부를 정보로 얻기 ====
	@RequestMapping(value = "kbs/{url}")
	public ModelAndView dd(@RequestParam("type") String type, @PathVariable String url
	) {
		//ModelAndView view = new ModelAndView("show");
		//view.addObject("message", "기타 : " + type + " " + url);
		//return view;
		
		ModelAndView view = new ModelAndView("show");
		if(url.equals("login")) {
			view.addObject("message", type);
		} else if(url.equals("korea")) {
			view.addObject("message", "대한민국 만세");
		} else {
			view.addObject("message", "기타");
		}
		
		return view;
	}
	
	@RequestMapping(value = "/ent/{co}/singer/{singer}")
	public ModelAndView ee(
			@RequestParam("title") String title,
			@PathVariable("co") String sosok,
			@PathVariable String singer) {
			ModelAndView view = new ModelAndView("show");
			String ss = "소속사 : " + sosok + ",가수 : " + singer + ", 대표곡" +title;
			
			view.addObject("message", ss);
			return view;
	}
			
}