function calculate() 
{
	//Dajaxice.examples.multiply(Dajax.process,{'a':$('#a').val(),'b':$('#b').val()})
	Dajaxice.examples.multiply(Dajax.process,{'a':$('#a').val(),'b':$('#b').val()})
}

function my_js_callback(data)
{
	alert(data.message);
}