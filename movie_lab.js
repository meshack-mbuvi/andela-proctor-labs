/**
*   :Author: Mbuvi
*   :javascript function to whether and who should accompany those going to 
*   :watch a movie called Deadpool
*   :params:age-age value of an individual
*   :Return:msg-string with condition statement to be fullfilled to watch the movie
*/
function canIWatch(age)
{
  if (age < 0 ){
    msg = 'Invalid age.';
  }
  else if (age < 6) {
      msg = 'You are not allowed to watch Deadpool after 6.00pm.';
      }
  else if (age >= 6 && age < 17) {
    msg ='You must be accompanied by a guardian who is 21 or older.';
    }
  else if (age >= 17 && age < 25) {
    msg = 'You are allowed to watch Deadpool, right after you show some ID.';
  }
  else if(age >= 25){
     msg = 'Yay! You can watch Deadpool with no strings attached!';
  }
    return msg;
}
