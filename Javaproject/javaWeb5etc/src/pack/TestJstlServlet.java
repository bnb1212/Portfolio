package pack;


import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;



@WebServlet("/TestJstlServlet")
public class TestJstlServlet extends HttpServlet {
	
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String irum="사오정";
		req.setAttribute("man", irum);
		
		Person person = new Person();
		person.setName("한국인");
		req.setAttribute("person", person);
		
		Student student = new Student();
		student.setAge(33);
		req.setAttribute("student", student);
		
		String[] ani = {"말", "댕댕이","호랑이"};
		req.setAttribute("animal", ani);
		
		String[] foods = {"당근", "개밥", "동물"};
		List<Object> list = new ArrayList<Object>();
		list.add(ani);
		list.add(foods);
		req.setAttribute("list", list);
		
		req.getRequestDispatcher("test_jstl.jsp").forward(req, resp);
	}
}
