package pack;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class TestController implements Controller {
	@Override
	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
		// 컨트롤러 영역에 있는 클래스 : 모델에 있는 특정 클래스와 커뮤니케이션을 위함
		System.out.println("TestController 수행 : 모델에 다녀왔다 가정");
		
		//return new ModelAndView("list");
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("list");
		modelAndView.addObject("key","모델에서 얻은 스프링 만세");
		return modelAndView;
		
		
		
	}

}
