package pack.reviewboard;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;


public interface SqlMapperInter4 {
	
	@Select("select * from reviewboard order by review_gnum desc, review_onum asc")
	public List<ReviewBoardDto> selectDataAll1(int page, String stype, String sword);	//annotation과 세트

	@Select("select * from reviewboard where review_title like '%다이어트%' order by review_gnum desc, review_onum asc")
	public List<ReviewBoardDto> selectDataAll2(int page, String stype, String sword);	//annotation과 세트
	
	@Select("select max(review_no) from reviewboard")
	public int currentGetNum();	//annotation과 세트
	
	@Select("select * from reviewboard where review_no = #{review_no}")
	public ReviewBoardDto getData(String review_no); 
	
	@Select("select count(*) from reviewboard")
	public String totalList();
	
	@Select("select * from reviewboard where review_no = #{review_no}")
	public ReviewBoardDto getReplyData(String no);
	
	@Insert("insert into reviewboard values(#{review_no},#{review_title},#{review_cont},now(),0,#{review_gnum},0,0)")
	public int saveData(ReviewBoardBean bean);

	@Insert("insert into reviewboard values(#{review_no},#{review_title},#{review_cont},now(),0,#{review_gnum},#{review_onum},#{review_nested})")
	public void saveReplyData(ReviewBoardBean bean);
	
	@Update("update reviewboard set review_title=#{review_title},review_cont=#{review_cont} where review_no=#{review_no}")
	public int updataData(ReviewBoardBean bean);
	
	@Update("update reviewboard set review_readcnt = review_readcnt + 1 where review_no=#{review_no}")
	public void updateReadcnt(String no);
	
	@Update("update reviewboard set review_title=#{review_title},review_cont=#{review_cont} where review_no=#{review_no}")
	public int editSave(ReviewBoardBean bean);
	
	@Update("update reviewboard set review_onum = review_onum+1 where review_onum >= #{review_onum} and review_gnum = #{review_gnum}")
	public void updateOnum(int onum, int gnum);
	
	@Delete("delete from reviewboard where review_no=#{review_no}")
	public int deleteData(int no);

}
