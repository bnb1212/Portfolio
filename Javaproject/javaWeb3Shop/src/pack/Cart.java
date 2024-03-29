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
 * Servlet implementation class Cart
 */
@WebServlet("/Cart")
public class Cart extends HttpServlet {
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String name = request.getParameter("name");
		int price = Integer.parseInt(request.getParameter("price"));
		
		// System.out.println(name + " " + price);
		
		HttpSession session = request.getSession(true);
		ArrayList<Goods> glist = (ArrayList<Goods>)session.getAttribute("list");
		if(glist == null) glist = new ArrayList<Goods>();
		
		glist.add(new Goods(name, price)); // 상품 하나가 객체로 Goods객체로 생성후 glist에 저장
		session.setAttribute("list", glist);
		
		// 장바구니에 담긴 내용 출력
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body> "+name + " 구입하셨네요");
		out.println("<br><a href='Shop.html'>계속 쇼핑</a>");
		out.println("<br><a href='Buy'>결제하기</a>");
		out.println("<p/><table border='1' width='70%'>");
		out.println("<tr><th>상품명</th><th>가격</th></tr>");
		for(int i = 0; i <glist.size(); i++) {
			Goods goods = (Goods)glist.get(i);
			out.println("<tr><td>" + goods.getName()+ "</td>");
			out.println("<td>" + goods.getPrice() + "</td></tr>");			
		}
		out.println("</table>");
		out.print("</body></html>");
		out.close();
		
	}

}
