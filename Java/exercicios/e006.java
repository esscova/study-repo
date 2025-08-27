
/**
 * 	EXERCICIO: Operadores de atribuição
 * 	OBJETIVO: Use diferentes operadores de atribuição para manipular o valor de uma variável inteira.
 */

public class e006 {
	public static void main (String[] args){
		// variavel
		int numero = 5;

		// processamento
		numero += 3; // 5 + 3  = 8
		numero -= 2; // 8 - 2  = 6
		numero *= 4; // 6 x 4  = 24
		numero /= 2; // 24 / 2 = 12
		numero %= 5; // 12 / 5 = 2

		// escrita de dados
		System.out.println("VALOR ATUAL: " + numero);
	}
}