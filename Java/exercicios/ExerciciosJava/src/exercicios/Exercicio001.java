

package exercicios;

import java.util.Locale;
import java.util.Scanner;


public class Exercicio001 {
    public static void executar() {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US);
        
        // declaracoes
        int A, B, soma;
        
        // leitura de dados
        A = sc.nextInt();
        B = sc.nextInt();
        
        // processamento
        soma = A + B;
        
        // escrita
        System.out.println("SOMA = " + soma);
        
        // fechamento
        sc.close();
    }
    
}
