package pack.reviewboard;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import pack.mybatis.SqlMapConfig;

public class ReviewBoardProcess {

	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();

	private int tot; // 전체 레코드 수
	private int pList = 5; // 페이지 당 출력 행 수 5개
	private int pageSu; // 전체 페이지 수
	
	// 전체 출력
	//public List<ReviewBoardDto> selectDataAll(int page, ReviewBoardBean bean) {
	public List<ReviewBoardDto> selectDataAll(int page, String stype, String sword) {
		SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
		List<ReviewBoardDto> list = null;
		try {
			SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
			if(sword == null) {	//검색x
				list = inter.selectDataAll1(page, stype, sword);	
			}else {	//검색O
				list = inter.selectDataAll2(page, stype, sword);	
			}
			/*
			for (int i = 0; i < (page -1)*pList; i++) {
				// 레코드 포인터 위치 이동 - 0번째 위치.~5번 수행 (처음은 page가 0이라 수행 안함.)
				// 레코드 포인터 위치 이동 - 4번째 위치. 5번부터 시작함.
				// 레코드 포인터 위치 이동 - 9번째 위치. 10번부터 시작.
			}
			*/

		} catch (Exception e) {
			System.out.println("selectDataAll err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return list;
	}

	// 게시글 최고번호 계산
	public int currentGetNum() {
		SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
		ReviewBoardDto dto = new ReviewBoardDto();
		int cnt = 0;
		try {
			SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
			// dto = inter.currentGetNum();
			cnt = inter.currentGetNum();
		} catch (Exception e) {
			System.out.println("currentGetNum err : " + e);
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return cnt;
	}

	// 게시글 추가
	public boolean saveData(ReviewBoardBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
		try {
			SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
			if (inter.saveData(bean) > 0)
				b = true;
			sqlSession.commit(); // 수동 commit();

		} catch (Exception e) {
			System.out.println("saveData err : " + e);
			sqlSession.rollback(); // 수동 rollback();
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return b;
	}

	// 게시판 업데이트
	public boolean updateData(ReviewBoardBean bean) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
		try {
			SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
			/*
			 * // 비밀번호 비교 후 수정여부 판단 ReviewBoardDto dto = inter.selectDataPart(bean.getId()); //
			 * 아이디로 검색해 회원 정보 호출 // 데이터베이스에 들어가 있는 dto 회원 비밀번호와 입력한 bean 비밀번호가 같으면 작업한다. if
			 * (dto.getPasswd().equalsIgnoreCase(bean.getPasswd())) { if
			 * (inter.updataData(bean) > 0) { b = true; sqlSession.commit(); }
			 */
			if (inter.updataData(bean) > 0)
				b = true;
			sqlSession.commit();

		} catch (Exception e) {
			System.out.println("updateData err : " + e);
			sqlSession.rollback();
		} finally {
			if (sqlSession != null)
				sqlSession.close();
		}
		return b;
	}

	// 게시글 삭제
	public boolean deleteData(int no) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
		try {
			SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
			int cou = inter.deleteData(no);
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
	
	//조회수 체크
		public void updateReadcnt(String no) { // 글 내용 보기 전에 조회수 증가 
			SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
			try {
				SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
				inter.updateReadcnt(no);
				sqlSession.commit();
			} catch (Exception e) {
				System.out.println("updateReadcnt err : " + e);
				sqlSession.rollback();
			}finally {
				if (sqlSession != null)
					sqlSession.close();
			}
		}
		
		//상세 게시글 보기
		public ReviewBoardDto getData(String qna_no) {
			SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
			ReviewBoardDto dto = null;
			try {
				SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
				dto = inter.getData(qna_no);
			} catch (Exception e) {
				System.out.println("getData err : " + e);
			}finally {
				if (sqlSession != null)
					sqlSession.close();
			}
			return dto;
		}
		
		public void totalList() {
			SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
			try {
				SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
				tot = Integer.parseInt(inter.totalList()); //전체 건수(전체 레코드의 개수)
				//System.out.println(tot);
			} catch (Exception e) {
				System.out.println("totalList err : " + e);
			}finally {
				if (sqlSession != null)
					sqlSession.close();
			}
		}
		
		//pageSu 계산 
		public int getPageSu() {
			pageSu = tot/pList; //정수나누기. 몫만 취함.
			//나머지가 있으면 페이지수를 하나 늘린다.
			if(tot % pList > 0) pageSu++;
			//System.out.println(pageSu);
			return pageSu;	
		}
		
		// 게시판 업데이트
		public boolean editSave(ReviewBoardBean bean) {
			boolean b = false;
			SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
			ReviewBoardDto dto = null;
			try {
				//System.out.println(bean.getQna_no() + " " + bean.getQna_title());
				SqlMapperInter4 inter = (SqlMapperInter4)sqlSession.getMapper(SqlMapperInter4.class);
					if (inter.editSave(bean) > 0) {
						b = true;
						sqlSession.commit();
				}
			} catch (Exception e) {
				System.out.println("editSave err : " + e);
				sqlSession.rollback();
			} finally {
				if (sqlSession != null)
					sqlSession.close();
			}
			return b;
		}
		
		//댓글 보기
		public ReviewBoardDto getReplyData(String no) {	
			SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
			ReviewBoardDto dto = null;
			try {
				SqlMapperInter4 inter = (SqlMapperInter4)sqlSession.getMapper(SqlMapperInter4.class);
				dto = inter.getReplyData(no);
			} catch (Exception e) {
				System.out.println("getReplyData err : " + e);
			}finally {
				if (sqlSession != null)
					sqlSession.close();
			}
			return dto;
		}
		
		//댓글 onum 갱신
		public void updateOnum(int onum, int gnum) { 
			SqlSession sqlSession = factory.openSession(); // 작업 처리를 위한 선언. 문을 연다.
			try {
				SqlMapperInter4 inter = (SqlMapperInter4)sqlSession.getMapper(SqlMapperInter4.class);
				inter.updateOnum(onum, gnum);
				sqlSession.commit();
			} catch (Exception e) {
				System.out.println("updateOnum err : " + e);
				sqlSession.rollback();
			}finally {
				if (sqlSession != null)
					sqlSession.close();
			}
		}
		
		//댓글 저장
		public void saveReplyData(ReviewBoardBean bean) {
			SqlSession sqlSession = factory.openSession();
			try {
				SqlMapperInter4 inter = (SqlMapperInter4) sqlSession.getMapper(SqlMapperInter4.class);
				inter.saveReplyData(bean);
				sqlSession.commit();
			} catch (Exception e) {
				System.out.println("saveReplyData err : " + e);
				sqlSession.rollback();
			} finally {
				if (sqlSession != null)
					sqlSession.close();
			}
		}
}
