/**
 * Exercício: 003: Calculo da area de um retangulo
 * Objetivo: Criar um programa que calcule a área de um retangulo com base em sua altura e largura.
 */

public class e003 {
	public static void main (String[] args){
		// variaveis
		double largura = 5.0, altura = 3.0, area;

		// processamento
		area = largura * altura;

		System.out.println("=== CALCULADORA DE ÁŔEA DE RETÂNGULO ===");
		System.out.printf("LARGURA: %f \n", largura);
		System.out.printf("ALTURA: %f \n", altura);
		System.out.printf("RESULTADO: %f \n ===== FIM ===== \n", area);
	}
}