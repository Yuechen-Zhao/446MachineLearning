import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class HW1main {
	public static final int AGE_LOWER = 0;
	public static final int AGE_UPPER = 100;
	public static final int SAL_LOWER = 0;
	public static final int SAL_UPPER = 120000;
	
	public static void main(String[] args) throws FileNotFoundException {
		File f = new File("/Users/Della/Downloads/Folx/University/421/446hw1/src/problem1.txt");
		Scanner input = new Scanner(f);
		
		int[] age = new int[10];
		int[] sal = new int[10];
		boolean[] college = new boolean[10];
		
		for (int i = 0; i < 10; i++) { // initialize tree arrays
			age[i] = input.nextInt();
			sal[i] = input.nextInt();
			if (input.nextInt() == 1) {
				college[i] = true;
			} else {
				college[i] = false;
			}
		}
		
		int maxIGthreshold = -1;
		double maxIG = 0;
		double maxYesLeft = -1.0;
		double maxNoLeft = -1.0;
		double maxYesRight = -1.0;
		double maxNoRight = -1.0;
		
		for (int i = 0; i < 10; i++) { // pick one threshold
			int threshold = age[i];
			if (threshold <= AGE_LOWER || threshold > AGE_UPPER) {
				continue;
			}
			double yesleft = 0.0;
			double noleft = 0;
			double yesright = 0.0;
			double noright = 0.0;
			double yes = 0;
			double no = 0;
			
			for (int j = 0; j < 10; j++) { // iterate through list, calculate IG (by age)
				if (age[j] <= AGE_LOWER || age[j] > AGE_UPPER) {
					continue;
				}
				if (age[j] <= threshold) {
					if (college[j]) {
						yesleft++;
						yes++;
					} else {
						noleft++;
						no++;
					}
				} else {
					if (college[j]) {
						yesright++;
						yes++;
					} else {
						noright++;
						no++;
					}
				}
			}
			
			if (yes + no > 0 && yesleft + noleft > 0 && yesright + noright > 0) {
			
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
				
				if (hyxneg - hyneg > maxIG) {
					maxIG = hyxneg - hyneg;
					maxIGthreshold = threshold;
					maxYesLeft = yesleft;
					maxNoLeft = noleft;
					maxYesRight = yesright;
					maxNoRight = noright;
				}
			}
		}
		
		for (int i = 0; i < 10; i++) { // pick one threshold
			int threshold = sal[i];
			if (threshold <= SAL_LOWER || threshold > SAL_UPPER) {
				continue;
			}
			double yesleft = 0.0;
			double noleft = 0;
			double yesright = 0.0;
			double noright = 0.0;
			double yes = 0;
			double no = 0;
			
			for (int j = 0; j < 10; j++) { // iterate through list, calculate IG (by salary)
				if (sal[j] <= SAL_LOWER || sal[j] > SAL_UPPER) {
					continue;
				}
				if (sal[j] <= threshold) {
					if (college[j]) {
						yesleft++;
						yes++;
					} else {
						noleft++;
						no++;
					}
				} else {
					if (college[j]) {
						yesright++;
						yes++;
					} else {
						noright++;
						no++;
					}
				}
			}
			
			if (yes + no > 0 && yesleft + noleft > 0 && yesright + noright > 0) {
				
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
				if (hyxneg - hyneg > maxIG) {
					maxIG = hyxneg - hyneg;
					maxIGthreshold = threshold;
					maxYesLeft = yesleft;
					maxNoLeft = noleft;
					maxYesRight = yesright;
					maxNoRight = noright;
				}
			}
		}
		System.out.println("LEFT YES = " + maxYesLeft + " LEFT NO = " + maxNoLeft);
		System.out.println("RIGHT YES = " + maxYesRight + " RIGHT NO = " + maxNoRight);
		System.out.println("Max threashold is " + maxIGthreshold + ". MaxIG is " + maxIG);
	}
}
