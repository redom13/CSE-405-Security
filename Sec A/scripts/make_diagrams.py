"""Generate editable vector schematics for the Sec A worked examples."""
from pathlib import Path
import os
SECTION=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(SECTION/'_build/matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyBboxPatch,Polygon
import numpy as np
OUT=SECTION/'solutions/assets';OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none','mathtext.fontset':'cm'})
BLUE='#28557e';LIGHT='#e8f0f7';RED='#a83e3e';GREEN='#35745b'
def canvas(w=10,h=4):
 fig,ax=plt.subplots(figsize=(w,h));ax.set_xlim(0,10);ax.set_ylim(0,5);ax.axis('off');return fig,ax
def box(ax,x,y,w,h,label,color=LIGHT):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.03',facecolor=color,edgecolor=BLUE));ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10,wrap=True)
def arrow(ax,x1,y1,x2,y2,label='',color=BLUE):
 ax.annotate('',(x2,y2),(x1,y1),arrowprops={'arrowstyle':'->','color':color,'lw':1.6});
 if label:ax.text((x1+x2)/2,(y1+y2)/2+.13,label,ha='center',va='bottom',fontsize=9,color=color)
def save(name,fig):
 fig.tight_layout(pad=.5)
 for ext in ['svg','pdf','png']:fig.savefig(OUT/f'{name}.{ext}',bbox_inches='tight',dpi=160)
 plt.close(fig)

fig,ax=canvas();box(ax,.3,2,2,1,'Alice\nDHCP client');box(ax,4,2,2,1,'Attacker\n10.10.10.32');box(ax,7.6,2,2,1,'Real router\n10.10.10.4');arrow(ax,2.3,2.7,4,2.7,'local next hop');arrow(ax,6,2.7,7.6,2.7,'forward');arrow(ax,7.6,2.2,6,2.2);arrow(ax,4,2.2,2.3,2.2);ax.text(5,4.2,'Rogue gateway offer OR forged ARP mapping',ha='center',color=BLUE);ax.text(5,.8,'Bidirectional interception also needs a return path through the relay.',ha='center',fontsize=10);save('lan-mitm',fig)

fig,ax=canvas();
for x,l in [(1.4,'Client'),(8.4,'Server')]:ax.plot([x,x],[.6,4.4],color=BLUE);ax.text(x,4.65,l,ha='center')
arrow(ax,1.4,4,8.4,3.5,'SYN, seq = x');arrow(ax,8.4,3.1,1.4,2.6,'SYN-ACK, seq = cookie, ack = x+1');arrow(ax,1.4,2.2,8.4,1.7,'ACK, ack = cookie+1');ax.text(8.4,3.75,'no per-request state',ha='center',fontsize=9,color=GREEN);ax.text(8.4,1.15,'validate cookie\nthen allocate state',ha='center',fontsize=10,color=GREEN);save('syn-cookie',fig)

fig,ax=canvas();
for x,l in [(1,'Attacker'),(4.6,'Resolver'),(8.9,'Authoritative')]:ax.plot([x,x],[.7,4.3],color=BLUE);ax.text(x,4.6,l,ha='center')
arrow(ax,4.6,3.9,8.9,3.3,'fresh-name lookup');arrow(ax,1,3.5,4.6,2.5,'forged matching reply',RED);arrow(ax,8.9,2.8,4.6,1.8,'authentic reply');ax.text(5,.6,'First acceptable reply may win the race; DNSSEC validates the data,\nnot merely arrival order or an untrusted key in the response.',ha='center',fontsize=10);save('dns-race',fig)

fig,ax=canvas();box(ax,4,2,2,1,'Switch\nfinite FDB');box(ax,.4,3.6,2,1,'Host A');box(ax,7.6,3.6,2,1,'Host B');box(ax,.4,.6,2,1,'Attacker');arrow(ax,2.4,1.2,4,2.2,'many fake sources',RED);arrow(ax,2.4,3.8,4,2.8);arrow(ax,6,2.8,7.6,3.8);arrow(ax,4,2.4,2.4,1.5,'unknown unicast',RED);ax.text(7.5,1,'Flooding stays within\nthe forwarding VLAN.\nKnown destinations may\nstill use learned ports.',ha='center',fontsize=10);save('switch-flood',fig)

fig,ax=canvas();box(ax,.3,2,2.4,1,'User computer\nadware + spyware');box(ax,4,2,2.2,1,'Ad / collection\nagent');box(ax,7.5,2,2.2,1,'Advertisers');arrow(ax,6.2,2.8,7.5,2.8,'audience / clicks');arrow(ax,7.5,2.2,6.2,2.2,'payment');arrow(ax,4,2.8,2.7,2.8,'advertisements');arrow(ax,2.7,2.2,4,2.2,'profile / events');ax.text(5,4.15,'Unauthorized tracking can increase targeting value and revenue.',ha='center',fontsize=10);save('adware',fig)

fig,ax=canvas();box(ax,.3,2,1.5,1,'Internet');box(ax,3,2,1.7,1,'Firewall /\nsegmentation');box(ax,7,3.4,2.3,1,'Production');box(ax,7,1.3,2.3,1,'Honeypot\nisolated decoy');box(ax,3.2,.1,2.7,1,'Protected collector');arrow(ax,1.8,2.5,3,2.5);arrow(ax,4.7,2.8,7,3.9);arrow(ax,4.7,2.2,7,1.8);arrow(ax,7,.8,5.9,.7,'logs');ax.text(7.7,.25,'Restrict decoy egress',ha='center',fontsize=9,color=RED);save('honeypot',fig)

fig,ax=canvas();
for x,y,l,c in [(3.7,2.9,'Information\nsecurity','#8eb8d9'),(6.2,2.9,'IT security','#abd3b2'),(5,1.7,'Cybersecurity','#e5c394')]:
 ax.add_patch(Circle((x,y),1.9,alpha=.34,color=c));ax.text(x+(x-5)*.6,y+.7,l,ha='center',va='center')
ax.text(5,2.6,'Shared digital\nprotection',ha='center',fontsize=10);ax.text(.15,.15,'Conceptual overlap; exact boundaries depend on the adopted definitions.',fontsize=9);save('security-scopes',fig)

fig,ax=canvas(h=3.3)
for y,title,labels in [(3.3,'ESP transport',['Outer IP','ESP hdr','TCP / data / trailer','Tag']),(1.5,'ESP tunnel',['New IP','ESP hdr','Original IP / TCP / data / trailer','Tag'])]:
 ax.text(.1,y+.9,title,color=BLUE)
 for x,w,l in [(.1,1.4,labels[0]),(1.5,1.4,labels[1]),(2.9,5.5,labels[2]),(8.4,1.3,labels[3])]:box(ax,x,y,w,.7,l,'#cce5d8' if x==2.9 else LIGHT)
ax.text(5,.4,'Green region encrypted; outer IP remains visible.\nIntegrity coverage depends on the selected ESP transform.',ha='center',fontsize=10);save('ipsec',fig)

fig,ax=plt.subplots(figsize=(9,3.5));t=np.linspace(0,12,300);I=1000/(1+999*np.exp(-t));ax.plot(t,I,color=BLUE,lw=2);ax.set_xlabel('Scaled time (β N t)');ax.set_ylabel('Infected hosts I(t)');ax.grid(alpha=.2);ax.annotate('near-exponential growth',(4.5,80),(1,380),arrowprops={'arrowstyle':'->'});ax.annotate('susceptible depletion',(10,955),(7,600),arrowprops={'arrowstyle':'->'});save('worm-growth',fig)

fig,ax=canvas(h=3.3)
for y,l in [(3.5,'R+8: pointer to argument string'),(2.7,'R+4: system return / continuation'),(1.9,'R: address of system'),(.7,'local buffer and padding')]:box(ax,2,y,6,.7,l)
ax.text(8.3,2.65,'ESP on entry\nto system',fontsize=10,va='center');ax.text(1.7,4.5,'Higher addresses ↑',fontsize=10);save('retlibc-stack',fig)

fig,ax=canvas(h=4.5);ax.add_patch(Rectangle((1,1),8,3.5,facecolor='#f1f3f5',edgecolor=BLUE));ax.add_patch(Rectangle((1,1),8,1.7,facecolor=LIGHT,edgecolor=BLUE));ax.plot([.5,9.4],[2.7,2.7],'--',color=RED);ax.text(9.35,2.85,'shear',ha='right',color=RED)
for x,k in [(2,1),(4,1.5),(6,.7),(8,1.2)]:
 ax.add_patch(Rectangle((x-.28,2.7),.56,.9,facecolor='#8eb8d9',edgecolor=BLUE));ax.add_patch(Rectangle((x-.28,2.7-k),.56,k,facecolor='#e5c394',edgecolor=BLUE));ax.plot([x-.2,x+.2,x-.2,x+.2,x],[4.2,4.05,3.9,3.75,3.6],color=BLUE)
ax.add_patch(Polygon([(1.2,1.02),(1.2,1.45),(2,1.7),(4,1.2),(6,2.0),(8,1.5),(8.6,1.45),(8.6,1.02)],facecolor='#b8b8b8',edgecolor=BLUE))
ax.text(.2,4.6,'shell / housing',color=BLUE);ax.text(1.1,.65,'key inside rotating plug',fontsize=10);ax.annotate('spring',(8,4),(8.7,4.65),arrowprops={'arrowstyle':'->'},fontsize=10);ax.annotate('keyway',(1.4,1.3),(.2,1.7),arrowprops={'arrowstyle':'->'},fontsize=9);ax.text(4.9,.3,'Correct key lifts every pin boundary to the shear line.',ha='center',fontsize=10);ax.annotate('driver pins',(2,3.1),(3,4.6),arrowprops={'arrowstyle':'->'});ax.annotate('key pins',(6,2.3),(7.5,.7),arrowprops={'arrowstyle':'->'});save('pin-lock',fig)

fig,ax=plt.subplots(figsize=(9,4));bottom=np.array([2,2,5,2,6]);wafer=np.array([2,2,0,3,0]);lift=np.array([8,6,5,8,4]);x=np.arange(1,6)
ax.bar(x,bottom,bottom=lift,color='#e5c394',edgecolor=BLUE,label='key pin');ax.bar(x,wafer,bottom=lift+bottom,color='#9cc7ae',edgecolor=BLUE,label='master wafer');ax.bar(x,np.full(5,5),bottom=lift+bottom+wafer,color='#8eb8d9',edgecolor=BLUE,label='driver');ax.axhline(10,color=RED,ls='--',label='shear H=10');ax.set_xticks(x);ax.set_xlabel('Chamber (with K1 inserted)');ax.set_ylabel('Height above datum');ax.legend(ncol=2,fontsize=9);ax.set_ylim(0,19);save('master-lock',fig)
print('Generated 12 vector diagrams')
