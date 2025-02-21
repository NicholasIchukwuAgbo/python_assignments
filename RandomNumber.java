import java.security.SecureRandom;

public class RandomNumber{

    public static void main(String[] args) {

    SecureRandom randomNummber = new SecureRandom();

    int frequency1 = 0;
    int frequency2 = 0;
    int frequency3 = 0;
    int frequency4 = 0;
    int frequency5 = 0;
    int frequency6 = 0;

    for(int roll = 1; roll <= 60000000; roll++){
    
    int face = 1 + randomNummber.nextInt();

    switch(face){

        case 1:
            ++frequency1;
            break;
        case 2:
            ++frequency2;
            break;
        case 3:
            ++frequency3;
            break;
        case 4:
            ++frequency4;
            break;
        case 5:
            ++frequency5;
            break;
        case 6:
            ++frequency6;
            break;
       }

      }
    System.out.println("Faces\tFrequency");
    System.out.printf("\t%d%n\t%d%n\t%d%n\t%d%n\t%d%n\t%d%n", frequency1, frequency2, frequency3, frequency4, frequency5, frequency6);
    }

}