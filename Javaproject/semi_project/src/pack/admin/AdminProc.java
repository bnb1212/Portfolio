package pack.admin;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.admin.AdminDto;
import pack.mybatis.SqlMapConfig;

public class AdminProc {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();

	public boolean adminLogin(String id, String password){
		boolean b = false;
		List<AdminDto> list = null;
		SqlSession sqlSession = factory.openSession();

		try {
			SqlMapperInter inter = (SqlMapperInter) sqlSession.getMapper(SqlMapperInter.class);
			list = inter.selectAdmin();
			//System.out.println(id);
			//System.out.println(password);
			for (int i = 0; i < list.size(); i++) {
				AdminDto dto = list.get(i);
				//System.out.println(dto.getAdmin_id());
				//System.out.println(dto.getAdmin_password());
				if (dto.getAdmin_id().equals(id) && dto.getAdmin_password().equals(password)) {
					b = true;
				}
			}
		} catch (Exception e) {
			System.out.println("Login err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return b;
	}

}
