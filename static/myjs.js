$( document ).ready(function() {
    console.log( "ready!" );
	$("#submit1").click(function(){
		var myFile = $('#image').prop('files')[0];
		formdata = new FormData();
		formdata.append("image", myFile);
		$.ajax(
			{
				url: $SCRIPT_ROOT + "/upload",
				data:formdata,
				type:'POST',
				processData: false,
				contentType: false,
				success: function(result)
				{
					$("#baseimage").attr("src", 'data:image/jpg;base64,'+result);
					$("#baseimage").attr("style",'display:block; width :500px;')
				}
			}
		);
	});
});