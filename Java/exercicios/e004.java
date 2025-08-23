/**
 * Exercício: 004: Promoção automática de tipos
 * Objetivo: Criar um programa Java que demonstre a promoção automática de tipos em expressões.
 */

public class e004 {
	public static void main (String[] args){
		// variaveis
		byte a = 10;
		short b = 20;
		char c = 'A';
		int d = 30;
		long e = 40L;
		float f = 1.5f;
		double g = 2.5;

		// Exemplo de promoção automática: byte e short promovidos
		int resultado = a + b;
		System.out.println("Resultado da soma: " + resultado);

		// Mais exemplos com outros tipos
		long resultadoLong = d + e; // int promovido para long
		float resultadoFloat = d * f; // int promovido para float
		double resultadoDouble = d * g; // int promovido para double

		System.out.println("Resultado long: " + resultadoLong);
		System.out.println("Resultado float: " + resultadoFloat);
		System.out.println("Resultado double: " + resultadoDouble);
		
		// Exibindo o valor do char (conteúdo)
		System.out.println("Valor do char: " + c);
	}
}