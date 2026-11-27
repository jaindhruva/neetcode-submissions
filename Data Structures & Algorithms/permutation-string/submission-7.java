class Solution {
    public boolean isAnagram(String s1, String s2){
        if(s1.length() != s2.length())
            return false;
        HashMap<Character,Integer> countMap = new HashMap<>();
        for(char c: s1.toCharArray()){
            countMap.put(c, countMap.getOrDefault(c,0)+1);
        }

        for(char c: s2.toCharArray()){
            if(countMap.get(c)==null)
                return false;
            countMap.put(c,countMap.get(c)-1);
            if(countMap.get(c)==0)
                countMap.remove(c);
        }
        return true;
    }

    public boolean checkInclusion(String s1, String s2) {

        int l=0,r=s1.length();
        while(r<=s2.length()){
            if(isAnagram(s1,new String(s2.substring(l,r))))
                return true;
            l++;
            r++;
        }
        return false;
    }
}
