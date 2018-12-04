public class Beer {
    private static int bityn(String[] beers) {
        int n = beers.length, m = beers[0].length();
        int[] beer = new int[n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                beer[i] = beer[i] << 1;
                beer[i] += (beers[i].charAt(j) == 'Y') ? 1 : 0;
            }
        int min = Integer.MAX_VALUE;
        loop: for (int i = 1; i < (1 << m); i++) {
            for (int j = 0; j < n; j++)
                if ((i & beer[j]) == 0)
                    continue loop;
            min = Math.min(Integer.bitCount(i), min);
        }
        return min;
    }

    public static void main(String[] args) {
        String[] beers = new String[]{"YNY", "NYY", "NYY", "YNY", "YNY"};
        System.out.println(bityn(beers));
    }
}