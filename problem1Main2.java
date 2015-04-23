import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class HW1main2 {
	public static void main(String[] args) throws FileNotFoundException {
		File f = new File("/Users/Della/Downloads/Folx/University/421/446hw1/src/problem1.txt");
		Scanner input = new Scanner(f);
		
		int[] age = new int[10];
		int[] sal = new int[10];
		boolean[] college = new boolean[10];
		double[] sign = new double[10];
		
		for (int i = 0; i < 10; i++) { // initialize three arrays
			age[i] = input.nextInt();
			sal[i] = input.nextInt();
			if (input.nextInt() == 1) {
				college[i] = true;
			} else {
				college[i] = false;
			}
		}
		
		for (int i = 0; i < 10; i++) { // iterate, and initialize the signs
			sign[i] = -1.0 / 10.0 * age[i] + sal[i] / 10000.0 - 1.0;
		}
		
		double yesleft = 0.0;
		double noleft = 0;
		double yesright = 0.0;
		double noright = 0.0;
		double yes = 0;
		double no = 0;
		for (int i = 0; i < 10; i++) { // iterate through, calculate yes/no
			if (sign[i] <= 0) {
				if (college[i]) {
					yesleft++;
					yes++;
				} else {
					noleft++;
					no++;
				}
			} else {
				if (college[i]) {
					yesright++;
					yes++;
				} else {
					noright++;
					no++;
				}
			}
		}
		
		double ig = -1.0;
		if (yes + no > 0 && yesleft + noleft > 0 && yesright + noright > 0) { // all greater than zero
			
			double yyn;
			double nyn;
			
			if (yes == 0) {
				yyn = 0;
			} else {
				yyn = Math.log10((double) yes / (yes + no)) / Math.log10(2.0);
			}
			
			if (no == 0) {
				nyn = 0;
			} else {
				nyn = Math.log10((double) no / (yes + no)) / Math.log10(2.0);
			}
			
			double yynl;
			double nynl;
			if (yesleft == 0) {
				yynl = 0;
			} else {
				yynl = Math.log10((double) yesleft / (yesleft + noleft)) / Math.log10(2.0);
			}
			if (noleft == 0) {
				nynl = 0;
			} else {
				nynl = Math.log10((double) noleft / (yesleft + noleft)) / Math.log10(2.0);
			}
			
			double yynr;
			double nynr;
			if (yesright == 0) {
				yynr = 0;
			} else {
				yynr = Math.log10((double) yesright / (yesright + noright)) / Math.log10(2.0);
			}
			if (noright == 0) {
				nynr = 0;
			} else {
				nynr = Math.log10((double) noright / (yesright + noright)) / Math.log10(2.0);
			}
			
			double hyneg = yes / (yes + no) * yyn + (no / (yes + no) * nyn);
			double hyxneg = ((yesleft + noleft) / (yes + no) * ((yesleft / (yesleft + noleft) * yynl)
					+ (noleft / (yesleft + noleft) * nynl)))
					+ ((yesright + noright) / (yes + no) * ((yesright / (yesright + noright) * yynr)
					+ (noright / (yesright + noright) * nynr)));
			ig = hyxneg - hyneg;
		}
		System.out.println("LEFT YES = " + yesleft + " LEFT NO = " + noleft);
		System.out.println("RIGHT YES = " + yesright + " RIGHT NO = " + noright);
		System.out.println("This information gain is : " + ig);
	}
}
