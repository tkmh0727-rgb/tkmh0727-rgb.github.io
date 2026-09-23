"""Build the static CV with Python's standard library."""
from pathlib import Path
from html import escape as e
import json
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'data/cv.json').read_text(encoding='utf-8'))

def section(id,title,body,intro=''):
    return f'<section id="{id}" class="cv-section"><h2>{title}</h2>'+ (f'<p class="section-intro">{e(intro)}</p>' if intro else '')+body+'</section>'
def records(items):
    return ''.join(f'<article class="record"><p class="date">{e(x["period"])}</p><div><h3>{e(x["title"])}</h3><p class="subtitle">{e(x["subtitle"])}</p><p>{e(x["description"])}</p></div></article>' for x in items)
def authors(text):
    text=e(text)
    for name in ['Myeonghyeon Kim','Kim Myeonghyeon','김명현']:text=text.replace(name,f'<strong>{name}</strong>')
    return text
def publications(kind):
    items=sorted((p for p in D['publications'] if p['kind']==kind),key=lambda p:-p['year'])
    return ''.join(f'<article class="publication" id="{p["id"]}"><div class="pub-meta"><span class="date">{p["year"]}</span><span class="badge">{e(p["status"])}</span></div><h3>{e(p["title"])}</h3><p class="authors">{authors(p["authors"])}</p><p class="venue">{e(p["venue"])}</p>'+(f'<a class="text-link" href="{e(p["url"])}">DOI ↗</a>' if p.get('url') else '')+'</article>' for p in items)
def projects():
    return ''.join(f'<article class="project" id="{p["id"]}"><div class="pub-meta"><span class="date">{e(p["period"])}</span><span class="badge">{e(p["stage"])}</span></div><h3>{e(p["title"])}</h3><p>{e(p["description"])}</p><ul class="tags">'+''.join(f'<li>{e(t)}</li>' for t in p['tags'])+'</ul></article>' for p in D['projects'])
def skill_list():
    return '<dl class="skills">'+''.join(f'<div><dt>{e(s["title"])}</dt><dd>{e(s["items"])}</dd></div>' for s in D['skills'])+'</dl>'
