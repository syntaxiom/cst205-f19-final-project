const md = 
    $('#content').text()
    .trim()
    .split('\n').map(line => line.trim())
    .join('\n')

$('#content').html(marked(md))