/**
 * OBJETIVO: Praticar controle de fluxo com operadores logicos
 * DESCRICAO: Implemente um programa que utilize operadores lógicos para determinar se um aluno foi aprovado ou não.
 **/

public class e013{
	public static void main (String[] args){
		// variaveis
		double nota1=5, nota2=4, media;
		String resultado;

		// processamento
		media = (nota1+nota2)/2;
		resultado = (media>=6) ? "Aprovado." : "Reprovado.";
		

		// escrita
		System.out.printf("Média: %.2f. O aluno foi %s\n", media, resultado);
	}
}