def page(file,title,body,contents,home=False,description=''):
    nav=''.join(f'<a href="{f}"'+(' aria-current="page"' if file==f else '')+f'>{label}</a>' for f,label in [('index.html','CV'),('research.html','Research'),('projects.html','Projects'),('publications.html','Publications'),('achievements.html','Honors')])
    toc=''.join(f'<a href="#{id}">{label}</a>' for id,label in contents)
    if home:
        hero=f'<div class="identity"><div><p class="eyebrow">Curriculum vitae <span> / </span> {e(D["role"])}</p><h1>{e(D["name"])}<span class="korean" lang="ko">{e(D["korean_name"])}</span></h1><p class="affiliation">{e(D["affiliation"])}<br>Korea Advanced Institute of Science and Technology</p><p class="lead">{e(D["intro"])}</p><div class="hero-links"><a href="mailto:{e(D["email"])}">Email ↗</a><a href="{e(D["github"])}">GitHub ↗</a><a href="#education">Read CV ↓</a></div></div><img class="portrait" src="assets/profile.jpg" width="168" height="210" alt="Portrait of Myeonghyeon Kim"></div>'
    else:hero=f'<p class="eyebrow">Myeonghyeon Kim / Academic CV</p><h1>{e(title)}</h1><p class="lead">{e(description)}</p>'
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{e(description or D['intro'])}"><meta name="theme-color" content="#183d43"><title>{e(title)} | Myeonghyeon Kim</title><link rel="stylesheet" href="theme.css"></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><nav class="nav" aria-label="Main navigation"><a class="brand" href="index.html">MK<span> / Myeonghyeon Kim</span></a><div class="nav-links">{nav}</div></nav></header>
<main id="main"><div class="page-heading">{hero}</div><div class="page-layout"><aside class="contents"><p class="eyebrow">On this page</p><nav aria-label="On this page">{toc}</nav><p class="updated">Updated<br><time datetime="{D['updated']}">{D['updated']}</time></p><p class="print-hint">Print / save PDF<br>Ctrl+P · ⌘P</p></aside><div class="cv-body">{body}</div></div></main>
<footer><span>© 2026 Myeonghyeon Kim</span><a href="index.html#contact">Contact</a><a href="https://github.com/tkmh0727-rgb/tkmh0727-rgb.github.io">Source on GitHub ↗</a></footer></body></html>
'''
    (ROOT/file).write_text(html,encoding='utf-8')
edu=section('education','Education',records(D['education']))
exp=section('experience','Research experience',records(D['experience']))
journal=section('journals','Journal publications',publications('journal'))
conf=section('conferences','Conference contributions',publications('conference'))
drafts=section('manuscripts','Conference manuscripts',publications('manuscript'),'Manuscripts are listed separately from published work and accepted contributions.')
awards=section('awards','Honors & scholarships',records(D['awards']))
training=section('training','Additional education',records(D['training']))
skills=section('skills','Technical skills',skill_list())
research=section('research','Research interests','<p>Autonomous mobile robot navigation · SPaT/R2X communication · Infrastructure-based perception · Vision-language models · Intelligent transportation systems</p><p class="research-note"><span class="badge">Thesis research</span> VLM-based intersection context understanding for AMR crossing decisions.</p><a class="text-link" href="research.html">Research direction ↗</a>')
contact=section('contact','Contact',f'<p>For research collaborations and inquiries:</p><div class="contact-links"><a href="mailto:{e(D["email"])}">{e(D["email"])}</a><a href="{e(D["github"])}">GitHub ↗</a></div>')
page('index.html','Curriculum Vitae',edu+exp+research+journal+conf+drafts+awards+training+skills+contact,[('education','Education'),('experience','Experience'),('research','Research'),('journals','Publications'),('conferences','Conferences'),('manuscripts','Manuscripts'),('awards','Honors'),('training','Education & training'),('skills','Skills'),('contact','Contact')],home=True)
page('publications.html','Publications & presentations',journal+conf+drafts,[('journals','Journal publications'),('conferences','Conferences'),('manuscripts','Manuscripts')],description='Research in robot navigation, intelligent transportation and computer vision. Publication types and contribution status are listed with each entry.')
page('projects.html','Research projects',section('projects','Selected work',projects()),[('projects','Selected work')]+[(p['id'],p['title'].split(' & ')[0]) for p in D['projects'][:6]],description='From infrastructure perception to communication-assisted robot navigation: research prototypes, field experiments and system integration.')
page('achievements.html','Honors & education',awards+training+section('internship','Internship',records(D['experience'][1:])),[('awards','Honors & scholarships'),('training','Additional education'),('internship','Internship')],description='Academic and team awards, merit scholarships, and completed education programs.')
body=section('direction','Research direction','<p>I work on safe AMR navigation at signalized urban intersections, combining infrastructure information with robot perception and motion planning.</p><div class="focus-grid"><article><span class="focus-number">01</span><h3>Communication</h3><p>SPaT/R2X messages provide signal phase and remaining time for crossing decisions.</p></article><article><span class="focus-number">02</span><h3>Navigation</h3><p>ROS 2, localization and Nav2 connect crossing decisions to robot motion.</p></article><article><span class="focus-number">03</span><h3>Context</h3><p>Infrastructure cameras and VLMs support research on scene understanding beyond traffic signals.</p></article></div>')
body+=section('thesis','Master’s thesis research','<span class="badge">Research in progress</span><h3 class="thesis-title">A Study on Intersection Crossing Navigation for Autonomous Mobile Robots Using VLM-Based Intersection Context Understanding</h3><p>Advisor: Prof. Inhi Kim · KAIST</p><p>The research plan investigates pedestrians, vehicles, crosswalk occupancy and occlusion using infrastructure-camera images. The goal is to inform robot waiting, entry and crossing decisions, with evaluation across lighting and mixed-traffic scenarios.</p>')
body+=section('related','Related implementation','<p>Field-tested SPaT crossing decisions, LiDAR navigation, a delivery robot digital twin, and earlier multi-camera tracking and LLM-guided planning experiments.</p><a class="text-link" href="projects.html">Explore the projects ↗</a>')
page('research.html','Robot navigation with infrastructure intelligence',body,[('direction','Research direction'),('thesis','Master’s thesis'),('related','Implementation')],description='Connecting communication, navigation and scene understanding for autonomous mobile robots in urban intersections.')
print('Built 5 static pages from data/cv.json')
