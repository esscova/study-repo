/**
 * EXERCICIO: Verificacao de numero par
 * OBJETIVO: O programa deve receber um número inteiro fixo (por exemplo, 10). 
 * 			 Dependendo do resultado da verificação, o programa exibirá a mensagem apropriada: "O número é par" ou "O número é ímpar".
 *
 */

public class e008 {
	public static void main (String[] args){
		// variaveis
		int num = 10;
		String res;
		
		// processamento
		res = (10 % 2 == 0) ? "Par" : "Ímpar";

		// escrita
		System.out.println(res + "\n");

	}
}