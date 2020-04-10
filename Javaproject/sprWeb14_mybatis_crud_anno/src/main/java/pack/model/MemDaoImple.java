package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.controller.MemBean;

@Repository
public class MemDaoImple implements MemDaoInter {

	@Autowired
	public MemAnnoInter memAnnoInter;

	@Override
	public List<MemDto> getDataAll() {
		return memAnnoInter.getDataAll();
	}

	@Override
	public boolean deleteData(String num) {
		return memAnnoInter.deleteData(num);
	}

	@Override
	public boolean insertData(MemBean bean) {
		return memAnnoInter.insertData(bean);
	}

	@Override
	public MemDto selectPart(String num) {
		return memAnnoInter.selectPart(num);
	}

	@Override
	public boolean updateData(MemBean bean) {
		return memAnnoInter.updateData(bean);

	}
}
