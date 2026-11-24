#!/usr/bin/env python3
"""Generiert didaktische BPMN-2.0-Diagramme für UE 3 als editierbares draw.io und SVG/PNG.
Keine draw.io-Uploads und keine Vorlagen bei eigenständigen Textmodellierungsaufgaben."""
from pathlib import Path
import xml.etree.ElementTree as ET
import html,textwrap
D=Path(__file__).resolve().parents[1]/'assets'/'diagramme';D.mkdir(parents=True,exist_ok=True)
# clean old UE2 diagrams to avoid duplicate outdated assets
for p in D.glob('*'):
 if p.is_file():p.unlink()

NODE_STYLE={'start':'ellipse;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#EAF5FF;strokeColor=#1F4A6D;',
            'end':'ellipse;whiteSpace=wrap;html=1;strokeWidth=6;fillColor=#FFEDEF;strokeColor=#A33349;',
            'task':'rounded=1;arcSize=16;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#F8FCFF;strokeColor=#385D89;',
            'xor':'rhombus;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#FFF3D8;strokeColor=#916B1C;',
            'and':'rhombus;whiteSpace=wrap;html=1;strokeWidth=2;fillColor=#EAF8EF;strokeColor=#287A58;'}
COLORS={'start':'#BDE7FA','end':'#FBD5DA','task':'#F5FAFF','xor':'#FFF1C6','and':'#E0F4E4'}

def textlines(t,width=21):
 return textwrap.wrap(t,width=width,break_long_words=False,break_on_hyphens=False) or ['']

def mkloop(name, start='Druckdatei eingegangen',check='Auflösung prüfen',cond='Auflösung ausreichend?',repair='Datei überarbeiten',yes='Datei freigeben',end='Datei freigegeben',partial=False):
 nodes=[('s','start',start,45,200,52,52),('a','task',check,206,189,150,70),('x','xor',cond,469,194,64,64),('g','task',yes,690,127,168,74),('e','end',end,1003,138,54,54)]
 edges=[('s','a','',None),('a','x','',None),('x','g','Ja',None),('g','e','',None)]
 if not partial:
  nodes.append(('r','task',repair,694,309,164,70))
  edges.extend([('x','r','Nein',None),('r','a','Zurück zur Prüfung',[(775,417),(280,417)])])
 return (1250,490,nodes,edges)

def mkparallel(name, start='Auftrag freigegeben', t1='Druckdatei fertigstellen',t2='Textilien bereitstellen',action='Druck starten',end='Druck gestartet',bad=False):
 nodes=[('s','start',start,38,230,54,54),('split','xor' if bad else 'and','',211,223,65,65),('t1','task',t1,413,105,182,71),('t2','task',t2,413,335,182,71),('join','xor' if bad else 'and','',744,223,65,65),('act','task',action,895,225,173,70),('e','end',end,1165,234,54,54)]
 edges=[('s','split','',None),('split','t1','',[(333,141)]),('split','t2','',[(333,371)]),('t1','join','',[(678,141)]),('t2','join','',[(678,371)]),('join','act','',None),('act','e','',None)]
 return (1330,515,nodes,edges)

def mkcombined(name,start='Bestellung eingegangen', check='Druckdatei prüfen',cond='druckbar?',repair='Datei überarbeiten',task1='Druckdaten vorbereiten',task2='Hoodies bereitstellen',action='Druck starten',end='Druck gestartet'):
 nodes=[('s','start',start,30,225,55,55),('c','task',check,169,217,150,73),('x','xor',cond,375,221,66,66),('r','task',repair,362,408,160,70),('split','and','',566,221,66,66),('t1','task',task1,731,112,172,72),('t2','task',task2,731,335,172,72),('join','and','',995,220,66,66),('act','task',action,1120,219,164,72),('end','end',end,1392,229,55,55)]
 edges=[('s','c','',None),('c','x','',None),('x','r','Nein',[(409,347)]),('r','c','Zurück zur Prüfung',[(440,516),(244,516)]),('x','split','Ja',None),('split','t1','',[(670,148)]),('split','t2','',[(670,371)]),('t1','join','',[(949,148)]),('t2','join','',[(949,371)]),('join','act','',None),('act','end','',None)]
 return (1560,575,nodes,edges)

