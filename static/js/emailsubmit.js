function send_email_callback(data){
    //alert("I am an alert box!");
    if (data.submite_action_result == 'ok') {
        $("#thankyoumessage").html("Thank you!")
    }
    
    if (data.submite_action_result == 'error') {
        $("#thankyoumessage").html("Please check your e-mail address and submit it again.")
    }    
    return true;
}

function send_dashboard_email() {
    //alert("Test");
    comment_form_name = "#email_form";
    form = $(comment_form_name).serializeObject();
    //alert("Test");
    Dajaxice.dashboard.send_email(send_email_callback, {'form': form});
}