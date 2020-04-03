package pack;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLDecoder;
import java.net.URLEncoder;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/CookieLogin")
public class CookieLogin extends HttpServlet {
	protected void doGet(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response)
			throws javax.servlet.ServletException, java.io.IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		// 쿠키를 읽기
		String id = null;
		String pwd = null;
		try {
			Cookie[] cookies = request.getCookies(); // 클라이언트 컴퓨터의 모든 쿠키를 읽음
			for(int i = 0; i < cookies.length; i++) {
				String name = cookies[i].getName();
				System.out.println("name : " + name);
				if(name.equals("id")) {
					id = URLDecoder.decode(cookies[i].getValue(), "utf-8");
				}
				if(name.equals("pwd")) {
					pwd = URLDecoder.decode(cookies[i].getValue(), "utf-8");
				}
				
			}
		}catch (Exception e) {

		}
		if(id != null && pwd != null) {
			out.println(id + "님 쿠키를 통해 로그인한 상태 입니다");
			out.println("</body></html>");
			out.close();
			return;
		}

		// 쿠키를 읽어 없으면 로그인 화면 출력
		
		out.print("** 로그인**");
		out.println("<form method='post'>");
		out.println("id : <input type='text' name='id'><br>");
		out.println("pwd : <input type='text' name='pwd'><br>");
		out.println("<input type='submit' value='전송'>");
		out.println("</form>");

		out.println("</body></html>");
		out.close();
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		// System.out.println(id+ " " + pwd);

		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		
		out.print("<html><body>");
		
		if (id.equals("aa") && pwd.equals("11")) {
			try {
				id = URLEncoder.encode(id, "utf-8");
				Cookie idCookie = new Cookie("id", id);
				idCookie.setMaxAge(60 * 60 * 24 * 365); // 1년간 유효
				
				pwd = URLEncoder.encode(pwd, "utf-8"); // 암호화
				Cookie pwdCookie = new Cookie("pwd", pwd);
				pwdCookie.setMaxAge(60 * 60 * 24 * 365);
				
				response.addCookie(idCookie);
				response.addCookie(pwdCookie);
				
				
				
			} catch (Exception e) {

			}
			out.println("로그인 성공 쿠키 생성");
			
		} else {
			out.print("로그인 실패");
		}
		out.println("</body><html>");
		out.close();

	}
}
