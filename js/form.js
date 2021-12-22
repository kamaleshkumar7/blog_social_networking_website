$(document).ready(function() {

	$('#sign_up').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#signUpUser').val(),
				email : $('#signUpEmail').val(),
                pass1 : $('#signPass1').val(),
				pass2 : $('#signPass2').val()
			},
			type : 'POST',
			url : '/sign_inprocess'
		})
		.done(function(data) {

			if (data.error) {
				//$('#errorAlert1').text(data.error).show();
				document.getElementById('errorAlert1').style.display="block";
				document.getElementById('errorAlert1').innerHTML=text(data.error);
			}
			else {
				//$('#errorAlert1').hide();
				document.getElementById('errorAlert1').style.display="none";
			}

		});

		event.preventDefault();

	});

});

$(document).ready(function() {

	$('#sign_in').on('submit', function(event) {

		$.ajax({
			data : {
				usernameoremail : $('#loginUser').val(),
				pass : $('#loginPass').val()
			},
			type : 'POST',
			url : '/sign_up_process'
		})
		.done(function(data) {

			if (data.error) {
				//$('#errorAlert2').text(data.error).show();
				document.getElementById('errorAlert2').style.display="block";
				document.getElementById('errorAlert2').innerHTML=text(data.error);
			}
			else {
				//$('#errorAlert2').hide();
				document.getElementById('errorAlert2').style.display="none";
			}

		});

		event.preventDefault();

	});

});