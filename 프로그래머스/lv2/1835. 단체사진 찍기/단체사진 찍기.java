import java.util.*;

class Solution {
    public int solution(int n, String[] data) {
        int answer = 0;
        String friends = "ACFJMNRT";
        List<String> permutations = generatePermutation(friends);
        Queue<String> queue = new LinkedList<>();
        
        for (String p : permutations) {
            queue.add(p);
        }
        
        while (true) {
            String s = queue.peek();
            int count = 0;
            for (int i = 0; i < data.length; i++) {
                if (!validate(s, data[i])) {
                    break;
                }
                count++;
            }
            
            if (count == data.length) {
                answer++;
            }
            
            count = 0;
            queue.poll();
            if (queue.isEmpty()) {
                break;
            }
        }
        return answer;
    }
    
    public List<String> generatePermutation(String input) {
        List<String> result = new ArrayList<>();
        generatePermutationRecursive(input.toCharArray(), 0, result);
        return result;
    }
    
    private void generatePermutationRecursive(char[] arr, int index, List<String> result) {
        if (index == arr.length - 1) {
            result.add(new String(arr));
            return;
        }
        
        for (int i = index; i < arr.length; i++) {
            swap(arr, index, i);
            generatePermutationRecursive(arr, index + 1, result);
            swap(arr, index, i);
        }
    }
    
    private void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    private boolean validate(String friends, String data) {
        char operator = data.charAt(3);
        char target1 = data.charAt(0);
        char target2 = data.charAt(2);
        int interval = Character.getNumericValue(data.charAt(4));
        int abs = Math.abs(friends.indexOf(target1) - friends.indexOf(target2)) - 1;
        switch (operator) {
            case '=':
                if (abs == interval) return true;
                break;
            case '>':
                if (abs > interval) return true;
                break;
            case '<':
                if (abs < interval) return true;
                break;
        }
        return false;
    }
}