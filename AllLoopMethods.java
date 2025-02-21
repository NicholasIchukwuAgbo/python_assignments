public class AllLoopMethods{

	public static main(String[] args){

	int[] array = {2, 4, 7, 2};

	System.out.println("sum using for-loop is: " + sum(array));

     }
public static fooLoop(int[] array){

	int sum = 0;

	for(int total : array){

	sum += total;
     }
  return sum;
  }



 }