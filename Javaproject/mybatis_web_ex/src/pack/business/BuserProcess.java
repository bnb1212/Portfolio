package pack.business;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.mybatis.SqlMapConfig;

public class BuserProcess {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();

	// 이 메소드 하나가 Mybatis 하나의 작업 단위
	public List<DataDto> selectDataAll() {
		SqlSession sqlSession = factory.openSession();
		List<DataDto> list = null;
		try {
			SqlMapperInter inter = (SqlMapperInter) sqlSession.getMapper(SqlMapperInter.class);
			list = inter.selectDataAll();
		} catch (Exception e) {
			System.out.println("selectDataAll err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return list;
	}

}