def draw_xml(name,spec):
 width,height,nodes,edges=spec
 mx=ET.Element('mxfile',host='app.diagrams.net',modified='2026-11-24T09:00:00.000Z',agent='BPMN-Labor UE3',version='24.7.17',type='device')
 diag=ET.SubElement(mx,'diagram',id=name,name='BPMN');model=ET.SubElement(diag,'mxGraphModel',dx='1800',dy='900',grid='1',gridSize='10',guides='1',tooltips='1',connect='1',arrows='1',fold='1',page='1',pageScale='1',pageWidth=str(width),pageHeight=str(height),math='0',shadow='0');rt=ET.SubElement(model,'root');ET.SubElement(rt,'mxCell',id='0');ET.SubElement(rt,'mxCell',id='1',parent='0')
 for id,typ,txt,x,y,w,h in nodes:
  lab=txt if typ=='task' else {'start':'','end':'','xor':'X','and':'+'}[typ]
  style=NODE_STYLE[typ]
  if typ in ('xor','and'):style+='fontSize=30;fontStyle=1;align=center;verticalAlign=middle;'
  if typ=='task':style+='fontSize=14;align=center;verticalAlign=middle;'
  c=ET.SubElement(rt,'mxCell',id=id,value=lab,style=style,vertex='1',parent='1');ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
  if typ!='task' and txt:
   # put labels below diagram symbols
   lc=ET.SubElement(rt,'mxCell',id='label-'+id,value=txt,style='text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;fontSize=12;fontColor=#34425F;',vertex='1',parent='1');ET.SubElement(lc,'mxGeometry',x=str(x-55),y=str(y+h+4),width=str(w+110),height='37',attrib={'as':'geometry'})
 for i,(s,t,label,waypoints) in enumerate(edges):
  c=ET.SubElement(rt,'mxCell',id=f'flow-{i}',value=label,style='edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;rounded=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#314668;fontColor=#254B74;fontSize=12;labelBackgroundColor=#ffffff;',edge='1',parent='1',source=s,target=t)
  g=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
  if waypoints:
   ar=ET.SubElement(g,'Array',attrib={'as':'points'})
   for x,y in waypoints:ET.SubElement(ar,'mxPoint',x=str(x),y=str(y))
 return ET.tostring(mx,encoding='unicode',xml_declaration=True)

def svg(name,spec):
 width,height,nodes,edges=spec;by={n[0]:n for n in nodes}; parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#314668"/></marker></defs>',
 f'<rect width="{width}" height="{height}" rx="18" fill="#F8FAFF"/><rect x="10" y="10" width="{width-20}" height="{height-20}" rx="15" fill="none" stroke="#E0E8F4"/>']
 # draw edges first
 def ports(n1,n2,way):
  _,_,_,x,y,w,h=n1;_,_,_,x2,y2,w2,h2=n2
  if way:
   # reverse feedback to top of check for loop
   if n1[0]=='r' and n2[0] in ['a','c']:
    return [(x+w/2,y+h),*way,(x2+w2/2,y2+h)]
   return [(x+w/2 if n1[0] in ('split',) else x+w, y+h/2),*way,(x2, y2+h2/2)]
  return [(x+w,y+h/2),(x2,y2+h2/2)]
 for a,b,label,way in edges:
  pts=ports(by[a],by[b],way)
  # edges from top/bottom branch: go orthogonally via intermediate points and last position
  path='M '+' L '.join(f'{x:.0f},{y:.0f}' for x,y in pts)
  parts.append(f'<path d="{path}" fill="none" stroke="#314668" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"/>')
  if label:
   xx,yy=(pts[0][0]+pts[1][0])/2,(pts[0][1]+pts[1][1])/2
   if label.startswith('Zurück'):xx,yy=way[0][0]-85,way[0][1]-8
   parts.append(f'<text x="{xx:.0f}" y="{yy-10:.0f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#315C88">{html.escape(label)}</text>')
 # nodes
 for id,typ,txt,x,y,w,h in nodes:
  cx,cy=x+w/2,y+h/2
  if typ in ('start','end'):
   parts.append(f'<circle cx="{cx}" cy="{cy}" r="{w/2-4}" fill="{COLORS[typ]}" stroke="{("#A33349" if typ=="end" else "#1F4A6D")}" stroke-width="{6 if typ=="end" else 3}"/>')
  elif typ=='task':parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{COLORS[typ]}" stroke="#385D89" stroke-width="2.5"/>')
  else:
   parts.append(f'<path d="M {cx} {y+3} L {x+w-3} {cy} L {cx} {y+h-3} L {x+3} {cy} Z" fill="{COLORS[typ]}" stroke="{("#916B1C" if typ=="xor" else "#287A58")}" stroke-width="2.5"/>')
   parts.append(f'<text x="{cx}" y="{cy+11}" text-anchor="middle" font-family="Arial,sans-serif" font-size="34" font-weight="bold" fill="#30405F">{"X" if typ=="xor" else "+"}</text>')
  if typ=='task':
   lines=textlines(txt,19)
   for i,ln in enumerate(lines):parts.append(f'<text x="{cx}" y="{cy+(i-(len(lines)-1)/2)*18+5:.0f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" fill="#253653">{html.escape(ln)}</text>')
  elif txt:
   lines=textlines(txt,26)
   for i,ln in enumerate(lines):parts.append(f'<text x="{cx}" y="{y+h+23+i*16}" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#394B68">{html.escape(ln)}</text>')
 parts.append('</svg>');return '\n'.join(parts)

