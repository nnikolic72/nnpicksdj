function send_email_callback(data){
    //alert(data.submit_action_result);
    if (data.status == "ok") {
        $("#thankyoumessage").html("<b>Thank you, your e-mail was saved successfully!</b>")
        $("#emailformcontainer").hide();
    }
    
    if (data.status == "error") {
        $("#thankyoumessage").html("<b>Please check your e-mail address and submit it again.</b>")
    }    
    return true;
}

function send_dashboard_email() {
    //alert("Email Test");
    comment_form_name = "#email_form";
    form = $(comment_form_name).serializeObject();
    //alert("Test");
    Dajaxice.members.send_email(send_email_callback, {'form': form});
}