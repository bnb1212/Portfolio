package pack2;

public class LogicImpl implements LogicInter{	//핵심 로직
	private ArticleInter articleInter;
	
	public LogicImpl() {
		
	}

	public LogicImpl(ArticleInter articleInter) {	//생성자 주입
		this.articleInter = articleInter;
	}
	
	public void selectDataProcess() {
		articleInter.selectAll();
	}
	
	public void updateDataPart() {
		System.out.println("updateDataPart 수행");
	}
	
	public void abc() {	//고유 메소드
		System.out.println("abc 수행");
	}
}
