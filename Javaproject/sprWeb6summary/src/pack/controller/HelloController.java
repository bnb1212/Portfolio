package pack.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;
import org.springframework.web.servlet.mvc.Controller;

import pack.model.HelloModel;

/*
public class HelloController implements Controller{
	
	
	@Override 
	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
		// TODO Auto-generated method stub
		return null;
	}
}
*/
public class HelloController extends AbstractController {
	private HelloModel helloModel; // 모델 영역의 클래스와 통신하기 위함

	public void setHelloModel(HelloModel helloModel) {
		this.helloModel = helloModel;
	}

	@Override
	protected ModelAndView handleRequestInternal(HttpServletRequest request, HttpServletResponse response)
			throws Exception {
		request.setCharacterEncoding("utf-8");
		String result = helloModel.getGreeting();

		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("hello"); // forwarding (기본값)
		
		//set attribute로 준것
		modelAndView.addObject("result", result);
		// request.setAttribute("result", result); 위와 같은 뜻
		
//		modelAndView.setViewName("redirect:WEB-INF/views/hello.jsp?result=" + result); // redirect 방식
		

		return modelAndView;
	}

}
