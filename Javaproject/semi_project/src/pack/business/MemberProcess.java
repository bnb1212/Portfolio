package pack.business;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.mybatis.SqlMapConfig;

public class MemberProcess {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();
	
	public List<DataDto> selectDataAll(){
		SqlSession sqlSession = factory.openSession();
		List<DataDto> list = null;
		try {
			list = sqlSession.selectList("selectDataAll");//selectDataAll 이건 MemberMapper의 id중 하나다.
		} catch (Exception e) {
			System.out.println("selectDataAll err : " + e);
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		return list;
	}
	
	public boolean insertData(DataFormBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		try {
			if(sqlSession.insert("insertData", bean) > 0 ) b=true;
			sqlSession.commit();
		} catch (Exception e) {
			System.out.println("insertData err : " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		return b;
	}
	
	public DataDto selectDataPart(String id) {
		SqlSession sqlSession = factory.openSession();
		DataDto dto = null;
		
		try {
			dto = sqlSession.selectOne("selectDataPart", id);
		} catch (Exception e) {
			System.out.println("selectDataPart err : " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		return dto;
		
	}
	
	public boolean updateData(DataFormBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		bean.setColname("id");//colname에 id를 넣어서 sql문 완성하는 방식.동적으로 
		try {
			//비밀번호 비교 후 수정여부 판단
			DataDto dto = selectDataPart(bean.getId());
			if(dto.getPasswd().equalsIgnoreCase(bean.getPasswd())) {
				if(sqlSession.update("upData", bean) > 0) {
					b = true;
					sqlSession.commit();
				}
			}
			
		}catch (Exception e) {
			System.out.println("updateData err : " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		return b;
	}
	
	public boolean deleteData(String id) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		
		try {
			int cou = sqlSession.delete("dalData", id);
			if(cou > 0) b = true;
			sqlSession.commit();
			
		}catch (Exception e) {
			System.out.println("deleteData err : " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		return b;
	}
	
	
	
}
