import java.util.Arrays;
import static java.lang.Math.abs;

public class IterativeMethod { //Решение СЛАУ методом простых итераций
    public static boolean checkIfDiagonalPredominant(double[][] matrix) {
        int numOfEq = 0;
        for(int i = 0; i < matrix.length; i++) {
            float absRowSum = 0;
            for(int j = 0; j < matrix.length; j++) {
                absRowSum += abs(matrix[i][j]);
            }
            absRowSum -= abs(matrix[i][i]);
            if(abs(matrix[i][i]) < absRowSum) {
                return false;
            } else if(matrix[i][i] == absRowSum) {
                numOfEq++;
            }
        }
        if(numOfEq == matrix.length) return false;
        return true;
    }

    public static double[][] tryToConvertToDiagonalPredominant(double[][] matrix) {
        int size = matrix.length;
        double[][] newMatrix = new double[size][size+1];
        for(double[] eq : matrix) {
            System.out.println("newMatrix:");
            for(int i = 0; i<size; i++) {;
                System.out.println(Arrays.toString(newMatrix[i]));
            }
            double maxInRow = Arrays.stream(eq, 0, size).map(Math::abs).max().getAsDouble();
            int mxInd = 0;
            for(int i = 0; i < size; i++) {
                if(abs(eq[i]) == maxInRow) {
                    mxInd = i;
                    break;
                }
            }
            if(!Arrays.equals(newMatrix[mxInd], new double[size + 1])) {
                System.out.println("1");
                return null;
            }
            newMatrix[mxInd] = eq;
        }
        if(checkIfDiagonalPredominant(newMatrix)) {
            return newMatrix;
        }
        return null;
    }

    static double compose(double[] M, double[] v) {
        double result = 0;
        for(int i = 0; i < M.length-1; i++) {
            result += M[i]*v[i];
        }
        return result;
    }

    public static void doIterations(double[][] matrix, double eps) {
        int size = matrix.length;
        int iterations = 0;
        double[] difference = new double[size];
        double[] xNext = new double[size];
        double[] x = new double[size];

        for(int i = 0; i < size; i++) {
            x[i] = matrix[i][size];
        }
        while(iterations == 0 || Arrays.stream(difference).map(Math::abs).max().getAsDouble() > eps) {
            for(int i = 0; i < size; i++) {
                xNext[i] = compose(matrix[i], x) + matrix[i][size];
            }
            iterations++;
            for(int i = 0; i < size; i++) {
                difference[i] = xNext[i] - x[i];
            }
            x = xNext.clone();
        }
        System.out.println("Решение СЛАУ (x1...xn):");
        System.out.println(Arrays.toString(xNext) + "\n");
        System.out.println("Решение было найдено за " + iterations + " итераций.\n");
        System.out.println("Вектор погрешностей: ");
        System.out.println(Arrays.toString(difference));
        return;
    }

    public static double[][] transformMatrixFromABToCD(double[][] matrix) {
        int size = matrix.length;
        double[][] newMatrix = new double[size][size+1];
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size + 1; j++) {
                newMatrix[i][j] = j == size ? matrix[i][j]/matrix[i][i] : (i == j ? 0 : -(matrix[i][j]/matrix[i][i]));
            }
        }
        return newMatrix;
    }
    public static void printMtx(double[][] a)
    {
        int size = a.length;
        for (double[] doubles : a) {
            for (int j = 0; j < size + 1; j++) {
                System.out.printf("%.2f\t", doubles[j]);
            }
            System.out.println();
        }
        System.out.println();
    }
}