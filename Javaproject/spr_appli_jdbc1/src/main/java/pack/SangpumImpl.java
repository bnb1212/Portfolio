package pack;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLClientInfoException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;

/*
//spring이 제공하는 JDBCdaosupprot를 사용하는 방법
public class SangpumImpl extends JdbcDaoSupport implements SangpumInter {
	
	
	public SangpumImpl(){

	}

	public List<SangpumDto> selectList() throws DataAccessException {
		RowMapper rowMapper = new SangRowMapper();
		
		return getJdbcTemplate().query("select * from sangdata", rowMapper);
	}

	class SangRowMapper implements RowMapper {
		public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
			// select로 수행된 레코드 수 만큼 호출당함
			System.out.println("rowNum : " + rowNum);
			SangpumDto dto = new SangpumDto();
			dto.setCode(rs.getString("code"));
			dto.setSang(rs.getString("sang"));
			dto.setSu(rs.getString("su"));
			dto.setDan(rs.getString("dan"));
			return dto; // List 컬렉션에 계속 기억됨
		}
	}
}
*/
// 전통적 방법
public class SangpumImpl implements SangpumInter {
	
	
	public SangpumImpl() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			
		} catch (Exception e) {
			System.out.println("SangpumImp1 err : " + e);
		}
	}
	
	public List<SangpumDto> selectList() throws DataAccessException {
		ArrayList<SangpumDto> list = new ArrayList<SangpumDto>();
		try {
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
			PreparedStatement pstmt = conn.prepareStatement("select * from sangdata");
			ResultSet rs = pstmt.executeQuery();
			while(rs.next()) {
				SangpumDto dto = new SangpumDto();
				dto.setCode(rs.getString("code"));
				dto.setSang(rs.getString("sang"));
				dto.setSu(rs.getString("su"));
				dto.setDan(rs.getString("dan"));
				list.add(dto);
			}
		} catch (Exception e) {
			System.out.println("selectList err : " + e);
		}
		return list;
	}
}

