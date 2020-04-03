package pack;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Buy
 */
@WebServlet("/Buy")
public class Buy extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession(false);
		if(session == null) return; //세션 없으면 작업 안함
		
		ArrayList<Goods> glist = (ArrayList<Goods>)session.getAttribute("list");
		if(glist == null) return; // 리스트 없으면 작업 안함
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<p/><table border='1' width='70%'>");
		out.println("<tr><th>상품명</th><th>가격</th></tr>");
		int sum = 0;
		for(int i = 0; i <glist.size(); i++) {
			Goods goods = (Goods)glist.get(i);
			out.println("<tr><td>" + goods.getName()+ "</td>");
			out.println("<td>" + goods.getPrice() + "</td></tr>");			
			sum += goods.getPrice();
		}
		out.println("<tr><td colspan='2'>결제 총액 : " + sum+ "</td></tr>");
		out.println("</table>");
		out.println("<br>호갱님 결제 감사링감사띠 꺼억 ㅋㅋ");
		
		// session.invalidate() // 해당 고객의 모든 세션 삭제
		session.removeAttribute("list"); // 해당 고객의 특정 세션 삭제
		
		out.println("<br><a href='Shop.html'>첫화면으로 돌아가기</a>");
		out.print("</body></html>");
		out.close();
		

	}
}
