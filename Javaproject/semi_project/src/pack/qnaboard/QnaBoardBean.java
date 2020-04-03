package pack.qnaboard;

import java.util.Calendar;

public class QnaBoardBean { // 폼빈 (Form Bean)
	private String qna_title, qna_cont, qna_bdate, page_first, page_last;
	private int qna_no, qna_readcnt, qna_gnum, qna_onum, qna_nested;
	private String qna_sword, qna_stype;
	
	public String getQna_sword() {
		return qna_sword;
	}

	public void setQna_sword(String qna_sword) {
		this.qna_sword = qna_sword;
	}

	public String getQna_stype() {
		return qna_stype;
	}

	public void setQna_stype(String qna_stype) {
		this.qna_stype = qna_stype;
	}

	public String getPage_first() {
		return page_first;
	}

	public void setPage_first(String page_first) {
		this.page_first = page_first;
	}

	public String getPage_last() {
		return page_last;
	}

	public void setPage_last(String page_last) {
		this.page_last = page_last;
	}

	public String getQna_title() {
		return qna_title;
	}

	public void setQna_title(String qna_title) {
		this.qna_title = qna_title;
	}

	public String getQna_cont() {
		return qna_cont;
	}

	public void setQna_cont(String qna_cont) {
		this.qna_cont = qna_cont;
	}

	public String getQna_bdate() {
		return qna_bdate;
	}

	public void setQna_bdate(String qna_bdate) {
		this.qna_bdate = qna_bdate;
	}

	public int getQna_no() {
		return qna_no;
	}

	public void setQna_no(int qna_no) {
		this.qna_no = qna_no;
	}

	public int getQna_readcnt() {
		return qna_readcnt;
	}

	public void setQna_readcnt(int qna_readcnt) {
		this.qna_readcnt = qna_readcnt;
	}

	public int getQna_gnum() {
		return qna_gnum;
	}

	public void setQna_gnum(int qna_gnum) {
		this.qna_gnum = qna_gnum;
	}

	public int getQna_onum() {
		return qna_onum;
	}

	public void setQna_onum(int qna_onum) {
		this.qna_onum = qna_onum;
	}

	public int getQna_nested() {
		return qna_nested;
	}

	public void setQna_nested(int qna_nested) {
		this.qna_nested = qna_nested;
	}

	public void setQna_bdate() {
		Calendar calendar = Calendar.getInstance();
		int year = calendar.get(Calendar.YEAR);
		int month = calendar.get(Calendar.MONTH) + 1;
		int day = calendar.get(Calendar.DATE);
		this.qna_bdate = year + "-" + month + "-" + day;
	}

}
