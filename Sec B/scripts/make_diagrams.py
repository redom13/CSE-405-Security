from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR',str(Path(__file__).resolve().parents[1]/'_build/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from PIL import Image
A=Path(__file__).resolve().parents[1]/'solutions/assets';A.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none','mathtext.fontset':'cm'})
blue='#244a75';green='#267261';red='#aa3d46';ink='#172c44'
def setup(w=10,h=3):
 fig,ax=plt.subplots(figsize=(w,h));ax.set_xlim(0,10);ax.set_ylim(0,h);ax.axis('off');fig.patch.set_facecolor('white');return fig,ax
def box(ax,x,y,w,h,t,c=blue):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.03,rounding_size=0.07',linewidth=1.2,edgecolor=c,facecolor=c+'0d'))
 ax.text(x+w/2,y+h/2,t,ha='center',va='center',color=ink,fontsize=10)
def arrow(ax,x,y,u,v,label='',c=blue):
 ax.add_patch(FancyArrowPatch((x,y),(u,v),arrowstyle='-|>',mutation_scale=13,lw=1.3,color=c))
 if label:ax.text((x+u)/2,(y+v)/2+.08,label,ha='center',va='bottom',fontsize=9,color=c)
def save(fig,name):
 fig.savefig(A/(name+'.svg'),bbox_inches='tight',pad_inches=.12)
 fig.savefig(A/(name+'.pdf'),bbox_inches='tight',pad_inches=.12)
 fig.savefig(A/(name+'.png'),bbox_inches='tight',pad_inches=.12,dpi=180);plt.close(fig)
def sequence(name,people,events,foot='',h=4.3):
 fig,ax=setup(h=h);xs=[.7+8.6*i/(len(people)-1) for i in range(len(people))]
 for x,p in zip(xs,people):
  ax.text(x,h-.25,p,ha='center',va='center',fontweight='bold',color=ink)
  ax.plot([x,x],[.5,h-.55],color='#bac8d5',ls='--',lw=1)
 step=(h-1.3)/max(len(events),1)
 for i,(a,b,t) in enumerate(events):
  y=h-.85-i*step;arrow(ax,xs[a],y,xs[b],y,t,red if a==1 and len(people)==3 else blue)
 if foot:ax.text(5,.1,foot,ha='center',va='bottom',fontsize=10,color=green)
 save(fig,name)
sequence('dh-mitm',['Alice','Mallory','Bob'],[(0,1,'$A=g^a$'),(1,2,'$X=g^x$ (substituted)'),(2,1,'$B=g^b$'),(1,0,'$Y=g^y$ (substituted)'),(0,1,'traffic under $K_A=g^{ay}$'),(1,2,'re-encrypted traffic under $K_B=g^{bx}$')],'Mallory knows $K_A=A^y$ and $K_B=B^x$; Alice and Bob do not share one authenticated key.',5)
sequence('csrf',['Attacker page','Victim browser','Bank'],[(1,2,'earlier login → session cookie'),(0,1,'load page containing forged request'),(1,2,'request + automatically attached bank cookie'),(2,1,'accept only if session AND CSRF token validate')],'The remote attacker cannot read the victim’s session-bound form token.',4.2)
sequence('relay',['Victim','Phishing relay','Real service'],[(0,1,'password'),(1,2,'forward password'),(2,0,'SMS code arrives'),(0,1,'user enters code'),(1,2,'forward code before expiry')],'A one-time code can still be relayed live unless authentication is bound to the real origin.',4.7)
fig,ax=setup(h=2.5)
for x,t in [(0,'Message M'),(2.5,'Hash H(M)'),(5,'Sign with SK'),(7.5,'Signature s')]:box(ax,x,.95,2.15,.65,t)
for x in [2.2,4.7,7.2]:arrow(ax,x,1.28,x+.25,1.28)
ax.text(5,.45,'Verifier: authentic PK + M + s → verify exact content and context',ha='center',color=green)
save(fig,'signature')
fig,ax=setup(h=3.1)
for i in range(3):
 x=.25+i*3.35
 box(ax,x,2.2,2.8,.5,['$C_1\\oplus IV_2$','C2','C3'][i]);box(ax,x+.55,1.25,1.7,.55,'D under K')
 arrow(ax,x+1.4,2.15,x+1.4,1.85)
 box(ax,x,.25,2.8,.55,['$\\oplus IV_1\\;\\to P_1$','$\\oplus C_1\\;\\to P_2$','$\\oplus C_2\\;\\to P_3$'][i]);arrow(ax,x+1.4,1.2,x+1.4,.85)
