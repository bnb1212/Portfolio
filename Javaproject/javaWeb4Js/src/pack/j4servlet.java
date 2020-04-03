package pack;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class j4servlet
 */
@WebServlet("/irum.go")
public class j4servlet extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String data = request.getParameter("data");
		//이런 저런 작업후 
		
		// 파일 호출 방법 1 : 대상 - jsp or servlet : redirect - client를 통해 서버에 있는 파일 호출
		//response.sendRedirect("j4Called.jsp?data="+ data); // data는 String만 가능함
		
		// 파일 호출 방법 2 :대상 - jsp or servlet : forward - server에서 직접 server에 있는 파일 호출
		request.setAttribute("key", data); // 세션에 값 담는 것과 유사함. key-value.
											// 자바의 모든 객체가 가능
		//RequestDispatcher dispatcher = request.getRequestDispatcher("j4Called.jsp");
		//dispatcher.forward(request, response);
		request.getRequestDispatcher("j4Called.jsp").forward(request, response);
		

}
}