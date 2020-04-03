package pack.qnaboard;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

public interface SqlMapperInter3 {
	
	//paging 처리 하다가 실패함. 나중에 보충하자
	//@Select("select * from qnaboard order by qna_no desc limit #{page_first},#{page_last}")
	//public List<QnaBoardDto> selectDataAll(int page, QnaBoardBean bean);	//annotation과 세트
	
	@Select("select * from qnaboard order by qna_gnum desc, qna_onum asc")
	public List<QnaBoardDto> selectDataAll1(int page, String stype, String sword);	//annotation과 세트

	@Select("select * from qnaboard where qna_title like '%질문%' order by qna_no desc, qna_onum asc")
	public List<QnaBoardDto> selectDataAll2(int page, String stype, String sword);	//annotation과 세트
	
	@Select("select max(qna_no) from qnaboard")
	public int currentGetNum();	//annotation과 세트
	
	@Select("select * from qnaboard where qna_no = #{qna_no}")
	public QnaBoardDto getData(String qna_no); 
	
	@Select("select count(*) from qnaboard")
	public String totalList();
	
	@Select("select * from qnaboard where qna_no = #{qna_no}")
	public QnaBoardDto getReplyData(String no);
	
	@Insert("insert into qnaboard values(#{qna_no},#{qna_title},#{qna_cont},now(),0,#{qna_gnum},0,0)")
	public int saveData(QnaBoardBean bean);

	@Insert("insert into qnaboard values(#{qna_no},#{qna_title},#{qna_cont},now(),0,#{qna_gnum},#{qna_onum},#{qna_nested})")
	public void saveReplyData(QnaBoardBean bean);
	
	@Update("update qnaboard set qna_title=#{qna_title},qna_cont=#{qna_cont} where qna_no=#{qna_no}")
	public int updataData(QnaBoardBean bean);
	
	@Update("update qnaboard set qna_readcnt = qna_readcnt + 1 where qna_no=#{qna_no}")
	public void updateReadcnt(String no);
	
	@Update("update qnaboard set qna_title=#{qna_title},qna_cont=#{qna_cont} where qna_no=#{qna_no}")
	public int editSave(QnaBoardBean bean);
	
	@Update("update qnaboard set qna_onum = qna_onum+1 where qna_onum >= #{qna_onum} and qna_gnum = #{qna_gnum}")
	public void updateOnum(int onum, int gnum);
	
	@Delete("delete from qnaboard where qna_no=#{qna_no}")
	public int deleteData(int no);

	/*
	@Select("select id,name,passwd,reg_date from membertab where id=#{id}")
	public QnaBoardDto selectDataPart(String id);
	
	
	
	*/
}
