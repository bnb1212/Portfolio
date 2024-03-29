package pack;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet({"/hobby.do", "/kbs.do", "*.nice", "*.kor"})
public class HobbyController extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// 컨트롤러
		String hobby = request.getParameter("hobby");

		// 모델과 연결
		HobbyModel hobbyModel = HobbyModel.getInstance();
		ArrayList<String> list = hobbyModel.getHobby(hobby);

		// 뷰로 출력
		request.setAttribute("datas", list);
		String viewname="hobby.jsp";
		
		request.getRequestDispatcher(viewname).forward(request, response);
	}

}
