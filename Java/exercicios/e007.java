/**
 * 	EXERCÍCIO: Incremento e decremento
 * 	OBJETIVO: Praticar o uso dos operadores de incremento (++) e decremento (--).
 */
public class e007 {
    public static void main(String[] args) {
        // variavel inicial
        int contador = 5;
        System.out.println("Valor inicial: " + contador);

        // pos incremento
        System.out.println("Após pós-incremento (contador++): " + contador++);
        System.out.println("Valor após pós-incremento: " + contador);

        // pre incremento
        System.out.println("Após pré-incremento (++contador): " + (++contador));

        // posdecremento
        System.out.println("Após pós-decremento (contador--): " + contador--);
        System.out.println("Valor após pós-decremento: " + contador);

        // pre decremento
        System.out.println("Após pré-decremento (--contador): " + (--contador));

        // resultado final
        System.out.println("Resultado final: " + contador);
    }
}
