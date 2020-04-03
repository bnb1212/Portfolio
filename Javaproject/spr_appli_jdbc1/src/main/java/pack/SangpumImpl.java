package pack;

import java.sql.ResultSet;
import java.sql.SQLClientInfoException;
import java.sql.SQLException;
import java.util.List;

import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;

public class SangpumImpl extends JdbcDaoSupport implements SangpumInter {
	public SangpumImpl() {

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
