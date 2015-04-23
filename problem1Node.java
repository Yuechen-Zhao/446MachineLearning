public class Node {
	int minage;
	int maxage;
	
	int minsal;
	int maxsal;
	
	int yes;
	int no;
	
	Node left;
	Node right;
	
	public Node(int minage, int maxage, int minsal, int maxsal, int yes, int no) {
		this.minage = minage;
		this.maxage = maxage;
		this.minsal = minsal;
		this.maxsal = maxsal;
		this.yes = yes;
		this.no = no;
		this.left = null;
		this.right = null;
	}
}
