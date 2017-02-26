/**
 * Created by itc_user1 on 2/15/2017.
 */
console.log("heyeyeyey")

board = {};


board.updateall = function(){

        $(".comments").hide();
        $(".newcommentbox").hide();
        $(".delete_post").bind("click",board.delete_post);
        $(".showcomments").bind("click",board.showcomments);

        $("#closebtn").bind("click",board.cancelnewmsg);
        $(".addcomment").bind("click",board.addcomment);
        $(".confirmcommentbtn").bind("click",board.sendnewcomment);
        $(".clostcomment").bind("click",board.closenewcomment);
};


board.delete_post = function(){
    console.log(this.id);
    $(this).closest("fieldset").slideUp();
    $.ajax("/board/"+this.id,{
        type: "POST",
        data:{"post_id":this.id},
        success: function(data){
            console.log("post has been deleted")

        }
    });
};

board.addnewpost = function(){
    $("#newpostbtn").slideUp();
    $("#newpostdiv").slideDown();
    $("#confirmbox").slideDown();


};

board.cancelnewmsg = function(){
    $("#newpostdiv").slideUp();
    $("#confirmbox").slideUp();
    $("#newpostbtn").slideDown();
};

board.createnewpost = function(){
    $("#newpostdiv").fadeOut().delay(200);
    $("#confirmbox").fadeOut().delay(400);
    $("#newpostbtn").slideDown().delay(500).fadeIn();

    $.ajax("/board/newpost",{
    type: "POST",
    data:{"text":$("#newtext").val(),
          "title":$("#newtitle").val(),
          "author":$("#newauthor").val()
    },
    success: function(data)
    {
        $("#row").html(data + $("#row").html())
        board.updateall();
        $("#newtext").val(""),
        $("#newtitle").val(""),
        $("#newauthor").val("")
        $("#nomsgbox").hide();
    }});
};



board.showcomments = function(){
    console.log("comment work");
    $(this).html("Hide Comments");
    $(this).next("div").slideDown();
    $(this).unbind().bind("click",board.hidecomments)
};

board.hidecomments = function(){
    console.log("comment work hide");
    $(this).html("Show Comments");
    $(this).next("div").slideUp();
    $(this).unbind().bind("click",board.showcomments)
};



board.addcomment = function(){
    $(this).hide();
    $(this).closest("div").slideDown();
    var thisdiv = $(this).next("div").slideDown();
    console.log(thisdiv)
};

board.sendnewcomment = function(){
    $(this).closest("div").slideUp();
    var addbtnid =   $(this).attr('id');
    console.log(addbtnid);
    $("#add_"+addbtnid).show();

    $.ajax("/board/newcomment",{
    type: "POST",
    data:{"text":$("#newcoomenttext_"+addbtnid).val(),
          "author":$("#newcommentauthor_"+addbtnid).val(),
        "post":addbtnid
    },
    success: function(data)
    {
        $("#commentbox_"+addbtnid).html($("#commentbox_"+addbtnid).html() + data)
    }});

};

board.closenewcomment = function(){
    $(this).closest("div").slideUp();
    var addbtnid =   $(this).attr('id');
    console.log(addbtnid);
    $("#add_"+addbtnid).show();
};

board.formatDate = function(date){
    var day = date.getDate();
    // month start from 0, this i why plus '1'
    var month = date.getMonth() + 1;
    if (month<=9){
        month = '0' + String(month)
    }
    var year = date.getFullYear();
    var finaldate = day + "/" + month + "/" + year;
    return finaldate
}
board.start = function(){
    $(document).ready(function(){
        $("#newpostdiv").hide();
        $("#confirmbox").hide();
        $("#plusbtn").bind("click",board.addnewpost);

        $(".comments").hide();
        $(".newcommentbox").hide();
        $(".delete_post").bind("click",board.delete_post);
        $(".showcomments").bind("click",board.showcomments);
        $("#confirmbtn").bind("click",board.createnewpost);
        $("#closebtn").bind("click",board.cancelnewmsg);
        $(".addcomment").bind("click",board.addcomment);
        $(".confirmcommentbtn").bind("click",board.sendnewcomment);
        $(".clostcomment").bind("click",board.closenewcomment);
        $("#newpostdate").text(board.formatDate(new Date));
    })


};




board.start();