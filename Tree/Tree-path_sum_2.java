package Tree;
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

import java.util.*;
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> arr = new ArrayList<>();
        dfs(root, 0, res, arr, targetSum);
        return res;
    }
    public void dfs(TreeNode root, int curSum, List<List<Integer>> res, List<Integer> arr, int targetSum){
        if(root == null){
            return;
        }
        curSum += root.val;
        arr.add(root.val);
        if(root.left == null && root.right == null && curSum == targetSum){
            res.add(new ArrayList<>(arr));
        }
        dfs(root.left, curSum, res, arr, targetSum);
        dfs(root.right, curSum, res, arr, targetSum);
        arr.remove(arr.size() - 1);
        return;
    }
}
