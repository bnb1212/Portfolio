package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/PostServlet")
public class PostServlet extends HttpServlet {
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		
		String name = request.getParameter("name");
		// String addr = request.getParameter("addr"); 
		//여러개를 받을때는 배열로 받아야한다
		String addr[] = request.getParameterValues("addr");
		
		//checkbox
		String lan[] = request.getParameterValues("lan"); // checkbox도 배열로 받자
		
		//radio
		String os = request.getParameter("os"); 
		
		//select
		String tr = request.getParameter("tr");
		
		//hidden
		String msg = request.getParameter("msg");
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter(); // 클라이언트 브라우저로 자료 전송
		out.println("<html><html><head>연습</head>");
		out.println("<body>");
		out.println("<b style='color:red'>* 결과 출력 * </b>");
		out.println("<br>이름은 " + name + "<br>");
		
		out.println("<br>주소는 " + addr[0] + addr[1] + "<br>");
		out.println("<a href='postex.html'>자료 다시 입력</a>");
		
		//checkbox
		try {
			out.print("<br>선택한 언어는 ");
			for(String la:lan) {
				out.print(la + ", ");
			}
			out.print("<br>");
		} catch(Exception e) {
			out.println("<br>하나 이상의 언어를 선택해 보세요 ");
		}
		//radio
		out.println("<br>운영체제는 " + os + "<br>");
		
		out.println("<br>교통수단은 " + tr + "<br>");
		
		out.println("<br>" + msg);
		out.println("</body></html>");
		out.close();
		
		System.out.println(name + " " + addr[0] + " " + addr[1]); // StandardContext 기억
	}
}