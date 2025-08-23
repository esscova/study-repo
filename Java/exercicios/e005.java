/**
* Enunciado: Calculadora simples
* Objetivo: Criar um programa Java que realiza operações aritméticas básicas usando os operadores.
*/

public class e005 {
	public static void main (String[] args){

		// variaveis
		int a=10, b=2;
		int soma, subtracao, produto, resto;
		float razao;

		// processamento
		soma = a+b;
		subtracao = a-b;
		produto = a*b;
		razao = (float)a/(float)b;
		resto = a%b;

		// escrita
		System.out.println("Resultados:");
		System.out.println("Soma: " + soma);
		System.out.println("subtração: " + subtracao);
		System.out.println("Multiplicação: " + produto );
		System.out.println("Divisão: " + razao);
		System.out.println("Resto da Divisão: " + resto);

		//fim

	}
}