DGRAMS={
 'loesung-schleife':mkloop('loesung-schleife'),
 'loesung-parallel':mkparallel('loesung-parallel',start='Messeauftritt freigegeben',t1='Folien erstellen',t2='Infomaterial bestellen',action='Stand vorbereiten',end='Stand vorbereitet'),
 'loesung-kombi':mkcombined('loesung-kombi',start='Entwurf vorhanden',check='Entwurf prüfen',cond='geeignet?',repair='Entwurf überarbeiten',task1='Einladung vorbereiten',task2='Raumplanung erstellen',action='Veranstaltung freigeben',end='Veranstaltung freigegeben'),
 'aufgabe-fehler-ue3':mkparallel('aufgabe-fehler-ue3',bad=True),
 'loesung-fehler-ue3':mkparallel('loesung-fehler-ue3'),
 'aufgabe-erweitern':mkloop('aufgabe-erweitern',check='Motiv prüfen',cond='geeignet?',yes='Druckauftrag freigeben',end='Auftrag freigegeben',partial=True),
 'loesung-erweitern':mkcombined('loesung-erweitern',check='Motiv prüfen',cond='geeignet?',repair='Motiv überarbeiten',task1='Datei vorbereiten',task2='Material bereitstellen',action='Druckauftrag freigeben',end='Auftrag freigegeben'),
 'loesung-lk-campus':mkcombined('loesung-lk-campus',start='Sammelbestellung eingegangen',check='Druckdatei prüfen',cond='druckbar?',repair='Druckdatei überarbeiten',task1='Druckdaten vorbereiten',task2='Hoodies zusammenstellen',action='Druck starten',end='Druck gestartet'),
 'loesung-lk-trikot':mkcombined('loesung-lk-trikot',start='Trikotauftrag eingegangen',check='Entwurf prüfen',cond='fehlerfrei?',repair='Entwurf überarbeiten',task1='Größenliste überprüfen',task2='Druckmaterial bereitstellen',action='Produktion starten',end='Produktion gestartet'),
 'loesung-bonus-retoure':mkcombined('loesung-bonus-retoure',start='Retoure eingegangen',check='Angaben prüfen',cond='vollständig?',repair='Angaben nachfordern',task1='Ware prüfen',task2='Erstattung vorbereiten',action='Rückzahlung freigeben',end='Rückzahlung freigegeben'),
 'loesung-test':mkcombined('loesung-test',start='Entwurf vorhanden',check='Entwurf prüfen',cond='korrekt?',repair='Entwurf überarbeiten',task1='Werbematerial vorbereiten',task2='Raumplanung erstellen',action='Veranstaltung freigeben',end='Veranstaltung freigegeben')
}
for name,spec in DGRAMS.items():
 (D/f'{name}.svg').write_text(svg(name,spec),encoding='utf-8')
 (D/f'{name}.drawio').write_text(draw_xml(name,spec),encoding='utf-8')
try:
 import cairosvg
 for p in D.glob('*.svg'):cairosvg.svg2png(url=str(p),write_to=str(p.with_suffix('.png')),output_width=1400)
except ImportError:print('cairosvg nicht vorhanden: PNG optional')
print('Diagramme:',len(DGRAMS),'Dateien',len(list(D.iterdir())))
