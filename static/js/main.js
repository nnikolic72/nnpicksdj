
function message_callback(data){
  if (data.status == 'Success!'){
    $('#contact_errors').html(data.status);
  }else{
    for (message in data.status){
      $('#contact_errors').append("<p><b>" + message + ":</b>" + data.status["message"] + "</p>");
    }
  }
}

function send_message(){
  data = $('#contact_form').serializeObject();
  Dajaxice.goodusers.send_message(message_callback, {'form':data});
  return false;
}