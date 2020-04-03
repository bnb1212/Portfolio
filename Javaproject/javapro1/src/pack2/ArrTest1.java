package pack2;

public class ArrTest1 {

	public static void main(String[] args) {
		// 배열 : 성격과 크기가 일치하는 여러 개의 기억장소에 대해 대표명을 주고 첨자로 각 기억장소를 구분
		// 반복처리가 효과적
		// int[] arr;
//		int arr[]; // 정수형 기억장소 arr을 잡을거야
//		arr = new int[5]; // 배열 기억장소 5칸 확보
//		
//		System.out.println("ar의 크기 : " + arr.length);

		int arr[] = new int[5];
		System.out.println("ar의 크기 : " + arr.length);
		arr[0] = 10;
		arr[1] = 20;
		arr[4] = arr[0] + arr[1]; // 열첨자(index)로 기억장소를 구분
		System.out.println("arr[4] : " + arr[4]); // 배열은 one two three가 아니고 first second third
		System.out.println("arr[3] : " + arr[3]);
//		System.out.println("arr[5] : " + arr[5]); ArrayIndexOutOfBoundsException
		int a = 4, b = 4;
		System.out.println(arr[4] + " " + arr[a] + " " + arr[b] + " " + arr[1 + 3]);
		// index는 상수를 써도 괜찮

		System.out.println();
		int[] ar1 = { 1, 2, 3, 4, 5 }; // 배열 선언 및 초기값 기억
//		System.out.println(ar1[0]);
		for (int i = 0; i < ar1.length; i++) {
			System.out.print(ar1[i] + " ");
		}
		System.out.println();
		for (int no : ar1) { // 향상된 for문 : 객체 자료를 출력시 사용 가능
			System.out.print(no + " ");
		}
		System.out.println();
		String[] city = { "서울", "인천", "수원", "안산", "성남" };
//		System.out.println(city[0]);
		for (String c : city) {
			System.out.println("도시명 : " + c);
		}

		int[] ar2 = new int[5];
		for (int i = 0; i < ar2.length; i++) {
			ar2[i] = i + 1;
		}
		System.out.println("--------------------------------");
		int tot = 0;
		for (int i = 0; i < ar2.length; i++) {
			System.out.println("ar[i] : " + ar2[i]);
			tot += i;
		}
		System.out.println("\ntot :" + tot);

		System.out.println("\n******다차원 배열****** ");
		int su[][] = new int[3][4];
		System.out.println(su.length + " " + su[0].length);
		su[0][0] = 100;
//		System.out.println(su[0][0]);
		int num = 10;
		for (int i = 0; i < su.length; i++) {
			for (int j = 0; j < su[i].length; j++) {
//				System.out.println("i : " + i + ", j:" + j);
				su[i][j] = num++;
			}
		}
		System.out.println(su[0][0]);
		for (int m = 0; m < 3; m++) {
			for (int n = 0; n < 4; n++) {
				System.out.println(su[m][n] + " ");
			}
			System.out.println();
		}
		
		System.out.println("\n가변배열");
		int[][] scores = new int[2][];
		scores[0] = new int[2];
		scores[1] = new int[3];
		System.out.println(scores.length + " " + scores[0].length + " " + scores[1].length + " " );
		
		System.out.println();
		int[][] jum = {{90, 96}, {89, 87, 85}};
		for(int i = 0 ; i < jum.length; i++) {
			for (int j = 0; j < jum.length; j++) {
				System.out.println(jum[i][j] + " ");
			}
			System.out.println();
		}
	}

}
