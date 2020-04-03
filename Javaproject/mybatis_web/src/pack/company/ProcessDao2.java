package pack.company;

import java.sql.SQLException;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.exam.SqlMapConfig2;

public class ProcessDao2 {
	private SqlSessionFactory factory = SqlMapConfig2.getSqlSession();

	public List selectJikDataAll() throws SQLException {
		SqlSession sqlSession = factory.openSession();
		List list = sqlSession.selectList("selectDataAll");
		sqlSession.close();
		return list;
	}

	public List selectDataPart() throws SQLException {
		SqlSession sqlSession = factory.openSession(); // 세션을 열어요
		List list = sqlSession.selectList("selectDataPart");// 하나 읽을땐 selectOne
		sqlSession.close(); // 작업이 끝나면 세션을 닫아요
		return list;
	}
	// ===================================================
	// 프로그래머라면 이렇게 한다
	/*
	public boolean deleteData(int arg) throws SQLException {
		SqlSession sqlSession = factory.openSession(); // sqlSession을 열고 configure에 mapper를 만나고
		boolean re = false;
		try { 
			int cou = sqlSession.delete("delData", arg);
			if(cou >0) re =true;
			sqlSession.commit(); // 제대로 되면 커밋
		} catch (Exception e) {
			System.out.println("deleteData err : " + e);
			sqlSession.rollback(); // 아니믄 롤백
		} finally { 
			if (sqlSession != null)
				sqlSession.close(); 
		}
		return re;

	}
	*/
}
