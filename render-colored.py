import re
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
base=Path('/tmp/openspec-list-review');ansi=re.compile(r'\x1b\[([0-9;]*)m')
font=ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',22)
boldfont=ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',22,index=1)
colors={31:'#d99696',32:'#a3c798',33:'#d5b778',34:'#a5b8d8',36:'#8ac6bd'}
for name,command,filename in [('changes','openspec list','changes-color.txt'),('specs','openspec list --specs','specs-color.txt'),('narrow','openspec list --no-color','narrow.txt')]:
    raw=(base/filename).read_text();lines=('$ '+command+'\n'+raw).rstrip().splitlines()
    image=Image.new('RGB',(int(max(font.getlength(ansi.sub('',line)) for line in lines))+64,32*len(lines)+56),'#0c0c0c');draw=ImageDraw.Draw(image)
    color=None;dim=False;bold=False
    for i,line in enumerate(lines):
        x=28;pos=0
        for match in list(ansi.finditer(line))+[None]:
            end=match.start() if match else len(line);chunk=line[pos:end]
            draw.text((x,24+i*32),chunk,font=boldfont if bold else font,fill=colors.get(color,'#939087' if dim else '#dedbd2'))
            x+=font.getlength(chunk)
            if match:
                for code in (int(v or 0) for v in match.group(1).split(';')):
                    if code==0:color=None;dim=False;bold=False
                    elif code==1:bold=True
                    elif code==2:dim=True
                    elif code==22:bold=False;dim=False
                    elif code==39:color=None
                    elif code in colors:color=code
                pos=match.end()
    image.save(base/(name+'.png'))
