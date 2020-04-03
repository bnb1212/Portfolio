<%@ page language="java" contentType="text/plain; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>

[
<%Connection conn = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;

			request.setCharacterEncoding("utf-8");
			String buser = request.getParameter("buserName");
			//System.out.print(buser);

			try {
				Class.forName("org.mariadb.jdbc.Driver");
			} catch (Exception e) {
				System.out.println("loading err : " + e);
				return;
			}

			try {
				conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
				String sql = "";

				sql = "select jikwon_no, jikwon_name, buser_tel, (select count(gogek_damsano) from jikwon count_jik left join gogek on jikwon_no = gogek_damsano where main_jik.jikwon_no = count_jik.jikwon_no) as gogek_su "
						+ "from jikwon main_jik " + "inner join buser on main_jik.buser_num = buser_no ";

				if (buser.equals("전체")) {
					pstmt = conn.prepareStatement(sql);
				} else {
					sql += "where buser_name = ?";
					pstmt = conn.prepareStatement(sql);
					pstmt.setString(1, buser);
				}

				rs = pstmt.executeQuery();
				String result = "";

				while (rs.next()) {
					result += "{";
					result += "\"jikNo\":" + "\"" + rs.getString("jikwon_no") + "\",";
					result += "\"jikName\":" + "\"" + rs.getString("jikwon_name") + "\",";
					result += "\"buserTel\":" + "\"" + rs.getString("buser_tel") + "\",";
					result += "\"gogekSu\":" + "\"" + rs.getString("gogek_su") + "\"";
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
