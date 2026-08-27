async function load(){
 const m=await (await fetch('/api/metrics')).json();
 document.getElementById('metrics').innerHTML=[
  ['Incidents',m.incidents],['Open',m.open_incidents],['Critical Open',m.critical_open],
  ['Projects',m.projects],['At Risk',m.at_risk_projects]
 ].map(x=>`<div class="card"><b>${x[1]}</b>${x[0]}</div>`).join('');

 const inc=await (await fetch('/api/incidents')).json();
 document.getElementById('incidents').innerHTML=inc.map(i=>
 `<tr><td>${i.id}</td><td>${i.title}</td><td><span class="badge">${i.severity}</span></td>
 <td>${i.status}</td><td>${i.owner}</td><td>${i.customer}</td><td>${i.sla_hours}h</td></tr>`).join('');

 const p=await (await fetch('/api/projects')).json();
 document.getElementById('projects').innerHTML=p.map(x=>
 `<div class="item"><b>${x.name}</b><br>Owner: ${x.owner}<br>Progress: ${x.progress}%<br>Status: ${x.status} | Risk: ${x.risk}<br>Due: ${x.due_date}</div>`).join('');

 const a=await (await fetch('/api/activities')).json();
 document.getElementById('activities').innerHTML=a.map(x=>
 `<div class="item"><b>${x.item}</b><br>${x.type} • ${x.owner}<br>Status: ${x.status} • Due: ${x.due_date}</div>`).join('');
}
document.getElementById('incidentForm').addEventListener('submit',async e=>{
 e.preventDefault(); const d=Object.fromEntries(new FormData(e.target));
 const r=await fetch('/api/incidents',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
 document.getElementById('result').textContent=r.ok?'Incident created successfully':'Could not create incident';
 e.target.reset(); load();
});
load();
