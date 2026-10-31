import re,sys,html
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    return t
out=['<div style="font-family:Arial,sans-serif;font-size:14px;line-height:1.5;color:#222;max-width:680px">']
inlist=False
for line in open(sys.argv[1]).read().splitlines():
    if line.startswith('- '):
        if not inlist: out.append('<ul>'); inlist=True
        out.append('<li>'+inline(line[2:])+'</li>'); continue
    if inlist: out.append('</ul>'); inlist=False
    if line.startswith('## '): out.append('<h3 style="margin:20px 0 6px">'+inline(line[3:])+'</h3>')
    elif line.startswith('# '): out.append('<h2>'+inline(line[2:])+'</h2>')
    elif line.strip(): out.append('<p>'+inline(line)+'</p>')
if inlist: out.append('</ul>')
out.append('</div>')
print('\n'.join(out))
