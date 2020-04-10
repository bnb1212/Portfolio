package pack.board.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.board.controller.BoardBean;

@Repository
public class BoardDao extends SqlSessionDaoSupport implements BoardDaoInter {

	@Autowired
	public BoardDao(SqlSessionFactory sqlSessionFactory) {
		setSqlSessionFactory(sqlSessionFactory);
	}

	public List<Board> getDataAll() {
		return getSqlSession().selectList("selectDataAll");
	}

	public int addReadCnt(String num) {
		return getSqlSession().update("addReadCnt", num);
	}

	public Board detail(String num) {
		return getSqlSession().selectOne("selectDetail", num);
	}

	public boolean update(BoardBean bean) {
		try {
			getSqlSession().update("updateData", bean);
			return true;
		} catch (Exception e) {
			System.out.println("update err :" + e);
			return false;
		}
	}

	public boolean delete(String num) {
		try {
			int re = getSqlSession().delete("deleteData", num);
			if (re > 0)
				return true;
		} catch (Exception e) {
			System.out.println("deleteDB err : " + e);
			return false;
		}

		return false;
	}

	public int insert(BoardBean bean) {
		try {
			return getSqlSession().insert("insertData", bean);
		} catch (Exception e) {
			System.out.println("insert err : " + e);
			return 0;
		}
	}


	public List<Board> search(BoardBean bean) {
		return getSqlSession().selectList("selectSearch", bean);
	}

}
