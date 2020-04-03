package javapro4_normal;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JDesktopPane;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.WindowConstants;

// 2020-02-19
// SDI, MDI 실습

public class MdiSample extends JFrame implements ActionListener{
	
	JMenuItem mnuNew, mnuExit;
	JInternalFrame childWin;
	JDesktopPane desktopPane = new JDesktopPane();
	
	public MdiSample() {
		setTitle("Mdi Test");
		
		JMenuBar mbar = new JMenuBar();
		JMenu mnuFile = new JMenu("파일");
		mnuNew = new JMenuItem("새 창");
		mnuExit = new JMenuItem("종료");
		mnuFile.add(mnuNew);
		mnuFile.add(mnuExit);
		mbar.add(mnuFile);
		setJMenuBar(mbar);
		
		mnuNew.addActionListener(this);
		mnuExit.addActionListener(this);
		
		setBounds(300, 300, 400, 300);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getActionCommand().equals("새 창")) {
			getContentPane().add(desktopPane);
			createListen();
			desktopPane.add(childWin);
			childWin.setLocation(10,10);
			childWin.show();
		} else if(e.getActionCommand().equals("종료")) {
			System.exit(0);
		}
	}
	
	private void createListen() {
		childWin = new JInternalFrame("자식창", true, true, true, true);
		childWin.getContentPane().setLayout(new BorderLayout());
		childWin.setSize(300, 200);
		childWin.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
	}
	public static void main(String[] args) {
		new MdiSample();
	}

}
