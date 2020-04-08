package aa.bb.model;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Repository;

import aa.bb.controller.MemberBean;

@Repository
public class MemberDao extends JdbcDaoSupport {
	
	@Autowired
	public MemberDao(DriverManagerDataSource dataSource) {
		setDataSource(dataSource);
	}
/*
	public List<MemberDto> getMemberAll() {
		String sql = "select * from member";
		List<MemberDto> list = getJdbcTemplate().query(sql, new RowMapper() {
			@Override
			public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
				MemberDto dto = new MemberDto();
				
				dto.setId(rs.getString("id"));
				dto.setPasswd(rs.getString("passwd"));
				dto.setName(rs.getString("name"));
				dto.setRegdate(rs.getString("regdate"));
				
				return dto;
			}
		});
		return list;
	}
	*/
	
	// 페이징 처리
	public List<MemberDto> getMemberAll(int startRow, int endRow) { // 매개변수 받아서 처리
		String sql = "select * from member limit ?, ?"; // oracle : rownum
		List<MemberDto> list = getJdbcTemplate().query(sql,  
			new Object[] {startRow, endRow},
			new RowMapper() {
			@Override
			public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
				MemberDto dto = new MemberDto();
				
				dto.setId(rs.getString("id"));
				dto.setPasswd(rs.getString("passwd"));
				dto.setName(rs.getString("name"));
				dto.setRegdate(rs.getString("regdate"));
				
				return dto;
			}
		});
		return list;
	}
	
	public int getMemberCount() { // 전체 레코드 수 구하기 (페이징할 떄 필요함)
		String sql = "select count(*) from member";
		return getJdbcTemplate().queryForObject(sql, Integer.class);
	}
	
	public void insData(MemberBean bean) {
		String sql = "insert into member values (?,?,?, now())";
		Object[] params = {bean.getId(), bean.getPasswd(), bean.getName()};
		getJdbcTemplate().update(sql, params);
	}
	
	public void upData(MemberBean bean) {
		String sql = "update member set passwd=?, name=? where id=?";
		Object[] params = {bean.getPasswd(), bean.getName(), bean.getId()};
		getJdbcTemplate().update(sql, params);
	}
	
	public void delData(String id) {
		String sql = "delete from member where id=?";
		getJdbcTemplate().update(sql, new Object[] {id});
	}
	
	public MemberDto getMember(String id) { //1 레코드 상세보기
		String sql = "select * from member where id=?";
		MemberDto dto = (MemberDto)getJdbcTemplate().queryForObject(sql, new Object[] {id}, new RowMapper(){
			@Override
			public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
				MemberDto dto = new MemberDto();
				
				dto.setId(rs.getString("id"));
				dto.setPasswd(rs.getString("passwd"));
				dto.setName(rs.getString("name"));
				dto.setRegdate(rs.getString("regdate"));
				
				return dto;
			}
		});
		
		return dto;
		
	}

}
