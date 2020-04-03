package bang;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class BangList
 */
@WebServlet("/BangList")
public class BangList extends HttpServlet {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;

	public void init() throws ServletException {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "123");
			// properties 파일을 이용한다 원래는
			pstmt = conn.prepareStatement("select * from miniguest");

		} catch (Exception e) {
			System.out.println("init err : " + e);
		}
	}

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body><h2>* 글 내용 *</h2>");
		out.println("<a href='bang/bangMain.html'>글쓰기</a><br>");		
		out.println("<table border='1' width='80%'>");
		try {
			rs = pstmt.executeQuery();
			while(rs.next()) {
				out.println("<tr style='background-color:yellow;'>");
				out.println("<td>코드 : "+rs.getString("code")+"</td>");
				out.println("</tr>");
				out.println("<tr>");
				out.println("<td>작성자 : "+rs.getString("name")+"</td>");
				out.println("</tr>");
				out.println("<tr>");
				out.println("<td>글제목 : "+rs.getString("subject")+"</td>");
				out.println("</tr>");
				out.println("<tr>");
				out.println("<td height='100'> "+rs.getString("content")+"</td>");
				out.println("</tr>");
				
			}
		} catch(Exception e) {
			System.out.println("doGet err : "+ e);
		}
	}
	
	public void destroy() {
		try {
			if (pstmt != null)
				pstmt.close();
			if (conn != null)
				conn.close();
		} catch (Exception e) {

		}
	}
}