ax.text(5,2.95,'Three independent decryption paths: all inputs are already received',ha='center',fontsize=11,color=ink)
save(fig,'custom-decryption')
fig,ax=setup(h=3)
box(ax,.15,1.65,2,.6,'$P_i\\oplus C_{i-1}$');box(ax,3.3,1.65,1.8,.6,'E under K');box(ax,6.4,1.65,1.8,.6,'Ci')
arrow(ax,2.2,1.95,3.25,1.95);arrow(ax,5.15,1.95,6.35,1.95)
ax.text(9,1.95,'CBC',ha='center',color=blue,fontweight='bold')
box(ax,.15,.35,2,.6,'nonce || counter_i');box(ax,3.3,.35,1.8,.6,'E under K');box(ax,6.4,.35,1.8,.6,'$Z_i\\oplus P_i=C_i$')
arrow(ax,2.2,.65,3.25,.65);arrow(ax,5.15,.65,6.35,.65)
ax.text(9,.65,'CTR',ha='center',color=green,fontweight='bold')
ax.text(5,2.65,'CBC chains ciphertext; CTR generates independent keystream blocks',ha='center',color=ink)
save(fig,'modes')
fig,ax=setup(h=3.6)
box(ax,.3,.3,6.7,2.65,'',blue)
ax.text(3.65,2.7,'Visible attacker page',ha='center',fontweight='bold',color=blue)
box(ax,1.3,.9,4.7,1.05,'“Win a free subscription”',green)
ax.add_patch(Rectangle((1.15,.75),5,1.35,fill=True,alpha=.12,facecolor=red,edgecolor=red,lw=2))
ax.text(3.65,1.95,'Transparent target iframe over the decoy',ha='center',fontsize=9,color=red)
box(ax,3.05,1.08,1.25,.45,'BUY',red);arrow(ax,8.8,2.7,3.7,1.55,'actual click',red)
ax.text(8.25,.7,'User intends decoy;\ntarget receives click.',ha='center',color=ink)
save(fig,'clickjacking')
fig,ax=setup(h=3.2)
for y,title,labels in [(1.85,'Stored',['Attacker entry','Database / page','Victim executes']),(.35,'Reflected',['Crafted link','Request / echo','Victim executes'])]:
 ax.text(.1,y+.85,title,color=blue,fontweight='bold')
 for x,t in zip([.2,3.65,7.1],labels):box(ax,x,y,2.6,.6,t)
 arrow(ax,2.85,y+.3,3.6,y+.3);arrow(ax,6.3,y+.3,7.05,y+.3)
save(fig,'xss')
fig,ax=setup(h=2.8)
box(ax,.2,1.4,2.5,.7,'$(K_0\\oplus\\mathrm{ipad})\\parallel M$');box(ax,3.5,1.4,1.2,.7,'H');box(ax,5.3,1.4,4.3,.7,'inner digest')
arrow(ax,2.75,1.75,3.45,1.75);arrow(ax,4.75,1.75,5.25,1.75)
box(ax,.2,.15,4.8,.7,'$(K_0\\oplus\\mathrm{opad})\\parallel h_{\\mathrm{inner}}$');box(ax,5.8,.15,1.2,.7,'H');box(ax,8,.15,1.6,.7,'tag T')
arrow(ax,5.05,.5,5.75,.5);arrow(ax,7.05,.5,7.95,.5)
ax.text(5,2.5,'HMAC: inner and outer hashes use distinct pads',ha='center',color=ink)
save(fig,'hmac')
fig,ax=setup(h=2.8)
for x,t in [(0.2,'Trusted root CA\npublic key installed'),(3.65,'Intermediate CA\ncertificate'),(7.1,'Server certificate\nname + public key')]:box(ax,x,1.1,2.7,.85,t)
arrow(ax,2.95,1.55,3.6,1.55,'signs');arrow(ax,6.4,1.55,7.05,1.55,'signs')
ax.text(5,.35,'Trust starts at a configured anchor; validate the entire chain and hostname.',ha='center',color=green)
save(fig,'certificate-chain')
fig,ax=setup(h=2.8)
box(ax,.1,1.1,1.3,.65,'fixed IV')
for i in range(3):
 x=2.1+i*2.75;box(ax,x,1.1,1.25,.65,'f');ax.text(x+.65,2.25,f'm{i+1}',ha='center',color=ink);arrow(ax,x+.65,2.05,x+.65,1.8)
 arrow(ax,1.45 if i==0 else x-1.4,1.43,x-.05,1.43,f'h{i}' if i else '')
arrow(ax,8.9,1.43,9.8,1.43,'H(M)')
ax.text(5,.3,'Length-strengthened padding → blocks; hi = f(h(i−1), mi)',ha='center',color=green)
save(fig,'merkle-damgard')
# Crop the exact original printed diagram used to trace the permutation.
if not (A/'original-pboxes.png').exists():
 raise FileNotFoundError('Keep the original-pboxes.png source figure in solutions/assets')
# Finite-field point plot supplements, but does not replace, the exact table.
pts=[(x,y) for x in range(11) for y in range(11) if (y*y-x**3-x-6)%11==0]
fig,ax=plt.subplots(figsize=(5.7,3.8));ax.scatter(*zip(*pts),s=60,c=blue);ax.set_xticks(range(11));ax.set_yticks(range(11));ax.grid(alpha=.2);ax.set_xlabel('x modulo 11');ax.set_ylabel('y modulo 11');ax.set_title('y² = x³ + x + 6 over F₁₁: 12 finite points + O');save(fig,'ecc-points')
print('Created',len(list(A.glob('*.svg'))),'SVG diagrams plus PNG equivalents')
