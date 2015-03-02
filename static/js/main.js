
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

function like_callback(data){
    //alert("I am an alert box!");
    idname = '#likesdiv';
    idname = idname.concat(data.photo_id);
    
    imgname = '#imglike_';
    imgname = imgname.concat(data.photo_id);
    
    liketxt = '#iglikestxt_';
    liketxt = liketxt.concat(data.photo_id);
    $(liketxt).html(data.no_of_likes);
    

    //alert(data.photo_id);
    //alert(data.like_action_result);
    if (data.like_action_result == 'like') {
        html_text = '<img class="heartimage"';
        html_text = html_text.concat(' id="');
        html_text = html_text.concat(imgname);
        html_text = html_text.concat('" src="');
        html_text = html_text.concat(data.static_url);
        html_text = html_text.concat('img/redheart.png"></img>');
        $(idname).html(html_text);
    }
    if (data.like_action_result == 'unlike') {
        html_text = '<img class="heartimage"';
        html_text = html_text.concat(' id="');
        html_text = html_text.concat(imgname);
        html_text = html_text.concat('" src="');
        html_text = html_text.concat(data.static_url);
        html_text = html_text.concat('img/greyheart.png"></img>');
        $(idname).html(html_text);
    }
    if (data.like_action_result == 'error') {
        $(idname).html('E');
    }
    return true;
}

function like(p_photo_id) {
    idname = '#imglike_';
    idname = idname.concat(p_photo_id);
    //ajax_loader-small
    html_text = '<img class="heartimage"';
    html_text = html_text.concat(' id="');
    html_text = html_text.concat(imgname);
    html_text = html_text.concat('" src="');
    html_text = html_text.concat(data.static_url);
    html_text = html_text.concat('img/ajax_loader-small.gif"></img>');
    $(idname).html(html_text);
        

    Dajaxice.goodusers.like(like_callback, {'p_photo_id':p_photo_id});
}


function send_comment_callback(data){
    //alert("I am an alert box!");
    
    return true;
}

function send_comment(p_photo_id) {
    
    comment_form_name = "#comment_form_";
    comment_form_name = comment_form_name.concat(p_photo_id);
    form = $(comment_form_name).serializeObject();
    //alert(form);
    Dajaxice.goodusers.send_comment(send_comment_callback, {'p_photo_id':p_photo_id, 'form': form});
}