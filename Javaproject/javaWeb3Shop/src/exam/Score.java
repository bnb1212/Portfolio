package exam;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import pack.Goods;

@WebServlet("/Score")
public class Score extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// System.out.println("넘어옴");

		request.setCharacterEncoding("utf-8");
		int no = Integer.parseInt(request.getParameter("no"));
		String name = request.getParameter("name");
		int kor = Integer.parseInt(request.getParameter("kor"));
		int eng = Integer.parseInt(request.getParameter("eng"));
		Student adStudent = new Student(no, name, kor, eng);

		HttpSession session = request.getSession(true);
		ArrayList<Student> studentList = (ArrayList<Student>) session.getAttribute("list");
		if (studentList == null) {
			studentList = new ArrayList<Student>();
			studentList.add(adStudent);
			session.setAttribute("list", studentList);
		} else {
			boolean check = true;
			for (int i = 0; i < studentList.size(); i++) {
				Student students = (Student) studentList.get(i);
				if (adStudent.getNo() == students.getNo()) {
					System.out.print("중복에러");
					check = false;
					break;
				}
			}

			if (check) {
				studentList.add(adStudent);
				session.setAttribute("list", studentList);
			}

		}

		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body><h2>학생들 성적표</h2>");
		out.println("<p/><table border='1' width='70%'>");
		out.println("<tr><th>번호</th><th>이름</th><th>국어</th><th>영어</th><th>총점</th></tr>");
		for (int i = 0; i < studentList.size(); i++) {
			Student students = (Student) studentList.get(i);
			out.println("<tr><td>" + students.getNo() + "</td>");
			out.println("<td>" + students.getName() + "</td>");
			out.println("<td>" + students.getKor() + "</td>");
			out.println("<td>" + students.getEng() + "</td>");
			out.println("<td>" + (students.getKor() + students.getEng()) + "</td></tr>");
		}
		out.println("</table>");
		out.println("인원수 : " + studentList.size() + "명");
		out.println("<br><a href='#' onclick='history.back()'>새로 입력</a>&nbsp;&nbsp;");
		out.println("<a href='Del' name='del'>세션 삭제</a>");
		out.print("</body></html>");
		out.close();
	}
}
