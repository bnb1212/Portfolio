package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.controller.MemBean;

@Repository
public class MemDaoImple extends SqlSessionDaoSupport implements MemDaoInter {

	@Autowired
	public MemDaoImple(SqlSessionFactory factory) {
		setSqlSessionFactory(factory);
	}

	@Override
	public List<MemDto> getDataAll() {
		return getSqlSession().selectList("selectDataAll");
	}

	@Override
	public boolean deleteData(String num) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean insertData(MemBean bean) {
		try {
			getSqlSession().insert("", bean);
			return true;
		} catch (Exception e) {
			System.out.println("insert err : " + e);
			return false;
		}
	}

	@Override
	public MemDto selectPart(String num) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean updateData(MemBean bean) {
		// TODO Auto-generated method stub
		return false;

	}
}
