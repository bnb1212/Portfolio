package pack;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class GoMvc
 */
@WebServlet("/GoMvc")
public class GoMvc extends HttpServlet { // 컨트롤러 역할
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		
		String msg;
		String result ="", viewName ="";
		try {
			msg = request.getParameter("msg");
			//더 많은 요청이 있다고 가정하자.
		} catch (Exception e) {
			msg = null;
		} 
		
		// 클라이언트의 요청을 판단해서 BL과 View 를 판단
		if(msg == null || msg.equals("")) {
			result = "환영합니다"; // 모델에서 수행된 결과를 치환했다 가정
			//모델이 제공한 view 파일명을 얻었다고 가정
			viewName = "/WEB-INF/views/gomvc1.jsp"; // 클라이언트들이 접근하지 못하는 WEB-INF폴더에 view를 만든다
		}else if(msg.equals("korea")){
			result = "대한민국"; 
			viewName = "/WEB-INF/views/gomvc2.jsp";
		} else {
			result = msg;
			viewName = "/WEB-INF/views/gomvc2.jsp";
		}
		
		//여기서 부터의부분이 장고등 다른 프레임워크에서도 비슷한부분
		RequestDispatcher dispatcher = request.getRequestDispatcher(viewName);
		request.setAttribute("result", result);
		dispatcher.forward(request, response);
	}

}
