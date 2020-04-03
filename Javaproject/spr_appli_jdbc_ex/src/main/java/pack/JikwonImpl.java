package pack;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import javax.annotation.Resource;

import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;
import org.springframework.stereotype.Repository;

@Repository
public class JikwonImpl extends JdbcDaoSupport implements JikwonInter{

		private List<JikwonDto> list = null;
	
	public JikwonImpl(DbDataSource dataSource) {
		setDataSource(dataSource);
	}
		
	public void initList() throws DataAccessException {
		RowMapper rowMapper = new JikRowMapper();

		list = getJdbcTemplate().query("select jikwon_no, jikwon_name, buser_name, jikwon_jik from jikwon left join buser on buser_no = buser_num", rowMapper);
	}
	
	public List<JikwonDto> getList() {
		return list;
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
