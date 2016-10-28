$(document).ready(function(){
	var path = location.pathname
	if (path == '\/cfms\/users\/add\/') {
		$('li[href="/cfms/users/"]').addClass('active')
	} else {
		$('li[href="' + location.pathname + '"]').addClass('active')	
	}
})