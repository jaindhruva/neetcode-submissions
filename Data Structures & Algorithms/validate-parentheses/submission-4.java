class Solution {
    public boolean isValid(String s) {
        Stack<Character> parStack = new Stack<>();
        for(char c : s.toCharArray()){
            if(parStack.size()==0 || c=='(' || c=='[' || c=='{'){
                parStack.add(c);
                continue;
            }
            if(c==')' && parStack.peek()!='(')
                return false;
            if(c==']' && parStack.peek()!='[')
                return false;
            if(c=='}' && parStack.peek()!='{')
                return false;
            parStack.pop();
        }
        if(parStack.size()==0)
            return true;
        else
            return false;
    }
}
