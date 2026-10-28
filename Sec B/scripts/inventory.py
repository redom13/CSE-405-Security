"""Refresh the repository-relative Sec B source inventory (requires Poppler)."""
from pathlib import Path
import json,re,subprocess
SECTION=Path(__file__).resolve().parents[1]
ROOT=SECTION.parent
CACHE=SECTION/'_build/extracted';CACHE.mkdir(parents=True,exist_ok=True)
items=[]
files=[ROOT/'CSE405-Security_Merged.pdf']+sorted((SECTION/'slides').glob('*.pdf'))+sorted((SECTION/'notes').glob('*.pdf'))
for f in files:
 rel=f.relative_to(ROOT).as_posix();out=CACHE/(f.stem+'.txt')
 subprocess.run(['pdftotext','-layout',str(f),str(out)],check=True,capture_output=True)
 info=subprocess.check_output(['pdfinfo',str(f)],text=True)
 txt=out.read_text();pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1])
 item={'file':rel,'pages':pages,'text_characters':len(txt),'text_file':out.relative_to(ROOT).as_posix(),'short_pages':[i+1 for i,p in enumerate(txt.split('\f')[:-1]) if len(p.strip())<80]}
 m=re.match(r'lecture-(\d+)-',f.stem)
 if m:item['lecture']=int(m[1])
 items.append(item)
(SECTION/'analysis/inventory.json').write_text(json.dumps(items,indent=2)+'\n')
print(f'Inventoried {len(items)} PDFs, {sum(x["pages"] for x in items)} pages')
