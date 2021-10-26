$(document).ready(function() {
    $(document).delegate(":checkbox", "click", onCheck);
    $('input[id="myinput"]').keypress(function(event){
        if(event.which == 13){
            plan_id = $(this).next().val()

            $.post("/todo/add/"+plan_id, { todo : "'"+$(this).val()+"'" },
                  function(data){
                   $("#collapse"+plan_id).append(data)
                });
        }
    })

});

function onCheck(){
    id = $(this).data("todo-id")
    progressbarid = $(this).val()
    $.post("/todo/change/"+id, function(data){
        $("#progerssbar" + progressbarid).attr('aria-valuenow', data.done)
        $("#progerssbar" + progressbarid).attr('aria-valuemax', data.all)
        $("#progerssbar" + progressbarid).attr('style', 'width: '+data.done/data.all*100+'%')
    });
}


