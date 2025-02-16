/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
 
    public void result(StringBuilder res,TreeNode root)
    {
      if(root==null)
      {
      res.append("N.");
      return;  
      }
      res.append(Integer.toString(root.val)+".");
      result(res,root.left);
      result(res,root.right);
    }
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) 
    {
        StringBuilder res=new StringBuilder("");
        result(res,root);
        res.deleteCharAt(res.length()-1);
        return res.toString();
    }
    public TreeNode construct(String arr[],int s[])
    {
       if(arr[s[0]].equals("N"))
       {
       return null;
       }
       TreeNode node =new TreeNode(Integer.parseInt(arr[s[0]]));
       ++s[0];
       node.left=construct(arr,s);
       s[0]++;
       node.right= construct (arr,s);
       return node;
    }
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) 
    {
        if(data.length()==0)
        return null;
        String arr[]=data.split("\\.");
        int idx[]=new int[1];
       // System.out.println(Arrays.toString(arr));
        return construct(arr,idx);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));