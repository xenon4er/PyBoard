import templater

tmpr = templater.Templater()

a = {'text' : 'FUCK YEAH', 'title' : 'Daiver'}

str = '{$title} this text about {$text}'

print tmpr.MkPage(str,a)