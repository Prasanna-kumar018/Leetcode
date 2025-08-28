/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void traverse(TreeNode root,List<Integer> l,int i)
    {
       if(root==null)
       return ;
       if(i>l.size())
       {
         l.add(root.val);
       }
       traverse(root.right,l,i+1);
       traverse(root.left,l,i+1);
    }
    public List<Integer> rightSideView(TreeNode root) 
    {
        List<Integer> l=new ArrayList<>();
        traverse(root,l,1);
        return l; 
    }
}