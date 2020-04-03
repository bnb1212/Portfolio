package pack;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Service;

@Service
public class JikwonImpl extends JdbcDaoSupport implements JikwonInter{

	public List<JikwonDto> selectList() throws DataAccessException {
		RowMapper rowMapper = new JikRowMapper();

		return getJdbcTemplate().query("select jikwon_no, jikwon_name, buser_name, jikwon_jik from jikwon left join buser on buser_no = buser_num", rowMapper);
	}

	class JikRowMapper implements RowMapper {
		public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
			// select로 수행된 레코드 수 만큼 호출당함
			JikwonDto dto = new JikwonDto();
			dto.setJikwon_no(rs.getString("jikwon_no"));
			dto.setJikwon_name(rs.getString("jikwon_name"));
			dto.setBuser_name(rs.getString("buser_name"));
			dto.setJikwon_jik(rs.getString("jikwon_jik"));
			
			return dto; // List 컬렉션에 계속 기억됨
		}
	}
}
