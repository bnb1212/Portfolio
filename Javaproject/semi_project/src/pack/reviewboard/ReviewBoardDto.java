package pack.reviewboard;

public class ReviewBoardDto { // 폼빈 (Form Bean)
	private String review_title, review_cont, review_bdate;
	private int review_no, review_readcnt, review_gnum, review_onum, review_nested;
	private String review_sword, review_stype;
	
	public String getReview_sword() {
		return review_sword;
	}

	public void setReview_sword(String review_sword) {
		this.review_sword = review_sword;
	}

	public String getReview_stype() {
		return review_stype;
	}

	public void setReview_stype(String review_stype) {
		this.review_stype = review_stype;
	}

	public String getReview_title() {
		return review_title;
	}

	public void setReview_title(String review_title) {
		this.review_title = review_title;
	}

	public String getReview_cont() {
		return review_cont;
	}

	public void setReview_cont(String review_cont) {
		this.review_cont = review_cont;
	}

	public String getReview_bdate() {
		return review_bdate;
	}

	public void setReview_bdate(String review_bdate) {
		this.review_bdate = review_bdate;
	}

	public int getReview_no() {
		return review_no;
	}

	public void setReview_no(int review_no) {
		this.review_no = review_no;
	}

	public int getReview_readcnt() {
		return review_readcnt;
	}

	public void setReview_readcnt(int review_readcnt) {
		this.review_readcnt = review_readcnt;
	}

	public int getReview_gnum() {
		return review_gnum;
	}

	public void setReview_gnum(int review_gnum) {
		this.review_gnum = review_gnum;
	}

	public int getReview_onum() {
		return review_onum;
	}

	public void setReview_onum(int review_onum) {
		this.review_onum = review_onum;
	}

	public int getReview_nested() {
		return review_nested;
	}

	public void setReview_nested(int review_nested) {
		this.review_nested = review_nested;
	}

}
