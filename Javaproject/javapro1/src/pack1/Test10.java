package pack1;

public class Test10 {

	public static void main(String[] args) {
		// 다중 for, etc
		for (int m = 1; m < 4; m++) {
			System.out.println("m: " + m);
			for (int n = 1; n <= 4; n++) {
				System.out.print("n = " + n + " ");
				if (n == 4) {
					System.out.println();
					System.out.println("-----------------");
				}
			}
		}
		System.out.println();
		for (char i = 65; i <= 90; i++) {
			System.out.print(i + " : ");
			for (char j = i; j <= 'Z'; j++) {
				System.out.print(j);
			}
			System.out.println();
		}

		System.out.println();

		// continue, break

		for (int aa = -1 + 2; aa <= 10; aa++) {
			if (aa == 3)
				continue; // 3일때 다음 반복으로 속행
			System.out.println(aa);
			// if(aa == 5) System.exit(0);
			// if (aa == 5) return;
			if(aa == 5) break;
			System.out.println("nice!");
		}

		System.out.println("--------------------");
		int kk = 0;
		for(;;) { // 이렇게 for문으로도 무한루핑을 할 수 있지만 바람직하지 않다.
			kk++;
			System.out.println("출력");
			if(kk ==5) break;
		}
		
		System.out.println("label이 있는 경우"); // 사용은 가능하지만 프로그래밍의 가독성을 떨어뜨리므로 권장하지 않음
		
		kbs:for(int i = 1; i <= 3; i++) {
			mbc:for(int j = 1; j <= 5; j++) {
				System.out.print(i + " " + j + " ");
				if(j == 3) continue kbs;
				if(j == 3) break kbs;
			}
		System.out.println("********************");
		}
		System.out.println("프로그램 종료");
	}

}
