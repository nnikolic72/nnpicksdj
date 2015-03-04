function friend_photo_selected(p_photo_id, p_friend_id, static_url, p_ig_photo_url) {
    //alert("test");
    id = "#fivethumbscontainer_";
    id = id.concat(p_friend_id);
    //alert(id);
    $(id).children().animate({ opacity: 0 }, duration=800);
    
    newhtml = "<img src='"
    newhtml = newhtml.concat(p_ig_photo_url);
    newhtml = newhtml.concat("'></img>");
    $(id).html(newhtml);
    $(id).children().animate({ opacity: 100 });
}