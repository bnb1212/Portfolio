package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/SessionTest")
public class SessionTest extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		HttpSession session = request.getSession(true); // 세션이 있으면 읽는당, 없으면 만든당
//		HttpSession session = request.getSession(false); // 세션이 있으면 읽고, 없으면 생성 안함

		session.setMaxInactiveInterval(60); // 1분간 세션 유효
		if (session != null)
			session.setAttribute("name", "홍길동"); // 쿠키는 String, 세션은 object로 처리

		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("session id: " + session.getId());
		out.println("<br>사용자명: " + session.getAttribute("name"));

		out.println("</body></html>");
		out.close();
	}
}
