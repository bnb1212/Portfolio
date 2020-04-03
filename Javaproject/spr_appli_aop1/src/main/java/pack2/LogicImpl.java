package pack2;

public class LogicImpl implements LogicInter {
	private ArticleInter articleInter;
	
	public LogicImpl() {
		// TODO Auto-generated constructor stub
	}
	
	public LogicImpl(ArticleInter articleInter) {
		this.articleInter = articleInter;
	}
	public void selectDataProcess() {
		articleInter.selectAll();

	}

	public void updateDataPart() {
		System.out.println("updateDataPart 수행");

	}
	
	
}
