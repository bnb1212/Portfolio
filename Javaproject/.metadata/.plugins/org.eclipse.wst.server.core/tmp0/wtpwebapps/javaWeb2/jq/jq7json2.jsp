<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*"%>

[
<%Connection conn = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;

			//request.setCharacterEncoding("utf-8");
			String jikNo = request.getParameter("jikwonNo");
			System.out.print(jikNo);

			try {
				Class.forName("org.mariadb.jdbc.Driver");
			} catch (Exception e) {
				System.out.println("loading err : " + e);
				return;
			}

			try {
				conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
				String sql = "";

				sql = "select gogek_name, gogek_tel, " 
					+ "case when substr(gogek_jumin, 8, 1) in ('1', '3') then '남' when substr(gogek_jumin, 8, 1) in ('2', '4') then '여' else '미상' end as gogek_gen "
					+ "from gogek inner join jikwon on jikwon_no = gogek_damsano "
					+ "where jikwon_no = ?";

				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, jikNo);
				rs = pstmt.executeQuery();
				String result = "";

				while (rs.next()) {
					result += "{";
					result += "\"gogekName\":" + "\"" + rs.getString("gogek_name") + "\",";
					result += "\"gogekTel\":" + "\"" + rs.getString("gogek_tel") + "\",";
					result += "\"gogekGen\":" + "\"" + rs.getString("gogek_gen") + "\"";
					result += "},";
				}

				if (result.length() > 0) {
					result = result.substring(0, result.length() - 1);
				}
				out.println(result);

				rs.close();
				pstmt.close();
				conn.close();
			} catch (Exception e) {
				System.out.println("err : " + e);
				return;
			}%>
]
