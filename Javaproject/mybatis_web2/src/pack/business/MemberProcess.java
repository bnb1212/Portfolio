package pack.business;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.mybatis.SqlMapConfig;

public class MemberProcess {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();

	// 이 메소드 하나가 Mybatis 하나의 작업 단위
	public List<DataDto> selectDataAll() {
		SqlSession sqlSession = factory.openSession();
		List<DataDto> list = null;
		try {
			list = sqlSession.selectList("selectDataAll");
		} catch (Exception e) {
			System.out.println("selectDataAll err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return list;
	}

	public boolean insertData(DataFormBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();

		try {
			if (sqlSession.insert("insertData", bean) > 0)
				b = true;
			sqlSession.commit();
		} catch (Exception e) {
			System.out.println("insertData err : " + e);
			sqlSession.rollback();
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return b;
	}

	public DataDto selectDataPart(String id) {
		SqlSession sqlSession = factory.openSession();
		DataDto dto = new DataDto();

		try {
			dto = sqlSession.selectOne("selectDataPart", id);
		} catch (Exception e) {
			System.out.println("selectPartData err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}

		return dto;

	}

	public boolean updateData(DataFormBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		bean.setColname("id");
		try {
			DataDto dto = selectDataPart(bean.getId());
			if (dto.getPasswd().equalsIgnoreCase(bean.getPasswd())) {
				if (sqlSession.update("upData", bean) > 0) {
					b = true;
					sqlSession.commit();
				}
			}
		} catch (Exception e) {
			System.out.println("updateDataPart err : " + e);
			sqlSession.rollback();
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}

		return b;
	}

	public boolean deleteData(String id) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		try {

			int cou = sqlSession.delete("delData", id);
			if (cou > 0)
				b = true;
				sqlSession.commit();
			
		} catch (Exception e) {
			System.out.println("deleteData err : " + e);
			sqlSession.rollback();
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return b;
	}
}
