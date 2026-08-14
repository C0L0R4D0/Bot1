import os, sys, zlib, struct, binascii, random, hashlib
root = sys.argv[1] if len(sys.argv)>1 else 'VideoPropsProject/src/main/resources/assets/videoprops/textures'
items = ['money_stack','black_mask','hacker_device','money_bundle','camera_tablet','money_bag','signal_jammer','lockpick_set','crowbar','usb_flash','money_bundle_3','gold_stack','vault_key','drill','radio','money_bundle_2','access_card','ghost_phone']
blocks = ['camera_body','keypad','vault_door','camera_lens','safe','cctv_monitor','keyboard','laptop_screen','alarm','laptop_body']

def png_chunk(t,d):
    return struct.pack('>I',len(d))+t+d+struct.pack('>I',binascii.crc32(t+d)&0xffffffff)
def write_png(path,w,h,pix):
    raw=b''.join(b'\x00'+bytes(pix[y*w*4:(y+1)*w*4]) for y in range(h))
    data=b'\x89PNG\r\n\x1a\n'+png_chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,6,0,0,0))+png_chunk(b'IDAT',zlib.compress(raw,9))+png_chunk(b'IEND',b'')
    os.makedirs(os.path.dirname(path),exist_ok=True)
    open(path,'wb').write(data)

def palette(name):
    if 'money' in name: return (42,90,50),(115,170,95),(215,205,145)
    if 'gold' in name or 'vault_key' in name: return (105,72,12),(220,168,36),(255,225,105)
    if name=='alarm': return (80,12,15),(220,42,42),(255,145,110)
    if name in ('vault_door','safe','crowbar','drill'): return (42,47,52),(105,115,122),(190,198,202)
    if 'lens' in name: return (3,8,12),(15,61,80),(65,205,230)
    return (12,18,22),(30,55,60),(45,215,190)

def make(name,folder):
    w=h=256; a,b,c=palette(name); seed=int(hashlib.sha256(name.encode()).hexdigest()[:8],16); rng=random.Random(seed)
    p=[]
    for y in range(h):
        for x in range(w):
            g=(x+y)/(2*(w-1)); n=rng.randint(-7,7)
            r=int(a[0]*(1-g)+b[0]*g)+n; gg=int(a[1]*(1-g)+b[1]*g)+n; bb=int(a[2]*(1-g)+b[2]*g)+n
            edge=min(x,y,w-1-x,h-1-y)
            if edge<7: r//=3; gg//=3; bb//=3
            if ((x//16)+(y//16))%2==0: r+=4; gg+=4; bb+=4
            if (x+y+seed)%61<2: r=min(255,r+25); gg=min(255,gg+25); bb=min(255,bb+25)
            if name in ('camera_tablet','ghost_phone','laptop_screen','cctv_monitor') and 24<x<232 and 30<y<220:
                r=max(5,r//3); gg=min(255,gg+35); bb=min(255,bb+28)
                if x%32==0 or y%32==0: gg=min(255,gg+25)
            if name=='keyboard' and 16<x<240 and 24<y<220 and (x%24<18 and y%20<14):
                r=max(20,r-4); gg=max(25,gg-4); bb=max(25,bb-4)
            p.extend((max(0,min(255,r)),max(0,min(255,gg)),max(0,min(255,bb)),255))
    write_png(os.path.join(root,folder,name+'.png'),w,h,p)

for n in items: make(n,'items')
for n in blocks: make(n,'blocks')
print('Generated',len(items)+len(blocks),'PNG textures at 256x256')
