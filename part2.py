"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(5) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""

def diamond(size):
  row=1
  while row<=size:
    if row == 1:
      print(" "*(size-row)+"*")
    else:
      print(" "*(size-row)+"*"+" "*(2*(row-2)+1)+"*")
    row+=1
  row=size-1
  while row>=1:
    if row == 1:
      print(" "*(size-row)+"*")
    else:
      print(" "*(size-row)+"*"+" "*(2*(row-2)+1)+"*")
    row-=1