package pack.qnaboard;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class QnaBoardMgr { // 게시판의 Business Logic을 가지고있음
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;

	private int tot; // 전체 레코드 수
	private int pList = 5; // 페이지 당 출력 행 수 5개
	private int pageSu; // 전체 페이지 수

	public QnaBoardMgr() {
		try {
			Context context = new InitialContext();
			ds = (DataSource) context.lookup("java:comp/env/jdbc_maria");
		} catch (Exception e) {
			System.out.println("BoardMgr err : " + e);
		}
	}

	public int currentGetNum() {
		String sql = "select max(num) from shopboard";
		int cnt = 0;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			if (rs.next())
				cnt = rs.getInt(1);
			
		} catch (Exception e) {
			System.out.println("currentGetNum err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
		return cnt;
	}

	public void saveData(BoardBean bean) {
		String sql = "insert into shopboard values(?,?,?,?,?,?,?,?,?,?,?)"; // 12개
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, bean.getNum());
			pstmt.setString(2, bean.getName());
			pstmt.setString(3, bean.getPass());
			pstmt.setString(4, bean.getMail());
			pstmt.setString(5, bean.getTitle());
			pstmt.setString(6, bean.getCont());
			pstmt.setString(7, bean.getBdate());
			pstmt.setInt(8, 0);	 //readcnt
			pstmt.setInt(9, bean.getGnum());
			pstmt.setInt(10, 0); //onum
			pstmt.setInt(11, 0); //nested
			
			pstmt.executeUpdate();
		} catch (Exception e) {
			System.out.println("saveData err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
	public ArrayList<BoardDto> getDataAll(int page, String stype, String sword){
		ArrayList<BoardDto> list = new ArrayList<BoardDto>();
		String sql = "select *from shopboard";
		try {
			conn = ds.getConnection();
			
			if(sword == null) {	//검색 X
				sql += " order by gnum desc, onum asc";
				pstmt = conn.prepareStatement(sql);
			}else { //검색 O
				sql += " where " + stype + " like ?";
				sql += " order by gnum desc, onum asc";
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, "%" + sword + "%"); //%sword% sword가 포함되어있는 모든 게시글 검색
				
			}
			
			rs = pstmt.executeQuery();
			
			for (int i = 0; i < (page -1)*pList; i++) {
				// 레코드 포인터 위치 이동 - 0번째 위치.~5번 수행 (처음은 page가 0이라 수행 안함.)
				// 레코드 포인터 위치 이동 - 4번째 위치. 5번부터 시작함.
				// 레코드 포인터 위치 이동 - 9번째 위치. 10번부터 시작.
				rs.next(); 
			}
			
			int k = 0;
			while(rs.next() && k < pList) { //pList는 5. 5번만 돈다.
				BoardDto dto = new BoardDto();
				dto.setNum(rs.getInt("num"));
				dto.setName(rs.getString("name"));
				dto.setTitle(rs.getString("title"));
				dto.setBdate(rs.getString("bdate"));
				dto.setReadcnt(rs.getInt("readcnt"));
				dto.setNested(rs.getInt("nested"));
				list.add(dto);
				k++;
			}
			
		} catch (Exception e) {
			System.out.println("getDataAll err : " + e);
		}finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
		return list;
	}

	public void totalList() {
		String sql = "select count(*) from shopboard";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			rs.next(); //포인터이동
			tot = rs.getInt(1); //전체 건수(전체 레코드의 개수)
		} catch (Exception e) {
			System.out.println("totalList err : " + e);
		}finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
	//pageSu 계산 
	public int getPageSu() {
		pageSu = tot/pList; //정수나누기. 몫만 취함.
		//나머지가 있으면 페이지수를 하나 늘린다.
		if(tot % pList > 0) pageSu++;
			
		return pageSu;	
	}
	
	//조회수 체크
	public void updateReadcnt(String num) { // 글 내용 보기 전에 조회수 증가 
		String sql = "update shopboard set readcnt = readcnt + 1 where num = ?";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			pstmt.executeUpdate();
			
		} catch (Exception e) {
			System.out.println("updateReadcnt err : " + e);
		}finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
	//상세 게시글 보기
	public BoardDto getData(String num) {
		String sql = "select * from shopboard where num = ?";
		BoardDto dto = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				dto = new BoardDto();
				dto.setName(rs.getString("name"));
				dto.setPass(rs.getString("pass"));
				dto.setMail(rs.getString("mail"));
				dto.setTitle(rs.getString("title"));
				dto.setCont(rs.getString("cont"));
				dto.setBip(rs.getString("bip"));
				dto.setBdate(rs.getString("bdate"));
				dto.setReadcnt(rs.getInt("readcnt"));
			}
		} catch (Exception e) {
			System.out.println("getData err : " + e);
		}finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
		return dto;
	}
	
	//댓글 보기
	public BoardDto getReplyData(String num) {	
		String sql = "select * from shopboard where num = ?";
		BoardDto dto = null;
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			rs = pstmt.executeQuery();
			if(rs.next()) {
				dto = new BoardDto();
				dto.setTitle(rs.getString("title"));
				dto.setGnum(rs.getInt("gnum"));
				dto.setOnum(rs.getInt("onum"));
				dto.setNested(rs.getInt("nested"));
			}
		} catch (Exception e) {
			System.out.println("getReplyData err : " + e);
		}finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
		return dto;
	}
	
	//댓글 onum 갱신
	public void updateOnum(int gnum, int onum) { 
		String sql = "update shopboard set onum=onum+1 where onum >=? and gnum = ?";
		//같은 그룹의 레코드는 모두 작업에 참여
		//댓글의 onum은 이미 DB에 있는 onum보다 크거나 같은 값을 변경
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, onum);
			pstmt.setInt(2, gnum);
			pstmt.executeUpdate();
		} catch (Exception e) {
			System.out.println("updateOnum err : " + e);
		}finally {
			try {
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
	//댓글 저장
	public void saveReplyData(BoardBean bean) {
		String sql = "insert into shopboard values(?,?,?,?,?,?,?,?,?,?,?)"; // 12개
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, bean.getNum());
			pstmt.setString(2, bean.getName());
			pstmt.setString(3, bean.getPass());
			pstmt.setString(4, bean.getMail());
			pstmt.setString(5, bean.getTitle());
			pstmt.setString(6, bean.getCont());
			pstmt.setString(7, bean.getBdate());
			pstmt.setInt(8, 0);	 //readcnt
			pstmt.setInt(9, bean.getGnum());
			pstmt.setInt(10, bean.getOnum()); //onum
			pstmt.setInt(11, bean.getNested()); //nested
			pstmt.executeUpdate();
		} catch (Exception e) {
			System.out.println("saveReplyData err : " + e);
		} finally {
			try {
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
	//edit 비밀번호 비교
	public boolean chkPass(int num, String new_pass) {
		boolean b = false;
		try {
			String sql = "select pass from shopboard where num=?";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, num);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				if(new_pass.equals(rs.getString("pass"))){
					b = true;
				}
			}
		} catch (Exception e) {
			System.out.println("chkPass err : " + e);
		}finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
		
		return b;
	}
	
	public void saveEdit(BoardBean bean) {
		String sql = "update shopboard set name=?,mail=?,title=?,cont=? where num=?";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, bean.getName());
			pstmt.setString(2, bean.getMail());
			pstmt.setString(3, bean.getTitle());
			pstmt.setString(4, bean.getCont());
			pstmt.setInt(5, bean.getNum());
			pstmt.executeUpdate();
			
		} catch (Exception e) {
			System.out.println("saveEdit err : " + e);
		}finally {
			try {
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
	public void deleteData(String num) {
		String sql = "delete from shopboard where num = ?";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			pstmt.executeUpdate();
			
		} catch (Exception e) {
			System.out.println("deleteData err : " + e);
		}finally {
			try {
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}
	
}
