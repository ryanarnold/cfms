$('.datetime-picker').datetimepicker();

// For todays date;
Date.prototype.today = function () {
    return (((this.getMonth() + 1) < 10) ? "0" : "") + (this.getMonth() + 1) + "/" + ((this.getDate() < 10) ? "0" : "") + this.getDate() + "/" + this.getFullYear();
}

// For the time now
Date.prototype.timeNow = function () {
    return ((this.getHours() < 10) ? "0" : "") + this.getHours() + ":" + ((this.getMinutes() < 10) ? "0" : "") + this.getMinutes();
}

$('#id_done').bind('change', function(event) {
	var $this = $(this);
	var $dateAction = $('#id_date_action');
	var $remarks = $('#id_remarks');

	var dateNow = new Date();

	if ($this.is(':checked')) {
		$remarks.val('CLOSED');
		$dateAction.val(dateNow.today() + ' ' + dateNow.timeNow());
	} else {
		$remarks.val('');
		$dateAction.val('');
	}
})