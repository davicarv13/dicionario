function insert_result(item){
	$('#'+ this.valueOf() +'').append('<li>'+ item +'</li>')
}

function insert_antonimos(item){
	$('#sinonimos').append('<p>'+ item +'</p>')
}

function search_word(){
	word = $('#word').val()

	
	$.ajax({
	  url: "/search-word/",
	  data: {
	    'word':word
	  },
	  dataType: 'json',
	  success: function (data) {
	    var sinonimos = JSON.parse(data.sinonimos);
	    var antonimos = JSON.parse(data.antonimos);

	    $('#lista_sinonimos').empty();
	    $('#lista_antonimos').empty();
	    sinonimos.forEach(insert_result, 'lista_sinonimos');
	    antonimos.forEach(insert_result, 'lista_antonimos');
	  }
	});
}