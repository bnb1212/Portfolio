package bang;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/bangServlet")
public class bangServlet extends HttpServlet {
	private Connection conn;
	private PreparedStatement pstmt;

	public void init(ServletConfig config) throws ServletException {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "123");
			// properties 파일을 이용한다 원래는
			pstmt = conn.prepareStatement("insert into miniguest(name, subject, content) values (?,?,?)");

			
		} catch (Exception e) {
			System.out.println("init err : " + e);
		}
	}

	public void destroy() {
		try {
			if(pstmt != null) pstmt.close();
			if(conn != null) conn.close();
		}catch(Exception e) {
			
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String name = request.getParameter("name");
		String subject = request.getParameter("subject");
		String content = request.getParameter("content");
		System.out.println(name + " " + subject + " " + content);
		
		try {
			pstmt.setString(1, name);
			pstmt.setString(2, subject);
			pstmt.setString(3, content);
			pstmt.executeUpdate();
			
			// response.sendRedirect("bang/bangMain.html"); 이렇게 하는게 원칙
			
			response.setContentType("text/html;charset=utf-8");
			PrintWriter out = response.getWriter();
			out.println("<html><body><b>" + name + "</b>님 등록 완료");
			out.println("<br><a href='bang/bangMain.html'>새 글 입력</a>");
			out.println("<br><a href='BangList'>글 내용 보기</a>");	
			out.println("</body></html>");
			out.close();
			
		}catch (Exception e) {
			System.out.println("doPost err" + e);
		}
		
	}

}
