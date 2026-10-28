"""Protect canonical dollar-delimited TeX while Markdown handles surrounding prose."""
import re,html
import markdown

def render_markdown(source):
    protected={}
    def save(match):
        token=f'CODEPROTECTED{len(protected):06d}TOKEN'
        protected[token]=match.group(0)
        return token
    source=re.sub(r'```[^\n]*\n.*?```',save,source,flags=re.S)
    source=re.sub(r'`[^`\n]+`',save,source)
    math={}
    def display(match):
        token=f'MATHPROTECTED{len(math):06d}TOKEN'
        tex=match.group(1).strip()
        math[token]='<div class="math-display" data-tex="'+html.escape(tex,quote=True)+'">\\['+html.escape(tex)+'\\]</div>'
        return '\n\n'+token+'\n\n'
    source=re.sub(r'\$\$(.*?)\$\$',display,source,flags=re.S)
    def inline(match):
        token=f'MATHPROTECTED{len(math):06d}TOKEN'
        tex=match.group(1)
        math[token]='<span class="math-inline" data-tex="'+html.escape(tex,quote=True)+'">\\('+html.escape(tex)+'\\)</span>'
        return token
    source=re.sub(r'(?<!\\)\$(?![\s$])([^$\n]+?)(?<!\s)\$(?!\d)',inline,source)
    for token,code in protected.items():source=source.replace(token,code)
    result=markdown.markdown(source,extensions=['tables','fenced_code','sane_lists'])
    for token,markup in math.items():
        if markup.startswith('<div'):result=result.replace('<p>'+token+'</p>',markup)
        result=result.replace(token,markup)
    return result

def render_native_math(soup):
    """Use Pandoc's TeX parser to embed native MathML, without a network runtime."""
    import shutil,subprocess
    from bs4 import BeautifulSoup
    nodes=soup.select('.math-display,.math-inline')
    if not nodes or not shutil.which('pandoc'):return False
    source='\n\n'.join(('$$\n'+n['data-tex']+'\n$$') if 'math-display' in n.get('class',[]) else '$'+n['data-tex']+'$' for n in nodes)
    result=subprocess.run(['pandoc','--from=markdown+tex_math_dollars','--to=html5','--mathml'],input=source,text=True,capture_output=True)
    if result.returncode:return False
    native=BeautifulSoup(result.stdout,'html.parser').find_all('math')
    if len(native)!=len(nodes):
        print('Native math preview unavailable for some formulas; retaining MathJax rendering.')
        return False
    for node,math in zip(nodes,native):node.clear();node.append(math)
    print(f'Embedded {len(nodes)} native MathML formulas in HTML')
    return True
