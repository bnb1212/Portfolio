package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/kor.mbc") // web.xml에서 일일히 적어주지 않고 어느테이션으로 해결(신기능)
public class ServletGo extends HttpServlet {
//	public ServletGo() {
//		System.out.println("ServletGO 생성자\n");
//	}
	private OurClass our = null;
	// 서블릿 라이프 사이클
	public void init(ServletConfig config) throws ServletException {
		System.out.println("init"); // 웹에서는 생성자를 거의 사용지 않는다. init함수가 초기화를 담당.
		our = new OurClass();// 1회 수행됨
		
	}

	public void destroy() {
		System.out.println("destroy"); // 마무리 담당. 서비스 종료 시 1회 수행
		our = null;
	}

	//중요한거 9개 딱 들어가있는 메소드 
	/*
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("good-service"); // JSP에서는 멤버 변수를 선언할수 없다. 메소드만 있기 때문에
											// JSP에서 선언하는 모든 변수는 지역변수가 됨
											// JSP가 이 안에 들어 간다.
	}
	*/
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//System.out.println("nice - doGet");
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter(); // 클라이언트 브라우저로 자료 전송
		out.println("<html><html><head>연습</head>");
		out.println("<body><h1>서블릿 시작</h1>");
		int a = 10, b = 20;
		out.println("a=" + a + ", b=" + b);
		int tot = myCalc(a,b);
		
		
		out.println("<br>이름은=" + our.getIrum()); // our 객체를 초기화 과정에서 만들어두면 부를때마다 init에서 만들어진 our을 쓴다
		out.println("<br>tot=" + tot);
		out.println("</body></html>");
		out.close();
		
	}

	private int myCalc(int a, int b) {
		return a + b;
	}
	//protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	//	doGet(request, response);
	//}

}
