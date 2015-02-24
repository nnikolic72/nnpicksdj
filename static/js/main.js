
function message_callback(){
  $('#contact_errors').html('Pozvao callback')
}

function send_message(){
  $('#contact_errors').html('Proba');
  //data = $('#contact_form').serializeObject();
  $('#contact_errors').html('Proba2');
  Dajaxice.nnpicksdj.goodusers.send_message(message_callback);
  $('#contact_errors').html('Proba3');
  return false;
}