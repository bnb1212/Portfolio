<%@ page language="java" contentType="text/plain; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>

[
<%Connection conn = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;

			try {
				Class.forName("org.mariadb.jdbc.Driver");
			} catch (Exception e) {
				System.out.println("loading err : " + e);
				return;
			}

			try {
				conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
				pstmt = conn.prepareStatement("select * from sangdata");
				rs = pstmt.executeQuery();
				String result = "";

				// Thread.sleep(5000);

				while (rs.next()) {
					result += "{";
					result += "\"code\":" + "\"" + rs.getString("code") + "\",";
					result += "\"sang\":" + "\"" + rs.getString("sang") + "\",";
					result += "\"su\":" + "\"" + rs.getString("su") + "\",";
					result += "\"dan\":" + "\"" + rs.getString("dan") + "\"";
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
