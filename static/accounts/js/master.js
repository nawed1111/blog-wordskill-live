var form_fields = document.getElementsByTagName('input')
form_fields[2].placeholder='Username..';
form_fields[3].placeholder='Email..';
form_fields[4].placeholder='Enter password...';
form_fields[5].placeholder='Re-enter Password...';

for (var field in form_fields){
	form_fields[field].className += ' form-control'
}