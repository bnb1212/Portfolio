package pack.equip;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.equip.SqlMapperInter2;
import pack.mybatis.SqlMapConfig;

public class EquipProc {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();

	public List<EquipDto> selectEquip() {
		SqlSession sqlSession = factory.openSession();
		List<EquipDto> list = null;
		try {
			SqlMapperInter2 inter = (SqlMapperInter2) sqlSession.getMapper(SqlMapperInter2.class);
			list = inter.selectEquip();
		} catch (Exception e) {
			System.out.println("selectEquip err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return list;
	}
	
	public EquipDto selectEquipOne(String no){
		SqlSession sqlSession = factory.openSession();
		EquipDto dto = new EquipDto();
		try {
			SqlMapperInter2 inter = (SqlMapperInter2) sqlSession.getMapper(SqlMapperInter2.class);
			dto = inter.selectEquipOne(no);
		} catch (Exception e) {
			System.out.println("selectEquipData err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}

		return dto;
	}
	
	public boolean insertEquip(EquipFormBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		String uploadDir = "C:/work/jsou/semi_project/WebContent/upload";
		
		try {
			SqlMapperInter2 inter = (SqlMapperInter2) sqlSession.getMapper(SqlMapperInter2.class);
			if (inter.insertEquip(bean) > 0)
				b = true;
			sqlSession.commit();
		} catch (Exception e) {
			System.out.println("insertEquip err : " + e);
			sqlSession.rollback();
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return b;
	}
	
	public boolean deleteEquip(String equip_no) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		try {
			SqlMapperInter2 inter = (SqlMapperInter2) sqlSession.getMapper(SqlMapperInter2.class);
			
			int cou = inter.deleteEquip(equip_no);
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
