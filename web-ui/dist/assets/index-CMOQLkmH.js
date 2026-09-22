(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const s of document.querySelectorAll('link[rel="modulepreload"]'))i(s);new MutationObserver(s=>{for(const r of s)if(r.type==="childList")for(const a of r.addedNodes)a.tagName==="LINK"&&a.rel==="modulepreload"&&i(a)}).observe(document,{childList:!0,subtree:!0});function e(s){const r={};return s.integrity&&(r.integrity=s.integrity),s.referrerPolicy&&(r.referrerPolicy=s.referrerPolicy),s.crossOrigin==="use-credentials"?r.credentials="include":s.crossOrigin==="anonymous"?r.credentials="omit":r.credentials="same-origin",r}function i(s){if(s.ep)return;s.ep=!0;const r=e(s);fetch(s.href,r)}})();let Fn=null;async function od(){if(Fn)return Fn;try{const n=await fetch("/api/config");if(n.ok)return Fn=await n.json(),Fn}catch{}try{const n=await fetch("/config.json");if(n.ok)return Fn=await n.json(),Fn}catch{}return Fn={name:"HOUDINI",agent:{name:"HOUDINI",emoji:"🤖",skills:[]},theme:{}},Fn}function Yr(){return Fn}function ra(n,t,e){t/=100,e/=100;const i=a=>(a+n/30)%12,s=t*Math.min(e,1-e),r=a=>e-s*Math.max(-1,Math.min(i(a)-3,Math.min(9-i(a),1)));return{r:Math.round(255*r(0)),g:Math.round(255*r(8)),b:Math.round(255*r(4))}}function eu(n){const t=document.documentElement;t.style.setProperty("--hue",n);const e=ra(n,100,63);t.style.setProperty("--accent-r",e.r),t.style.setProperty("--accent-g",e.g),t.style.setProperty("--accent-b",e.b),t.style.setProperty("--accent-rgb",`${e.r}, ${e.g}, ${e.b}`);const i=ra(n,62,47);t.style.setProperty("--accent-secondary-rgb",`${i.r}, ${i.g}, ${i.b}`);const s=ra(n,100,84);t.style.setProperty("--accent-tertiary-rgb",`${s.r}, ${s.g}, ${s.b}`),localStorage.setItem("jarvis-theme-hue",n),window.dispatchEvent(new CustomEvent("theme-change",{detail:{hue:n,primary:{r:e.r,g:e.g,b:e.b},secondary:{r:i.r,g:i.g,b:i.b},tertiary:{r:s.r,g:s.g,b:s.b}}}))}function Cs(){const n=localStorage.getItem("jarvis-theme-hue");return n?parseInt(n,10):5}function Bs(){return getComputedStyle(document.documentElement).getPropertyValue("--accent-rgb").trim()}function ld(){const n=Bs(),[t,e,i]=n.split(",").map(s=>parseInt(s.trim(),10));return{r:t,g:e,b:i}}function Ko(){const{r:n,g:t,b:e}=ld();return`#${[n,t,e].map(i=>i.toString(16).padStart(2,"0")).join("")}`}function Al(){const n=Cs();eu(n)}const cd=[{name:"紅色",emoji:"🔴",hue:5},{name:"橙色",emoji:"🟠",hue:30},{name:"綠色",emoji:"🟢",hue:140},{name:"青色",emoji:"🩵",hue:180},{name:"藍色",emoji:"🔵",hue:220},{name:"紫色",emoji:"🟣",hue:270}];const Zo="175",ji={ROTATE:0,DOLLY:1,PAN:2},Wi={ROTATE:0,PAN:1,DOLLY_PAN:2,DOLLY_ROTATE:3},ud=0,wl=1,dd=2,nu=1,hd=2,Bn=3,oi=0,Le=1,zn=2,ri=0,Ki=1,Fr=2,Rl=3,Cl=4,fd=5,_i=100,pd=101,md=102,gd=103,_d=104,vd=200,xd=201,Sd=202,yd=203,Ja=204,Qa=205,Ed=206,Md=207,Td=208,bd=209,Ad=210,wd=211,Rd=212,Cd=213,Pd=214,to=0,eo=1,no=2,es=3,io=4,so=5,ro=6,ao=7,iu=0,Ld=1,Dd=2,ai=0,Id=1,Ud=2,Nd=3,Od=4,Fd=5,Bd=6,zd=7,su=300,ns=301,is=302,oo=303,lo=304,jr=306,co=1e3,xi=1001,uo=1002,gn=1003,kd=1004,Ys=1005,Rn=1006,aa=1007,Si=1008,Wn=1009,ru=1010,au=1011,Ps=1012,Jo=1013,Mi=1014,Hn=1015,zs=1016,Qo=1017,tl=1018,Ls=1020,ou=35902,lu=1021,cu=1022,pn=1023,uu=1024,du=1025,Ds=1026,Is=1027,hu=1028,el=1029,fu=1030,nl=1031,il=1033,br=33776,Ar=33777,wr=33778,Rr=33779,ho=35840,fo=35841,po=35842,mo=35843,go=36196,_o=37492,vo=37496,xo=37808,So=37809,yo=37810,Eo=37811,Mo=37812,To=37813,bo=37814,Ao=37815,wo=37816,Ro=37817,Co=37818,Po=37819,Lo=37820,Do=37821,Cr=36492,Io=36494,Uo=36495,pu=36283,No=36284,Oo=36285,Fo=36286,Hd=3200,Vd=3201,Gd=0,Wd=1,ni="",Qe="srgb",ss="srgb-linear",Br="linear",Yt="srgb",Ci=7680,Pl=519,Xd=512,$d=513,qd=514,mu=515,Yd=516,jd=517,Kd=518,Zd=519,Ll=35044,Dl="300 es",Vn=2e3,zr=2001;class wi{addEventListener(t,e){this._listeners===void 0&&(this._listeners={});const i=this._listeners;i[t]===void 0&&(i[t]=[]),i[t].indexOf(e)===-1&&i[t].push(e)}hasEventListener(t,e){const i=this._listeners;return i===void 0?!1:i[t]!==void 0&&i[t].indexOf(e)!==-1}removeEventListener(t,e){const i=this._listeners;if(i===void 0)return;const s=i[t];if(s!==void 0){const r=s.indexOf(e);r!==-1&&s.splice(r,1)}}dispatchEvent(t){const e=this._listeners;if(e===void 0)return;const i=e[t.type];if(i!==void 0){t.target=this;const s=i.slice(0);for(let r=0,a=s.length;r<a;r++)s[r].call(this,t);t.target=null}}}const Ae=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],Pr=Math.PI/180,Bo=180/Math.PI;function ks(){const n=Math.random()*4294967295|0,t=Math.random()*4294967295|0,e=Math.random()*4294967295|0,i=Math.random()*4294967295|0;return(Ae[n&255]+Ae[n>>8&255]+Ae[n>>16&255]+Ae[n>>24&255]+"-"+Ae[t&255]+Ae[t>>8&255]+"-"+Ae[t>>16&15|64]+Ae[t>>24&255]+"-"+Ae[e&63|128]+Ae[e>>8&255]+"-"+Ae[e>>16&255]+Ae[e>>24&255]+Ae[i&255]+Ae[i>>8&255]+Ae[i>>16&255]+Ae[i>>24&255]).toLowerCase()}function Nt(n,t,e){return Math.max(t,Math.min(e,n))}function Jd(n,t){return(n%t+t)%t}function oa(n,t,e){return(1-e)*n+e*t}function cs(n,t){switch(t.constructor){case Float32Array:return n;case Uint32Array:return n/4294967295;case Uint16Array:return n/65535;case Uint8Array:return n/255;case Int32Array:return Math.max(n/2147483647,-1);case Int16Array:return Math.max(n/32767,-1);case Int8Array:return Math.max(n/127,-1);default:throw new Error("Invalid component type.")}}function Ie(n,t){switch(t.constructor){case Float32Array:return n;case Uint32Array:return Math.round(n*4294967295);case Uint16Array:return Math.round(n*65535);case Uint8Array:return Math.round(n*255);case Int32Array:return Math.round(n*2147483647);case Int16Array:return Math.round(n*32767);case Int8Array:return Math.round(n*127);default:throw new Error("Invalid component type.")}}const Qd={DEG2RAD:Pr};class Tt{constructor(t=0,e=0){Tt.prototype.isVector2=!0,this.x=t,this.y=e}get width(){return this.x}set width(t){this.x=t}get height(){return this.y}set height(t){this.y=t}set(t,e){return this.x=t,this.y=e,this}setScalar(t){return this.x=t,this.y=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y)}copy(t){return this.x=t.x,this.y=t.y,this}add(t){return this.x+=t.x,this.y+=t.y,this}addScalar(t){return this.x+=t,this.y+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this}subScalar(t){return this.x-=t,this.y-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this}multiply(t){return this.x*=t.x,this.y*=t.y,this}multiplyScalar(t){return this.x*=t,this.y*=t,this}divide(t){return this.x/=t.x,this.y/=t.y,this}divideScalar(t){return this.multiplyScalar(1/t)}applyMatrix3(t){const e=this.x,i=this.y,s=t.elements;return this.x=s[0]*e+s[3]*i+s[6],this.y=s[1]*e+s[4]*i+s[7],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this}clamp(t,e){return this.x=Nt(this.x,t.x,e.x),this.y=Nt(this.y,t.y,e.y),this}clampScalar(t,e){return this.x=Nt(this.x,t,e),this.y=Nt(this.y,t,e),this}clampLength(t,e){const i=this.length();return this.divideScalar(i||1).multiplyScalar(Nt(i,t,e))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(t){return this.x*t.x+this.y*t.y}cross(t){return this.x*t.y-this.y*t.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(t){const e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;const i=this.dot(t)/e;return Math.acos(Nt(i,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){const e=this.x-t.x,i=this.y-t.y;return e*e+i*i}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this}lerpVectors(t,e,i){return this.x=t.x+(e.x-t.x)*i,this.y=t.y+(e.y-t.y)*i,this}equals(t){return t.x===this.x&&t.y===this.y}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this}rotateAround(t,e){const i=Math.cos(e),s=Math.sin(e),r=this.x-t.x,a=this.y-t.y;return this.x=r*i-a*s+t.x,this.y=r*s+a*i+t.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}}class Pt{constructor(t,e,i,s,r,a,o,l,c){Pt.prototype.isMatrix3=!0,this.elements=[1,0,0,0,1,0,0,0,1],t!==void 0&&this.set(t,e,i,s,r,a,o,l,c)}set(t,e,i,s,r,a,o,l,c){const u=this.elements;return u[0]=t,u[1]=s,u[2]=o,u[3]=e,u[4]=r,u[5]=l,u[6]=i,u[7]=a,u[8]=c,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(t){const e=this.elements,i=t.elements;return e[0]=i[0],e[1]=i[1],e[2]=i[2],e[3]=i[3],e[4]=i[4],e[5]=i[5],e[6]=i[6],e[7]=i[7],e[8]=i[8],this}extractBasis(t,e,i){return t.setFromMatrix3Column(this,0),e.setFromMatrix3Column(this,1),i.setFromMatrix3Column(this,2),this}setFromMatrix4(t){const e=t.elements;return this.set(e[0],e[4],e[8],e[1],e[5],e[9],e[2],e[6],e[10]),this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){const i=t.elements,s=e.elements,r=this.elements,a=i[0],o=i[3],l=i[6],c=i[1],u=i[4],d=i[7],h=i[2],p=i[5],_=i[8],S=s[0],m=s[3],f=s[6],b=s[1],M=s[4],y=s[7],P=s[2],R=s[5],A=s[8];return r[0]=a*S+o*b+l*P,r[3]=a*m+o*M+l*R,r[6]=a*f+o*y+l*A,r[1]=c*S+u*b+d*P,r[4]=c*m+u*M+d*R,r[7]=c*f+u*y+d*A,r[2]=h*S+p*b+_*P,r[5]=h*m+p*M+_*R,r[8]=h*f+p*y+_*A,this}multiplyScalar(t){const e=this.elements;return e[0]*=t,e[3]*=t,e[6]*=t,e[1]*=t,e[4]*=t,e[7]*=t,e[2]*=t,e[5]*=t,e[8]*=t,this}determinant(){const t=this.elements,e=t[0],i=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],u=t[8];return e*a*u-e*o*c-i*r*u+i*o*l+s*r*c-s*a*l}invert(){const t=this.elements,e=t[0],i=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],u=t[8],d=u*a-o*c,h=o*l-u*r,p=c*r-a*l,_=e*d+i*h+s*p;if(_===0)return this.set(0,0,0,0,0,0,0,0,0);const S=1/_;return t[0]=d*S,t[1]=(s*c-u*i)*S,t[2]=(o*i-s*a)*S,t[3]=h*S,t[4]=(u*e-s*l)*S,t[5]=(s*r-o*e)*S,t[6]=p*S,t[7]=(i*l-c*e)*S,t[8]=(a*e-i*r)*S,this}transpose(){let t;const e=this.elements;return t=e[1],e[1]=e[3],e[3]=t,t=e[2],e[2]=e[6],e[6]=t,t=e[5],e[5]=e[7],e[7]=t,this}getNormalMatrix(t){return this.setFromMatrix4(t).invert().transpose()}transposeIntoArray(t){const e=this.elements;return t[0]=e[0],t[1]=e[3],t[2]=e[6],t[3]=e[1],t[4]=e[4],t[5]=e[7],t[6]=e[2],t[7]=e[5],t[8]=e[8],this}setUvTransform(t,e,i,s,r,a,o){const l=Math.cos(r),c=Math.sin(r);return this.set(i*l,i*c,-i*(l*a+c*o)+a+t,-s*c,s*l,-s*(-c*a+l*o)+o+e,0,0,1),this}scale(t,e){return this.premultiply(la.makeScale(t,e)),this}rotate(t){return this.premultiply(la.makeRotation(-t)),this}translate(t,e){return this.premultiply(la.makeTranslation(t,e)),this}makeTranslation(t,e){return t.isVector2?this.set(1,0,t.x,0,1,t.y,0,0,1):this.set(1,0,t,0,1,e,0,0,1),this}makeRotation(t){const e=Math.cos(t),i=Math.sin(t);return this.set(e,-i,0,i,e,0,0,0,1),this}makeScale(t,e){return this.set(t,0,0,0,e,0,0,0,1),this}equals(t){const e=this.elements,i=t.elements;for(let s=0;s<9;s++)if(e[s]!==i[s])return!1;return!0}fromArray(t,e=0){for(let i=0;i<9;i++)this.elements[i]=t[i+e];return this}toArray(t=[],e=0){const i=this.elements;return t[e]=i[0],t[e+1]=i[1],t[e+2]=i[2],t[e+3]=i[3],t[e+4]=i[4],t[e+5]=i[5],t[e+6]=i[6],t[e+7]=i[7],t[e+8]=i[8],t}clone(){return new this.constructor().fromArray(this.elements)}}const la=new Pt;function gu(n){for(let t=n.length-1;t>=0;--t)if(n[t]>=65535)return!0;return!1}function kr(n){return document.createElementNS("http://www.w3.org/1999/xhtml",n)}function th(){const n=kr("canvas");return n.style.display="block",n}const Il={};function Lr(n){n in Il||(Il[n]=!0,console.warn(n))}function eh(n,t,e){return new Promise(function(i,s){function r(){switch(n.clientWaitSync(t,n.SYNC_FLUSH_COMMANDS_BIT,0)){case n.WAIT_FAILED:s();break;case n.TIMEOUT_EXPIRED:setTimeout(r,e);break;default:i()}}setTimeout(r,e)})}function nh(n){const t=n.elements;t[2]=.5*t[2]+.5*t[3],t[6]=.5*t[6]+.5*t[7],t[10]=.5*t[10]+.5*t[11],t[14]=.5*t[14]+.5*t[15]}function ih(n){const t=n.elements;t[11]===-1?(t[10]=-t[10]-1,t[14]=-t[14]):(t[10]=-t[10],t[14]=-t[14]+1)}const Ul=new Pt().set(.4123908,.3575843,.1804808,.212639,.7151687,.0721923,.0193308,.1191948,.9505322),Nl=new Pt().set(3.2409699,-1.5373832,-.4986108,-.9692436,1.8759675,.0415551,.0556301,-.203977,1.0569715);function sh(){const n={enabled:!0,workingColorSpace:ss,spaces:{},convert:function(s,r,a){return this.enabled===!1||r===a||!r||!a||(this.spaces[r].transfer===Yt&&(s.r=Gn(s.r),s.g=Gn(s.g),s.b=Gn(s.b)),this.spaces[r].primaries!==this.spaces[a].primaries&&(s.applyMatrix3(this.spaces[r].toXYZ),s.applyMatrix3(this.spaces[a].fromXYZ)),this.spaces[a].transfer===Yt&&(s.r=Zi(s.r),s.g=Zi(s.g),s.b=Zi(s.b))),s},fromWorkingColorSpace:function(s,r){return this.convert(s,this.workingColorSpace,r)},toWorkingColorSpace:function(s,r){return this.convert(s,r,this.workingColorSpace)},getPrimaries:function(s){return this.spaces[s].primaries},getTransfer:function(s){return s===ni?Br:this.spaces[s].transfer},getLuminanceCoefficients:function(s,r=this.workingColorSpace){return s.fromArray(this.spaces[r].luminanceCoefficients)},define:function(s){Object.assign(this.spaces,s)},_getMatrix:function(s,r,a){return s.copy(this.spaces[r].toXYZ).multiply(this.spaces[a].fromXYZ)},_getDrawingBufferColorSpace:function(s){return this.spaces[s].outputColorSpaceConfig.drawingBufferColorSpace},_getUnpackColorSpace:function(s=this.workingColorSpace){return this.spaces[s].workingColorSpaceConfig.unpackColorSpace}},t=[.64,.33,.3,.6,.15,.06],e=[.2126,.7152,.0722],i=[.3127,.329];return n.define({[ss]:{primaries:t,whitePoint:i,transfer:Br,toXYZ:Ul,fromXYZ:Nl,luminanceCoefficients:e,workingColorSpaceConfig:{unpackColorSpace:Qe},outputColorSpaceConfig:{drawingBufferColorSpace:Qe}},[Qe]:{primaries:t,whitePoint:i,transfer:Yt,toXYZ:Ul,fromXYZ:Nl,luminanceCoefficients:e,outputColorSpaceConfig:{drawingBufferColorSpace:Qe}}}),n}const Gt=sh();function Gn(n){return n<.04045?n*.0773993808:Math.pow(n*.9478672986+.0521327014,2.4)}function Zi(n){return n<.0031308?n*12.92:1.055*Math.pow(n,.41666)-.055}let Pi;class rh{static getDataURL(t,e="image/png"){if(/^data:/i.test(t.src)||typeof HTMLCanvasElement>"u")return t.src;let i;if(t instanceof HTMLCanvasElement)i=t;else{Pi===void 0&&(Pi=kr("canvas")),Pi.width=t.width,Pi.height=t.height;const s=Pi.getContext("2d");t instanceof ImageData?s.putImageData(t,0,0):s.drawImage(t,0,0,t.width,t.height),i=Pi}return i.toDataURL(e)}static sRGBToLinear(t){if(typeof HTMLImageElement<"u"&&t instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&t instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&t instanceof ImageBitmap){const e=kr("canvas");e.width=t.width,e.height=t.height;const i=e.getContext("2d");i.drawImage(t,0,0,t.width,t.height);const s=i.getImageData(0,0,t.width,t.height),r=s.data;for(let a=0;a<r.length;a++)r[a]=Gn(r[a]/255)*255;return i.putImageData(s,0,0),e}else if(t.data){const e=t.data.slice(0);for(let i=0;i<e.length;i++)e instanceof Uint8Array||e instanceof Uint8ClampedArray?e[i]=Math.floor(Gn(e[i]/255)*255):e[i]=Gn(e[i]);return{data:e,width:t.width,height:t.height}}else return console.warn("THREE.ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),t}}let ah=0;class sl{constructor(t=null){this.isSource=!0,Object.defineProperty(this,"id",{value:ah++}),this.uuid=ks(),this.data=t,this.dataReady=!0,this.version=0}set needsUpdate(t){t===!0&&this.version++}toJSON(t){const e=t===void 0||typeof t=="string";if(!e&&t.images[this.uuid]!==void 0)return t.images[this.uuid];const i={uuid:this.uuid,url:""},s=this.data;if(s!==null){let r;if(Array.isArray(s)){r=[];for(let a=0,o=s.length;a<o;a++)s[a].isDataTexture?r.push(ca(s[a].image)):r.push(ca(s[a]))}else r=ca(s);i.url=r}return e||(t.images[this.uuid]=i),i}}function ca(n){return typeof HTMLImageElement<"u"&&n instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&n instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&n instanceof ImageBitmap?rh.getDataURL(n):n.data?{data:Array.from(n.data),width:n.width,height:n.height,type:n.data.constructor.name}:(console.warn("THREE.Texture: Unable to serialize Texture."),{})}let oh=0;class Be extends wi{constructor(t=Be.DEFAULT_IMAGE,e=Be.DEFAULT_MAPPING,i=xi,s=xi,r=Rn,a=Si,o=pn,l=Wn,c=Be.DEFAULT_ANISOTROPY,u=ni){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:oh++}),this.uuid=ks(),this.name="",this.source=new sl(t),this.mipmaps=[],this.mapping=e,this.channel=0,this.wrapS=i,this.wrapT=s,this.magFilter=r,this.minFilter=a,this.anisotropy=c,this.format=o,this.internalFormat=null,this.type=l,this.offset=new Tt(0,0),this.repeat=new Tt(1,1),this.center=new Tt(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new Pt,this.generateMipmaps=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,this.colorSpace=u,this.userData={},this.version=0,this.onUpdate=null,this.renderTarget=null,this.isRenderTargetTexture=!1,this.pmremVersion=0}get image(){return this.source.data}set image(t=null){this.source.data=t}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}clone(){return new this.constructor().copy(this)}copy(t){return this.name=t.name,this.source=t.source,this.mipmaps=t.mipmaps.slice(0),this.mapping=t.mapping,this.channel=t.channel,this.wrapS=t.wrapS,this.wrapT=t.wrapT,this.magFilter=t.magFilter,this.minFilter=t.minFilter,this.anisotropy=t.anisotropy,this.format=t.format,this.internalFormat=t.internalFormat,this.type=t.type,this.offset.copy(t.offset),this.repeat.copy(t.repeat),this.center.copy(t.center),this.rotation=t.rotation,this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrix.copy(t.matrix),this.generateMipmaps=t.generateMipmaps,this.premultiplyAlpha=t.premultiplyAlpha,this.flipY=t.flipY,this.unpackAlignment=t.unpackAlignment,this.colorSpace=t.colorSpace,this.renderTarget=t.renderTarget,this.isRenderTargetTexture=t.isRenderTargetTexture,this.userData=JSON.parse(JSON.stringify(t.userData)),this.needsUpdate=!0,this}toJSON(t){const e=t===void 0||typeof t=="string";if(!e&&t.textures[this.uuid]!==void 0)return t.textures[this.uuid];const i={metadata:{version:4.6,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(t).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(i.userData=this.userData),e||(t.textures[this.uuid]=i),i}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(t){if(this.mapping!==su)return t;if(t.applyMatrix3(this.matrix),t.x<0||t.x>1)switch(this.wrapS){case co:t.x=t.x-Math.floor(t.x);break;case xi:t.x=t.x<0?0:1;break;case uo:Math.abs(Math.floor(t.x)%2)===1?t.x=Math.ceil(t.x)-t.x:t.x=t.x-Math.floor(t.x);break}if(t.y<0||t.y>1)switch(this.wrapT){case co:t.y=t.y-Math.floor(t.y);break;case xi:t.y=t.y<0?0:1;break;case uo:Math.abs(Math.floor(t.y)%2)===1?t.y=Math.ceil(t.y)-t.y:t.y=t.y-Math.floor(t.y);break}return this.flipY&&(t.y=1-t.y),t}set needsUpdate(t){t===!0&&(this.version++,this.source.needsUpdate=!0)}set needsPMREMUpdate(t){t===!0&&this.pmremVersion++}}Be.DEFAULT_IMAGE=null;Be.DEFAULT_MAPPING=su;Be.DEFAULT_ANISOTROPY=1;class Kt{constructor(t=0,e=0,i=0,s=1){Kt.prototype.isVector4=!0,this.x=t,this.y=e,this.z=i,this.w=s}get width(){return this.z}set width(t){this.z=t}get height(){return this.w}set height(t){this.w=t}set(t,e,i,s){return this.x=t,this.y=e,this.z=i,this.w=s,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this.w=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setW(t){return this.w=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;case 3:this.w=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this.w=t.w!==void 0?t.w:1,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this.w+=t.w,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this.w+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this.w=t.w+e.w,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this.w+=t.w*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this.w-=t.w,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this.w-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this.w=t.w-e.w,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this.w*=t.w,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this.w*=t,this}applyMatrix4(t){const e=this.x,i=this.y,s=this.z,r=this.w,a=t.elements;return this.x=a[0]*e+a[4]*i+a[8]*s+a[12]*r,this.y=a[1]*e+a[5]*i+a[9]*s+a[13]*r,this.z=a[2]*e+a[6]*i+a[10]*s+a[14]*r,this.w=a[3]*e+a[7]*i+a[11]*s+a[15]*r,this}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this.w/=t.w,this}divideScalar(t){return this.multiplyScalar(1/t)}setAxisAngleFromQuaternion(t){this.w=2*Math.acos(t.w);const e=Math.sqrt(1-t.w*t.w);return e<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=t.x/e,this.y=t.y/e,this.z=t.z/e),this}setAxisAngleFromRotationMatrix(t){let e,i,s,r;const l=t.elements,c=l[0],u=l[4],d=l[8],h=l[1],p=l[5],_=l[9],S=l[2],m=l[6],f=l[10];if(Math.abs(u-h)<.01&&Math.abs(d-S)<.01&&Math.abs(_-m)<.01){if(Math.abs(u+h)<.1&&Math.abs(d+S)<.1&&Math.abs(_+m)<.1&&Math.abs(c+p+f-3)<.1)return this.set(1,0,0,0),this;e=Math.PI;const M=(c+1)/2,y=(p+1)/2,P=(f+1)/2,R=(u+h)/4,A=(d+S)/4,I=(_+m)/4;return M>y&&M>P?M<.01?(i=0,s=.707106781,r=.707106781):(i=Math.sqrt(M),s=R/i,r=A/i):y>P?y<.01?(i=.707106781,s=0,r=.707106781):(s=Math.sqrt(y),i=R/s,r=I/s):P<.01?(i=.707106781,s=.707106781,r=0):(r=Math.sqrt(P),i=A/r,s=I/r),this.set(i,s,r,e),this}let b=Math.sqrt((m-_)*(m-_)+(d-S)*(d-S)+(h-u)*(h-u));return Math.abs(b)<.001&&(b=1),this.x=(m-_)/b,this.y=(d-S)/b,this.z=(h-u)/b,this.w=Math.acos((c+p+f-1)/2),this}setFromMatrixPosition(t){const e=t.elements;return this.x=e[12],this.y=e[13],this.z=e[14],this.w=e[15],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this.w=Math.min(this.w,t.w),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this.w=Math.max(this.w,t.w),this}clamp(t,e){return this.x=Nt(this.x,t.x,e.x),this.y=Nt(this.y,t.y,e.y),this.z=Nt(this.z,t.z,e.z),this.w=Nt(this.w,t.w,e.w),this}clampScalar(t,e){return this.x=Nt(this.x,t,e),this.y=Nt(this.y,t,e),this.z=Nt(this.z,t,e),this.w=Nt(this.w,t,e),this}clampLength(t,e){const i=this.length();return this.divideScalar(i||1).multiplyScalar(Nt(i,t,e))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z+this.w*t.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this.w+=(t.w-this.w)*e,this}lerpVectors(t,e,i){return this.x=t.x+(e.x-t.x)*i,this.y=t.y+(e.y-t.y)*i,this.z=t.z+(e.z-t.z)*i,this.w=t.w+(e.w-t.w)*i,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z&&t.w===this.w}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this.w=t[e+3],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t[e+3]=this.w,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this.w=t.getW(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}}class lh extends wi{constructor(t=1,e=1,i={}){super(),this.isRenderTarget=!0,this.width=t,this.height=e,this.depth=1,this.scissor=new Kt(0,0,t,e),this.scissorTest=!1,this.viewport=new Kt(0,0,t,e);const s={width:t,height:e,depth:1};i=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:Rn,depthBuffer:!0,stencilBuffer:!1,resolveDepthBuffer:!0,resolveStencilBuffer:!0,depthTexture:null,samples:0,count:1},i);const r=new Be(s,i.mapping,i.wrapS,i.wrapT,i.magFilter,i.minFilter,i.format,i.type,i.anisotropy,i.colorSpace);r.flipY=!1,r.generateMipmaps=i.generateMipmaps,r.internalFormat=i.internalFormat,this.textures=[];const a=i.count;for(let o=0;o<a;o++)this.textures[o]=r.clone(),this.textures[o].isRenderTargetTexture=!0,this.textures[o].renderTarget=this;this.depthBuffer=i.depthBuffer,this.stencilBuffer=i.stencilBuffer,this.resolveDepthBuffer=i.resolveDepthBuffer,this.resolveStencilBuffer=i.resolveStencilBuffer,this._depthTexture=i.depthTexture,this.samples=i.samples}get texture(){return this.textures[0]}set texture(t){this.textures[0]=t}set depthTexture(t){this._depthTexture!==null&&(this._depthTexture.renderTarget=null),t!==null&&(t.renderTarget=this),this._depthTexture=t}get depthTexture(){return this._depthTexture}setSize(t,e,i=1){if(this.width!==t||this.height!==e||this.depth!==i){this.width=t,this.height=e,this.depth=i;for(let s=0,r=this.textures.length;s<r;s++)this.textures[s].image.width=t,this.textures[s].image.height=e,this.textures[s].image.depth=i;this.dispose()}this.viewport.set(0,0,t,e),this.scissor.set(0,0,t,e)}clone(){return new this.constructor().copy(this)}copy(t){this.width=t.width,this.height=t.height,this.depth=t.depth,this.scissor.copy(t.scissor),this.scissorTest=t.scissorTest,this.viewport.copy(t.viewport),this.textures.length=0;for(let e=0,i=t.textures.length;e<i;e++){this.textures[e]=t.textures[e].clone(),this.textures[e].isRenderTargetTexture=!0,this.textures[e].renderTarget=this;const s=Object.assign({},t.textures[e].image);this.textures[e].source=new sl(s)}return this.depthBuffer=t.depthBuffer,this.stencilBuffer=t.stencilBuffer,this.resolveDepthBuffer=t.resolveDepthBuffer,this.resolveStencilBuffer=t.resolveStencilBuffer,t.depthTexture!==null&&(this.depthTexture=t.depthTexture.clone()),this.samples=t.samples,this}dispose(){this.dispatchEvent({type:"dispose"})}}class Ti extends lh{constructor(t=1,e=1,i={}){super(t,e,i),this.isWebGLRenderTarget=!0}}class _u extends Be{constructor(t=null,e=1,i=1,s=1){super(null),this.isDataArrayTexture=!0,this.image={data:t,width:e,height:i,depth:s},this.magFilter=gn,this.minFilter=gn,this.wrapR=xi,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1,this.layerUpdates=new Set}addLayerUpdate(t){this.layerUpdates.add(t)}clearLayerUpdates(){this.layerUpdates.clear()}}class ch extends Be{constructor(t=null,e=1,i=1,s=1){super(null),this.isData3DTexture=!0,this.image={data:t,width:e,height:i,depth:s},this.magFilter=gn,this.minFilter=gn,this.wrapR=xi,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}}class bi{constructor(t=0,e=0,i=0,s=1){this.isQuaternion=!0,this._x=t,this._y=e,this._z=i,this._w=s}static slerpFlat(t,e,i,s,r,a,o){let l=i[s+0],c=i[s+1],u=i[s+2],d=i[s+3];const h=r[a+0],p=r[a+1],_=r[a+2],S=r[a+3];if(o===0){t[e+0]=l,t[e+1]=c,t[e+2]=u,t[e+3]=d;return}if(o===1){t[e+0]=h,t[e+1]=p,t[e+2]=_,t[e+3]=S;return}if(d!==S||l!==h||c!==p||u!==_){let m=1-o;const f=l*h+c*p+u*_+d*S,b=f>=0?1:-1,M=1-f*f;if(M>Number.EPSILON){const P=Math.sqrt(M),R=Math.atan2(P,f*b);m=Math.sin(m*R)/P,o=Math.sin(o*R)/P}const y=o*b;if(l=l*m+h*y,c=c*m+p*y,u=u*m+_*y,d=d*m+S*y,m===1-o){const P=1/Math.sqrt(l*l+c*c+u*u+d*d);l*=P,c*=P,u*=P,d*=P}}t[e]=l,t[e+1]=c,t[e+2]=u,t[e+3]=d}static multiplyQuaternionsFlat(t,e,i,s,r,a){const o=i[s],l=i[s+1],c=i[s+2],u=i[s+3],d=r[a],h=r[a+1],p=r[a+2],_=r[a+3];return t[e]=o*_+u*d+l*p-c*h,t[e+1]=l*_+u*h+c*d-o*p,t[e+2]=c*_+u*p+o*h-l*d,t[e+3]=u*_-o*d-l*h-c*p,t}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get w(){return this._w}set w(t){this._w=t,this._onChangeCallback()}set(t,e,i,s){return this._x=t,this._y=e,this._z=i,this._w=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(t){return this._x=t.x,this._y=t.y,this._z=t.z,this._w=t.w,this._onChangeCallback(),this}setFromEuler(t,e=!0){const i=t._x,s=t._y,r=t._z,a=t._order,o=Math.cos,l=Math.sin,c=o(i/2),u=o(s/2),d=o(r/2),h=l(i/2),p=l(s/2),_=l(r/2);switch(a){case"XYZ":this._x=h*u*d+c*p*_,this._y=c*p*d-h*u*_,this._z=c*u*_+h*p*d,this._w=c*u*d-h*p*_;break;case"YXZ":this._x=h*u*d+c*p*_,this._y=c*p*d-h*u*_,this._z=c*u*_-h*p*d,this._w=c*u*d+h*p*_;break;case"ZXY":this._x=h*u*d-c*p*_,this._y=c*p*d+h*u*_,this._z=c*u*_+h*p*d,this._w=c*u*d-h*p*_;break;case"ZYX":this._x=h*u*d-c*p*_,this._y=c*p*d+h*u*_,this._z=c*u*_-h*p*d,this._w=c*u*d+h*p*_;break;case"YZX":this._x=h*u*d+c*p*_,this._y=c*p*d+h*u*_,this._z=c*u*_-h*p*d,this._w=c*u*d-h*p*_;break;case"XZY":this._x=h*u*d-c*p*_,this._y=c*p*d-h*u*_,this._z=c*u*_+h*p*d,this._w=c*u*d+h*p*_;break;default:console.warn("THREE.Quaternion: .setFromEuler() encountered an unknown order: "+a)}return e===!0&&this._onChangeCallback(),this}setFromAxisAngle(t,e){const i=e/2,s=Math.sin(i);return this._x=t.x*s,this._y=t.y*s,this._z=t.z*s,this._w=Math.cos(i),this._onChangeCallback(),this}setFromRotationMatrix(t){const e=t.elements,i=e[0],s=e[4],r=e[8],a=e[1],o=e[5],l=e[9],c=e[2],u=e[6],d=e[10],h=i+o+d;if(h>0){const p=.5/Math.sqrt(h+1);this._w=.25/p,this._x=(u-l)*p,this._y=(r-c)*p,this._z=(a-s)*p}else if(i>o&&i>d){const p=2*Math.sqrt(1+i-o-d);this._w=(u-l)/p,this._x=.25*p,this._y=(s+a)/p,this._z=(r+c)/p}else if(o>d){const p=2*Math.sqrt(1+o-i-d);this._w=(r-c)/p,this._x=(s+a)/p,this._y=.25*p,this._z=(l+u)/p}else{const p=2*Math.sqrt(1+d-i-o);this._w=(a-s)/p,this._x=(r+c)/p,this._y=(l+u)/p,this._z=.25*p}return this._onChangeCallback(),this}setFromUnitVectors(t,e){let i=t.dot(e)+1;return i<Number.EPSILON?(i=0,Math.abs(t.x)>Math.abs(t.z)?(this._x=-t.y,this._y=t.x,this._z=0,this._w=i):(this._x=0,this._y=-t.z,this._z=t.y,this._w=i)):(this._x=t.y*e.z-t.z*e.y,this._y=t.z*e.x-t.x*e.z,this._z=t.x*e.y-t.y*e.x,this._w=i),this.normalize()}angleTo(t){return 2*Math.acos(Math.abs(Nt(this.dot(t),-1,1)))}rotateTowards(t,e){const i=this.angleTo(t);if(i===0)return this;const s=Math.min(1,e/i);return this.slerp(t,s),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(t){return this._x*t._x+this._y*t._y+this._z*t._z+this._w*t._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let t=this.length();return t===0?(this._x=0,this._y=0,this._z=0,this._w=1):(t=1/t,this._x=this._x*t,this._y=this._y*t,this._z=this._z*t,this._w=this._w*t),this._onChangeCallback(),this}multiply(t){return this.multiplyQuaternions(this,t)}premultiply(t){return this.multiplyQuaternions(t,this)}multiplyQuaternions(t,e){const i=t._x,s=t._y,r=t._z,a=t._w,o=e._x,l=e._y,c=e._z,u=e._w;return this._x=i*u+a*o+s*c-r*l,this._y=s*u+a*l+r*o-i*c,this._z=r*u+a*c+i*l-s*o,this._w=a*u-i*o-s*l-r*c,this._onChangeCallback(),this}slerp(t,e){if(e===0)return this;if(e===1)return this.copy(t);const i=this._x,s=this._y,r=this._z,a=this._w;let o=a*t._w+i*t._x+s*t._y+r*t._z;if(o<0?(this._w=-t._w,this._x=-t._x,this._y=-t._y,this._z=-t._z,o=-o):this.copy(t),o>=1)return this._w=a,this._x=i,this._y=s,this._z=r,this;const l=1-o*o;if(l<=Number.EPSILON){const p=1-e;return this._w=p*a+e*this._w,this._x=p*i+e*this._x,this._y=p*s+e*this._y,this._z=p*r+e*this._z,this.normalize(),this}const c=Math.sqrt(l),u=Math.atan2(c,o),d=Math.sin((1-e)*u)/c,h=Math.sin(e*u)/c;return this._w=a*d+this._w*h,this._x=i*d+this._x*h,this._y=s*d+this._y*h,this._z=r*d+this._z*h,this._onChangeCallback(),this}slerpQuaternions(t,e,i){return this.copy(t).slerp(e,i)}random(){const t=2*Math.PI*Math.random(),e=2*Math.PI*Math.random(),i=Math.random(),s=Math.sqrt(1-i),r=Math.sqrt(i);return this.set(s*Math.sin(t),s*Math.cos(t),r*Math.sin(e),r*Math.cos(e))}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._w===this._w}fromArray(t,e=0){return this._x=t[e],this._y=t[e+1],this._z=t[e+2],this._w=t[e+3],this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._w,t}fromBufferAttribute(t,e){return this._x=t.getX(e),this._y=t.getY(e),this._z=t.getZ(e),this._w=t.getW(e),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}}class L{constructor(t=0,e=0,i=0){L.prototype.isVector3=!0,this.x=t,this.y=e,this.z=i}set(t,e,i){return i===void 0&&(i=this.z),this.x=t,this.y=e,this.z=i,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this}multiplyVectors(t,e){return this.x=t.x*e.x,this.y=t.y*e.y,this.z=t.z*e.z,this}applyEuler(t){return this.applyQuaternion(Ol.setFromEuler(t))}applyAxisAngle(t,e){return this.applyQuaternion(Ol.setFromAxisAngle(t,e))}applyMatrix3(t){const e=this.x,i=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[3]*i+r[6]*s,this.y=r[1]*e+r[4]*i+r[7]*s,this.z=r[2]*e+r[5]*i+r[8]*s,this}applyNormalMatrix(t){return this.applyMatrix3(t).normalize()}applyMatrix4(t){const e=this.x,i=this.y,s=this.z,r=t.elements,a=1/(r[3]*e+r[7]*i+r[11]*s+r[15]);return this.x=(r[0]*e+r[4]*i+r[8]*s+r[12])*a,this.y=(r[1]*e+r[5]*i+r[9]*s+r[13])*a,this.z=(r[2]*e+r[6]*i+r[10]*s+r[14])*a,this}applyQuaternion(t){const e=this.x,i=this.y,s=this.z,r=t.x,a=t.y,o=t.z,l=t.w,c=2*(a*s-o*i),u=2*(o*e-r*s),d=2*(r*i-a*e);return this.x=e+l*c+a*d-o*u,this.y=i+l*u+o*c-r*d,this.z=s+l*d+r*u-a*c,this}project(t){return this.applyMatrix4(t.matrixWorldInverse).applyMatrix4(t.projectionMatrix)}unproject(t){return this.applyMatrix4(t.projectionMatrixInverse).applyMatrix4(t.matrixWorld)}transformDirection(t){const e=this.x,i=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[4]*i+r[8]*s,this.y=r[1]*e+r[5]*i+r[9]*s,this.z=r[2]*e+r[6]*i+r[10]*s,this.normalize()}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this}divideScalar(t){return this.multiplyScalar(1/t)}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this}clamp(t,e){return this.x=Nt(this.x,t.x,e.x),this.y=Nt(this.y,t.y,e.y),this.z=Nt(this.z,t.z,e.z),this}clampScalar(t,e){return this.x=Nt(this.x,t,e),this.y=Nt(this.y,t,e),this.z=Nt(this.z,t,e),this}clampLength(t,e){const i=this.length();return this.divideScalar(i||1).multiplyScalar(Nt(i,t,e))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this}lerpVectors(t,e,i){return this.x=t.x+(e.x-t.x)*i,this.y=t.y+(e.y-t.y)*i,this.z=t.z+(e.z-t.z)*i,this}cross(t){return this.crossVectors(this,t)}crossVectors(t,e){const i=t.x,s=t.y,r=t.z,a=e.x,o=e.y,l=e.z;return this.x=s*l-r*o,this.y=r*a-i*l,this.z=i*o-s*a,this}projectOnVector(t){const e=t.lengthSq();if(e===0)return this.set(0,0,0);const i=t.dot(this)/e;return this.copy(t).multiplyScalar(i)}projectOnPlane(t){return ua.copy(this).projectOnVector(t),this.sub(ua)}reflect(t){return this.sub(ua.copy(t).multiplyScalar(2*this.dot(t)))}angleTo(t){const e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;const i=this.dot(t)/e;return Math.acos(Nt(i,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){const e=this.x-t.x,i=this.y-t.y,s=this.z-t.z;return e*e+i*i+s*s}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)+Math.abs(this.z-t.z)}setFromSpherical(t){return this.setFromSphericalCoords(t.radius,t.phi,t.theta)}setFromSphericalCoords(t,e,i){const s=Math.sin(e)*t;return this.x=s*Math.sin(i),this.y=Math.cos(e)*t,this.z=s*Math.cos(i),this}setFromCylindrical(t){return this.setFromCylindricalCoords(t.radius,t.theta,t.y)}setFromCylindricalCoords(t,e,i){return this.x=t*Math.sin(e),this.y=i,this.z=t*Math.cos(e),this}setFromMatrixPosition(t){const e=t.elements;return this.x=e[12],this.y=e[13],this.z=e[14],this}setFromMatrixScale(t){const e=this.setFromMatrixColumn(t,0).length(),i=this.setFromMatrixColumn(t,1).length(),s=this.setFromMatrixColumn(t,2).length();return this.x=e,this.y=i,this.z=s,this}setFromMatrixColumn(t,e){return this.fromArray(t.elements,e*4)}setFromMatrix3Column(t,e){return this.fromArray(t.elements,e*3)}setFromEuler(t){return this.x=t._x,this.y=t._y,this.z=t._z,this}setFromColor(t){return this.x=t.r,this.y=t.g,this.z=t.b,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){const t=Math.random()*Math.PI*2,e=Math.random()*2-1,i=Math.sqrt(1-e*e);return this.x=i*Math.cos(t),this.y=e,this.z=i*Math.sin(t),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}}const ua=new L,Ol=new bi;class Hs{constructor(t=new L(1/0,1/0,1/0),e=new L(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=t,this.max=e}set(t,e){return this.min.copy(t),this.max.copy(e),this}setFromArray(t){this.makeEmpty();for(let e=0,i=t.length;e<i;e+=3)this.expandByPoint(ln.fromArray(t,e));return this}setFromBufferAttribute(t){this.makeEmpty();for(let e=0,i=t.count;e<i;e++)this.expandByPoint(ln.fromBufferAttribute(t,e));return this}setFromPoints(t){this.makeEmpty();for(let e=0,i=t.length;e<i;e++)this.expandByPoint(t[e]);return this}setFromCenterAndSize(t,e){const i=ln.copy(e).multiplyScalar(.5);return this.min.copy(t).sub(i),this.max.copy(t).add(i),this}setFromObject(t,e=!1){return this.makeEmpty(),this.expandByObject(t,e)}clone(){return new this.constructor().copy(this)}copy(t){return this.min.copy(t.min),this.max.copy(t.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(t){return this.isEmpty()?t.set(0,0,0):t.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(t){return this.isEmpty()?t.set(0,0,0):t.subVectors(this.max,this.min)}expandByPoint(t){return this.min.min(t),this.max.max(t),this}expandByVector(t){return this.min.sub(t),this.max.add(t),this}expandByScalar(t){return this.min.addScalar(-t),this.max.addScalar(t),this}expandByObject(t,e=!1){t.updateWorldMatrix(!1,!1);const i=t.geometry;if(i!==void 0){const r=i.getAttribute("position");if(e===!0&&r!==void 0&&t.isInstancedMesh!==!0)for(let a=0,o=r.count;a<o;a++)t.isMesh===!0?t.getVertexPosition(a,ln):ln.fromBufferAttribute(r,a),ln.applyMatrix4(t.matrixWorld),this.expandByPoint(ln);else t.boundingBox!==void 0?(t.boundingBox===null&&t.computeBoundingBox(),js.copy(t.boundingBox)):(i.boundingBox===null&&i.computeBoundingBox(),js.copy(i.boundingBox)),js.applyMatrix4(t.matrixWorld),this.union(js)}const s=t.children;for(let r=0,a=s.length;r<a;r++)this.expandByObject(s[r],e);return this}containsPoint(t){return t.x>=this.min.x&&t.x<=this.max.x&&t.y>=this.min.y&&t.y<=this.max.y&&t.z>=this.min.z&&t.z<=this.max.z}containsBox(t){return this.min.x<=t.min.x&&t.max.x<=this.max.x&&this.min.y<=t.min.y&&t.max.y<=this.max.y&&this.min.z<=t.min.z&&t.max.z<=this.max.z}getParameter(t,e){return e.set((t.x-this.min.x)/(this.max.x-this.min.x),(t.y-this.min.y)/(this.max.y-this.min.y),(t.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(t){return t.max.x>=this.min.x&&t.min.x<=this.max.x&&t.max.y>=this.min.y&&t.min.y<=this.max.y&&t.max.z>=this.min.z&&t.min.z<=this.max.z}intersectsSphere(t){return this.clampPoint(t.center,ln),ln.distanceToSquared(t.center)<=t.radius*t.radius}intersectsPlane(t){let e,i;return t.normal.x>0?(e=t.normal.x*this.min.x,i=t.normal.x*this.max.x):(e=t.normal.x*this.max.x,i=t.normal.x*this.min.x),t.normal.y>0?(e+=t.normal.y*this.min.y,i+=t.normal.y*this.max.y):(e+=t.normal.y*this.max.y,i+=t.normal.y*this.min.y),t.normal.z>0?(e+=t.normal.z*this.min.z,i+=t.normal.z*this.max.z):(e+=t.normal.z*this.max.z,i+=t.normal.z*this.min.z),e<=-t.constant&&i>=-t.constant}intersectsTriangle(t){if(this.isEmpty())return!1;this.getCenter(us),Ks.subVectors(this.max,us),Li.subVectors(t.a,us),Di.subVectors(t.b,us),Ii.subVectors(t.c,us),$n.subVectors(Di,Li),qn.subVectors(Ii,Di),ui.subVectors(Li,Ii);let e=[0,-$n.z,$n.y,0,-qn.z,qn.y,0,-ui.z,ui.y,$n.z,0,-$n.x,qn.z,0,-qn.x,ui.z,0,-ui.x,-$n.y,$n.x,0,-qn.y,qn.x,0,-ui.y,ui.x,0];return!da(e,Li,Di,Ii,Ks)||(e=[1,0,0,0,1,0,0,0,1],!da(e,Li,Di,Ii,Ks))?!1:(Zs.crossVectors($n,qn),e=[Zs.x,Zs.y,Zs.z],da(e,Li,Di,Ii,Ks))}clampPoint(t,e){return e.copy(t).clamp(this.min,this.max)}distanceToPoint(t){return this.clampPoint(t,ln).distanceTo(t)}getBoundingSphere(t){return this.isEmpty()?t.makeEmpty():(this.getCenter(t.center),t.radius=this.getSize(ln).length()*.5),t}intersect(t){return this.min.max(t.min),this.max.min(t.max),this.isEmpty()&&this.makeEmpty(),this}union(t){return this.min.min(t.min),this.max.max(t.max),this}applyMatrix4(t){return this.isEmpty()?this:(Ln[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(t),Ln[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(t),Ln[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(t),Ln[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(t),Ln[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(t),Ln[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(t),Ln[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(t),Ln[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(t),this.setFromPoints(Ln),this)}translate(t){return this.min.add(t),this.max.add(t),this}equals(t){return t.min.equals(this.min)&&t.max.equals(this.max)}}const Ln=[new L,new L,new L,new L,new L,new L,new L,new L],ln=new L,js=new Hs,Li=new L,Di=new L,Ii=new L,$n=new L,qn=new L,ui=new L,us=new L,Ks=new L,Zs=new L,di=new L;function da(n,t,e,i,s){for(let r=0,a=n.length-3;r<=a;r+=3){di.fromArray(n,r);const o=s.x*Math.abs(di.x)+s.y*Math.abs(di.y)+s.z*Math.abs(di.z),l=t.dot(di),c=e.dot(di),u=i.dot(di);if(Math.max(-Math.max(l,c,u),Math.min(l,c,u))>o)return!1}return!0}const uh=new Hs,ds=new L,ha=new L;class Kr{constructor(t=new L,e=-1){this.isSphere=!0,this.center=t,this.radius=e}set(t,e){return this.center.copy(t),this.radius=e,this}setFromPoints(t,e){const i=this.center;e!==void 0?i.copy(e):uh.setFromPoints(t).getCenter(i);let s=0;for(let r=0,a=t.length;r<a;r++)s=Math.max(s,i.distanceToSquared(t[r]));return this.radius=Math.sqrt(s),this}copy(t){return this.center.copy(t.center),this.radius=t.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(t){return t.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(t){return t.distanceTo(this.center)-this.radius}intersectsSphere(t){const e=this.radius+t.radius;return t.center.distanceToSquared(this.center)<=e*e}intersectsBox(t){return t.intersectsSphere(this)}intersectsPlane(t){return Math.abs(t.distanceToPoint(this.center))<=this.radius}clampPoint(t,e){const i=this.center.distanceToSquared(t);return e.copy(t),i>this.radius*this.radius&&(e.sub(this.center).normalize(),e.multiplyScalar(this.radius).add(this.center)),e}getBoundingBox(t){return this.isEmpty()?(t.makeEmpty(),t):(t.set(this.center,this.center),t.expandByScalar(this.radius),t)}applyMatrix4(t){return this.center.applyMatrix4(t),this.radius=this.radius*t.getMaxScaleOnAxis(),this}translate(t){return this.center.add(t),this}expandByPoint(t){if(this.isEmpty())return this.center.copy(t),this.radius=0,this;ds.subVectors(t,this.center);const e=ds.lengthSq();if(e>this.radius*this.radius){const i=Math.sqrt(e),s=(i-this.radius)*.5;this.center.addScaledVector(ds,s/i),this.radius+=s}return this}union(t){return t.isEmpty()?this:this.isEmpty()?(this.copy(t),this):(this.center.equals(t.center)===!0?this.radius=Math.max(this.radius,t.radius):(ha.subVectors(t.center,this.center).setLength(t.radius),this.expandByPoint(ds.copy(t.center).add(ha)),this.expandByPoint(ds.copy(t.center).sub(ha))),this)}equals(t){return t.center.equals(this.center)&&t.radius===this.radius}clone(){return new this.constructor().copy(this)}}const Dn=new L,fa=new L,Js=new L,Yn=new L,pa=new L,Qs=new L,ma=new L;class Zr{constructor(t=new L,e=new L(0,0,-1)){this.origin=t,this.direction=e}set(t,e){return this.origin.copy(t),this.direction.copy(e),this}copy(t){return this.origin.copy(t.origin),this.direction.copy(t.direction),this}at(t,e){return e.copy(this.origin).addScaledVector(this.direction,t)}lookAt(t){return this.direction.copy(t).sub(this.origin).normalize(),this}recast(t){return this.origin.copy(this.at(t,Dn)),this}closestPointToPoint(t,e){e.subVectors(t,this.origin);const i=e.dot(this.direction);return i<0?e.copy(this.origin):e.copy(this.origin).addScaledVector(this.direction,i)}distanceToPoint(t){return Math.sqrt(this.distanceSqToPoint(t))}distanceSqToPoint(t){const e=Dn.subVectors(t,this.origin).dot(this.direction);return e<0?this.origin.distanceToSquared(t):(Dn.copy(this.origin).addScaledVector(this.direction,e),Dn.distanceToSquared(t))}distanceSqToSegment(t,e,i,s){fa.copy(t).add(e).multiplyScalar(.5),Js.copy(e).sub(t).normalize(),Yn.copy(this.origin).sub(fa);const r=t.distanceTo(e)*.5,a=-this.direction.dot(Js),o=Yn.dot(this.direction),l=-Yn.dot(Js),c=Yn.lengthSq(),u=Math.abs(1-a*a);let d,h,p,_;if(u>0)if(d=a*l-o,h=a*o-l,_=r*u,d>=0)if(h>=-_)if(h<=_){const S=1/u;d*=S,h*=S,p=d*(d+a*h+2*o)+h*(a*d+h+2*l)+c}else h=r,d=Math.max(0,-(a*h+o)),p=-d*d+h*(h+2*l)+c;else h=-r,d=Math.max(0,-(a*h+o)),p=-d*d+h*(h+2*l)+c;else h<=-_?(d=Math.max(0,-(-a*r+o)),h=d>0?-r:Math.min(Math.max(-r,-l),r),p=-d*d+h*(h+2*l)+c):h<=_?(d=0,h=Math.min(Math.max(-r,-l),r),p=h*(h+2*l)+c):(d=Math.max(0,-(a*r+o)),h=d>0?r:Math.min(Math.max(-r,-l),r),p=-d*d+h*(h+2*l)+c);else h=a>0?-r:r,d=Math.max(0,-(a*h+o)),p=-d*d+h*(h+2*l)+c;return i&&i.copy(this.origin).addScaledVector(this.direction,d),s&&s.copy(fa).addScaledVector(Js,h),p}intersectSphere(t,e){Dn.subVectors(t.center,this.origin);const i=Dn.dot(this.direction),s=Dn.dot(Dn)-i*i,r=t.radius*t.radius;if(s>r)return null;const a=Math.sqrt(r-s),o=i-a,l=i+a;return l<0?null:o<0?this.at(l,e):this.at(o,e)}intersectsSphere(t){return this.distanceSqToPoint(t.center)<=t.radius*t.radius}distanceToPlane(t){const e=t.normal.dot(this.direction);if(e===0)return t.distanceToPoint(this.origin)===0?0:null;const i=-(this.origin.dot(t.normal)+t.constant)/e;return i>=0?i:null}intersectPlane(t,e){const i=this.distanceToPlane(t);return i===null?null:this.at(i,e)}intersectsPlane(t){const e=t.distanceToPoint(this.origin);return e===0||t.normal.dot(this.direction)*e<0}intersectBox(t,e){let i,s,r,a,o,l;const c=1/this.direction.x,u=1/this.direction.y,d=1/this.direction.z,h=this.origin;return c>=0?(i=(t.min.x-h.x)*c,s=(t.max.x-h.x)*c):(i=(t.max.x-h.x)*c,s=(t.min.x-h.x)*c),u>=0?(r=(t.min.y-h.y)*u,a=(t.max.y-h.y)*u):(r=(t.max.y-h.y)*u,a=(t.min.y-h.y)*u),i>a||r>s||((r>i||isNaN(i))&&(i=r),(a<s||isNaN(s))&&(s=a),d>=0?(o=(t.min.z-h.z)*d,l=(t.max.z-h.z)*d):(o=(t.max.z-h.z)*d,l=(t.min.z-h.z)*d),i>l||o>s)||((o>i||i!==i)&&(i=o),(l<s||s!==s)&&(s=l),s<0)?null:this.at(i>=0?i:s,e)}intersectsBox(t){return this.intersectBox(t,Dn)!==null}intersectTriangle(t,e,i,s,r){pa.subVectors(e,t),Qs.subVectors(i,t),ma.crossVectors(pa,Qs);let a=this.direction.dot(ma),o;if(a>0){if(s)return null;o=1}else if(a<0)o=-1,a=-a;else return null;Yn.subVectors(this.origin,t);const l=o*this.direction.dot(Qs.crossVectors(Yn,Qs));if(l<0)return null;const c=o*this.direction.dot(pa.cross(Yn));if(c<0||l+c>a)return null;const u=-o*Yn.dot(ma);return u<0?null:this.at(u/a,r)}applyMatrix4(t){return this.origin.applyMatrix4(t),this.direction.transformDirection(t),this}equals(t){return t.origin.equals(this.origin)&&t.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}}class te{constructor(t,e,i,s,r,a,o,l,c,u,d,h,p,_,S,m){te.prototype.isMatrix4=!0,this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],t!==void 0&&this.set(t,e,i,s,r,a,o,l,c,u,d,h,p,_,S,m)}set(t,e,i,s,r,a,o,l,c,u,d,h,p,_,S,m){const f=this.elements;return f[0]=t,f[4]=e,f[8]=i,f[12]=s,f[1]=r,f[5]=a,f[9]=o,f[13]=l,f[2]=c,f[6]=u,f[10]=d,f[14]=h,f[3]=p,f[7]=_,f[11]=S,f[15]=m,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new te().fromArray(this.elements)}copy(t){const e=this.elements,i=t.elements;return e[0]=i[0],e[1]=i[1],e[2]=i[2],e[3]=i[3],e[4]=i[4],e[5]=i[5],e[6]=i[6],e[7]=i[7],e[8]=i[8],e[9]=i[9],e[10]=i[10],e[11]=i[11],e[12]=i[12],e[13]=i[13],e[14]=i[14],e[15]=i[15],this}copyPosition(t){const e=this.elements,i=t.elements;return e[12]=i[12],e[13]=i[13],e[14]=i[14],this}setFromMatrix3(t){const e=t.elements;return this.set(e[0],e[3],e[6],0,e[1],e[4],e[7],0,e[2],e[5],e[8],0,0,0,0,1),this}extractBasis(t,e,i){return t.setFromMatrixColumn(this,0),e.setFromMatrixColumn(this,1),i.setFromMatrixColumn(this,2),this}makeBasis(t,e,i){return this.set(t.x,e.x,i.x,0,t.y,e.y,i.y,0,t.z,e.z,i.z,0,0,0,0,1),this}extractRotation(t){const e=this.elements,i=t.elements,s=1/Ui.setFromMatrixColumn(t,0).length(),r=1/Ui.setFromMatrixColumn(t,1).length(),a=1/Ui.setFromMatrixColumn(t,2).length();return e[0]=i[0]*s,e[1]=i[1]*s,e[2]=i[2]*s,e[3]=0,e[4]=i[4]*r,e[5]=i[5]*r,e[6]=i[6]*r,e[7]=0,e[8]=i[8]*a,e[9]=i[9]*a,e[10]=i[10]*a,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromEuler(t){const e=this.elements,i=t.x,s=t.y,r=t.z,a=Math.cos(i),o=Math.sin(i),l=Math.cos(s),c=Math.sin(s),u=Math.cos(r),d=Math.sin(r);if(t.order==="XYZ"){const h=a*u,p=a*d,_=o*u,S=o*d;e[0]=l*u,e[4]=-l*d,e[8]=c,e[1]=p+_*c,e[5]=h-S*c,e[9]=-o*l,e[2]=S-h*c,e[6]=_+p*c,e[10]=a*l}else if(t.order==="YXZ"){const h=l*u,p=l*d,_=c*u,S=c*d;e[0]=h+S*o,e[4]=_*o-p,e[8]=a*c,e[1]=a*d,e[5]=a*u,e[9]=-o,e[2]=p*o-_,e[6]=S+h*o,e[10]=a*l}else if(t.order==="ZXY"){const h=l*u,p=l*d,_=c*u,S=c*d;e[0]=h-S*o,e[4]=-a*d,e[8]=_+p*o,e[1]=p+_*o,e[5]=a*u,e[9]=S-h*o,e[2]=-a*c,e[6]=o,e[10]=a*l}else if(t.order==="ZYX"){const h=a*u,p=a*d,_=o*u,S=o*d;e[0]=l*u,e[4]=_*c-p,e[8]=h*c+S,e[1]=l*d,e[5]=S*c+h,e[9]=p*c-_,e[2]=-c,e[6]=o*l,e[10]=a*l}else if(t.order==="YZX"){const h=a*l,p=a*c,_=o*l,S=o*c;e[0]=l*u,e[4]=S-h*d,e[8]=_*d+p,e[1]=d,e[5]=a*u,e[9]=-o*u,e[2]=-c*u,e[6]=p*d+_,e[10]=h-S*d}else if(t.order==="XZY"){const h=a*l,p=a*c,_=o*l,S=o*c;e[0]=l*u,e[4]=-d,e[8]=c*u,e[1]=h*d+S,e[5]=a*u,e[9]=p*d-_,e[2]=_*d-p,e[6]=o*u,e[10]=S*d+h}return e[3]=0,e[7]=0,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromQuaternion(t){return this.compose(dh,t,hh)}lookAt(t,e,i){const s=this.elements;return ke.subVectors(t,e),ke.lengthSq()===0&&(ke.z=1),ke.normalize(),jn.crossVectors(i,ke),jn.lengthSq()===0&&(Math.abs(i.z)===1?ke.x+=1e-4:ke.z+=1e-4,ke.normalize(),jn.crossVectors(i,ke)),jn.normalize(),tr.crossVectors(ke,jn),s[0]=jn.x,s[4]=tr.x,s[8]=ke.x,s[1]=jn.y,s[5]=tr.y,s[9]=ke.y,s[2]=jn.z,s[6]=tr.z,s[10]=ke.z,this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){const i=t.elements,s=e.elements,r=this.elements,a=i[0],o=i[4],l=i[8],c=i[12],u=i[1],d=i[5],h=i[9],p=i[13],_=i[2],S=i[6],m=i[10],f=i[14],b=i[3],M=i[7],y=i[11],P=i[15],R=s[0],A=s[4],I=s[8],E=s[12],x=s[1],C=s[5],V=s[9],z=s[13],Y=s[2],j=s[6],X=s[10],Z=s[14],H=s[3],it=s[7],ut=s[11],vt=s[15];return r[0]=a*R+o*x+l*Y+c*H,r[4]=a*A+o*C+l*j+c*it,r[8]=a*I+o*V+l*X+c*ut,r[12]=a*E+o*z+l*Z+c*vt,r[1]=u*R+d*x+h*Y+p*H,r[5]=u*A+d*C+h*j+p*it,r[9]=u*I+d*V+h*X+p*ut,r[13]=u*E+d*z+h*Z+p*vt,r[2]=_*R+S*x+m*Y+f*H,r[6]=_*A+S*C+m*j+f*it,r[10]=_*I+S*V+m*X+f*ut,r[14]=_*E+S*z+m*Z+f*vt,r[3]=b*R+M*x+y*Y+P*H,r[7]=b*A+M*C+y*j+P*it,r[11]=b*I+M*V+y*X+P*ut,r[15]=b*E+M*z+y*Z+P*vt,this}multiplyScalar(t){const e=this.elements;return e[0]*=t,e[4]*=t,e[8]*=t,e[12]*=t,e[1]*=t,e[5]*=t,e[9]*=t,e[13]*=t,e[2]*=t,e[6]*=t,e[10]*=t,e[14]*=t,e[3]*=t,e[7]*=t,e[11]*=t,e[15]*=t,this}determinant(){const t=this.elements,e=t[0],i=t[4],s=t[8],r=t[12],a=t[1],o=t[5],l=t[9],c=t[13],u=t[2],d=t[6],h=t[10],p=t[14],_=t[3],S=t[7],m=t[11],f=t[15];return _*(+r*l*d-s*c*d-r*o*h+i*c*h+s*o*p-i*l*p)+S*(+e*l*p-e*c*h+r*a*h-s*a*p+s*c*u-r*l*u)+m*(+e*c*d-e*o*p-r*a*d+i*a*p+r*o*u-i*c*u)+f*(-s*o*u-e*l*d+e*o*h+s*a*d-i*a*h+i*l*u)}transpose(){const t=this.elements;let e;return e=t[1],t[1]=t[4],t[4]=e,e=t[2],t[2]=t[8],t[8]=e,e=t[6],t[6]=t[9],t[9]=e,e=t[3],t[3]=t[12],t[12]=e,e=t[7],t[7]=t[13],t[13]=e,e=t[11],t[11]=t[14],t[14]=e,this}setPosition(t,e,i){const s=this.elements;return t.isVector3?(s[12]=t.x,s[13]=t.y,s[14]=t.z):(s[12]=t,s[13]=e,s[14]=i),this}invert(){const t=this.elements,e=t[0],i=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],u=t[8],d=t[9],h=t[10],p=t[11],_=t[12],S=t[13],m=t[14],f=t[15],b=d*m*c-S*h*c+S*l*p-o*m*p-d*l*f+o*h*f,M=_*h*c-u*m*c-_*l*p+a*m*p+u*l*f-a*h*f,y=u*S*c-_*d*c+_*o*p-a*S*p-u*o*f+a*d*f,P=_*d*l-u*S*l-_*o*h+a*S*h+u*o*m-a*d*m,R=e*b+i*M+s*y+r*P;if(R===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);const A=1/R;return t[0]=b*A,t[1]=(S*h*r-d*m*r-S*s*p+i*m*p+d*s*f-i*h*f)*A,t[2]=(o*m*r-S*l*r+S*s*c-i*m*c-o*s*f+i*l*f)*A,t[3]=(d*l*r-o*h*r-d*s*c+i*h*c+o*s*p-i*l*p)*A,t[4]=M*A,t[5]=(u*m*r-_*h*r+_*s*p-e*m*p-u*s*f+e*h*f)*A,t[6]=(_*l*r-a*m*r-_*s*c+e*m*c+a*s*f-e*l*f)*A,t[7]=(a*h*r-u*l*r+u*s*c-e*h*c-a*s*p+e*l*p)*A,t[8]=y*A,t[9]=(_*d*r-u*S*r-_*i*p+e*S*p+u*i*f-e*d*f)*A,t[10]=(a*S*r-_*o*r+_*i*c-e*S*c-a*i*f+e*o*f)*A,t[11]=(u*o*r-a*d*r-u*i*c+e*d*c+a*i*p-e*o*p)*A,t[12]=P*A,t[13]=(u*S*s-_*d*s+_*i*h-e*S*h-u*i*m+e*d*m)*A,t[14]=(_*o*s-a*S*s-_*i*l+e*S*l+a*i*m-e*o*m)*A,t[15]=(a*d*s-u*o*s+u*i*l-e*d*l-a*i*h+e*o*h)*A,this}scale(t){const e=this.elements,i=t.x,s=t.y,r=t.z;return e[0]*=i,e[4]*=s,e[8]*=r,e[1]*=i,e[5]*=s,e[9]*=r,e[2]*=i,e[6]*=s,e[10]*=r,e[3]*=i,e[7]*=s,e[11]*=r,this}getMaxScaleOnAxis(){const t=this.elements,e=t[0]*t[0]+t[1]*t[1]+t[2]*t[2],i=t[4]*t[4]+t[5]*t[5]+t[6]*t[6],s=t[8]*t[8]+t[9]*t[9]+t[10]*t[10];return Math.sqrt(Math.max(e,i,s))}makeTranslation(t,e,i){return t.isVector3?this.set(1,0,0,t.x,0,1,0,t.y,0,0,1,t.z,0,0,0,1):this.set(1,0,0,t,0,1,0,e,0,0,1,i,0,0,0,1),this}makeRotationX(t){const e=Math.cos(t),i=Math.sin(t);return this.set(1,0,0,0,0,e,-i,0,0,i,e,0,0,0,0,1),this}makeRotationY(t){const e=Math.cos(t),i=Math.sin(t);return this.set(e,0,i,0,0,1,0,0,-i,0,e,0,0,0,0,1),this}makeRotationZ(t){const e=Math.cos(t),i=Math.sin(t);return this.set(e,-i,0,0,i,e,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(t,e){const i=Math.cos(e),s=Math.sin(e),r=1-i,a=t.x,o=t.y,l=t.z,c=r*a,u=r*o;return this.set(c*a+i,c*o-s*l,c*l+s*o,0,c*o+s*l,u*o+i,u*l-s*a,0,c*l-s*o,u*l+s*a,r*l*l+i,0,0,0,0,1),this}makeScale(t,e,i){return this.set(t,0,0,0,0,e,0,0,0,0,i,0,0,0,0,1),this}makeShear(t,e,i,s,r,a){return this.set(1,i,r,0,t,1,a,0,e,s,1,0,0,0,0,1),this}compose(t,e,i){const s=this.elements,r=e._x,a=e._y,o=e._z,l=e._w,c=r+r,u=a+a,d=o+o,h=r*c,p=r*u,_=r*d,S=a*u,m=a*d,f=o*d,b=l*c,M=l*u,y=l*d,P=i.x,R=i.y,A=i.z;return s[0]=(1-(S+f))*P,s[1]=(p+y)*P,s[2]=(_-M)*P,s[3]=0,s[4]=(p-y)*R,s[5]=(1-(h+f))*R,s[6]=(m+b)*R,s[7]=0,s[8]=(_+M)*A,s[9]=(m-b)*A,s[10]=(1-(h+S))*A,s[11]=0,s[12]=t.x,s[13]=t.y,s[14]=t.z,s[15]=1,this}decompose(t,e,i){const s=this.elements;let r=Ui.set(s[0],s[1],s[2]).length();const a=Ui.set(s[4],s[5],s[6]).length(),o=Ui.set(s[8],s[9],s[10]).length();this.determinant()<0&&(r=-r),t.x=s[12],t.y=s[13],t.z=s[14],cn.copy(this);const c=1/r,u=1/a,d=1/o;return cn.elements[0]*=c,cn.elements[1]*=c,cn.elements[2]*=c,cn.elements[4]*=u,cn.elements[5]*=u,cn.elements[6]*=u,cn.elements[8]*=d,cn.elements[9]*=d,cn.elements[10]*=d,e.setFromRotationMatrix(cn),i.x=r,i.y=a,i.z=o,this}makePerspective(t,e,i,s,r,a,o=Vn){const l=this.elements,c=2*r/(e-t),u=2*r/(i-s),d=(e+t)/(e-t),h=(i+s)/(i-s);let p,_;if(o===Vn)p=-(a+r)/(a-r),_=-2*a*r/(a-r);else if(o===zr)p=-a/(a-r),_=-a*r/(a-r);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+o);return l[0]=c,l[4]=0,l[8]=d,l[12]=0,l[1]=0,l[5]=u,l[9]=h,l[13]=0,l[2]=0,l[6]=0,l[10]=p,l[14]=_,l[3]=0,l[7]=0,l[11]=-1,l[15]=0,this}makeOrthographic(t,e,i,s,r,a,o=Vn){const l=this.elements,c=1/(e-t),u=1/(i-s),d=1/(a-r),h=(e+t)*c,p=(i+s)*u;let _,S;if(o===Vn)_=(a+r)*d,S=-2*d;else if(o===zr)_=r*d,S=-1*d;else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+o);return l[0]=2*c,l[4]=0,l[8]=0,l[12]=-h,l[1]=0,l[5]=2*u,l[9]=0,l[13]=-p,l[2]=0,l[6]=0,l[10]=S,l[14]=-_,l[3]=0,l[7]=0,l[11]=0,l[15]=1,this}equals(t){const e=this.elements,i=t.elements;for(let s=0;s<16;s++)if(e[s]!==i[s])return!1;return!0}fromArray(t,e=0){for(let i=0;i<16;i++)this.elements[i]=t[i+e];return this}toArray(t=[],e=0){const i=this.elements;return t[e]=i[0],t[e+1]=i[1],t[e+2]=i[2],t[e+3]=i[3],t[e+4]=i[4],t[e+5]=i[5],t[e+6]=i[6],t[e+7]=i[7],t[e+8]=i[8],t[e+9]=i[9],t[e+10]=i[10],t[e+11]=i[11],t[e+12]=i[12],t[e+13]=i[13],t[e+14]=i[14],t[e+15]=i[15],t}}const Ui=new L,cn=new te,dh=new L(0,0,0),hh=new L(1,1,1),jn=new L,tr=new L,ke=new L,Fl=new te,Bl=new bi;class Xn{constructor(t=0,e=0,i=0,s=Xn.DEFAULT_ORDER){this.isEuler=!0,this._x=t,this._y=e,this._z=i,this._order=s}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get order(){return this._order}set order(t){this._order=t,this._onChangeCallback()}set(t,e,i,s=this._order){return this._x=t,this._y=e,this._z=i,this._order=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(t){return this._x=t._x,this._y=t._y,this._z=t._z,this._order=t._order,this._onChangeCallback(),this}setFromRotationMatrix(t,e=this._order,i=!0){const s=t.elements,r=s[0],a=s[4],o=s[8],l=s[1],c=s[5],u=s[9],d=s[2],h=s[6],p=s[10];switch(e){case"XYZ":this._y=Math.asin(Nt(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(-u,p),this._z=Math.atan2(-a,r)):(this._x=Math.atan2(h,c),this._z=0);break;case"YXZ":this._x=Math.asin(-Nt(u,-1,1)),Math.abs(u)<.9999999?(this._y=Math.atan2(o,p),this._z=Math.atan2(l,c)):(this._y=Math.atan2(-d,r),this._z=0);break;case"ZXY":this._x=Math.asin(Nt(h,-1,1)),Math.abs(h)<.9999999?(this._y=Math.atan2(-d,p),this._z=Math.atan2(-a,c)):(this._y=0,this._z=Math.atan2(l,r));break;case"ZYX":this._y=Math.asin(-Nt(d,-1,1)),Math.abs(d)<.9999999?(this._x=Math.atan2(h,p),this._z=Math.atan2(l,r)):(this._x=0,this._z=Math.atan2(-a,c));break;case"YZX":this._z=Math.asin(Nt(l,-1,1)),Math.abs(l)<.9999999?(this._x=Math.atan2(-u,c),this._y=Math.atan2(-d,r)):(this._x=0,this._y=Math.atan2(o,p));break;case"XZY":this._z=Math.asin(-Nt(a,-1,1)),Math.abs(a)<.9999999?(this._x=Math.atan2(h,c),this._y=Math.atan2(o,r)):(this._x=Math.atan2(-u,p),this._y=0);break;default:console.warn("THREE.Euler: .setFromRotationMatrix() encountered an unknown order: "+e)}return this._order=e,i===!0&&this._onChangeCallback(),this}setFromQuaternion(t,e,i){return Fl.makeRotationFromQuaternion(t),this.setFromRotationMatrix(Fl,e,i)}setFromVector3(t,e=this._order){return this.set(t.x,t.y,t.z,e)}reorder(t){return Bl.setFromEuler(this),this.setFromQuaternion(Bl,t)}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._order===this._order}fromArray(t){return this._x=t[0],this._y=t[1],this._z=t[2],t[3]!==void 0&&(this._order=t[3]),this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._order,t}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}}Xn.DEFAULT_ORDER="XYZ";class rl{constructor(){this.mask=1}set(t){this.mask=(1<<t|0)>>>0}enable(t){this.mask|=1<<t|0}enableAll(){this.mask=-1}toggle(t){this.mask^=1<<t|0}disable(t){this.mask&=~(1<<t|0)}disableAll(){this.mask=0}test(t){return(this.mask&t.mask)!==0}isEnabled(t){return(this.mask&(1<<t|0))!==0}}let fh=0;const zl=new L,Ni=new bi,In=new te,er=new L,hs=new L,ph=new L,mh=new bi,kl=new L(1,0,0),Hl=new L(0,1,0),Vl=new L(0,0,1),Gl={type:"added"},gh={type:"removed"},Oi={type:"childadded",child:null},ga={type:"childremoved",child:null};class Te extends wi{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:fh++}),this.uuid=ks(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=Te.DEFAULT_UP.clone();const t=new L,e=new Xn,i=new bi,s=new L(1,1,1);function r(){i.setFromEuler(e,!1)}function a(){e.setFromQuaternion(i,void 0,!1)}e._onChange(r),i._onChange(a),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:t},rotation:{configurable:!0,enumerable:!0,value:e},quaternion:{configurable:!0,enumerable:!0,value:i},scale:{configurable:!0,enumerable:!0,value:s},modelViewMatrix:{value:new te},normalMatrix:{value:new Pt}}),this.matrix=new te,this.matrixWorld=new te,this.matrixAutoUpdate=Te.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=Te.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new rl,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.customDepthMaterial=void 0,this.customDistanceMaterial=void 0,this.userData={}}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(t){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(t),this.matrix.decompose(this.position,this.quaternion,this.scale)}applyQuaternion(t){return this.quaternion.premultiply(t),this}setRotationFromAxisAngle(t,e){this.quaternion.setFromAxisAngle(t,e)}setRotationFromEuler(t){this.quaternion.setFromEuler(t,!0)}setRotationFromMatrix(t){this.quaternion.setFromRotationMatrix(t)}setRotationFromQuaternion(t){this.quaternion.copy(t)}rotateOnAxis(t,e){return Ni.setFromAxisAngle(t,e),this.quaternion.multiply(Ni),this}rotateOnWorldAxis(t,e){return Ni.setFromAxisAngle(t,e),this.quaternion.premultiply(Ni),this}rotateX(t){return this.rotateOnAxis(kl,t)}rotateY(t){return this.rotateOnAxis(Hl,t)}rotateZ(t){return this.rotateOnAxis(Vl,t)}translateOnAxis(t,e){return zl.copy(t).applyQuaternion(this.quaternion),this.position.add(zl.multiplyScalar(e)),this}translateX(t){return this.translateOnAxis(kl,t)}translateY(t){return this.translateOnAxis(Hl,t)}translateZ(t){return this.translateOnAxis(Vl,t)}localToWorld(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(this.matrixWorld)}worldToLocal(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(In.copy(this.matrixWorld).invert())}lookAt(t,e,i){t.isVector3?er.copy(t):er.set(t,e,i);const s=this.parent;this.updateWorldMatrix(!0,!1),hs.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?In.lookAt(hs,er,this.up):In.lookAt(er,hs,this.up),this.quaternion.setFromRotationMatrix(In),s&&(In.extractRotation(s.matrixWorld),Ni.setFromRotationMatrix(In),this.quaternion.premultiply(Ni.invert()))}add(t){if(arguments.length>1){for(let e=0;e<arguments.length;e++)this.add(arguments[e]);return this}return t===this?(console.error("THREE.Object3D.add: object can't be added as a child of itself.",t),this):(t&&t.isObject3D?(t.removeFromParent(),t.parent=this,this.children.push(t),t.dispatchEvent(Gl),Oi.child=t,this.dispatchEvent(Oi),Oi.child=null):console.error("THREE.Object3D.add: object not an instance of THREE.Object3D.",t),this)}remove(t){if(arguments.length>1){for(let i=0;i<arguments.length;i++)this.remove(arguments[i]);return this}const e=this.children.indexOf(t);return e!==-1&&(t.parent=null,this.children.splice(e,1),t.dispatchEvent(gh),ga.child=t,this.dispatchEvent(ga),ga.child=null),this}removeFromParent(){const t=this.parent;return t!==null&&t.remove(this),this}clear(){return this.remove(...this.children)}attach(t){return this.updateWorldMatrix(!0,!1),In.copy(this.matrixWorld).invert(),t.parent!==null&&(t.parent.updateWorldMatrix(!0,!1),In.multiply(t.parent.matrixWorld)),t.applyMatrix4(In),t.removeFromParent(),t.parent=this,this.children.push(t),t.updateWorldMatrix(!1,!0),t.dispatchEvent(Gl),Oi.child=t,this.dispatchEvent(Oi),Oi.child=null,this}getObjectById(t){return this.getObjectByProperty("id",t)}getObjectByName(t){return this.getObjectByProperty("name",t)}getObjectByProperty(t,e){if(this[t]===e)return this;for(let i=0,s=this.children.length;i<s;i++){const a=this.children[i].getObjectByProperty(t,e);if(a!==void 0)return a}}getObjectsByProperty(t,e,i=[]){this[t]===e&&i.push(this);const s=this.children;for(let r=0,a=s.length;r<a;r++)s[r].getObjectsByProperty(t,e,i);return i}getWorldPosition(t){return this.updateWorldMatrix(!0,!1),t.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(hs,t,ph),t}getWorldScale(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(hs,mh,t),t}getWorldDirection(t){this.updateWorldMatrix(!0,!1);const e=this.matrixWorld.elements;return t.set(e[8],e[9],e[10]).normalize()}raycast(){}traverse(t){t(this);const e=this.children;for(let i=0,s=e.length;i<s;i++)e[i].traverse(t)}traverseVisible(t){if(this.visible===!1)return;t(this);const e=this.children;for(let i=0,s=e.length;i<s;i++)e[i].traverseVisible(t)}traverseAncestors(t){const e=this.parent;e!==null&&(t(e),e.traverseAncestors(t))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale),this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(t){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||t)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,t=!0);const e=this.children;for(let i=0,s=e.length;i<s;i++)e[i].updateMatrixWorld(t)}updateWorldMatrix(t,e){const i=this.parent;if(t===!0&&i!==null&&i.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),e===!0){const s=this.children;for(let r=0,a=s.length;r<a;r++)s[r].updateWorldMatrix(!1,!0)}}toJSON(t){const e=t===void 0||typeof t=="string",i={};e&&(t={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},i.metadata={version:4.6,type:"Object",generator:"Object3D.toJSON"});const s={};s.uuid=this.uuid,s.type=this.type,this.name!==""&&(s.name=this.name),this.castShadow===!0&&(s.castShadow=!0),this.receiveShadow===!0&&(s.receiveShadow=!0),this.visible===!1&&(s.visible=!1),this.frustumCulled===!1&&(s.frustumCulled=!1),this.renderOrder!==0&&(s.renderOrder=this.renderOrder),Object.keys(this.userData).length>0&&(s.userData=this.userData),s.layers=this.layers.mask,s.matrix=this.matrix.toArray(),s.up=this.up.toArray(),this.matrixAutoUpdate===!1&&(s.matrixAutoUpdate=!1),this.isInstancedMesh&&(s.type="InstancedMesh",s.count=this.count,s.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(s.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(s.type="BatchedMesh",s.perObjectFrustumCulled=this.perObjectFrustumCulled,s.sortObjects=this.sortObjects,s.drawRanges=this._drawRanges,s.reservedRanges=this._reservedRanges,s.visibility=this._visibility,s.active=this._active,s.bounds=this._bounds.map(o=>({boxInitialized:o.boxInitialized,boxMin:o.box.min.toArray(),boxMax:o.box.max.toArray(),sphereInitialized:o.sphereInitialized,sphereRadius:o.sphere.radius,sphereCenter:o.sphere.center.toArray()})),s.maxInstanceCount=this._maxInstanceCount,s.maxVertexCount=this._maxVertexCount,s.maxIndexCount=this._maxIndexCount,s.geometryInitialized=this._geometryInitialized,s.geometryCount=this._geometryCount,s.matricesTexture=this._matricesTexture.toJSON(t),this._colorsTexture!==null&&(s.colorsTexture=this._colorsTexture.toJSON(t)),this.boundingSphere!==null&&(s.boundingSphere={center:s.boundingSphere.center.toArray(),radius:s.boundingSphere.radius}),this.boundingBox!==null&&(s.boundingBox={min:s.boundingBox.min.toArray(),max:s.boundingBox.max.toArray()}));function r(o,l){return o[l.uuid]===void 0&&(o[l.uuid]=l.toJSON(t)),l.uuid}if(this.isScene)this.background&&(this.background.isColor?s.background=this.background.toJSON():this.background.isTexture&&(s.background=this.background.toJSON(t).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(s.environment=this.environment.toJSON(t).uuid);else if(this.isMesh||this.isLine||this.isPoints){s.geometry=r(t.geometries,this.geometry);const o=this.geometry.parameters;if(o!==void 0&&o.shapes!==void 0){const l=o.shapes;if(Array.isArray(l))for(let c=0,u=l.length;c<u;c++){const d=l[c];r(t.shapes,d)}else r(t.shapes,l)}}if(this.isSkinnedMesh&&(s.bindMode=this.bindMode,s.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(r(t.skeletons,this.skeleton),s.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){const o=[];for(let l=0,c=this.material.length;l<c;l++)o.push(r(t.materials,this.material[l]));s.material=o}else s.material=r(t.materials,this.material);if(this.children.length>0){s.children=[];for(let o=0;o<this.children.length;o++)s.children.push(this.children[o].toJSON(t).object)}if(this.animations.length>0){s.animations=[];for(let o=0;o<this.animations.length;o++){const l=this.animations[o];s.animations.push(r(t.animations,l))}}if(e){const o=a(t.geometries),l=a(t.materials),c=a(t.textures),u=a(t.images),d=a(t.shapes),h=a(t.skeletons),p=a(t.animations),_=a(t.nodes);o.length>0&&(i.geometries=o),l.length>0&&(i.materials=l),c.length>0&&(i.textures=c),u.length>0&&(i.images=u),d.length>0&&(i.shapes=d),h.length>0&&(i.skeletons=h),p.length>0&&(i.animations=p),_.length>0&&(i.nodes=_)}return i.object=s,i;function a(o){const l=[];for(const c in o){const u=o[c];delete u.metadata,l.push(u)}return l}}clone(t){return new this.constructor().copy(this,t)}copy(t,e=!0){if(this.name=t.name,this.up.copy(t.up),this.position.copy(t.position),this.rotation.order=t.rotation.order,this.quaternion.copy(t.quaternion),this.scale.copy(t.scale),this.matrix.copy(t.matrix),this.matrixWorld.copy(t.matrixWorld),this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrixWorldAutoUpdate=t.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=t.matrixWorldNeedsUpdate,this.layers.mask=t.layers.mask,this.visible=t.visible,this.castShadow=t.castShadow,this.receiveShadow=t.receiveShadow,this.frustumCulled=t.frustumCulled,this.renderOrder=t.renderOrder,this.animations=t.animations.slice(),this.userData=JSON.parse(JSON.stringify(t.userData)),e===!0)for(let i=0;i<t.children.length;i++){const s=t.children[i];this.add(s.clone())}return this}}Te.DEFAULT_UP=new L(0,1,0);Te.DEFAULT_MATRIX_AUTO_UPDATE=!0;Te.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;const un=new L,Un=new L,_a=new L,Nn=new L,Fi=new L,Bi=new L,Wl=new L,va=new L,xa=new L,Sa=new L,ya=new Kt,Ea=new Kt,Ma=new Kt;class fn{constructor(t=new L,e=new L,i=new L){this.a=t,this.b=e,this.c=i}static getNormal(t,e,i,s){s.subVectors(i,e),un.subVectors(t,e),s.cross(un);const r=s.lengthSq();return r>0?s.multiplyScalar(1/Math.sqrt(r)):s.set(0,0,0)}static getBarycoord(t,e,i,s,r){un.subVectors(s,e),Un.subVectors(i,e),_a.subVectors(t,e);const a=un.dot(un),o=un.dot(Un),l=un.dot(_a),c=Un.dot(Un),u=Un.dot(_a),d=a*c-o*o;if(d===0)return r.set(0,0,0),null;const h=1/d,p=(c*l-o*u)*h,_=(a*u-o*l)*h;return r.set(1-p-_,_,p)}static containsPoint(t,e,i,s){return this.getBarycoord(t,e,i,s,Nn)===null?!1:Nn.x>=0&&Nn.y>=0&&Nn.x+Nn.y<=1}static getInterpolation(t,e,i,s,r,a,o,l){return this.getBarycoord(t,e,i,s,Nn)===null?(l.x=0,l.y=0,"z"in l&&(l.z=0),"w"in l&&(l.w=0),null):(l.setScalar(0),l.addScaledVector(r,Nn.x),l.addScaledVector(a,Nn.y),l.addScaledVector(o,Nn.z),l)}static getInterpolatedAttribute(t,e,i,s,r,a){return ya.setScalar(0),Ea.setScalar(0),Ma.setScalar(0),ya.fromBufferAttribute(t,e),Ea.fromBufferAttribute(t,i),Ma.fromBufferAttribute(t,s),a.setScalar(0),a.addScaledVector(ya,r.x),a.addScaledVector(Ea,r.y),a.addScaledVector(Ma,r.z),a}static isFrontFacing(t,e,i,s){return un.subVectors(i,e),Un.subVectors(t,e),un.cross(Un).dot(s)<0}set(t,e,i){return this.a.copy(t),this.b.copy(e),this.c.copy(i),this}setFromPointsAndIndices(t,e,i,s){return this.a.copy(t[e]),this.b.copy(t[i]),this.c.copy(t[s]),this}setFromAttributeAndIndices(t,e,i,s){return this.a.fromBufferAttribute(t,e),this.b.fromBufferAttribute(t,i),this.c.fromBufferAttribute(t,s),this}clone(){return new this.constructor().copy(this)}copy(t){return this.a.copy(t.a),this.b.copy(t.b),this.c.copy(t.c),this}getArea(){return un.subVectors(this.c,this.b),Un.subVectors(this.a,this.b),un.cross(Un).length()*.5}getMidpoint(t){return t.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(t){return fn.getNormal(this.a,this.b,this.c,t)}getPlane(t){return t.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(t,e){return fn.getBarycoord(t,this.a,this.b,this.c,e)}getInterpolation(t,e,i,s,r){return fn.getInterpolation(t,this.a,this.b,this.c,e,i,s,r)}containsPoint(t){return fn.containsPoint(t,this.a,this.b,this.c)}isFrontFacing(t){return fn.isFrontFacing(this.a,this.b,this.c,t)}intersectsBox(t){return t.intersectsTriangle(this)}closestPointToPoint(t,e){const i=this.a,s=this.b,r=this.c;let a,o;Fi.subVectors(s,i),Bi.subVectors(r,i),va.subVectors(t,i);const l=Fi.dot(va),c=Bi.dot(va);if(l<=0&&c<=0)return e.copy(i);xa.subVectors(t,s);const u=Fi.dot(xa),d=Bi.dot(xa);if(u>=0&&d<=u)return e.copy(s);const h=l*d-u*c;if(h<=0&&l>=0&&u<=0)return a=l/(l-u),e.copy(i).addScaledVector(Fi,a);Sa.subVectors(t,r);const p=Fi.dot(Sa),_=Bi.dot(Sa);if(_>=0&&p<=_)return e.copy(r);const S=p*c-l*_;if(S<=0&&c>=0&&_<=0)return o=c/(c-_),e.copy(i).addScaledVector(Bi,o);const m=u*_-p*d;if(m<=0&&d-u>=0&&p-_>=0)return Wl.subVectors(r,s),o=(d-u)/(d-u+(p-_)),e.copy(s).addScaledVector(Wl,o);const f=1/(m+S+h);return a=S*f,o=h*f,e.copy(i).addScaledVector(Fi,a).addScaledVector(Bi,o)}equals(t){return t.a.equals(this.a)&&t.b.equals(this.b)&&t.c.equals(this.c)}}const vu={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},Kn={h:0,s:0,l:0},nr={h:0,s:0,l:0};function Ta(n,t,e){return e<0&&(e+=1),e>1&&(e-=1),e<1/6?n+(t-n)*6*e:e<1/2?t:e<2/3?n+(t-n)*6*(2/3-e):n}class It{constructor(t,e,i){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(t,e,i)}set(t,e,i){if(e===void 0&&i===void 0){const s=t;s&&s.isColor?this.copy(s):typeof s=="number"?this.setHex(s):typeof s=="string"&&this.setStyle(s)}else this.setRGB(t,e,i);return this}setScalar(t){return this.r=t,this.g=t,this.b=t,this}setHex(t,e=Qe){return t=Math.floor(t),this.r=(t>>16&255)/255,this.g=(t>>8&255)/255,this.b=(t&255)/255,Gt.toWorkingColorSpace(this,e),this}setRGB(t,e,i,s=Gt.workingColorSpace){return this.r=t,this.g=e,this.b=i,Gt.toWorkingColorSpace(this,s),this}setHSL(t,e,i,s=Gt.workingColorSpace){if(t=Jd(t,1),e=Nt(e,0,1),i=Nt(i,0,1),e===0)this.r=this.g=this.b=i;else{const r=i<=.5?i*(1+e):i+e-i*e,a=2*i-r;this.r=Ta(a,r,t+1/3),this.g=Ta(a,r,t),this.b=Ta(a,r,t-1/3)}return Gt.toWorkingColorSpace(this,s),this}setStyle(t,e=Qe){function i(r){r!==void 0&&parseFloat(r)<1&&console.warn("THREE.Color: Alpha component of "+t+" will be ignored.")}let s;if(s=/^(\w+)\(([^\)]*)\)/.exec(t)){let r;const a=s[1],o=s[2];switch(a){case"rgb":case"rgba":if(r=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return i(r[4]),this.setRGB(Math.min(255,parseInt(r[1],10))/255,Math.min(255,parseInt(r[2],10))/255,Math.min(255,parseInt(r[3],10))/255,e);if(r=/^\s*(\d+)\%\s*,\s*(\d+)\%\s*,\s*(\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return i(r[4]),this.setRGB(Math.min(100,parseInt(r[1],10))/100,Math.min(100,parseInt(r[2],10))/100,Math.min(100,parseInt(r[3],10))/100,e);break;case"hsl":case"hsla":if(r=/^\s*(\d*\.?\d+)\s*,\s*(\d*\.?\d+)\%\s*,\s*(\d*\.?\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return i(r[4]),this.setHSL(parseFloat(r[1])/360,parseFloat(r[2])/100,parseFloat(r[3])/100,e);break;default:console.warn("THREE.Color: Unknown color model "+t)}}else if(s=/^\#([A-Fa-f\d]+)$/.exec(t)){const r=s[1],a=r.length;if(a===3)return this.setRGB(parseInt(r.charAt(0),16)/15,parseInt(r.charAt(1),16)/15,parseInt(r.charAt(2),16)/15,e);if(a===6)return this.setHex(parseInt(r,16),e);console.warn("THREE.Color: Invalid hex color "+t)}else if(t&&t.length>0)return this.setColorName(t,e);return this}setColorName(t,e=Qe){const i=vu[t.toLowerCase()];return i!==void 0?this.setHex(i,e):console.warn("THREE.Color: Unknown color "+t),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(t){return this.r=t.r,this.g=t.g,this.b=t.b,this}copySRGBToLinear(t){return this.r=Gn(t.r),this.g=Gn(t.g),this.b=Gn(t.b),this}copyLinearToSRGB(t){return this.r=Zi(t.r),this.g=Zi(t.g),this.b=Zi(t.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(t=Qe){return Gt.fromWorkingColorSpace(we.copy(this),t),Math.round(Nt(we.r*255,0,255))*65536+Math.round(Nt(we.g*255,0,255))*256+Math.round(Nt(we.b*255,0,255))}getHexString(t=Qe){return("000000"+this.getHex(t).toString(16)).slice(-6)}getHSL(t,e=Gt.workingColorSpace){Gt.fromWorkingColorSpace(we.copy(this),e);const i=we.r,s=we.g,r=we.b,a=Math.max(i,s,r),o=Math.min(i,s,r);let l,c;const u=(o+a)/2;if(o===a)l=0,c=0;else{const d=a-o;switch(c=u<=.5?d/(a+o):d/(2-a-o),a){case i:l=(s-r)/d+(s<r?6:0);break;case s:l=(r-i)/d+2;break;case r:l=(i-s)/d+4;break}l/=6}return t.h=l,t.s=c,t.l=u,t}getRGB(t,e=Gt.workingColorSpace){return Gt.fromWorkingColorSpace(we.copy(this),e),t.r=we.r,t.g=we.g,t.b=we.b,t}getStyle(t=Qe){Gt.fromWorkingColorSpace(we.copy(this),t);const e=we.r,i=we.g,s=we.b;return t!==Qe?`color(${t} ${e.toFixed(3)} ${i.toFixed(3)} ${s.toFixed(3)})`:`rgb(${Math.round(e*255)},${Math.round(i*255)},${Math.round(s*255)})`}offsetHSL(t,e,i){return this.getHSL(Kn),this.setHSL(Kn.h+t,Kn.s+e,Kn.l+i)}add(t){return this.r+=t.r,this.g+=t.g,this.b+=t.b,this}addColors(t,e){return this.r=t.r+e.r,this.g=t.g+e.g,this.b=t.b+e.b,this}addScalar(t){return this.r+=t,this.g+=t,this.b+=t,this}sub(t){return this.r=Math.max(0,this.r-t.r),this.g=Math.max(0,this.g-t.g),this.b=Math.max(0,this.b-t.b),this}multiply(t){return this.r*=t.r,this.g*=t.g,this.b*=t.b,this}multiplyScalar(t){return this.r*=t,this.g*=t,this.b*=t,this}lerp(t,e){return this.r+=(t.r-this.r)*e,this.g+=(t.g-this.g)*e,this.b+=(t.b-this.b)*e,this}lerpColors(t,e,i){return this.r=t.r+(e.r-t.r)*i,this.g=t.g+(e.g-t.g)*i,this.b=t.b+(e.b-t.b)*i,this}lerpHSL(t,e){this.getHSL(Kn),t.getHSL(nr);const i=oa(Kn.h,nr.h,e),s=oa(Kn.s,nr.s,e),r=oa(Kn.l,nr.l,e);return this.setHSL(i,s,r),this}setFromVector3(t){return this.r=t.x,this.g=t.y,this.b=t.z,this}applyMatrix3(t){const e=this.r,i=this.g,s=this.b,r=t.elements;return this.r=r[0]*e+r[3]*i+r[6]*s,this.g=r[1]*e+r[4]*i+r[7]*s,this.b=r[2]*e+r[5]*i+r[8]*s,this}equals(t){return t.r===this.r&&t.g===this.g&&t.b===this.b}fromArray(t,e=0){return this.r=t[e],this.g=t[e+1],this.b=t[e+2],this}toArray(t=[],e=0){return t[e]=this.r,t[e+1]=this.g,t[e+2]=this.b,t}fromBufferAttribute(t,e){return this.r=t.getX(e),this.g=t.getY(e),this.b=t.getZ(e),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}}const we=new It;It.NAMES=vu;let _h=0;class Vs extends wi{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:_h++}),this.uuid=ks(),this.name="",this.type="Material",this.blending=Ki,this.side=oi,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=Ja,this.blendDst=Qa,this.blendEquation=_i,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new It(0,0,0),this.blendAlpha=0,this.depthFunc=es,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=Pl,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=Ci,this.stencilZFail=Ci,this.stencilZPass=Ci,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.allowOverride=!0,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(t){this._alphaTest>0!=t>0&&this.version++,this._alphaTest=t}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(t){if(t!==void 0)for(const e in t){const i=t[e];if(i===void 0){console.warn(`THREE.Material: parameter '${e}' has value of undefined.`);continue}const s=this[e];if(s===void 0){console.warn(`THREE.Material: '${e}' is not a property of THREE.${this.type}.`);continue}s&&s.isColor?s.set(i):s&&s.isVector3&&i&&i.isVector3?s.copy(i):this[e]=i}}toJSON(t){const e=t===void 0||typeof t=="string";e&&(t={textures:{},images:{}});const i={metadata:{version:4.6,type:"Material",generator:"Material.toJSON"}};i.uuid=this.uuid,i.type=this.type,this.name!==""&&(i.name=this.name),this.color&&this.color.isColor&&(i.color=this.color.getHex()),this.roughness!==void 0&&(i.roughness=this.roughness),this.metalness!==void 0&&(i.metalness=this.metalness),this.sheen!==void 0&&(i.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(i.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(i.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(i.emissive=this.emissive.getHex()),this.emissiveIntensity!==void 0&&this.emissiveIntensity!==1&&(i.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(i.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(i.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(i.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(i.shininess=this.shininess),this.clearcoat!==void 0&&(i.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(i.clearcoatRoughness=this.clearcoatRoughness),this.clearcoatMap&&this.clearcoatMap.isTexture&&(i.clearcoatMap=this.clearcoatMap.toJSON(t).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(i.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(t).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(i.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(t).uuid,i.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.dispersion!==void 0&&(i.dispersion=this.dispersion),this.iridescence!==void 0&&(i.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(i.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessRange!==void 0&&(i.iridescenceThicknessRange=this.iridescenceThicknessRange),this.iridescenceMap&&this.iridescenceMap.isTexture&&(i.iridescenceMap=this.iridescenceMap.toJSON(t).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(i.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(t).uuid),this.anisotropy!==void 0&&(i.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(i.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(i.anisotropyMap=this.anisotropyMap.toJSON(t).uuid),this.map&&this.map.isTexture&&(i.map=this.map.toJSON(t).uuid),this.matcap&&this.matcap.isTexture&&(i.matcap=this.matcap.toJSON(t).uuid),this.alphaMap&&this.alphaMap.isTexture&&(i.alphaMap=this.alphaMap.toJSON(t).uuid),this.lightMap&&this.lightMap.isTexture&&(i.lightMap=this.lightMap.toJSON(t).uuid,i.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(i.aoMap=this.aoMap.toJSON(t).uuid,i.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(i.bumpMap=this.bumpMap.toJSON(t).uuid,i.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(i.normalMap=this.normalMap.toJSON(t).uuid,i.normalMapType=this.normalMapType,i.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(i.displacementMap=this.displacementMap.toJSON(t).uuid,i.displacementScale=this.displacementScale,i.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(i.roughnessMap=this.roughnessMap.toJSON(t).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(i.metalnessMap=this.metalnessMap.toJSON(t).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(i.emissiveMap=this.emissiveMap.toJSON(t).uuid),this.specularMap&&this.specularMap.isTexture&&(i.specularMap=this.specularMap.toJSON(t).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(i.specularIntensityMap=this.specularIntensityMap.toJSON(t).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(i.specularColorMap=this.specularColorMap.toJSON(t).uuid),this.envMap&&this.envMap.isTexture&&(i.envMap=this.envMap.toJSON(t).uuid,this.combine!==void 0&&(i.combine=this.combine)),this.envMapRotation!==void 0&&(i.envMapRotation=this.envMapRotation.toArray()),this.envMapIntensity!==void 0&&(i.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(i.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(i.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(i.gradientMap=this.gradientMap.toJSON(t).uuid),this.transmission!==void 0&&(i.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(i.transmissionMap=this.transmissionMap.toJSON(t).uuid),this.thickness!==void 0&&(i.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(i.thicknessMap=this.thicknessMap.toJSON(t).uuid),this.attenuationDistance!==void 0&&this.attenuationDistance!==1/0&&(i.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(i.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(i.size=this.size),this.shadowSide!==null&&(i.shadowSide=this.shadowSide),this.sizeAttenuation!==void 0&&(i.sizeAttenuation=this.sizeAttenuation),this.blending!==Ki&&(i.blending=this.blending),this.side!==oi&&(i.side=this.side),this.vertexColors===!0&&(i.vertexColors=!0),this.opacity<1&&(i.opacity=this.opacity),this.transparent===!0&&(i.transparent=!0),this.blendSrc!==Ja&&(i.blendSrc=this.blendSrc),this.blendDst!==Qa&&(i.blendDst=this.blendDst),this.blendEquation!==_i&&(i.blendEquation=this.blendEquation),this.blendSrcAlpha!==null&&(i.blendSrcAlpha=this.blendSrcAlpha),this.blendDstAlpha!==null&&(i.blendDstAlpha=this.blendDstAlpha),this.blendEquationAlpha!==null&&(i.blendEquationAlpha=this.blendEquationAlpha),this.blendColor&&this.blendColor.isColor&&(i.blendColor=this.blendColor.getHex()),this.blendAlpha!==0&&(i.blendAlpha=this.blendAlpha),this.depthFunc!==es&&(i.depthFunc=this.depthFunc),this.depthTest===!1&&(i.depthTest=this.depthTest),this.depthWrite===!1&&(i.depthWrite=this.depthWrite),this.colorWrite===!1&&(i.colorWrite=this.colorWrite),this.stencilWriteMask!==255&&(i.stencilWriteMask=this.stencilWriteMask),this.stencilFunc!==Pl&&(i.stencilFunc=this.stencilFunc),this.stencilRef!==0&&(i.stencilRef=this.stencilRef),this.stencilFuncMask!==255&&(i.stencilFuncMask=this.stencilFuncMask),this.stencilFail!==Ci&&(i.stencilFail=this.stencilFail),this.stencilZFail!==Ci&&(i.stencilZFail=this.stencilZFail),this.stencilZPass!==Ci&&(i.stencilZPass=this.stencilZPass),this.stencilWrite===!0&&(i.stencilWrite=this.stencilWrite),this.rotation!==void 0&&this.rotation!==0&&(i.rotation=this.rotation),this.polygonOffset===!0&&(i.polygonOffset=!0),this.polygonOffsetFactor!==0&&(i.polygonOffsetFactor=this.polygonOffsetFactor),this.polygonOffsetUnits!==0&&(i.polygonOffsetUnits=this.polygonOffsetUnits),this.linewidth!==void 0&&this.linewidth!==1&&(i.linewidth=this.linewidth),this.dashSize!==void 0&&(i.dashSize=this.dashSize),this.gapSize!==void 0&&(i.gapSize=this.gapSize),this.scale!==void 0&&(i.scale=this.scale),this.dithering===!0&&(i.dithering=!0),this.alphaTest>0&&(i.alphaTest=this.alphaTest),this.alphaHash===!0&&(i.alphaHash=!0),this.alphaToCoverage===!0&&(i.alphaToCoverage=!0),this.premultipliedAlpha===!0&&(i.premultipliedAlpha=!0),this.forceSinglePass===!0&&(i.forceSinglePass=!0),this.wireframe===!0&&(i.wireframe=!0),this.wireframeLinewidth>1&&(i.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!=="round"&&(i.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!=="round"&&(i.wireframeLinejoin=this.wireframeLinejoin),this.flatShading===!0&&(i.flatShading=!0),this.visible===!1&&(i.visible=!1),this.toneMapped===!1&&(i.toneMapped=!1),this.fog===!1&&(i.fog=!1),Object.keys(this.userData).length>0&&(i.userData=this.userData);function s(r){const a=[];for(const o in r){const l=r[o];delete l.metadata,a.push(l)}return a}if(e){const r=s(t.textures),a=s(t.images);r.length>0&&(i.textures=r),a.length>0&&(i.images=a)}return i}clone(){return new this.constructor().copy(this)}copy(t){this.name=t.name,this.blending=t.blending,this.side=t.side,this.vertexColors=t.vertexColors,this.opacity=t.opacity,this.transparent=t.transparent,this.blendSrc=t.blendSrc,this.blendDst=t.blendDst,this.blendEquation=t.blendEquation,this.blendSrcAlpha=t.blendSrcAlpha,this.blendDstAlpha=t.blendDstAlpha,this.blendEquationAlpha=t.blendEquationAlpha,this.blendColor.copy(t.blendColor),this.blendAlpha=t.blendAlpha,this.depthFunc=t.depthFunc,this.depthTest=t.depthTest,this.depthWrite=t.depthWrite,this.stencilWriteMask=t.stencilWriteMask,this.stencilFunc=t.stencilFunc,this.stencilRef=t.stencilRef,this.stencilFuncMask=t.stencilFuncMask,this.stencilFail=t.stencilFail,this.stencilZFail=t.stencilZFail,this.stencilZPass=t.stencilZPass,this.stencilWrite=t.stencilWrite;const e=t.clippingPlanes;let i=null;if(e!==null){const s=e.length;i=new Array(s);for(let r=0;r!==s;++r)i[r]=e[r].clone()}return this.clippingPlanes=i,this.clipIntersection=t.clipIntersection,this.clipShadows=t.clipShadows,this.shadowSide=t.shadowSide,this.colorWrite=t.colorWrite,this.precision=t.precision,this.polygonOffset=t.polygonOffset,this.polygonOffsetFactor=t.polygonOffsetFactor,this.polygonOffsetUnits=t.polygonOffsetUnits,this.dithering=t.dithering,this.alphaTest=t.alphaTest,this.alphaHash=t.alphaHash,this.alphaToCoverage=t.alphaToCoverage,this.premultipliedAlpha=t.premultipliedAlpha,this.forceSinglePass=t.forceSinglePass,this.visible=t.visible,this.toneMapped=t.toneMapped,this.userData=JSON.parse(JSON.stringify(t.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(t){t===!0&&this.version++}onBuild(){console.warn("Material: onBuild() has been removed.")}}class xu extends Vs{constructor(t){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new It(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new Xn,this.combine=iu,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.specularMap=t.specularMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.envMapRotation.copy(t.envMapRotation),this.combine=t.combine,this.reflectivity=t.reflectivity,this.refractionRatio=t.refractionRatio,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.fog=t.fog,this}}const ue=new L,ir=new Tt;let vh=0;class Xe{constructor(t,e,i=!1){if(Array.isArray(t))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,Object.defineProperty(this,"id",{value:vh++}),this.name="",this.array=t,this.itemSize=e,this.count=t!==void 0?t.length/e:0,this.normalized=i,this.usage=Ll,this.updateRanges=[],this.gpuType=Hn,this.version=0}onUploadCallback(){}set needsUpdate(t){t===!0&&this.version++}setUsage(t){return this.usage=t,this}addUpdateRange(t,e){this.updateRanges.push({start:t,count:e})}clearUpdateRanges(){this.updateRanges.length=0}copy(t){return this.name=t.name,this.array=new t.array.constructor(t.array),this.itemSize=t.itemSize,this.count=t.count,this.normalized=t.normalized,this.usage=t.usage,this.gpuType=t.gpuType,this}copyAt(t,e,i){t*=this.itemSize,i*=e.itemSize;for(let s=0,r=this.itemSize;s<r;s++)this.array[t+s]=e.array[i+s];return this}copyArray(t){return this.array.set(t),this}applyMatrix3(t){if(this.itemSize===2)for(let e=0,i=this.count;e<i;e++)ir.fromBufferAttribute(this,e),ir.applyMatrix3(t),this.setXY(e,ir.x,ir.y);else if(this.itemSize===3)for(let e=0,i=this.count;e<i;e++)ue.fromBufferAttribute(this,e),ue.applyMatrix3(t),this.setXYZ(e,ue.x,ue.y,ue.z);return this}applyMatrix4(t){for(let e=0,i=this.count;e<i;e++)ue.fromBufferAttribute(this,e),ue.applyMatrix4(t),this.setXYZ(e,ue.x,ue.y,ue.z);return this}applyNormalMatrix(t){for(let e=0,i=this.count;e<i;e++)ue.fromBufferAttribute(this,e),ue.applyNormalMatrix(t),this.setXYZ(e,ue.x,ue.y,ue.z);return this}transformDirection(t){for(let e=0,i=this.count;e<i;e++)ue.fromBufferAttribute(this,e),ue.transformDirection(t),this.setXYZ(e,ue.x,ue.y,ue.z);return this}set(t,e=0){return this.array.set(t,e),this}getComponent(t,e){let i=this.array[t*this.itemSize+e];return this.normalized&&(i=cs(i,this.array)),i}setComponent(t,e,i){return this.normalized&&(i=Ie(i,this.array)),this.array[t*this.itemSize+e]=i,this}getX(t){let e=this.array[t*this.itemSize];return this.normalized&&(e=cs(e,this.array)),e}setX(t,e){return this.normalized&&(e=Ie(e,this.array)),this.array[t*this.itemSize]=e,this}getY(t){let e=this.array[t*this.itemSize+1];return this.normalized&&(e=cs(e,this.array)),e}setY(t,e){return this.normalized&&(e=Ie(e,this.array)),this.array[t*this.itemSize+1]=e,this}getZ(t){let e=this.array[t*this.itemSize+2];return this.normalized&&(e=cs(e,this.array)),e}setZ(t,e){return this.normalized&&(e=Ie(e,this.array)),this.array[t*this.itemSize+2]=e,this}getW(t){let e=this.array[t*this.itemSize+3];return this.normalized&&(e=cs(e,this.array)),e}setW(t,e){return this.normalized&&(e=Ie(e,this.array)),this.array[t*this.itemSize+3]=e,this}setXY(t,e,i){return t*=this.itemSize,this.normalized&&(e=Ie(e,this.array),i=Ie(i,this.array)),this.array[t+0]=e,this.array[t+1]=i,this}setXYZ(t,e,i,s){return t*=this.itemSize,this.normalized&&(e=Ie(e,this.array),i=Ie(i,this.array),s=Ie(s,this.array)),this.array[t+0]=e,this.array[t+1]=i,this.array[t+2]=s,this}setXYZW(t,e,i,s,r){return t*=this.itemSize,this.normalized&&(e=Ie(e,this.array),i=Ie(i,this.array),s=Ie(s,this.array),r=Ie(r,this.array)),this.array[t+0]=e,this.array[t+1]=i,this.array[t+2]=s,this.array[t+3]=r,this}onUpload(t){return this.onUploadCallback=t,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){const t={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return this.name!==""&&(t.name=this.name),this.usage!==Ll&&(t.usage=this.usage),t}}class Su extends Xe{constructor(t,e,i){super(new Uint16Array(t),e,i)}}class yu extends Xe{constructor(t,e,i){super(new Uint32Array(t),e,i)}}class $e extends Xe{constructor(t,e,i){super(new Float32Array(t),e,i)}}let xh=0;const Ke=new te,ba=new Te,zi=new L,He=new Hs,fs=new Hs,ge=new L;class xn extends wi{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:xh++}),this.uuid=ks(),this.name="",this.type="BufferGeometry",this.index=null,this.indirect=null,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={}}getIndex(){return this.index}setIndex(t){return Array.isArray(t)?this.index=new(gu(t)?yu:Su)(t,1):this.index=t,this}setIndirect(t){return this.indirect=t,this}getIndirect(){return this.indirect}getAttribute(t){return this.attributes[t]}setAttribute(t,e){return this.attributes[t]=e,this}deleteAttribute(t){return delete this.attributes[t],this}hasAttribute(t){return this.attributes[t]!==void 0}addGroup(t,e,i=0){this.groups.push({start:t,count:e,materialIndex:i})}clearGroups(){this.groups=[]}setDrawRange(t,e){this.drawRange.start=t,this.drawRange.count=e}applyMatrix4(t){const e=this.attributes.position;e!==void 0&&(e.applyMatrix4(t),e.needsUpdate=!0);const i=this.attributes.normal;if(i!==void 0){const r=new Pt().getNormalMatrix(t);i.applyNormalMatrix(r),i.needsUpdate=!0}const s=this.attributes.tangent;return s!==void 0&&(s.transformDirection(t),s.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this}applyQuaternion(t){return Ke.makeRotationFromQuaternion(t),this.applyMatrix4(Ke),this}rotateX(t){return Ke.makeRotationX(t),this.applyMatrix4(Ke),this}rotateY(t){return Ke.makeRotationY(t),this.applyMatrix4(Ke),this}rotateZ(t){return Ke.makeRotationZ(t),this.applyMatrix4(Ke),this}translate(t,e,i){return Ke.makeTranslation(t,e,i),this.applyMatrix4(Ke),this}scale(t,e,i){return Ke.makeScale(t,e,i),this.applyMatrix4(Ke),this}lookAt(t){return ba.lookAt(t),ba.updateMatrix(),this.applyMatrix4(ba.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(zi).negate(),this.translate(zi.x,zi.y,zi.z),this}setFromPoints(t){const e=this.getAttribute("position");if(e===void 0){const i=[];for(let s=0,r=t.length;s<r;s++){const a=t[s];i.push(a.x,a.y,a.z||0)}this.setAttribute("position",new $e(i,3))}else{const i=Math.min(t.length,e.count);for(let s=0;s<i;s++){const r=t[s];e.setXYZ(s,r.x,r.y,r.z||0)}t.length>e.count&&console.warn("THREE.BufferGeometry: Buffer size too small for points data. Use .dispose() and create a new geometry."),e.needsUpdate=!0}return this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new Hs);const t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box.",this),this.boundingBox.set(new L(-1/0,-1/0,-1/0),new L(1/0,1/0,1/0));return}if(t!==void 0){if(this.boundingBox.setFromBufferAttribute(t),e)for(let i=0,s=e.length;i<s;i++){const r=e[i];He.setFromBufferAttribute(r),this.morphTargetsRelative?(ge.addVectors(this.boundingBox.min,He.min),this.boundingBox.expandByPoint(ge),ge.addVectors(this.boundingBox.max,He.max),this.boundingBox.expandByPoint(ge)):(this.boundingBox.expandByPoint(He.min),this.boundingBox.expandByPoint(He.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&console.error('THREE.BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new Kr);const t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere.",this),this.boundingSphere.set(new L,1/0);return}if(t){const i=this.boundingSphere.center;if(He.setFromBufferAttribute(t),e)for(let r=0,a=e.length;r<a;r++){const o=e[r];fs.setFromBufferAttribute(o),this.morphTargetsRelative?(ge.addVectors(He.min,fs.min),He.expandByPoint(ge),ge.addVectors(He.max,fs.max),He.expandByPoint(ge)):(He.expandByPoint(fs.min),He.expandByPoint(fs.max))}He.getCenter(i);let s=0;for(let r=0,a=t.count;r<a;r++)ge.fromBufferAttribute(t,r),s=Math.max(s,i.distanceToSquared(ge));if(e)for(let r=0,a=e.length;r<a;r++){const o=e[r],l=this.morphTargetsRelative;for(let c=0,u=o.count;c<u;c++)ge.fromBufferAttribute(o,c),l&&(zi.fromBufferAttribute(t,c),ge.add(zi)),s=Math.max(s,i.distanceToSquared(ge))}this.boundingSphere.radius=Math.sqrt(s),isNaN(this.boundingSphere.radius)&&console.error('THREE.BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){const t=this.index,e=this.attributes;if(t===null||e.position===void 0||e.normal===void 0||e.uv===void 0){console.error("THREE.BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}const i=e.position,s=e.normal,r=e.uv;this.hasAttribute("tangent")===!1&&this.setAttribute("tangent",new Xe(new Float32Array(4*i.count),4));const a=this.getAttribute("tangent"),o=[],l=[];for(let I=0;I<i.count;I++)o[I]=new L,l[I]=new L;const c=new L,u=new L,d=new L,h=new Tt,p=new Tt,_=new Tt,S=new L,m=new L;function f(I,E,x){c.fromBufferAttribute(i,I),u.fromBufferAttribute(i,E),d.fromBufferAttribute(i,x),h.fromBufferAttribute(r,I),p.fromBufferAttribute(r,E),_.fromBufferAttribute(r,x),u.sub(c),d.sub(c),p.sub(h),_.sub(h);const C=1/(p.x*_.y-_.x*p.y);isFinite(C)&&(S.copy(u).multiplyScalar(_.y).addScaledVector(d,-p.y).multiplyScalar(C),m.copy(d).multiplyScalar(p.x).addScaledVector(u,-_.x).multiplyScalar(C),o[I].add(S),o[E].add(S),o[x].add(S),l[I].add(m),l[E].add(m),l[x].add(m))}let b=this.groups;b.length===0&&(b=[{start:0,count:t.count}]);for(let I=0,E=b.length;I<E;++I){const x=b[I],C=x.start,V=x.count;for(let z=C,Y=C+V;z<Y;z+=3)f(t.getX(z+0),t.getX(z+1),t.getX(z+2))}const M=new L,y=new L,P=new L,R=new L;function A(I){P.fromBufferAttribute(s,I),R.copy(P);const E=o[I];M.copy(E),M.sub(P.multiplyScalar(P.dot(E))).normalize(),y.crossVectors(R,E);const C=y.dot(l[I])<0?-1:1;a.setXYZW(I,M.x,M.y,M.z,C)}for(let I=0,E=b.length;I<E;++I){const x=b[I],C=x.start,V=x.count;for(let z=C,Y=C+V;z<Y;z+=3)A(t.getX(z+0)),A(t.getX(z+1)),A(t.getX(z+2))}}computeVertexNormals(){const t=this.index,e=this.getAttribute("position");if(e!==void 0){let i=this.getAttribute("normal");if(i===void 0)i=new Xe(new Float32Array(e.count*3),3),this.setAttribute("normal",i);else for(let h=0,p=i.count;h<p;h++)i.setXYZ(h,0,0,0);const s=new L,r=new L,a=new L,o=new L,l=new L,c=new L,u=new L,d=new L;if(t)for(let h=0,p=t.count;h<p;h+=3){const _=t.getX(h+0),S=t.getX(h+1),m=t.getX(h+2);s.fromBufferAttribute(e,_),r.fromBufferAttribute(e,S),a.fromBufferAttribute(e,m),u.subVectors(a,r),d.subVectors(s,r),u.cross(d),o.fromBufferAttribute(i,_),l.fromBufferAttribute(i,S),c.fromBufferAttribute(i,m),o.add(u),l.add(u),c.add(u),i.setXYZ(_,o.x,o.y,o.z),i.setXYZ(S,l.x,l.y,l.z),i.setXYZ(m,c.x,c.y,c.z)}else for(let h=0,p=e.count;h<p;h+=3)s.fromBufferAttribute(e,h+0),r.fromBufferAttribute(e,h+1),a.fromBufferAttribute(e,h+2),u.subVectors(a,r),d.subVectors(s,r),u.cross(d),i.setXYZ(h+0,u.x,u.y,u.z),i.setXYZ(h+1,u.x,u.y,u.z),i.setXYZ(h+2,u.x,u.y,u.z);this.normalizeNormals(),i.needsUpdate=!0}}normalizeNormals(){const t=this.attributes.normal;for(let e=0,i=t.count;e<i;e++)ge.fromBufferAttribute(t,e),ge.normalize(),t.setXYZ(e,ge.x,ge.y,ge.z)}toNonIndexed(){function t(o,l){const c=o.array,u=o.itemSize,d=o.normalized,h=new c.constructor(l.length*u);let p=0,_=0;for(let S=0,m=l.length;S<m;S++){o.isInterleavedBufferAttribute?p=l[S]*o.data.stride+o.offset:p=l[S]*u;for(let f=0;f<u;f++)h[_++]=c[p++]}return new Xe(h,u,d)}if(this.index===null)return console.warn("THREE.BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;const e=new xn,i=this.index.array,s=this.attributes;for(const o in s){const l=s[o],c=t(l,i);e.setAttribute(o,c)}const r=this.morphAttributes;for(const o in r){const l=[],c=r[o];for(let u=0,d=c.length;u<d;u++){const h=c[u],p=t(h,i);l.push(p)}e.morphAttributes[o]=l}e.morphTargetsRelative=this.morphTargetsRelative;const a=this.groups;for(let o=0,l=a.length;o<l;o++){const c=a[o];e.addGroup(c.start,c.count,c.materialIndex)}return e}toJSON(){const t={metadata:{version:4.6,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(t.uuid=this.uuid,t.type=this.type,this.name!==""&&(t.name=this.name),Object.keys(this.userData).length>0&&(t.userData=this.userData),this.parameters!==void 0){const l=this.parameters;for(const c in l)l[c]!==void 0&&(t[c]=l[c]);return t}t.data={attributes:{}};const e=this.index;e!==null&&(t.data.index={type:e.array.constructor.name,array:Array.prototype.slice.call(e.array)});const i=this.attributes;for(const l in i){const c=i[l];t.data.attributes[l]=c.toJSON(t.data)}const s={};let r=!1;for(const l in this.morphAttributes){const c=this.morphAttributes[l],u=[];for(let d=0,h=c.length;d<h;d++){const p=c[d];u.push(p.toJSON(t.data))}u.length>0&&(s[l]=u,r=!0)}r&&(t.data.morphAttributes=s,t.data.morphTargetsRelative=this.morphTargetsRelative);const a=this.groups;a.length>0&&(t.data.groups=JSON.parse(JSON.stringify(a)));const o=this.boundingSphere;return o!==null&&(t.data.boundingSphere={center:o.center.toArray(),radius:o.radius}),t}clone(){return new this.constructor().copy(this)}copy(t){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;const e={};this.name=t.name;const i=t.index;i!==null&&this.setIndex(i.clone());const s=t.attributes;for(const c in s){const u=s[c];this.setAttribute(c,u.clone(e))}const r=t.morphAttributes;for(const c in r){const u=[],d=r[c];for(let h=0,p=d.length;h<p;h++)u.push(d[h].clone(e));this.morphAttributes[c]=u}this.morphTargetsRelative=t.morphTargetsRelative;const a=t.groups;for(let c=0,u=a.length;c<u;c++){const d=a[c];this.addGroup(d.start,d.count,d.materialIndex)}const o=t.boundingBox;o!==null&&(this.boundingBox=o.clone());const l=t.boundingSphere;return l!==null&&(this.boundingSphere=l.clone()),this.drawRange.start=t.drawRange.start,this.drawRange.count=t.drawRange.count,this.userData=t.userData,this}dispose(){this.dispatchEvent({type:"dispose"})}}const Xl=new te,hi=new Zr,sr=new Kr,$l=new L,rr=new L,ar=new L,or=new L,Aa=new L,lr=new L,ql=new L,cr=new L;class mn extends Te{constructor(t=new xn,e=new xu){super(),this.isMesh=!0,this.type="Mesh",this.geometry=t,this.material=e,this.morphTargetDictionary=void 0,this.morphTargetInfluences=void 0,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),t.morphTargetInfluences!==void 0&&(this.morphTargetInfluences=t.morphTargetInfluences.slice()),t.morphTargetDictionary!==void 0&&(this.morphTargetDictionary=Object.assign({},t.morphTargetDictionary)),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}updateMorphTargets(){const e=this.geometry.morphAttributes,i=Object.keys(e);if(i.length>0){const s=e[i[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){const o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}getVertexPosition(t,e){const i=this.geometry,s=i.attributes.position,r=i.morphAttributes.position,a=i.morphTargetsRelative;e.fromBufferAttribute(s,t);const o=this.morphTargetInfluences;if(r&&o){lr.set(0,0,0);for(let l=0,c=r.length;l<c;l++){const u=o[l],d=r[l];u!==0&&(Aa.fromBufferAttribute(d,t),a?lr.addScaledVector(Aa,u):lr.addScaledVector(Aa.sub(e),u))}e.add(lr)}return e}raycast(t,e){const i=this.geometry,s=this.material,r=this.matrixWorld;s!==void 0&&(i.boundingSphere===null&&i.computeBoundingSphere(),sr.copy(i.boundingSphere),sr.applyMatrix4(r),hi.copy(t.ray).recast(t.near),!(sr.containsPoint(hi.origin)===!1&&(hi.intersectSphere(sr,$l)===null||hi.origin.distanceToSquared($l)>(t.far-t.near)**2))&&(Xl.copy(r).invert(),hi.copy(t.ray).applyMatrix4(Xl),!(i.boundingBox!==null&&hi.intersectsBox(i.boundingBox)===!1)&&this._computeIntersections(t,e,hi)))}_computeIntersections(t,e,i){let s;const r=this.geometry,a=this.material,o=r.index,l=r.attributes.position,c=r.attributes.uv,u=r.attributes.uv1,d=r.attributes.normal,h=r.groups,p=r.drawRange;if(o!==null)if(Array.isArray(a))for(let _=0,S=h.length;_<S;_++){const m=h[_],f=a[m.materialIndex],b=Math.max(m.start,p.start),M=Math.min(o.count,Math.min(m.start+m.count,p.start+p.count));for(let y=b,P=M;y<P;y+=3){const R=o.getX(y),A=o.getX(y+1),I=o.getX(y+2);s=ur(this,f,t,i,c,u,d,R,A,I),s&&(s.faceIndex=Math.floor(y/3),s.face.materialIndex=m.materialIndex,e.push(s))}}else{const _=Math.max(0,p.start),S=Math.min(o.count,p.start+p.count);for(let m=_,f=S;m<f;m+=3){const b=o.getX(m),M=o.getX(m+1),y=o.getX(m+2);s=ur(this,a,t,i,c,u,d,b,M,y),s&&(s.faceIndex=Math.floor(m/3),e.push(s))}}else if(l!==void 0)if(Array.isArray(a))for(let _=0,S=h.length;_<S;_++){const m=h[_],f=a[m.materialIndex],b=Math.max(m.start,p.start),M=Math.min(l.count,Math.min(m.start+m.count,p.start+p.count));for(let y=b,P=M;y<P;y+=3){const R=y,A=y+1,I=y+2;s=ur(this,f,t,i,c,u,d,R,A,I),s&&(s.faceIndex=Math.floor(y/3),s.face.materialIndex=m.materialIndex,e.push(s))}}else{const _=Math.max(0,p.start),S=Math.min(l.count,p.start+p.count);for(let m=_,f=S;m<f;m+=3){const b=m,M=m+1,y=m+2;s=ur(this,a,t,i,c,u,d,b,M,y),s&&(s.faceIndex=Math.floor(m/3),e.push(s))}}}}function Sh(n,t,e,i,s,r,a,o){let l;if(t.side===Le?l=i.intersectTriangle(a,r,s,!0,o):l=i.intersectTriangle(s,r,a,t.side===oi,o),l===null)return null;cr.copy(o),cr.applyMatrix4(n.matrixWorld);const c=e.ray.origin.distanceTo(cr);return c<e.near||c>e.far?null:{distance:c,point:cr.clone(),object:n}}function ur(n,t,e,i,s,r,a,o,l,c){n.getVertexPosition(o,rr),n.getVertexPosition(l,ar),n.getVertexPosition(c,or);const u=Sh(n,t,e,i,rr,ar,or,ql);if(u){const d=new L;fn.getBarycoord(ql,rr,ar,or,d),s&&(u.uv=fn.getInterpolatedAttribute(s,o,l,c,d,new Tt)),r&&(u.uv1=fn.getInterpolatedAttribute(r,o,l,c,d,new Tt)),a&&(u.normal=fn.getInterpolatedAttribute(a,o,l,c,d,new L),u.normal.dot(i.direction)>0&&u.normal.multiplyScalar(-1));const h={a:o,b:l,c,normal:new L,materialIndex:0};fn.getNormal(rr,ar,or,h.normal),u.face=h,u.barycoord=d}return u}class Gs extends xn{constructor(t=1,e=1,i=1,s=1,r=1,a=1){super(),this.type="BoxGeometry",this.parameters={width:t,height:e,depth:i,widthSegments:s,heightSegments:r,depthSegments:a};const o=this;s=Math.floor(s),r=Math.floor(r),a=Math.floor(a);const l=[],c=[],u=[],d=[];let h=0,p=0;_("z","y","x",-1,-1,i,e,t,a,r,0),_("z","y","x",1,-1,i,e,-t,a,r,1),_("x","z","y",1,1,t,i,e,s,a,2),_("x","z","y",1,-1,t,i,-e,s,a,3),_("x","y","z",1,-1,t,e,i,s,r,4),_("x","y","z",-1,-1,t,e,-i,s,r,5),this.setIndex(l),this.setAttribute("position",new $e(c,3)),this.setAttribute("normal",new $e(u,3)),this.setAttribute("uv",new $e(d,2));function _(S,m,f,b,M,y,P,R,A,I,E){const x=y/A,C=P/I,V=y/2,z=P/2,Y=R/2,j=A+1,X=I+1;let Z=0,H=0;const it=new L;for(let ut=0;ut<X;ut++){const vt=ut*C-z;for(let Ut=0;Ut<j;Ut++){const Zt=Ut*x-V;it[S]=Zt*b,it[m]=vt*M,it[f]=Y,c.push(it.x,it.y,it.z),it[S]=0,it[m]=0,it[f]=R>0?1:-1,u.push(it.x,it.y,it.z),d.push(Ut/A),d.push(1-ut/I),Z+=1}}for(let ut=0;ut<I;ut++)for(let vt=0;vt<A;vt++){const Ut=h+vt+j*ut,Zt=h+vt+j*(ut+1),W=h+(vt+1)+j*(ut+1),tt=h+(vt+1)+j*ut;l.push(Ut,Zt,tt),l.push(Zt,W,tt),H+=6}o.addGroup(p,H,E),p+=H,h+=Z}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new Gs(t.width,t.height,t.depth,t.widthSegments,t.heightSegments,t.depthSegments)}}function rs(n){const t={};for(const e in n){t[e]={};for(const i in n[e]){const s=n[e][i];s&&(s.isColor||s.isMatrix3||s.isMatrix4||s.isVector2||s.isVector3||s.isVector4||s.isTexture||s.isQuaternion)?s.isRenderTargetTexture?(console.warn("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),t[e][i]=null):t[e][i]=s.clone():Array.isArray(s)?t[e][i]=s.slice():t[e][i]=s}}return t}function Pe(n){const t={};for(let e=0;e<n.length;e++){const i=rs(n[e]);for(const s in i)t[s]=i[s]}return t}function yh(n){const t=[];for(let e=0;e<n.length;e++)t.push(n[e].clone());return t}function Eu(n){const t=n.getRenderTarget();return t===null?n.outputColorSpace:t.isXRRenderTarget===!0?t.texture.colorSpace:Gt.workingColorSpace}const Eh={clone:rs,merge:Pe};var Mh=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,Th=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`;class _n extends Vs{constructor(t){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=Mh,this.fragmentShader=Th,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={clipCullDistance:!1,multiDraw:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,t!==void 0&&this.setValues(t)}copy(t){return super.copy(t),this.fragmentShader=t.fragmentShader,this.vertexShader=t.vertexShader,this.uniforms=rs(t.uniforms),this.uniformsGroups=yh(t.uniformsGroups),this.defines=Object.assign({},t.defines),this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.fog=t.fog,this.lights=t.lights,this.clipping=t.clipping,this.extensions=Object.assign({},t.extensions),this.glslVersion=t.glslVersion,this}toJSON(t){const e=super.toJSON(t);e.glslVersion=this.glslVersion,e.uniforms={};for(const s in this.uniforms){const a=this.uniforms[s].value;a&&a.isTexture?e.uniforms[s]={type:"t",value:a.toJSON(t).uuid}:a&&a.isColor?e.uniforms[s]={type:"c",value:a.getHex()}:a&&a.isVector2?e.uniforms[s]={type:"v2",value:a.toArray()}:a&&a.isVector3?e.uniforms[s]={type:"v3",value:a.toArray()}:a&&a.isVector4?e.uniforms[s]={type:"v4",value:a.toArray()}:a&&a.isMatrix3?e.uniforms[s]={type:"m3",value:a.toArray()}:a&&a.isMatrix4?e.uniforms[s]={type:"m4",value:a.toArray()}:e.uniforms[s]={value:a}}Object.keys(this.defines).length>0&&(e.defines=this.defines),e.vertexShader=this.vertexShader,e.fragmentShader=this.fragmentShader,e.lights=this.lights,e.clipping=this.clipping;const i={};for(const s in this.extensions)this.extensions[s]===!0&&(i[s]=!0);return Object.keys(i).length>0&&(e.extensions=i),e}}class Mu extends Te{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new te,this.projectionMatrix=new te,this.projectionMatrixInverse=new te,this.coordinateSystem=Vn}copy(t,e){return super.copy(t,e),this.matrixWorldInverse.copy(t.matrixWorldInverse),this.projectionMatrix.copy(t.projectionMatrix),this.projectionMatrixInverse.copy(t.projectionMatrixInverse),this.coordinateSystem=t.coordinateSystem,this}getWorldDirection(t){return super.getWorldDirection(t).negate()}updateMatrixWorld(t){super.updateMatrixWorld(t),this.matrixWorldInverse.copy(this.matrixWorld).invert()}updateWorldMatrix(t,e){super.updateWorldMatrix(t,e),this.matrixWorldInverse.copy(this.matrixWorld).invert()}clone(){return new this.constructor().copy(this)}}const Zn=new L,Yl=new Tt,jl=new Tt;class Ge extends Mu{constructor(t=50,e=1,i=.1,s=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=t,this.zoom=1,this.near=i,this.far=s,this.focus=10,this.aspect=e,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.fov=t.fov,this.zoom=t.zoom,this.near=t.near,this.far=t.far,this.focus=t.focus,this.aspect=t.aspect,this.view=t.view===null?null:Object.assign({},t.view),this.filmGauge=t.filmGauge,this.filmOffset=t.filmOffset,this}setFocalLength(t){const e=.5*this.getFilmHeight()/t;this.fov=Bo*2*Math.atan(e),this.updateProjectionMatrix()}getFocalLength(){const t=Math.tan(Pr*.5*this.fov);return .5*this.getFilmHeight()/t}getEffectiveFOV(){return Bo*2*Math.atan(Math.tan(Pr*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}getViewBounds(t,e,i){Zn.set(-1,-1,.5).applyMatrix4(this.projectionMatrixInverse),e.set(Zn.x,Zn.y).multiplyScalar(-t/Zn.z),Zn.set(1,1,.5).applyMatrix4(this.projectionMatrixInverse),i.set(Zn.x,Zn.y).multiplyScalar(-t/Zn.z)}getViewSize(t,e){return this.getViewBounds(t,Yl,jl),e.subVectors(jl,Yl)}setViewOffset(t,e,i,s,r,a){this.aspect=t/e,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=i,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){const t=this.near;let e=t*Math.tan(Pr*.5*this.fov)/this.zoom,i=2*e,s=this.aspect*i,r=-.5*s;const a=this.view;if(this.view!==null&&this.view.enabled){const l=a.fullWidth,c=a.fullHeight;r+=a.offsetX*s/l,e-=a.offsetY*i/c,s*=a.width/l,i*=a.height/c}const o=this.filmOffset;o!==0&&(r+=t*o/this.getFilmWidth()),this.projectionMatrix.makePerspective(r,r+s,e,e-i,t,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){const e=super.toJSON(t);return e.object.fov=this.fov,e.object.zoom=this.zoom,e.object.near=this.near,e.object.far=this.far,e.object.focus=this.focus,e.object.aspect=this.aspect,this.view!==null&&(e.object.view=Object.assign({},this.view)),e.object.filmGauge=this.filmGauge,e.object.filmOffset=this.filmOffset,e}}const ki=-90,Hi=1;class bh extends Te{constructor(t,e,i){super(),this.type="CubeCamera",this.renderTarget=i,this.coordinateSystem=null,this.activeMipmapLevel=0;const s=new Ge(ki,Hi,t,e);s.layers=this.layers,this.add(s);const r=new Ge(ki,Hi,t,e);r.layers=this.layers,this.add(r);const a=new Ge(ki,Hi,t,e);a.layers=this.layers,this.add(a);const o=new Ge(ki,Hi,t,e);o.layers=this.layers,this.add(o);const l=new Ge(ki,Hi,t,e);l.layers=this.layers,this.add(l);const c=new Ge(ki,Hi,t,e);c.layers=this.layers,this.add(c)}updateCoordinateSystem(){const t=this.coordinateSystem,e=this.children.concat(),[i,s,r,a,o,l]=e;for(const c of e)this.remove(c);if(t===Vn)i.up.set(0,1,0),i.lookAt(1,0,0),s.up.set(0,1,0),s.lookAt(-1,0,0),r.up.set(0,0,-1),r.lookAt(0,1,0),a.up.set(0,0,1),a.lookAt(0,-1,0),o.up.set(0,1,0),o.lookAt(0,0,1),l.up.set(0,1,0),l.lookAt(0,0,-1);else if(t===zr)i.up.set(0,-1,0),i.lookAt(-1,0,0),s.up.set(0,-1,0),s.lookAt(1,0,0),r.up.set(0,0,1),r.lookAt(0,1,0),a.up.set(0,0,-1),a.lookAt(0,-1,0),o.up.set(0,-1,0),o.lookAt(0,0,1),l.up.set(0,-1,0),l.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+t);for(const c of e)this.add(c),c.updateMatrixWorld()}update(t,e){this.parent===null&&this.updateMatrixWorld();const{renderTarget:i,activeMipmapLevel:s}=this;this.coordinateSystem!==t.coordinateSystem&&(this.coordinateSystem=t.coordinateSystem,this.updateCoordinateSystem());const[r,a,o,l,c,u]=this.children,d=t.getRenderTarget(),h=t.getActiveCubeFace(),p=t.getActiveMipmapLevel(),_=t.xr.enabled;t.xr.enabled=!1;const S=i.texture.generateMipmaps;i.texture.generateMipmaps=!1,t.setRenderTarget(i,0,s),t.render(e,r),t.setRenderTarget(i,1,s),t.render(e,a),t.setRenderTarget(i,2,s),t.render(e,o),t.setRenderTarget(i,3,s),t.render(e,l),t.setRenderTarget(i,4,s),t.render(e,c),i.texture.generateMipmaps=S,t.setRenderTarget(i,5,s),t.render(e,u),t.setRenderTarget(d,h,p),t.xr.enabled=_,i.texture.needsPMREMUpdate=!0}}class Tu extends Be{constructor(t=[],e=ns,i,s,r,a,o,l,c,u){super(t,e,i,s,r,a,o,l,c,u),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(t){this.image=t}}class Ah extends Ti{constructor(t=1,e={}){super(t,t,e),this.isWebGLCubeRenderTarget=!0;const i={width:t,height:t,depth:1},s=[i,i,i,i,i,i];this.texture=new Tu(s,e.mapping,e.wrapS,e.wrapT,e.magFilter,e.minFilter,e.format,e.type,e.anisotropy,e.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.generateMipmaps=e.generateMipmaps!==void 0?e.generateMipmaps:!1,this.texture.minFilter=e.minFilter!==void 0?e.minFilter:Rn}fromEquirectangularTexture(t,e){this.texture.type=e.type,this.texture.colorSpace=e.colorSpace,this.texture.generateMipmaps=e.generateMipmaps,this.texture.minFilter=e.minFilter,this.texture.magFilter=e.magFilter;const i={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},s=new Gs(5,5,5),r=new _n({name:"CubemapFromEquirect",uniforms:rs(i.uniforms),vertexShader:i.vertexShader,fragmentShader:i.fragmentShader,side:Le,blending:ri});r.uniforms.tEquirect.value=e;const a=new mn(s,r),o=e.minFilter;return e.minFilter===Si&&(e.minFilter=Rn),new bh(1,10,this).update(t,a),e.minFilter=o,a.geometry.dispose(),a.material.dispose(),this}clear(t,e=!0,i=!0,s=!0){const r=t.getRenderTarget();for(let a=0;a<6;a++)t.setRenderTarget(this,a),t.clear(e,i,s);t.setRenderTarget(r)}}class xs extends Te{constructor(){super(),this.isGroup=!0,this.type="Group"}}const wh={type:"move"};class wa{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new xs,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new xs,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new L,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new L),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new xs,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new L,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new L),this._grip}dispatchEvent(t){return this._targetRay!==null&&this._targetRay.dispatchEvent(t),this._grip!==null&&this._grip.dispatchEvent(t),this._hand!==null&&this._hand.dispatchEvent(t),this}connect(t){if(t&&t.hand){const e=this._hand;if(e)for(const i of t.hand.values())this._getHandJoint(e,i)}return this.dispatchEvent({type:"connected",data:t}),this}disconnect(t){return this.dispatchEvent({type:"disconnected",data:t}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(t,e,i){let s=null,r=null,a=null;const o=this._targetRay,l=this._grip,c=this._hand;if(t&&e.session.visibilityState!=="visible-blurred"){if(c&&t.hand){a=!0;for(const S of t.hand.values()){const m=e.getJointPose(S,i),f=this._getHandJoint(c,S);m!==null&&(f.matrix.fromArray(m.transform.matrix),f.matrix.decompose(f.position,f.rotation,f.scale),f.matrixWorldNeedsUpdate=!0,f.jointRadius=m.radius),f.visible=m!==null}const u=c.joints["index-finger-tip"],d=c.joints["thumb-tip"],h=u.position.distanceTo(d.position),p=.02,_=.005;c.inputState.pinching&&h>p+_?(c.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:t.handedness,target:this})):!c.inputState.pinching&&h<=p-_&&(c.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:t.handedness,target:this}))}else l!==null&&t.gripSpace&&(r=e.getPose(t.gripSpace,i),r!==null&&(l.matrix.fromArray(r.transform.matrix),l.matrix.decompose(l.position,l.rotation,l.scale),l.matrixWorldNeedsUpdate=!0,r.linearVelocity?(l.hasLinearVelocity=!0,l.linearVelocity.copy(r.linearVelocity)):l.hasLinearVelocity=!1,r.angularVelocity?(l.hasAngularVelocity=!0,l.angularVelocity.copy(r.angularVelocity)):l.hasAngularVelocity=!1));o!==null&&(s=e.getPose(t.targetRaySpace,i),s===null&&r!==null&&(s=r),s!==null&&(o.matrix.fromArray(s.transform.matrix),o.matrix.decompose(o.position,o.rotation,o.scale),o.matrixWorldNeedsUpdate=!0,s.linearVelocity?(o.hasLinearVelocity=!0,o.linearVelocity.copy(s.linearVelocity)):o.hasLinearVelocity=!1,s.angularVelocity?(o.hasAngularVelocity=!0,o.angularVelocity.copy(s.angularVelocity)):o.hasAngularVelocity=!1,this.dispatchEvent(wh)))}return o!==null&&(o.visible=s!==null),l!==null&&(l.visible=r!==null),c!==null&&(c.visible=a!==null),this}_getHandJoint(t,e){if(t.joints[e.jointName]===void 0){const i=new xs;i.matrixAutoUpdate=!1,i.visible=!1,t.joints[e.jointName]=i,t.add(i)}return t.joints[e.jointName]}}class al{constructor(t,e=25e-5){this.isFogExp2=!0,this.name="",this.color=new It(t),this.density=e}clone(){return new al(this.color,this.density)}toJSON(){return{type:"FogExp2",name:this.name,color:this.color.getHex(),density:this.density}}}class Rh extends Te{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.backgroundRotation=new Xn,this.environmentIntensity=1,this.environmentRotation=new Xn,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(t,e){return super.copy(t,e),t.background!==null&&(this.background=t.background.clone()),t.environment!==null&&(this.environment=t.environment.clone()),t.fog!==null&&(this.fog=t.fog.clone()),this.backgroundBlurriness=t.backgroundBlurriness,this.backgroundIntensity=t.backgroundIntensity,this.backgroundRotation.copy(t.backgroundRotation),this.environmentIntensity=t.environmentIntensity,this.environmentRotation.copy(t.environmentRotation),t.overrideMaterial!==null&&(this.overrideMaterial=t.overrideMaterial.clone()),this.matrixAutoUpdate=t.matrixAutoUpdate,this}toJSON(t){const e=super.toJSON(t);return this.fog!==null&&(e.object.fog=this.fog.toJSON()),this.backgroundBlurriness>0&&(e.object.backgroundBlurriness=this.backgroundBlurriness),this.backgroundIntensity!==1&&(e.object.backgroundIntensity=this.backgroundIntensity),e.object.backgroundRotation=this.backgroundRotation.toArray(),this.environmentIntensity!==1&&(e.object.environmentIntensity=this.environmentIntensity),e.object.environmentRotation=this.environmentRotation.toArray(),e}}const Ra=new L,Ch=new L,Ph=new Pt;class ti{constructor(t=new L(1,0,0),e=0){this.isPlane=!0,this.normal=t,this.constant=e}set(t,e){return this.normal.copy(t),this.constant=e,this}setComponents(t,e,i,s){return this.normal.set(t,e,i),this.constant=s,this}setFromNormalAndCoplanarPoint(t,e){return this.normal.copy(t),this.constant=-e.dot(this.normal),this}setFromCoplanarPoints(t,e,i){const s=Ra.subVectors(i,e).cross(Ch.subVectors(t,e)).normalize();return this.setFromNormalAndCoplanarPoint(s,t),this}copy(t){return this.normal.copy(t.normal),this.constant=t.constant,this}normalize(){const t=1/this.normal.length();return this.normal.multiplyScalar(t),this.constant*=t,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(t){return this.normal.dot(t)+this.constant}distanceToSphere(t){return this.distanceToPoint(t.center)-t.radius}projectPoint(t,e){return e.copy(t).addScaledVector(this.normal,-this.distanceToPoint(t))}intersectLine(t,e){const i=t.delta(Ra),s=this.normal.dot(i);if(s===0)return this.distanceToPoint(t.start)===0?e.copy(t.start):null;const r=-(t.start.dot(this.normal)+this.constant)/s;return r<0||r>1?null:e.copy(t.start).addScaledVector(i,r)}intersectsLine(t){const e=this.distanceToPoint(t.start),i=this.distanceToPoint(t.end);return e<0&&i>0||i<0&&e>0}intersectsBox(t){return t.intersectsPlane(this)}intersectsSphere(t){return t.intersectsPlane(this)}coplanarPoint(t){return t.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(t,e){const i=e||Ph.getNormalMatrix(t),s=this.coplanarPoint(Ra).applyMatrix4(t),r=this.normal.applyMatrix3(i).normalize();return this.constant=-s.dot(r),this}translate(t){return this.constant-=t.dot(this.normal),this}equals(t){return t.normal.equals(this.normal)&&t.constant===this.constant}clone(){return new this.constructor().copy(this)}}const fi=new Kr,dr=new L;class ol{constructor(t=new ti,e=new ti,i=new ti,s=new ti,r=new ti,a=new ti){this.planes=[t,e,i,s,r,a]}set(t,e,i,s,r,a){const o=this.planes;return o[0].copy(t),o[1].copy(e),o[2].copy(i),o[3].copy(s),o[4].copy(r),o[5].copy(a),this}copy(t){const e=this.planes;for(let i=0;i<6;i++)e[i].copy(t.planes[i]);return this}setFromProjectionMatrix(t,e=Vn){const i=this.planes,s=t.elements,r=s[0],a=s[1],o=s[2],l=s[3],c=s[4],u=s[5],d=s[6],h=s[7],p=s[8],_=s[9],S=s[10],m=s[11],f=s[12],b=s[13],M=s[14],y=s[15];if(i[0].setComponents(l-r,h-c,m-p,y-f).normalize(),i[1].setComponents(l+r,h+c,m+p,y+f).normalize(),i[2].setComponents(l+a,h+u,m+_,y+b).normalize(),i[3].setComponents(l-a,h-u,m-_,y-b).normalize(),i[4].setComponents(l-o,h-d,m-S,y-M).normalize(),e===Vn)i[5].setComponents(l+o,h+d,m+S,y+M).normalize();else if(e===zr)i[5].setComponents(o,d,S,M).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+e);return this}intersectsObject(t){if(t.boundingSphere!==void 0)t.boundingSphere===null&&t.computeBoundingSphere(),fi.copy(t.boundingSphere).applyMatrix4(t.matrixWorld);else{const e=t.geometry;e.boundingSphere===null&&e.computeBoundingSphere(),fi.copy(e.boundingSphere).applyMatrix4(t.matrixWorld)}return this.intersectsSphere(fi)}intersectsSprite(t){return fi.center.set(0,0,0),fi.radius=.7071067811865476,fi.applyMatrix4(t.matrixWorld),this.intersectsSphere(fi)}intersectsSphere(t){const e=this.planes,i=t.center,s=-t.radius;for(let r=0;r<6;r++)if(e[r].distanceToPoint(i)<s)return!1;return!0}intersectsBox(t){const e=this.planes;for(let i=0;i<6;i++){const s=e[i];if(dr.x=s.normal.x>0?t.max.x:t.min.x,dr.y=s.normal.y>0?t.max.y:t.min.y,dr.z=s.normal.z>0?t.max.z:t.min.z,s.distanceToPoint(dr)<0)return!1}return!0}containsPoint(t){const e=this.planes;for(let i=0;i<6;i++)if(e[i].distanceToPoint(t)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}}class Lh extends Vs{constructor(t){super(),this.isPointsMaterial=!0,this.type="PointsMaterial",this.color=new It(16777215),this.map=null,this.alphaMap=null,this.size=1,this.sizeAttenuation=!0,this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.alphaMap=t.alphaMap,this.size=t.size,this.sizeAttenuation=t.sizeAttenuation,this.fog=t.fog,this}}const Kl=new te,zo=new Zr,hr=new Kr,fr=new L;class Dh extends Te{constructor(t=new xn,e=new Lh){super(),this.isPoints=!0,this.type="Points",this.geometry=t,this.material=e,this.morphTargetDictionary=void 0,this.morphTargetInfluences=void 0,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}raycast(t,e){const i=this.geometry,s=this.matrixWorld,r=t.params.Points.threshold,a=i.drawRange;if(i.boundingSphere===null&&i.computeBoundingSphere(),hr.copy(i.boundingSphere),hr.applyMatrix4(s),hr.radius+=r,t.ray.intersectsSphere(hr)===!1)return;Kl.copy(s).invert(),zo.copy(t.ray).applyMatrix4(Kl);const o=r/((this.scale.x+this.scale.y+this.scale.z)/3),l=o*o,c=i.index,d=i.attributes.position;if(c!==null){const h=Math.max(0,a.start),p=Math.min(c.count,a.start+a.count);for(let _=h,S=p;_<S;_++){const m=c.getX(_);fr.fromBufferAttribute(d,m),Zl(fr,m,l,s,t,e,this)}}else{const h=Math.max(0,a.start),p=Math.min(d.count,a.start+a.count);for(let _=h,S=p;_<S;_++)fr.fromBufferAttribute(d,_),Zl(fr,_,l,s,t,e,this)}}updateMorphTargets(){const e=this.geometry.morphAttributes,i=Object.keys(e);if(i.length>0){const s=e[i[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){const o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}}function Zl(n,t,e,i,s,r,a){const o=zo.distanceSqToPoint(n);if(o<e){const l=new L;zo.closestPointToPoint(n,l),l.applyMatrix4(i);const c=s.ray.origin.distanceTo(l);if(c<s.near||c>s.far)return;r.push({distance:c,distanceToRay:Math.sqrt(o),point:l,index:t,face:null,faceIndex:null,barycoord:null,object:a})}}class bu extends Be{constructor(t,e,i=Mi,s,r,a,o=gn,l=gn,c,u=Ds){if(u!==Ds&&u!==Is)throw new Error("DepthTexture format must be either THREE.DepthFormat or THREE.DepthStencilFormat");super(null,s,r,a,o,l,u,i,c),this.isDepthTexture=!0,this.image={width:t,height:e},this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(t){return super.copy(t),this.source=new sl(Object.assign({},t.image)),this.compareFunction=t.compareFunction,this}toJSON(t){const e=super.toJSON(t);return this.compareFunction!==null&&(e.compareFunction=this.compareFunction),e}}class ll extends xn{constructor(t=[],e=[],i=1,s=0){super(),this.type="PolyhedronGeometry",this.parameters={vertices:t,indices:e,radius:i,detail:s};const r=[],a=[];o(s),c(i),u(),this.setAttribute("position",new $e(r,3)),this.setAttribute("normal",new $e(r.slice(),3)),this.setAttribute("uv",new $e(a,2)),s===0?this.computeVertexNormals():this.normalizeNormals();function o(b){const M=new L,y=new L,P=new L;for(let R=0;R<e.length;R+=3)p(e[R+0],M),p(e[R+1],y),p(e[R+2],P),l(M,y,P,b)}function l(b,M,y,P){const R=P+1,A=[];for(let I=0;I<=R;I++){A[I]=[];const E=b.clone().lerp(y,I/R),x=M.clone().lerp(y,I/R),C=R-I;for(let V=0;V<=C;V++)V===0&&I===R?A[I][V]=E:A[I][V]=E.clone().lerp(x,V/C)}for(let I=0;I<R;I++)for(let E=0;E<2*(R-I)-1;E++){const x=Math.floor(E/2);E%2===0?(h(A[I][x+1]),h(A[I+1][x]),h(A[I][x])):(h(A[I][x+1]),h(A[I+1][x+1]),h(A[I+1][x]))}}function c(b){const M=new L;for(let y=0;y<r.length;y+=3)M.x=r[y+0],M.y=r[y+1],M.z=r[y+2],M.normalize().multiplyScalar(b),r[y+0]=M.x,r[y+1]=M.y,r[y+2]=M.z}function u(){const b=new L;for(let M=0;M<r.length;M+=3){b.x=r[M+0],b.y=r[M+1],b.z=r[M+2];const y=m(b)/2/Math.PI+.5,P=f(b)/Math.PI+.5;a.push(y,1-P)}_(),d()}function d(){for(let b=0;b<a.length;b+=6){const M=a[b+0],y=a[b+2],P=a[b+4],R=Math.max(M,y,P),A=Math.min(M,y,P);R>.9&&A<.1&&(M<.2&&(a[b+0]+=1),y<.2&&(a[b+2]+=1),P<.2&&(a[b+4]+=1))}}function h(b){r.push(b.x,b.y,b.z)}function p(b,M){const y=b*3;M.x=t[y+0],M.y=t[y+1],M.z=t[y+2]}function _(){const b=new L,M=new L,y=new L,P=new L,R=new Tt,A=new Tt,I=new Tt;for(let E=0,x=0;E<r.length;E+=9,x+=6){b.set(r[E+0],r[E+1],r[E+2]),M.set(r[E+3],r[E+4],r[E+5]),y.set(r[E+6],r[E+7],r[E+8]),R.set(a[x+0],a[x+1]),A.set(a[x+2],a[x+3]),I.set(a[x+4],a[x+5]),P.copy(b).add(M).add(y).divideScalar(3);const C=m(P);S(R,x+0,b,C),S(A,x+2,M,C),S(I,x+4,y,C)}}function S(b,M,y,P){P<0&&b.x===1&&(a[M]=b.x-1),y.x===0&&y.z===0&&(a[M]=P/2/Math.PI+.5)}function m(b){return Math.atan2(b.z,-b.x)}function f(b){return Math.atan2(-b.y,Math.sqrt(b.x*b.x+b.z*b.z))}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new ll(t.vertices,t.indices,t.radius,t.details)}}class cl extends ll{constructor(t=1,e=0){const i=(1+Math.sqrt(5))/2,s=[-1,i,0,1,i,0,-1,-i,0,1,-i,0,0,-1,i,0,1,i,0,-1,-i,0,1,-i,i,0,-1,i,0,1,-i,0,-1,-i,0,1],r=[0,11,5,0,5,1,0,1,7,0,7,10,0,10,11,1,5,9,5,11,4,11,10,2,10,7,6,7,1,8,3,9,4,3,4,2,3,2,6,3,6,8,3,8,9,4,9,5,2,4,11,6,2,10,8,6,7,9,8,1];super(s,r,t,e),this.type="IcosahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new cl(t.radius,t.detail)}}class Jr extends xn{constructor(t=1,e=1,i=1,s=1){super(),this.type="PlaneGeometry",this.parameters={width:t,height:e,widthSegments:i,heightSegments:s};const r=t/2,a=e/2,o=Math.floor(i),l=Math.floor(s),c=o+1,u=l+1,d=t/o,h=e/l,p=[],_=[],S=[],m=[];for(let f=0;f<u;f++){const b=f*h-a;for(let M=0;M<c;M++){const y=M*d-r;_.push(y,-b,0),S.push(0,0,1),m.push(M/o),m.push(1-f/l)}}for(let f=0;f<l;f++)for(let b=0;b<o;b++){const M=b+c*f,y=b+c*(f+1),P=b+1+c*(f+1),R=b+1+c*f;p.push(M,y,R),p.push(y,P,R)}this.setIndex(p),this.setAttribute("position",new $e(_,3)),this.setAttribute("normal",new $e(S,3)),this.setAttribute("uv",new $e(m,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new Jr(t.width,t.height,t.widthSegments,t.heightSegments)}}class ul extends xn{constructor(t=1,e=32,i=16,s=0,r=Math.PI*2,a=0,o=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:t,widthSegments:e,heightSegments:i,phiStart:s,phiLength:r,thetaStart:a,thetaLength:o},e=Math.max(3,Math.floor(e)),i=Math.max(2,Math.floor(i));const l=Math.min(a+o,Math.PI);let c=0;const u=[],d=new L,h=new L,p=[],_=[],S=[],m=[];for(let f=0;f<=i;f++){const b=[],M=f/i;let y=0;f===0&&a===0?y=.5/e:f===i&&l===Math.PI&&(y=-.5/e);for(let P=0;P<=e;P++){const R=P/e;d.x=-t*Math.cos(s+R*r)*Math.sin(a+M*o),d.y=t*Math.cos(a+M*o),d.z=t*Math.sin(s+R*r)*Math.sin(a+M*o),_.push(d.x,d.y,d.z),h.copy(d).normalize(),S.push(h.x,h.y,h.z),m.push(R+y,1-M),b.push(c++)}u.push(b)}for(let f=0;f<i;f++)for(let b=0;b<e;b++){const M=u[f][b+1],y=u[f][b],P=u[f+1][b],R=u[f+1][b+1];(f!==0||a>0)&&p.push(M,y,R),(f!==i-1||l<Math.PI)&&p.push(y,P,R)}this.setIndex(p),this.setAttribute("position",new $e(_,3)),this.setAttribute("normal",new $e(S,3)),this.setAttribute("uv",new $e(m,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new ul(t.radius,t.widthSegments,t.heightSegments,t.phiStart,t.phiLength,t.thetaStart,t.thetaLength)}}class Ih extends Vs{constructor(t){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=Hd,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(t)}copy(t){return super.copy(t),this.depthPacking=t.depthPacking,this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this}}class Uh extends Vs{constructor(t){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(t)}copy(t){return super.copy(t),this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this}}class dl extends Te{constructor(t,e=1){super(),this.isLight=!0,this.type="Light",this.color=new It(t),this.intensity=e}dispose(){}copy(t,e){return super.copy(t,e),this.color.copy(t.color),this.intensity=t.intensity,this}toJSON(t){const e=super.toJSON(t);return e.object.color=this.color.getHex(),e.object.intensity=this.intensity,this.groundColor!==void 0&&(e.object.groundColor=this.groundColor.getHex()),this.distance!==void 0&&(e.object.distance=this.distance),this.angle!==void 0&&(e.object.angle=this.angle),this.decay!==void 0&&(e.object.decay=this.decay),this.penumbra!==void 0&&(e.object.penumbra=this.penumbra),this.shadow!==void 0&&(e.object.shadow=this.shadow.toJSON()),this.target!==void 0&&(e.object.target=this.target.uuid),e}}const Ca=new te,Jl=new L,Ql=new L;class Au{constructor(t){this.camera=t,this.intensity=1,this.bias=0,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new Tt(512,512),this.map=null,this.mapPass=null,this.matrix=new te,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new ol,this._frameExtents=new Tt(1,1),this._viewportCount=1,this._viewports=[new Kt(0,0,1,1)]}getViewportCount(){return this._viewportCount}getFrustum(){return this._frustum}updateMatrices(t){const e=this.camera,i=this.matrix;Jl.setFromMatrixPosition(t.matrixWorld),e.position.copy(Jl),Ql.setFromMatrixPosition(t.target.matrixWorld),e.lookAt(Ql),e.updateMatrixWorld(),Ca.multiplyMatrices(e.projectionMatrix,e.matrixWorldInverse),this._frustum.setFromProjectionMatrix(Ca),i.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1),i.multiply(Ca)}getViewport(t){return this._viewports[t]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(t){return this.camera=t.camera.clone(),this.intensity=t.intensity,this.bias=t.bias,this.radius=t.radius,this.mapSize.copy(t.mapSize),this}clone(){return new this.constructor().copy(this)}toJSON(){const t={};return this.intensity!==1&&(t.intensity=this.intensity),this.bias!==0&&(t.bias=this.bias),this.normalBias!==0&&(t.normalBias=this.normalBias),this.radius!==1&&(t.radius=this.radius),(this.mapSize.x!==512||this.mapSize.y!==512)&&(t.mapSize=this.mapSize.toArray()),t.camera=this.camera.toJSON(!1).object,delete t.camera.matrix,t}}const tc=new te,ps=new L,Pa=new L;class Nh extends Au{constructor(){super(new Ge(90,1,.5,500)),this.isPointLightShadow=!0,this._frameExtents=new Tt(4,2),this._viewportCount=6,this._viewports=[new Kt(2,1,1,1),new Kt(0,1,1,1),new Kt(3,1,1,1),new Kt(1,1,1,1),new Kt(3,0,1,1),new Kt(1,0,1,1)],this._cubeDirections=[new L(1,0,0),new L(-1,0,0),new L(0,0,1),new L(0,0,-1),new L(0,1,0),new L(0,-1,0)],this._cubeUps=[new L(0,1,0),new L(0,1,0),new L(0,1,0),new L(0,1,0),new L(0,0,1),new L(0,0,-1)]}updateMatrices(t,e=0){const i=this.camera,s=this.matrix,r=t.distance||i.far;r!==i.far&&(i.far=r,i.updateProjectionMatrix()),ps.setFromMatrixPosition(t.matrixWorld),i.position.copy(ps),Pa.copy(i.position),Pa.add(this._cubeDirections[e]),i.up.copy(this._cubeUps[e]),i.lookAt(Pa),i.updateMatrixWorld(),s.makeTranslation(-ps.x,-ps.y,-ps.z),tc.multiplyMatrices(i.projectionMatrix,i.matrixWorldInverse),this._frustum.setFromProjectionMatrix(tc)}}class La extends dl{constructor(t,e,i=0,s=2){super(t,e),this.isPointLight=!0,this.type="PointLight",this.distance=i,this.decay=s,this.shadow=new Nh}get power(){return this.intensity*4*Math.PI}set power(t){this.intensity=t/(4*Math.PI)}dispose(){this.shadow.dispose()}copy(t,e){return super.copy(t,e),this.distance=t.distance,this.decay=t.decay,this.shadow=t.shadow.clone(),this}}class wu extends Mu{constructor(t=-1,e=1,i=1,s=-1,r=.1,a=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=t,this.right=e,this.top=i,this.bottom=s,this.near=r,this.far=a,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.left=t.left,this.right=t.right,this.top=t.top,this.bottom=t.bottom,this.near=t.near,this.far=t.far,this.zoom=t.zoom,this.view=t.view===null?null:Object.assign({},t.view),this}setViewOffset(t,e,i,s,r,a){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=i,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){const t=(this.right-this.left)/(2*this.zoom),e=(this.top-this.bottom)/(2*this.zoom),i=(this.right+this.left)/2,s=(this.top+this.bottom)/2;let r=i-t,a=i+t,o=s+e,l=s-e;if(this.view!==null&&this.view.enabled){const c=(this.right-this.left)/this.view.fullWidth/this.zoom,u=(this.top-this.bottom)/this.view.fullHeight/this.zoom;r+=c*this.view.offsetX,a=r+c*this.view.width,o-=u*this.view.offsetY,l=o-u*this.view.height}this.projectionMatrix.makeOrthographic(r,a,o,l,this.near,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){const e=super.toJSON(t);return e.object.zoom=this.zoom,e.object.left=this.left,e.object.right=this.right,e.object.top=this.top,e.object.bottom=this.bottom,e.object.near=this.near,e.object.far=this.far,this.view!==null&&(e.object.view=Object.assign({},this.view)),e}}class Oh extends Au{constructor(){super(new wu(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}}class Fh extends dl{constructor(t,e){super(t,e),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(Te.DEFAULT_UP),this.updateMatrix(),this.target=new Te,this.shadow=new Oh}dispose(){this.shadow.dispose()}copy(t){return super.copy(t),this.target=t.target.clone(),this.shadow=t.shadow.clone(),this}}class Bh extends dl{constructor(t,e){super(t,e),this.isAmbientLight=!0,this.type="AmbientLight"}}class zh extends Ge{constructor(t=[]){super(),this.isArrayCamera=!0,this.cameras=t,this.index=0}}class kh{constructor(t=!0){this.autoStart=t,this.startTime=0,this.oldTime=0,this.elapsedTime=0,this.running=!1}start(){this.startTime=ec(),this.oldTime=this.startTime,this.elapsedTime=0,this.running=!0}stop(){this.getElapsedTime(),this.running=!1,this.autoStart=!1}getElapsedTime(){return this.getDelta(),this.elapsedTime}getDelta(){let t=0;if(this.autoStart&&!this.running)return this.start(),0;if(this.running){const e=ec();t=(e-this.oldTime)/1e3,this.oldTime=e,this.elapsedTime+=t}return t}}function ec(){return performance.now()}const nc=new te;class Hh{constructor(t,e,i=0,s=1/0){this.ray=new Zr(t,e),this.near=i,this.far=s,this.camera=null,this.layers=new rl,this.params={Mesh:{},Line:{threshold:1},LOD:{},Points:{threshold:1},Sprite:{}}}set(t,e){this.ray.set(t,e)}setFromCamera(t,e){e.isPerspectiveCamera?(this.ray.origin.setFromMatrixPosition(e.matrixWorld),this.ray.direction.set(t.x,t.y,.5).unproject(e).sub(this.ray.origin).normalize(),this.camera=e):e.isOrthographicCamera?(this.ray.origin.set(t.x,t.y,(e.near+e.far)/(e.near-e.far)).unproject(e),this.ray.direction.set(0,0,-1).transformDirection(e.matrixWorld),this.camera=e):console.error("THREE.Raycaster: Unsupported camera type: "+e.type)}setFromXRController(t){return nc.identity().extractRotation(t.matrixWorld),this.ray.origin.setFromMatrixPosition(t.matrixWorld),this.ray.direction.set(0,0,-1).applyMatrix4(nc),this}intersectObject(t,e=!0,i=[]){return ko(t,this,i,e),i.sort(ic),i}intersectObjects(t,e=!0,i=[]){for(let s=0,r=t.length;s<r;s++)ko(t[s],this,i,e);return i.sort(ic),i}}function ic(n,t){return n.distance-t.distance}function ko(n,t,e,i){let s=!0;if(n.layers.test(t.layers)&&n.raycast(t,e)===!1&&(s=!1),s===!0&&i===!0){const r=n.children;for(let a=0,o=r.length;a<o;a++)ko(r[a],t,e,!0)}}class sc{constructor(t=1,e=0,i=0){this.radius=t,this.phi=e,this.theta=i}set(t,e,i){return this.radius=t,this.phi=e,this.theta=i,this}copy(t){return this.radius=t.radius,this.phi=t.phi,this.theta=t.theta,this}makeSafe(){return this.phi=Nt(this.phi,1e-6,Math.PI-1e-6),this}setFromVector3(t){return this.setFromCartesianCoords(t.x,t.y,t.z)}setFromCartesianCoords(t,e,i){return this.radius=Math.sqrt(t*t+e*e+i*i),this.radius===0?(this.theta=0,this.phi=0):(this.theta=Math.atan2(t,i),this.phi=Math.acos(Nt(e/this.radius,-1,1))),this}clone(){return new this.constructor().copy(this)}}class Vh extends wi{constructor(t,e=null){super(),this.object=t,this.domElement=e,this.enabled=!0,this.state=-1,this.keys={},this.mouseButtons={LEFT:null,MIDDLE:null,RIGHT:null},this.touches={ONE:null,TWO:null}}connect(t){if(t===void 0){console.warn("THREE.Controls: connect() now requires an element.");return}this.domElement!==null&&this.disconnect(),this.domElement=t}disconnect(){}dispose(){}update(){}}function rc(n,t,e,i){const s=Gh(i);switch(e){case lu:return n*t;case uu:return n*t;case du:return n*t*2;case hu:return n*t/s.components*s.byteLength;case el:return n*t/s.components*s.byteLength;case fu:return n*t*2/s.components*s.byteLength;case nl:return n*t*2/s.components*s.byteLength;case cu:return n*t*3/s.components*s.byteLength;case pn:return n*t*4/s.components*s.byteLength;case il:return n*t*4/s.components*s.byteLength;case br:case Ar:return Math.floor((n+3)/4)*Math.floor((t+3)/4)*8;case wr:case Rr:return Math.floor((n+3)/4)*Math.floor((t+3)/4)*16;case fo:case mo:return Math.max(n,16)*Math.max(t,8)/4;case ho:case po:return Math.max(n,8)*Math.max(t,8)/2;case go:case _o:return Math.floor((n+3)/4)*Math.floor((t+3)/4)*8;case vo:return Math.floor((n+3)/4)*Math.floor((t+3)/4)*16;case xo:return Math.floor((n+3)/4)*Math.floor((t+3)/4)*16;case So:return Math.floor((n+4)/5)*Math.floor((t+3)/4)*16;case yo:return Math.floor((n+4)/5)*Math.floor((t+4)/5)*16;case Eo:return Math.floor((n+5)/6)*Math.floor((t+4)/5)*16;case Mo:return Math.floor((n+5)/6)*Math.floor((t+5)/6)*16;case To:return Math.floor((n+7)/8)*Math.floor((t+4)/5)*16;case bo:return Math.floor((n+7)/8)*Math.floor((t+5)/6)*16;case Ao:return Math.floor((n+7)/8)*Math.floor((t+7)/8)*16;case wo:return Math.floor((n+9)/10)*Math.floor((t+4)/5)*16;case Ro:return Math.floor((n+9)/10)*Math.floor((t+5)/6)*16;case Co:return Math.floor((n+9)/10)*Math.floor((t+7)/8)*16;case Po:return Math.floor((n+9)/10)*Math.floor((t+9)/10)*16;case Lo:return Math.floor((n+11)/12)*Math.floor((t+9)/10)*16;case Do:return Math.floor((n+11)/12)*Math.floor((t+11)/12)*16;case Cr:case Io:case Uo:return Math.ceil(n/4)*Math.ceil(t/4)*16;case pu:case No:return Math.ceil(n/4)*Math.ceil(t/4)*8;case Oo:case Fo:return Math.ceil(n/4)*Math.ceil(t/4)*16}throw new Error(`Unable to determine texture byte length for ${e} format.`)}function Gh(n){switch(n){case Wn:case ru:return{byteLength:1,components:1};case Ps:case au:case zs:return{byteLength:2,components:1};case Qo:case tl:return{byteLength:2,components:4};case Mi:case Jo:case Hn:return{byteLength:4,components:1};case ou:return{byteLength:4,components:3}}throw new Error(`Unknown texture type ${n}.`)}typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:Zo}}));typeof window<"u"&&(window.__THREE__?console.warn("WARNING: Multiple instances of Three.js being imported."):window.__THREE__=Zo);function Ru(){let n=null,t=!1,e=null,i=null;function s(r,a){e(r,a),i=n.requestAnimationFrame(s)}return{start:function(){t!==!0&&e!==null&&(i=n.requestAnimationFrame(s),t=!0)},stop:function(){n.cancelAnimationFrame(i),t=!1},setAnimationLoop:function(r){e=r},setContext:function(r){n=r}}}function Wh(n){const t=new WeakMap;function e(o,l){const c=o.array,u=o.usage,d=c.byteLength,h=n.createBuffer();n.bindBuffer(l,h),n.bufferData(l,c,u),o.onUploadCallback();let p;if(c instanceof Float32Array)p=n.FLOAT;else if(c instanceof Uint16Array)o.isFloat16BufferAttribute?p=n.HALF_FLOAT:p=n.UNSIGNED_SHORT;else if(c instanceof Int16Array)p=n.SHORT;else if(c instanceof Uint32Array)p=n.UNSIGNED_INT;else if(c instanceof Int32Array)p=n.INT;else if(c instanceof Int8Array)p=n.BYTE;else if(c instanceof Uint8Array)p=n.UNSIGNED_BYTE;else if(c instanceof Uint8ClampedArray)p=n.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+c);return{buffer:h,type:p,bytesPerElement:c.BYTES_PER_ELEMENT,version:o.version,size:d}}function i(o,l,c){const u=l.array,d=l.updateRanges;if(n.bindBuffer(c,o),d.length===0)n.bufferSubData(c,0,u);else{d.sort((p,_)=>p.start-_.start);let h=0;for(let p=1;p<d.length;p++){const _=d[h],S=d[p];S.start<=_.start+_.count+1?_.count=Math.max(_.count,S.start+S.count-_.start):(++h,d[h]=S)}d.length=h+1;for(let p=0,_=d.length;p<_;p++){const S=d[p];n.bufferSubData(c,S.start*u.BYTES_PER_ELEMENT,u,S.start,S.count)}l.clearUpdateRanges()}l.onUploadCallback()}function s(o){return o.isInterleavedBufferAttribute&&(o=o.data),t.get(o)}function r(o){o.isInterleavedBufferAttribute&&(o=o.data);const l=t.get(o);l&&(n.deleteBuffer(l.buffer),t.delete(o))}function a(o,l){if(o.isInterleavedBufferAttribute&&(o=o.data),o.isGLBufferAttribute){const u=t.get(o);(!u||u.version<o.version)&&t.set(o,{buffer:o.buffer,type:o.type,bytesPerElement:o.elementSize,version:o.version});return}const c=t.get(o);if(c===void 0)t.set(o,e(o,l));else if(c.version<o.version){if(c.size!==o.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");i(c.buffer,o,l),c.version=o.version}}return{get:s,remove:r,update:a}}var Xh=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,$h=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,qh=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,Yh=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,jh=`#ifdef USE_ALPHATEST
	#ifdef ALPHA_TO_COVERAGE
	diffuseColor.a = smoothstep( alphaTest, alphaTest + fwidth( diffuseColor.a ), diffuseColor.a );
	if ( diffuseColor.a == 0.0 ) discard;
	#else
	if ( diffuseColor.a < alphaTest ) discard;
	#endif
#endif`,Kh=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,Zh=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,Jh=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,Qh=`#ifdef USE_BATCHING
	#if ! defined( GL_ANGLE_multi_draw )
	#define gl_DrawID _gl_DrawID
	uniform int _gl_DrawID;
	#endif
	uniform highp sampler2D batchingTexture;
	uniform highp usampler2D batchingIdTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
	float getIndirectIndex( const in int i ) {
		int size = textureSize( batchingIdTexture, 0 ).x;
		int x = i % size;
		int y = i / size;
		return float( texelFetch( batchingIdTexture, ivec2( x, y ), 0 ).r );
	}
#endif
#ifdef USE_BATCHING_COLOR
	uniform sampler2D batchingColorTexture;
	vec3 getBatchingColor( const in float i ) {
		int size = textureSize( batchingColorTexture, 0 ).x;
		int j = int( i );
		int x = j % size;
		int y = j / size;
		return texelFetch( batchingColorTexture, ivec2( x, y ), 0 ).rgb;
	}
#endif`,tf=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( getIndirectIndex( gl_DrawID ) );
#endif`,ef=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,nf=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,sf=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,rf=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,af=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,of=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#ifdef ALPHA_TO_COVERAGE
		float distanceToPlane, distanceGradient;
		float clipOpacity = 1.0;
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
			distanceGradient = fwidth( distanceToPlane ) / 2.0;
			clipOpacity *= smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			if ( clipOpacity == 0.0 ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			float unionClipOpacity = 1.0;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
				distanceGradient = fwidth( distanceToPlane ) / 2.0;
				unionClipOpacity *= 1.0 - smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			}
			#pragma unroll_loop_end
			clipOpacity *= 1.0 - unionClipOpacity;
		#endif
		diffuseColor.a *= clipOpacity;
		if ( diffuseColor.a == 0.0 ) discard;
	#else
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			bool clipped = true;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
			}
			#pragma unroll_loop_end
			if ( clipped ) discard;
		#endif
	#endif
#endif`,lf=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,cf=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,uf=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,df=`#if defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#elif defined( USE_COLOR )
	diffuseColor.rgb *= vColor;
#endif`,hf=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR )
	varying vec3 vColor;
#endif`,ff=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	varying vec3 vColor;
#endif`,pf=`#if defined( USE_COLOR_ALPHA )
	vColor = vec4( 1.0 );
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	vColor = vec3( 1.0 );
#endif
#ifdef USE_COLOR
	vColor *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.xyz *= instanceColor.xyz;
#endif
#ifdef USE_BATCHING_COLOR
	vec3 batchingColor = getBatchingColor( getIndirectIndex( gl_DrawID ) );
	vColor.xyz *= batchingColor.xyz;
#endif`,mf=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
vec3 inverseTransformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( vec4( dir, 0.0 ) * matrix ).xyz );
}
mat3 transposeMat3( const in mat3 m ) {
	mat3 tmp;
	tmp[ 0 ] = vec3( m[ 0 ].x, m[ 1 ].x, m[ 2 ].x );
	tmp[ 1 ] = vec3( m[ 0 ].y, m[ 1 ].y, m[ 2 ].y );
	tmp[ 2 ] = vec3( m[ 0 ].z, m[ 1 ].z, m[ 2 ].z );
	return tmp;
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,gf=`#ifdef ENVMAP_TYPE_CUBE_UV
	#define cubeUV_minMipLevel 4.0
	#define cubeUV_minTileSize 16.0
	float getFace( vec3 direction ) {
		vec3 absDirection = abs( direction );
		float face = - 1.0;
		if ( absDirection.x > absDirection.z ) {
			if ( absDirection.x > absDirection.y )
				face = direction.x > 0.0 ? 0.0 : 3.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		} else {
			if ( absDirection.z > absDirection.y )
				face = direction.z > 0.0 ? 2.0 : 5.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		}
		return face;
	}
	vec2 getUV( vec3 direction, float face ) {
		vec2 uv;
		if ( face == 0.0 ) {
			uv = vec2( direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 1.0 ) {
			uv = vec2( - direction.x, - direction.z ) / abs( direction.y );
		} else if ( face == 2.0 ) {
			uv = vec2( - direction.x, direction.y ) / abs( direction.z );
		} else if ( face == 3.0 ) {
			uv = vec2( - direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 4.0 ) {
			uv = vec2( - direction.x, direction.z ) / abs( direction.y );
		} else {
			uv = vec2( direction.x, direction.y ) / abs( direction.z );
		}
		return 0.5 * ( uv + 1.0 );
	}
	vec3 bilinearCubeUV( sampler2D envMap, vec3 direction, float mipInt ) {
		float face = getFace( direction );
		float filterInt = max( cubeUV_minMipLevel - mipInt, 0.0 );
		mipInt = max( mipInt, cubeUV_minMipLevel );
		float faceSize = exp2( mipInt );
		highp vec2 uv = getUV( direction, face ) * ( faceSize - 2.0 ) + 1.0;
		if ( face > 2.0 ) {
			uv.y += faceSize;
			face -= 3.0;
		}
		uv.x += face * faceSize;
		uv.x += filterInt * 3.0 * cubeUV_minTileSize;
		uv.y += 4.0 * ( exp2( CUBEUV_MAX_MIP ) - faceSize );
		uv.x *= CUBEUV_TEXEL_WIDTH;
		uv.y *= CUBEUV_TEXEL_HEIGHT;
		#ifdef texture2DGradEXT
			return texture2DGradEXT( envMap, uv, vec2( 0.0 ), vec2( 0.0 ) ).rgb;
		#else
			return texture2D( envMap, uv ).rgb;
		#endif
	}
	#define cubeUV_r0 1.0
	#define cubeUV_m0 - 2.0
	#define cubeUV_r1 0.8
	#define cubeUV_m1 - 1.0
	#define cubeUV_r4 0.4
	#define cubeUV_m4 2.0
	#define cubeUV_r5 0.305
	#define cubeUV_m5 3.0
	#define cubeUV_r6 0.21
	#define cubeUV_m6 4.0
	float roughnessToMip( float roughness ) {
		float mip = 0.0;
		if ( roughness >= cubeUV_r1 ) {
			mip = ( cubeUV_r0 - roughness ) * ( cubeUV_m1 - cubeUV_m0 ) / ( cubeUV_r0 - cubeUV_r1 ) + cubeUV_m0;
		} else if ( roughness >= cubeUV_r4 ) {
			mip = ( cubeUV_r1 - roughness ) * ( cubeUV_m4 - cubeUV_m1 ) / ( cubeUV_r1 - cubeUV_r4 ) + cubeUV_m1;
		} else if ( roughness >= cubeUV_r5 ) {
			mip = ( cubeUV_r4 - roughness ) * ( cubeUV_m5 - cubeUV_m4 ) / ( cubeUV_r4 - cubeUV_r5 ) + cubeUV_m4;
		} else if ( roughness >= cubeUV_r6 ) {
			mip = ( cubeUV_r5 - roughness ) * ( cubeUV_m6 - cubeUV_m5 ) / ( cubeUV_r5 - cubeUV_r6 ) + cubeUV_m5;
		} else {
			mip = - 2.0 * log2( 1.16 * roughness );		}
		return mip;
	}
	vec4 textureCubeUV( sampler2D envMap, vec3 sampleDir, float roughness ) {
		float mip = clamp( roughnessToMip( roughness ), cubeUV_m0, CUBEUV_MAX_MIP );
		float mipF = fract( mip );
		float mipInt = floor( mip );
		vec3 color0 = bilinearCubeUV( envMap, sampleDir, mipInt );
		if ( mipF == 0.0 ) {
			return vec4( color0, 1.0 );
		} else {
			vec3 color1 = bilinearCubeUV( envMap, sampleDir, mipInt + 1.0 );
			return vec4( mix( color0, color1, mipF ), 1.0 );
		}
	}
#endif`,_f=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
	#ifdef FLIP_SIDED
		transformedTangent = - transformedTangent;
	#endif
#endif`,vf=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,xf=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,Sf=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	#ifdef DECODE_VIDEO_TEXTURE_EMISSIVE
		emissiveColor = sRGBTransferEOTF( emissiveColor );
	#endif
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,yf=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,Ef="gl_FragColor = linearToOutputTexel( gl_FragColor );",Mf=`vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferEOTF( in vec4 value ) {
	return vec4( mix( pow( value.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), value.rgb * 0.0773993808, vec3( lessThanEqual( value.rgb, vec3( 0.04045 ) ) ) ), value.a );
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}`,Tf=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, envMapRotation * vec3( flipEnvMap * reflectVec.x, reflectVec.yz ) );
	#else
		vec4 envColor = vec4( 0.0 );
	#endif
	#ifdef ENVMAP_BLENDING_MULTIPLY
		outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_MIX )
		outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_ADD )
		outgoingLight += envColor.xyz * specularStrength * reflectivity;
	#endif
#endif`,bf=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform float flipEnvMap;
	uniform mat3 envMapRotation;
	#ifdef ENVMAP_TYPE_CUBE
		uniform samplerCube envMap;
	#else
		uniform sampler2D envMap;
	#endif
	
#endif`,Af=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,wf=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,Rf=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,Cf=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,Pf=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,Lf=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,Df=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,If=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,Uf=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,Nf=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,Of=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,Ff=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
	if ( cutoffDistance > 0.0 ) {
		distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
	}
	return distanceFalloff;
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif`,Bf=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * worldNormal, 1.0 );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, roughness * roughness) );
			reflectVec = inverseTransformDirection( reflectVec, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * reflectVec, roughness );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_CUBE_UV
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
#endif`,zf=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,kf=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,Hf=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,Vf=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,Gf=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb * ( 1.0 - metalnessFactor );
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.0525 );material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = mix( min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = mix( vec3( 0.04 ), diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.0525 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_DISPERSION
	material.dispersion = dispersion;
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.07, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,Wf=`struct PhysicalMaterial {
	vec3 diffuseColor;
	float roughness;
	vec3 specularColor;
	float specularF90;
	float dispersion;
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		float v = 0.5 / ( gv + gl );
		return saturate(v);
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = material.clearcoatRoughness;
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColor;
	float f90 = material.specularF90;
	float roughness = material.roughness;
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float V = V_GGX_SmithCorrelated_Anisotropic( material.alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( material.alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transposeMat3( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float a = roughness < 0.25 ? -339.2 * r2 + 161.4 * roughness - 25.9 : -8.48 * r2 + 14.3 * roughness - 9.95;
	float b = roughness < 0.25 ? 44.0 * r2 - 23.7 * roughness + 3.26 : 1.97 * r2 - 3.27 * roughness + 0.72;
	float DG = exp( a * dotNV + b ) + ( roughness < 0.25 ? 0.0 : 0.1 * ( roughness - 0.25 ) );
	return saturate( DG * RECIPROCAL_PI );
}
vec2 DFGApprox( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	const vec4 c0 = vec4( - 1, - 0.0275, - 0.572, 0.022 );
	const vec4 c1 = vec4( 1, 0.0425, 1.04, - 0.04 );
	vec4 r = roughness * c0 + c1;
	float a004 = min( r.x * r.x, exp2( - 9.28 * dotNV ) ) * r.x + r.y;
	vec2 fab = vec2( - 1.04, 1.04 ) * a004 + r.zw;
	return fab;
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColor * t2.x + ( vec3( 1.0 ) - material.specularColor ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseColor * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
	#endif
	reflectedLight.directSpecular += irradiance * BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
	#endif
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.iridescence, material.iridescenceFresnel, material.roughness, singleScattering, multiScattering );
	#else
		computeMultiscattering( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.roughness, singleScattering, multiScattering );
	#endif
	vec3 totalScattering = singleScattering + multiScattering;
	vec3 diffuse = material.diffuseColor * ( 1.0 - max( max( totalScattering.r, totalScattering.g ), totalScattering.b ) );
	reflectedLight.indirectSpecular += radiance * singleScattering;
	reflectedLight.indirectSpecular += multiScattering * cosineWeightedIrradiance;
	reflectedLight.indirectDiffuse += diffuse * cosineWeightedIrradiance;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,Xf=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		material.iridescenceFresnel = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		material.iridescenceF0 = Schlick_to_F0( material.iridescenceFresnel, 1.0, dotNVi );
	}
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowIntensity, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowIntensity, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowIntensity, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,$f=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD ) && defined( ENVMAP_TYPE_CUBE_UV )
		iblIrradiance += getIBLIrradiance( geometryNormal );
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		radiance += getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		radiance += getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,qf=`#if defined( RE_IndirectDiffuse )
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,Yf=`#if defined( USE_LOGDEPTHBUF )
	gl_FragDepth = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,jf=`#if defined( USE_LOGDEPTHBUF )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Kf=`#ifdef USE_LOGDEPTHBUF
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Zf=`#ifdef USE_LOGDEPTHBUF
	vFragDepth = 1.0 + gl_Position.w;
	vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
#endif`,Jf=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = sRGBTransferEOTF( sampledDiffuseColor );
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,Qf=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,tp=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,ep=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,np=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,ip=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,sp=`#ifdef USE_INSTANCING_MORPH
	float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	float morphTargetBaseInfluence = texelFetch( morphTexture, ivec2( 0, gl_InstanceID ), 0 ).r;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		morphTargetInfluences[i] =  texelFetch( morphTexture, ivec2( i + 1, gl_InstanceID ), 0 ).r;
	}
#endif`,rp=`#if defined( USE_MORPHCOLORS )
	vColor *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,ap=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,op=`#ifdef USE_MORPHTARGETS
	#ifndef USE_INSTANCING_MORPH
		uniform float morphTargetBaseInfluence;
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	#endif
	uniform sampler2DArray morphTargetsTexture;
	uniform ivec2 morphTargetsTextureSize;
	vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
		int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
		int y = texelIndex / morphTargetsTextureSize.x;
		int x = texelIndex - y * morphTargetsTextureSize.x;
		ivec3 morphUV = ivec3( x, y, morphTargetIndex );
		return texelFetch( morphTargetsTexture, morphUV, 0 );
	}
#endif`,lp=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,cp=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,up=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,dp=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,hp=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,fp=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
	#endif
#endif`,pp=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,mp=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,gp=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,_p=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,vp=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,xp=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,Sp=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;const float ShiftRight8 = 1. / 256.;
const float Inv255 = 1. / 255.;
const vec4 PackFactors = vec4( 1.0, 256.0, 256.0 * 256.0, 256.0 * 256.0 * 256.0 );
const vec2 UnpackFactors2 = vec2( UnpackDownscale, 1.0 / PackFactors.g );
const vec3 UnpackFactors3 = vec3( UnpackDownscale / PackFactors.rg, 1.0 / PackFactors.b );
const vec4 UnpackFactors4 = vec4( UnpackDownscale / PackFactors.rgb, 1.0 / PackFactors.a );
vec4 packDepthToRGBA( const in float v ) {
	if( v <= 0.0 )
		return vec4( 0., 0., 0., 0. );
	if( v >= 1.0 )
		return vec4( 1., 1., 1., 1. );
	float vuf;
	float af = modf( v * PackFactors.a, vuf );
	float bf = modf( vuf * ShiftRight8, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec4( vuf * Inv255, gf * PackUpscale, bf * PackUpscale, af );
}
vec3 packDepthToRGB( const in float v ) {
	if( v <= 0.0 )
		return vec3( 0., 0., 0. );
	if( v >= 1.0 )
		return vec3( 1., 1., 1. );
	float vuf;
	float bf = modf( v * PackFactors.b, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec3( vuf * Inv255, gf * PackUpscale, bf );
}
vec2 packDepthToRG( const in float v ) {
	if( v <= 0.0 )
		return vec2( 0., 0. );
	if( v >= 1.0 )
		return vec2( 1., 1. );
	float vuf;
	float gf = modf( v * 256., vuf );
	return vec2( vuf * Inv255, gf );
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors4 );
}
float unpackRGBToDepth( const in vec3 v ) {
	return dot( v, UnpackFactors3 );
}
float unpackRGToDepth( const in vec2 v ) {
	return v.r * UnpackFactors2.r + v.g * UnpackFactors2.g;
}
vec4 pack2HalfToRGBA( const in vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( const in vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return depth * ( near - far ) - near;
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return ( near * far ) / ( ( far - near ) * depth - far );
}`,yp=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,Ep=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,Mp=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,Tp=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,bp=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,Ap=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,wp=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform sampler2D pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	float texture2DCompare( sampler2D depths, vec2 uv, float compare ) {
		return step( compare, unpackRGBAToDepth( texture2D( depths, uv ) ) );
	}
	vec2 texture2DDistribution( sampler2D shadow, vec2 uv ) {
		return unpackRGBATo2Half( texture2D( shadow, uv ) );
	}
	float VSMShadow (sampler2D shadow, vec2 uv, float compare ){
		float occlusion = 1.0;
		vec2 distribution = texture2DDistribution( shadow, uv );
		float hard_shadow = step( compare , distribution.x );
		if (hard_shadow != 1.0 ) {
			float distance = compare - distribution.x ;
			float variance = max( 0.00000, distribution.y * distribution.y );
			float softness_probability = variance / (variance + distance * distance );			softness_probability = clamp( ( softness_probability - 0.3 ) / ( 0.95 - 0.3 ), 0.0, 1.0 );			occlusion = clamp( max( hard_shadow, softness_probability ), 0.0, 1.0 );
		}
		return occlusion;
	}
	float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
		float shadow = 1.0;
		shadowCoord.xyz /= shadowCoord.w;
		shadowCoord.z += shadowBias;
		bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
		bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
		if ( frustumTest ) {
		#if defined( SHADOWMAP_TYPE_PCF )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx0 = - texelSize.x * shadowRadius;
			float dy0 = - texelSize.y * shadowRadius;
			float dx1 = + texelSize.x * shadowRadius;
			float dy1 = + texelSize.y * shadowRadius;
			float dx2 = dx0 / 2.0;
			float dy2 = dy0 / 2.0;
			float dx3 = dx1 / 2.0;
			float dy3 = dy1 / 2.0;
			shadow = (
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy1 ), shadowCoord.z )
			) * ( 1.0 / 17.0 );
		#elif defined( SHADOWMAP_TYPE_PCF_SOFT )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx = texelSize.x;
			float dy = texelSize.y;
			vec2 uv = shadowCoord.xy;
			vec2 f = fract( uv * shadowMapSize + 0.5 );
			uv -= f * texelSize;
			shadow = (
				texture2DCompare( shadowMap, uv, shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( dx, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( 0.0, dy ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + texelSize, shadowCoord.z ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, 0.0 ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 0.0 ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, dy ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( 0.0, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 0.0, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( texture2DCompare( shadowMap, uv + vec2( dx, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( dx, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( mix( texture2DCompare( shadowMap, uv + vec2( -dx, -dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, -dy ), shadowCoord.z ),
						  f.x ),
					 mix( texture2DCompare( shadowMap, uv + vec2( -dx, 2.0 * dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 2.0 * dy ), shadowCoord.z ),
						  f.x ),
					 f.y )
			) * ( 1.0 / 9.0 );
		#elif defined( SHADOWMAP_TYPE_VSM )
			shadow = VSMShadow( shadowMap, shadowCoord.xy, shadowCoord.z );
		#else
			shadow = texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z );
		#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	vec2 cubeToUV( vec3 v, float texelSizeY ) {
		vec3 absV = abs( v );
		float scaleToCube = 1.0 / max( absV.x, max( absV.y, absV.z ) );
		absV *= scaleToCube;
		v *= scaleToCube * ( 1.0 - 2.0 * texelSizeY );
		vec2 planar = v.xy;
		float almostATexel = 1.5 * texelSizeY;
		float almostOne = 1.0 - almostATexel;
		if ( absV.z >= almostOne ) {
			if ( v.z > 0.0 )
				planar.x = 4.0 - v.x;
		} else if ( absV.x >= almostOne ) {
			float signX = sign( v.x );
			planar.x = v.z * signX + 2.0 * signX;
		} else if ( absV.y >= almostOne ) {
			float signY = sign( v.y );
			planar.x = v.x + 2.0 * signY + 2.0;
			planar.y = v.z * signY - 2.0;
		}
		return vec2( 0.125, 0.25 ) * planar + vec2( 0.375, 0.75 );
	}
	float getPointShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		
		float lightToPositionLength = length( lightToPosition );
		if ( lightToPositionLength - shadowCameraFar <= 0.0 && lightToPositionLength - shadowCameraNear >= 0.0 ) {
			float dp = ( lightToPositionLength - shadowCameraNear ) / ( shadowCameraFar - shadowCameraNear );			dp += shadowBias;
			vec3 bd3D = normalize( lightToPosition );
			vec2 texelSize = vec2( 1.0 ) / ( shadowMapSize * vec2( 4.0, 2.0 ) );
			#if defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_PCF_SOFT ) || defined( SHADOWMAP_TYPE_VSM )
				vec2 offset = vec2( - 1, 1 ) * shadowRadius * texelSize.y;
				shadow = (
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxx, texelSize.y ), dp )
				) * ( 1.0 / 9.0 );
			#else
				shadow = texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp );
			#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
#endif`,Rp=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,Cp=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	vec3 shadowWorldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,Pp=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowIntensity, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowIntensity, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowIntensity, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,Lp=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,Dp=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,Ip=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,Up=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,Np=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,Op=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,Fp=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,Bp=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 CineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color *= toneMappingExposure;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	color = clamp( color, 0.0, 1.0 );
	return color;
}
vec3 NeutralToneMapping( vec3 color ) {
	const float StartCompression = 0.8 - 0.04;
	const float Desaturation = 0.15;
	color *= toneMappingExposure;
	float x = min( color.r, min( color.g, color.b ) );
	float offset = x < 0.08 ? x - 6.25 * x * x : 0.04;
	color -= offset;
	float peak = max( color.r, max( color.g, color.b ) );
	if ( peak < StartCompression ) return color;
	float d = 1. - StartCompression;
	float newPeak = 1. - d * d / ( peak + d - StartCompression );
	color *= newPeak / peak;
	float g = 1. - 1. / ( Desaturation * ( peak - newPeak ) + 1. );
	return mix( color, vec3( newPeak ), g );
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,zp=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = inverseTransformDirection( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseColor, material.specularColor, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.dispersion, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,kp=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float dispersion, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec4 transmittedLight;
		vec3 transmittance;
		#ifdef USE_DISPERSION
			float halfSpread = ( ior - 1.0 ) * 0.025 * dispersion;
			vec3 iors = vec3( ior - halfSpread, ior, ior + halfSpread );
			for ( int i = 0; i < 3; i ++ ) {
				vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, iors[ i ], modelMatrix );
				vec3 refractedRayExit = position + transmissionRay;
				vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
				vec2 refractionCoords = ndcPos.xy / ndcPos.w;
				refractionCoords += 1.0;
				refractionCoords /= 2.0;
				vec4 transmissionSample = getTransmissionSample( refractionCoords, roughness, iors[ i ] );
				transmittedLight[ i ] = transmissionSample[ i ];
				transmittedLight.a += transmissionSample.a;
				transmittance[ i ] = diffuseColor[ i ] * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance )[ i ];
			}
			transmittedLight.a /= 3.0;
		#else
			vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
			vec3 refractedRayExit = position + transmissionRay;
			vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
			vec2 refractionCoords = ndcPos.xy / ndcPos.w;
			refractionCoords += 1.0;
			refractionCoords /= 2.0;
			transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
			transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		#endif
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,Hp=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,Vp=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,Gp=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,Wp=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`;const Xp=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,$p=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,qp=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,Yp=`#ifdef ENVMAP_TYPE_CUBE
	uniform samplerCube envMap;
#elif defined( ENVMAP_TYPE_CUBE_UV )
	uniform sampler2D envMap;
#endif
uniform float flipEnvMap;
uniform float backgroundBlurriness;
uniform float backgroundIntensity;
uniform mat3 backgroundRotation;
varying vec3 vWorldDirection;
#include <cube_uv_reflection_fragment>
void main() {
	#ifdef ENVMAP_TYPE_CUBE
		vec4 texColor = textureCube( envMap, backgroundRotation * vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) );
	#elif defined( ENVMAP_TYPE_CUBE_UV )
		vec4 texColor = textureCubeUV( envMap, backgroundRotation * vWorldDirection, backgroundBlurriness );
	#else
		vec4 texColor = vec4( 0.0, 0.0, 0.0, 1.0 );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,jp=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,Kp=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Zp=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,Jp=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	float fragCoordZ = 0.5 * vHighPrecisionZW[0] / vHighPrecisionZW[1] + 0.5;
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#elif DEPTH_PACKING == 3202
		gl_FragColor = vec4( packDepthToRGB( fragCoordZ ), 1.0 );
	#elif DEPTH_PACKING == 3203
		gl_FragColor = vec4( packDepthToRG( fragCoordZ ), 0.0, 1.0 );
	#endif
}`,Qp=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,tm=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main () {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = packDepthToRGBA( dist );
}`,em=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,nm=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,im=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,sm=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,rm=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,am=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,om=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,lm=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,cm=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,um=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,dm=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,hm=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <packing>
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 0.0, 0.0, 0.0, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( packNormalToRGB( normal ), diffuseColor.a );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,fm=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,pm=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,mm=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,gm=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_DISPERSION
	uniform float dispersion;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <cube_uv_reflection_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
		float sheenEnergyComp = 1.0 - 0.157 * max3( material.sheenColor );
		outgoingLight = outgoingLight * sheenEnergyComp + sheenSpecularDirect + sheenSpecularIndirect;
	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,_m=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,vm=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,xm=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,Sm=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,ym=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Em=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <packing>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,Mm=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix[ 3 ];
	vec2 scale = vec2( length( modelMatrix[ 0 ].xyz ), length( modelMatrix[ 1 ].xyz ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,Tm=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,Dt={alphahash_fragment:Xh,alphahash_pars_fragment:$h,alphamap_fragment:qh,alphamap_pars_fragment:Yh,alphatest_fragment:jh,alphatest_pars_fragment:Kh,aomap_fragment:Zh,aomap_pars_fragment:Jh,batching_pars_vertex:Qh,batching_vertex:tf,begin_vertex:ef,beginnormal_vertex:nf,bsdfs:sf,iridescence_fragment:rf,bumpmap_pars_fragment:af,clipping_planes_fragment:of,clipping_planes_pars_fragment:lf,clipping_planes_pars_vertex:cf,clipping_planes_vertex:uf,color_fragment:df,color_pars_fragment:hf,color_pars_vertex:ff,color_vertex:pf,common:mf,cube_uv_reflection_fragment:gf,defaultnormal_vertex:_f,displacementmap_pars_vertex:vf,displacementmap_vertex:xf,emissivemap_fragment:Sf,emissivemap_pars_fragment:yf,colorspace_fragment:Ef,colorspace_pars_fragment:Mf,envmap_fragment:Tf,envmap_common_pars_fragment:bf,envmap_pars_fragment:Af,envmap_pars_vertex:wf,envmap_physical_pars_fragment:Bf,envmap_vertex:Rf,fog_vertex:Cf,fog_pars_vertex:Pf,fog_fragment:Lf,fog_pars_fragment:Df,gradientmap_pars_fragment:If,lightmap_pars_fragment:Uf,lights_lambert_fragment:Nf,lights_lambert_pars_fragment:Of,lights_pars_begin:Ff,lights_toon_fragment:zf,lights_toon_pars_fragment:kf,lights_phong_fragment:Hf,lights_phong_pars_fragment:Vf,lights_physical_fragment:Gf,lights_physical_pars_fragment:Wf,lights_fragment_begin:Xf,lights_fragment_maps:$f,lights_fragment_end:qf,logdepthbuf_fragment:Yf,logdepthbuf_pars_fragment:jf,logdepthbuf_pars_vertex:Kf,logdepthbuf_vertex:Zf,map_fragment:Jf,map_pars_fragment:Qf,map_particle_fragment:tp,map_particle_pars_fragment:ep,metalnessmap_fragment:np,metalnessmap_pars_fragment:ip,morphinstance_vertex:sp,morphcolor_vertex:rp,morphnormal_vertex:ap,morphtarget_pars_vertex:op,morphtarget_vertex:lp,normal_fragment_begin:cp,normal_fragment_maps:up,normal_pars_fragment:dp,normal_pars_vertex:hp,normal_vertex:fp,normalmap_pars_fragment:pp,clearcoat_normal_fragment_begin:mp,clearcoat_normal_fragment_maps:gp,clearcoat_pars_fragment:_p,iridescence_pars_fragment:vp,opaque_fragment:xp,packing:Sp,premultiplied_alpha_fragment:yp,project_vertex:Ep,dithering_fragment:Mp,dithering_pars_fragment:Tp,roughnessmap_fragment:bp,roughnessmap_pars_fragment:Ap,shadowmap_pars_fragment:wp,shadowmap_pars_vertex:Rp,shadowmap_vertex:Cp,shadowmask_pars_fragment:Pp,skinbase_vertex:Lp,skinning_pars_vertex:Dp,skinning_vertex:Ip,skinnormal_vertex:Up,specularmap_fragment:Np,specularmap_pars_fragment:Op,tonemapping_fragment:Fp,tonemapping_pars_fragment:Bp,transmission_fragment:zp,transmission_pars_fragment:kp,uv_pars_fragment:Hp,uv_pars_vertex:Vp,uv_vertex:Gp,worldpos_vertex:Wp,background_vert:Xp,background_frag:$p,backgroundCube_vert:qp,backgroundCube_frag:Yp,cube_vert:jp,cube_frag:Kp,depth_vert:Zp,depth_frag:Jp,distanceRGBA_vert:Qp,distanceRGBA_frag:tm,equirect_vert:em,equirect_frag:nm,linedashed_vert:im,linedashed_frag:sm,meshbasic_vert:rm,meshbasic_frag:am,meshlambert_vert:om,meshlambert_frag:lm,meshmatcap_vert:cm,meshmatcap_frag:um,meshnormal_vert:dm,meshnormal_frag:hm,meshphong_vert:fm,meshphong_frag:pm,meshphysical_vert:mm,meshphysical_frag:gm,meshtoon_vert:_m,meshtoon_frag:vm,points_vert:xm,points_frag:Sm,shadow_vert:ym,shadow_frag:Em,sprite_vert:Mm,sprite_frag:Tm},et={common:{diffuse:{value:new It(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new Pt},alphaMap:{value:null},alphaMapTransform:{value:new Pt},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new Pt}},envmap:{envMap:{value:null},envMapRotation:{value:new Pt},flipEnvMap:{value:-1},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new Pt}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new Pt}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new Pt},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new Pt},normalScale:{value:new Tt(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new Pt},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new Pt}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new Pt}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new Pt}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new It(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMap:{value:[]},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotShadowMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMap:{value:[]},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null}},points:{diffuse:{value:new It(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new Pt},alphaTest:{value:0},uvTransform:{value:new Pt}},sprite:{diffuse:{value:new It(16777215)},opacity:{value:1},center:{value:new Tt(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new Pt},alphaMap:{value:null},alphaMapTransform:{value:new Pt},alphaTest:{value:0}}},En={basic:{uniforms:Pe([et.common,et.specularmap,et.envmap,et.aomap,et.lightmap,et.fog]),vertexShader:Dt.meshbasic_vert,fragmentShader:Dt.meshbasic_frag},lambert:{uniforms:Pe([et.common,et.specularmap,et.envmap,et.aomap,et.lightmap,et.emissivemap,et.bumpmap,et.normalmap,et.displacementmap,et.fog,et.lights,{emissive:{value:new It(0)}}]),vertexShader:Dt.meshlambert_vert,fragmentShader:Dt.meshlambert_frag},phong:{uniforms:Pe([et.common,et.specularmap,et.envmap,et.aomap,et.lightmap,et.emissivemap,et.bumpmap,et.normalmap,et.displacementmap,et.fog,et.lights,{emissive:{value:new It(0)},specular:{value:new It(1118481)},shininess:{value:30}}]),vertexShader:Dt.meshphong_vert,fragmentShader:Dt.meshphong_frag},standard:{uniforms:Pe([et.common,et.envmap,et.aomap,et.lightmap,et.emissivemap,et.bumpmap,et.normalmap,et.displacementmap,et.roughnessmap,et.metalnessmap,et.fog,et.lights,{emissive:{value:new It(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:Dt.meshphysical_vert,fragmentShader:Dt.meshphysical_frag},toon:{uniforms:Pe([et.common,et.aomap,et.lightmap,et.emissivemap,et.bumpmap,et.normalmap,et.displacementmap,et.gradientmap,et.fog,et.lights,{emissive:{value:new It(0)}}]),vertexShader:Dt.meshtoon_vert,fragmentShader:Dt.meshtoon_frag},matcap:{uniforms:Pe([et.common,et.bumpmap,et.normalmap,et.displacementmap,et.fog,{matcap:{value:null}}]),vertexShader:Dt.meshmatcap_vert,fragmentShader:Dt.meshmatcap_frag},points:{uniforms:Pe([et.points,et.fog]),vertexShader:Dt.points_vert,fragmentShader:Dt.points_frag},dashed:{uniforms:Pe([et.common,et.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:Dt.linedashed_vert,fragmentShader:Dt.linedashed_frag},depth:{uniforms:Pe([et.common,et.displacementmap]),vertexShader:Dt.depth_vert,fragmentShader:Dt.depth_frag},normal:{uniforms:Pe([et.common,et.bumpmap,et.normalmap,et.displacementmap,{opacity:{value:1}}]),vertexShader:Dt.meshnormal_vert,fragmentShader:Dt.meshnormal_frag},sprite:{uniforms:Pe([et.sprite,et.fog]),vertexShader:Dt.sprite_vert,fragmentShader:Dt.sprite_frag},background:{uniforms:{uvTransform:{value:new Pt},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:Dt.background_vert,fragmentShader:Dt.background_frag},backgroundCube:{uniforms:{envMap:{value:null},flipEnvMap:{value:-1},backgroundBlurriness:{value:0},backgroundIntensity:{value:1},backgroundRotation:{value:new Pt}},vertexShader:Dt.backgroundCube_vert,fragmentShader:Dt.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:Dt.cube_vert,fragmentShader:Dt.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:Dt.equirect_vert,fragmentShader:Dt.equirect_frag},distanceRGBA:{uniforms:Pe([et.common,et.displacementmap,{referencePosition:{value:new L},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:Dt.distanceRGBA_vert,fragmentShader:Dt.distanceRGBA_frag},shadow:{uniforms:Pe([et.lights,et.fog,{color:{value:new It(0)},opacity:{value:1}}]),vertexShader:Dt.shadow_vert,fragmentShader:Dt.shadow_frag}};En.physical={uniforms:Pe([En.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new Pt},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new Pt},clearcoatNormalScale:{value:new Tt(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new Pt},dispersion:{value:0},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new Pt},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new Pt},sheen:{value:0},sheenColor:{value:new It(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new Pt},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new Pt},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new Pt},transmissionSamplerSize:{value:new Tt},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new Pt},attenuationDistance:{value:0},attenuationColor:{value:new It(0)},specularColor:{value:new It(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new Pt},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new Pt},anisotropyVector:{value:new Tt},anisotropyMap:{value:null},anisotropyMapTransform:{value:new Pt}}]),vertexShader:Dt.meshphysical_vert,fragmentShader:Dt.meshphysical_frag};const pr={r:0,b:0,g:0},pi=new Xn,bm=new te;function Am(n,t,e,i,s,r,a){const o=new It(0);let l=r===!0?0:1,c,u,d=null,h=0,p=null;function _(M){let y=M.isScene===!0?M.background:null;return y&&y.isTexture&&(y=(M.backgroundBlurriness>0?e:t).get(y)),y}function S(M){let y=!1;const P=_(M);P===null?f(o,l):P&&P.isColor&&(f(P,1),y=!0);const R=n.xr.getEnvironmentBlendMode();R==="additive"?i.buffers.color.setClear(0,0,0,1,a):R==="alpha-blend"&&i.buffers.color.setClear(0,0,0,0,a),(n.autoClear||y)&&(i.buffers.depth.setTest(!0),i.buffers.depth.setMask(!0),i.buffers.color.setMask(!0),n.clear(n.autoClearColor,n.autoClearDepth,n.autoClearStencil))}function m(M,y){const P=_(y);P&&(P.isCubeTexture||P.mapping===jr)?(u===void 0&&(u=new mn(new Gs(1,1,1),new _n({name:"BackgroundCubeMaterial",uniforms:rs(En.backgroundCube.uniforms),vertexShader:En.backgroundCube.vertexShader,fragmentShader:En.backgroundCube.fragmentShader,side:Le,depthTest:!1,depthWrite:!1,fog:!1,allowOverride:!1})),u.geometry.deleteAttribute("normal"),u.geometry.deleteAttribute("uv"),u.onBeforeRender=function(R,A,I){this.matrixWorld.copyPosition(I.matrixWorld)},Object.defineProperty(u.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),s.update(u)),pi.copy(y.backgroundRotation),pi.x*=-1,pi.y*=-1,pi.z*=-1,P.isCubeTexture&&P.isRenderTargetTexture===!1&&(pi.y*=-1,pi.z*=-1),u.material.uniforms.envMap.value=P,u.material.uniforms.flipEnvMap.value=P.isCubeTexture&&P.isRenderTargetTexture===!1?-1:1,u.material.uniforms.backgroundBlurriness.value=y.backgroundBlurriness,u.material.uniforms.backgroundIntensity.value=y.backgroundIntensity,u.material.uniforms.backgroundRotation.value.setFromMatrix4(bm.makeRotationFromEuler(pi)),u.material.toneMapped=Gt.getTransfer(P.colorSpace)!==Yt,(d!==P||h!==P.version||p!==n.toneMapping)&&(u.material.needsUpdate=!0,d=P,h=P.version,p=n.toneMapping),u.layers.enableAll(),M.unshift(u,u.geometry,u.material,0,0,null)):P&&P.isTexture&&(c===void 0&&(c=new mn(new Jr(2,2),new _n({name:"BackgroundMaterial",uniforms:rs(En.background.uniforms),vertexShader:En.background.vertexShader,fragmentShader:En.background.fragmentShader,side:oi,depthTest:!1,depthWrite:!1,fog:!1,allowOverride:!1})),c.geometry.deleteAttribute("normal"),Object.defineProperty(c.material,"map",{get:function(){return this.uniforms.t2D.value}}),s.update(c)),c.material.uniforms.t2D.value=P,c.material.uniforms.backgroundIntensity.value=y.backgroundIntensity,c.material.toneMapped=Gt.getTransfer(P.colorSpace)!==Yt,P.matrixAutoUpdate===!0&&P.updateMatrix(),c.material.uniforms.uvTransform.value.copy(P.matrix),(d!==P||h!==P.version||p!==n.toneMapping)&&(c.material.needsUpdate=!0,d=P,h=P.version,p=n.toneMapping),c.layers.enableAll(),M.unshift(c,c.geometry,c.material,0,0,null))}function f(M,y){M.getRGB(pr,Eu(n)),i.buffers.color.setClear(pr.r,pr.g,pr.b,y,a)}function b(){u!==void 0&&(u.geometry.dispose(),u.material.dispose(),u=void 0),c!==void 0&&(c.geometry.dispose(),c.material.dispose(),c=void 0)}return{getClearColor:function(){return o},setClearColor:function(M,y=1){o.set(M),l=y,f(o,l)},getClearAlpha:function(){return l},setClearAlpha:function(M){l=M,f(o,l)},render:S,addToRenderList:m,dispose:b}}function wm(n,t){const e=n.getParameter(n.MAX_VERTEX_ATTRIBS),i={},s=h(null);let r=s,a=!1;function o(x,C,V,z,Y){let j=!1;const X=d(z,V,C);r!==X&&(r=X,c(r.object)),j=p(x,z,V,Y),j&&_(x,z,V,Y),Y!==null&&t.update(Y,n.ELEMENT_ARRAY_BUFFER),(j||a)&&(a=!1,y(x,C,V,z),Y!==null&&n.bindBuffer(n.ELEMENT_ARRAY_BUFFER,t.get(Y).buffer))}function l(){return n.createVertexArray()}function c(x){return n.bindVertexArray(x)}function u(x){return n.deleteVertexArray(x)}function d(x,C,V){const z=V.wireframe===!0;let Y=i[x.id];Y===void 0&&(Y={},i[x.id]=Y);let j=Y[C.id];j===void 0&&(j={},Y[C.id]=j);let X=j[z];return X===void 0&&(X=h(l()),j[z]=X),X}function h(x){const C=[],V=[],z=[];for(let Y=0;Y<e;Y++)C[Y]=0,V[Y]=0,z[Y]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:C,enabledAttributes:V,attributeDivisors:z,object:x,attributes:{},index:null}}function p(x,C,V,z){const Y=r.attributes,j=C.attributes;let X=0;const Z=V.getAttributes();for(const H in Z)if(Z[H].location>=0){const ut=Y[H];let vt=j[H];if(vt===void 0&&(H==="instanceMatrix"&&x.instanceMatrix&&(vt=x.instanceMatrix),H==="instanceColor"&&x.instanceColor&&(vt=x.instanceColor)),ut===void 0||ut.attribute!==vt||vt&&ut.data!==vt.data)return!0;X++}return r.attributesNum!==X||r.index!==z}function _(x,C,V,z){const Y={},j=C.attributes;let X=0;const Z=V.getAttributes();for(const H in Z)if(Z[H].location>=0){let ut=j[H];ut===void 0&&(H==="instanceMatrix"&&x.instanceMatrix&&(ut=x.instanceMatrix),H==="instanceColor"&&x.instanceColor&&(ut=x.instanceColor));const vt={};vt.attribute=ut,ut&&ut.data&&(vt.data=ut.data),Y[H]=vt,X++}r.attributes=Y,r.attributesNum=X,r.index=z}function S(){const x=r.newAttributes;for(let C=0,V=x.length;C<V;C++)x[C]=0}function m(x){f(x,0)}function f(x,C){const V=r.newAttributes,z=r.enabledAttributes,Y=r.attributeDivisors;V[x]=1,z[x]===0&&(n.enableVertexAttribArray(x),z[x]=1),Y[x]!==C&&(n.vertexAttribDivisor(x,C),Y[x]=C)}function b(){const x=r.newAttributes,C=r.enabledAttributes;for(let V=0,z=C.length;V<z;V++)C[V]!==x[V]&&(n.disableVertexAttribArray(V),C[V]=0)}function M(x,C,V,z,Y,j,X){X===!0?n.vertexAttribIPointer(x,C,V,Y,j):n.vertexAttribPointer(x,C,V,z,Y,j)}function y(x,C,V,z){S();const Y=z.attributes,j=V.getAttributes(),X=C.defaultAttributeValues;for(const Z in j){const H=j[Z];if(H.location>=0){let it=Y[Z];if(it===void 0&&(Z==="instanceMatrix"&&x.instanceMatrix&&(it=x.instanceMatrix),Z==="instanceColor"&&x.instanceColor&&(it=x.instanceColor)),it!==void 0){const ut=it.normalized,vt=it.itemSize,Ut=t.get(it);if(Ut===void 0)continue;const Zt=Ut.buffer,W=Ut.type,tt=Ut.bytesPerElement,mt=W===n.INT||W===n.UNSIGNED_INT||it.gpuType===Jo;if(it.isInterleavedBufferAttribute){const st=it.data,Et=st.stride,Wt=it.offset;if(st.isInstancedInterleavedBuffer){for(let bt=0;bt<H.locationSize;bt++)f(H.location+bt,st.meshPerAttribute);x.isInstancedMesh!==!0&&z._maxInstanceCount===void 0&&(z._maxInstanceCount=st.meshPerAttribute*st.count)}else for(let bt=0;bt<H.locationSize;bt++)m(H.location+bt);n.bindBuffer(n.ARRAY_BUFFER,Zt);for(let bt=0;bt<H.locationSize;bt++)M(H.location+bt,vt/H.locationSize,W,ut,Et*tt,(Wt+vt/H.locationSize*bt)*tt,mt)}else{if(it.isInstancedBufferAttribute){for(let st=0;st<H.locationSize;st++)f(H.location+st,it.meshPerAttribute);x.isInstancedMesh!==!0&&z._maxInstanceCount===void 0&&(z._maxInstanceCount=it.meshPerAttribute*it.count)}else for(let st=0;st<H.locationSize;st++)m(H.location+st);n.bindBuffer(n.ARRAY_BUFFER,Zt);for(let st=0;st<H.locationSize;st++)M(H.location+st,vt/H.locationSize,W,ut,vt*tt,vt/H.locationSize*st*tt,mt)}}else if(X!==void 0){const ut=X[Z];if(ut!==void 0)switch(ut.length){case 2:n.vertexAttrib2fv(H.location,ut);break;case 3:n.vertexAttrib3fv(H.location,ut);break;case 4:n.vertexAttrib4fv(H.location,ut);break;default:n.vertexAttrib1fv(H.location,ut)}}}}b()}function P(){I();for(const x in i){const C=i[x];for(const V in C){const z=C[V];for(const Y in z)u(z[Y].object),delete z[Y];delete C[V]}delete i[x]}}function R(x){if(i[x.id]===void 0)return;const C=i[x.id];for(const V in C){const z=C[V];for(const Y in z)u(z[Y].object),delete z[Y];delete C[V]}delete i[x.id]}function A(x){for(const C in i){const V=i[C];if(V[x.id]===void 0)continue;const z=V[x.id];for(const Y in z)u(z[Y].object),delete z[Y];delete V[x.id]}}function I(){E(),a=!0,r!==s&&(r=s,c(r.object))}function E(){s.geometry=null,s.program=null,s.wireframe=!1}return{setup:o,reset:I,resetDefaultState:E,dispose:P,releaseStatesOfGeometry:R,releaseStatesOfProgram:A,initAttributes:S,enableAttribute:m,disableUnusedAttributes:b}}function Rm(n,t,e){let i;function s(c){i=c}function r(c,u){n.drawArrays(i,c,u),e.update(u,i,1)}function a(c,u,d){d!==0&&(n.drawArraysInstanced(i,c,u,d),e.update(u,i,d))}function o(c,u,d){if(d===0)return;t.get("WEBGL_multi_draw").multiDrawArraysWEBGL(i,c,0,u,0,d);let p=0;for(let _=0;_<d;_++)p+=u[_];e.update(p,i,1)}function l(c,u,d,h){if(d===0)return;const p=t.get("WEBGL_multi_draw");if(p===null)for(let _=0;_<c.length;_++)a(c[_],u[_],h[_]);else{p.multiDrawArraysInstancedWEBGL(i,c,0,u,0,h,0,d);let _=0;for(let S=0;S<d;S++)_+=u[S]*h[S];e.update(_,i,1)}}this.setMode=s,this.render=r,this.renderInstances=a,this.renderMultiDraw=o,this.renderMultiDrawInstances=l}function Cm(n,t,e,i){let s;function r(){if(s!==void 0)return s;if(t.has("EXT_texture_filter_anisotropic")===!0){const A=t.get("EXT_texture_filter_anisotropic");s=n.getParameter(A.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else s=0;return s}function a(A){return!(A!==pn&&i.convert(A)!==n.getParameter(n.IMPLEMENTATION_COLOR_READ_FORMAT))}function o(A){const I=A===zs&&(t.has("EXT_color_buffer_half_float")||t.has("EXT_color_buffer_float"));return!(A!==Wn&&i.convert(A)!==n.getParameter(n.IMPLEMENTATION_COLOR_READ_TYPE)&&A!==Hn&&!I)}function l(A){if(A==="highp"){if(n.getShaderPrecisionFormat(n.VERTEX_SHADER,n.HIGH_FLOAT).precision>0&&n.getShaderPrecisionFormat(n.FRAGMENT_SHADER,n.HIGH_FLOAT).precision>0)return"highp";A="mediump"}return A==="mediump"&&n.getShaderPrecisionFormat(n.VERTEX_SHADER,n.MEDIUM_FLOAT).precision>0&&n.getShaderPrecisionFormat(n.FRAGMENT_SHADER,n.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let c=e.precision!==void 0?e.precision:"highp";const u=l(c);u!==c&&(console.warn("THREE.WebGLRenderer:",c,"not supported, using",u,"instead."),c=u);const d=e.logarithmicDepthBuffer===!0,h=e.reverseDepthBuffer===!0&&t.has("EXT_clip_control"),p=n.getParameter(n.MAX_TEXTURE_IMAGE_UNITS),_=n.getParameter(n.MAX_VERTEX_TEXTURE_IMAGE_UNITS),S=n.getParameter(n.MAX_TEXTURE_SIZE),m=n.getParameter(n.MAX_CUBE_MAP_TEXTURE_SIZE),f=n.getParameter(n.MAX_VERTEX_ATTRIBS),b=n.getParameter(n.MAX_VERTEX_UNIFORM_VECTORS),M=n.getParameter(n.MAX_VARYING_VECTORS),y=n.getParameter(n.MAX_FRAGMENT_UNIFORM_VECTORS),P=_>0,R=n.getParameter(n.MAX_SAMPLES);return{isWebGL2:!0,getMaxAnisotropy:r,getMaxPrecision:l,textureFormatReadable:a,textureTypeReadable:o,precision:c,logarithmicDepthBuffer:d,reverseDepthBuffer:h,maxTextures:p,maxVertexTextures:_,maxTextureSize:S,maxCubemapSize:m,maxAttributes:f,maxVertexUniforms:b,maxVaryings:M,maxFragmentUniforms:y,vertexTextures:P,maxSamples:R}}function Pm(n){const t=this;let e=null,i=0,s=!1,r=!1;const a=new ti,o=new Pt,l={value:null,needsUpdate:!1};this.uniform=l,this.numPlanes=0,this.numIntersection=0,this.init=function(d,h){const p=d.length!==0||h||i!==0||s;return s=h,i=d.length,p},this.beginShadows=function(){r=!0,u(null)},this.endShadows=function(){r=!1},this.setGlobalState=function(d,h){e=u(d,h,0)},this.setState=function(d,h,p){const _=d.clippingPlanes,S=d.clipIntersection,m=d.clipShadows,f=n.get(d);if(!s||_===null||_.length===0||r&&!m)r?u(null):c();else{const b=r?0:i,M=b*4;let y=f.clippingState||null;l.value=y,y=u(_,h,M,p);for(let P=0;P!==M;++P)y[P]=e[P];f.clippingState=y,this.numIntersection=S?this.numPlanes:0,this.numPlanes+=b}};function c(){l.value!==e&&(l.value=e,l.needsUpdate=i>0),t.numPlanes=i,t.numIntersection=0}function u(d,h,p,_){const S=d!==null?d.length:0;let m=null;if(S!==0){if(m=l.value,_!==!0||m===null){const f=p+S*4,b=h.matrixWorldInverse;o.getNormalMatrix(b),(m===null||m.length<f)&&(m=new Float32Array(f));for(let M=0,y=p;M!==S;++M,y+=4)a.copy(d[M]).applyMatrix4(b,o),a.normal.toArray(m,y),m[y+3]=a.constant}l.value=m,l.needsUpdate=!0}return t.numPlanes=S,t.numIntersection=0,m}}function Lm(n){let t=new WeakMap;function e(a,o){return o===oo?a.mapping=ns:o===lo&&(a.mapping=is),a}function i(a){if(a&&a.isTexture){const o=a.mapping;if(o===oo||o===lo)if(t.has(a)){const l=t.get(a).texture;return e(l,a.mapping)}else{const l=a.image;if(l&&l.height>0){const c=new Ah(l.height);return c.fromEquirectangularTexture(n,a),t.set(a,c),a.addEventListener("dispose",s),e(c.texture,a.mapping)}else return null}}return a}function s(a){const o=a.target;o.removeEventListener("dispose",s);const l=t.get(o);l!==void 0&&(t.delete(o),l.dispose())}function r(){t=new WeakMap}return{get:i,dispose:r}}const Xi=4,ac=[.125,.215,.35,.446,.526,.582],vi=20,Da=new wu,oc=new It;let Ia=null,Ua=0,Na=0,Oa=!1;const gi=(1+Math.sqrt(5))/2,Vi=1/gi,lc=[new L(-gi,Vi,0),new L(gi,Vi,0),new L(-Vi,0,gi),new L(Vi,0,gi),new L(0,gi,-Vi),new L(0,gi,Vi),new L(-1,1,-1),new L(1,1,-1),new L(-1,1,1),new L(1,1,1)],Dm=new L;class cc{constructor(t){this._renderer=t,this._pingPongRenderTarget=null,this._lodMax=0,this._cubeSize=0,this._lodPlanes=[],this._sizeLods=[],this._sigmas=[],this._blurMaterial=null,this._cubemapMaterial=null,this._equirectMaterial=null,this._compileMaterial(this._blurMaterial)}fromScene(t,e=0,i=.1,s=100,r={}){const{size:a=256,position:o=Dm}=r;Ia=this._renderer.getRenderTarget(),Ua=this._renderer.getActiveCubeFace(),Na=this._renderer.getActiveMipmapLevel(),Oa=this._renderer.xr.enabled,this._renderer.xr.enabled=!1,this._setSize(a);const l=this._allocateTargets();return l.depthBuffer=!0,this._sceneToCubeUV(t,i,s,l,o),e>0&&this._blur(l,0,0,e),this._applyPMREM(l),this._cleanup(l),l}fromEquirectangular(t,e=null){return this._fromTexture(t,e)}fromCubemap(t,e=null){return this._fromTexture(t,e)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=hc(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=dc(),this._compileMaterial(this._equirectMaterial))}dispose(){this._dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose()}_setSize(t){this._lodMax=Math.floor(Math.log2(t)),this._cubeSize=Math.pow(2,this._lodMax)}_dispose(){this._blurMaterial!==null&&this._blurMaterial.dispose(),this._pingPongRenderTarget!==null&&this._pingPongRenderTarget.dispose();for(let t=0;t<this._lodPlanes.length;t++)this._lodPlanes[t].dispose()}_cleanup(t){this._renderer.setRenderTarget(Ia,Ua,Na),this._renderer.xr.enabled=Oa,t.scissorTest=!1,mr(t,0,0,t.width,t.height)}_fromTexture(t,e){t.mapping===ns||t.mapping===is?this._setSize(t.image.length===0?16:t.image[0].width||t.image[0].image.width):this._setSize(t.image.width/4),Ia=this._renderer.getRenderTarget(),Ua=this._renderer.getActiveCubeFace(),Na=this._renderer.getActiveMipmapLevel(),Oa=this._renderer.xr.enabled,this._renderer.xr.enabled=!1;const i=e||this._allocateTargets();return this._textureToCubeUV(t,i),this._applyPMREM(i),this._cleanup(i),i}_allocateTargets(){const t=3*Math.max(this._cubeSize,112),e=4*this._cubeSize,i={magFilter:Rn,minFilter:Rn,generateMipmaps:!1,type:zs,format:pn,colorSpace:ss,depthBuffer:!1},s=uc(t,e,i);if(this._pingPongRenderTarget===null||this._pingPongRenderTarget.width!==t||this._pingPongRenderTarget.height!==e){this._pingPongRenderTarget!==null&&this._dispose(),this._pingPongRenderTarget=uc(t,e,i);const{_lodMax:r}=this;({sizeLods:this._sizeLods,lodPlanes:this._lodPlanes,sigmas:this._sigmas}=Im(r)),this._blurMaterial=Um(r,t,e)}return s}_compileMaterial(t){const e=new mn(this._lodPlanes[0],t);this._renderer.compile(e,Da)}_sceneToCubeUV(t,e,i,s,r){const l=new Ge(90,1,e,i),c=[1,-1,1,1,1,1],u=[1,1,1,-1,-1,-1],d=this._renderer,h=d.autoClear,p=d.toneMapping;d.getClearColor(oc),d.toneMapping=ai,d.autoClear=!1;const _=new xu({name:"PMREM.Background",side:Le,depthWrite:!1,depthTest:!1}),S=new mn(new Gs,_);let m=!1;const f=t.background;f?f.isColor&&(_.color.copy(f),t.background=null,m=!0):(_.color.copy(oc),m=!0);for(let b=0;b<6;b++){const M=b%3;M===0?(l.up.set(0,c[b],0),l.position.set(r.x,r.y,r.z),l.lookAt(r.x+u[b],r.y,r.z)):M===1?(l.up.set(0,0,c[b]),l.position.set(r.x,r.y,r.z),l.lookAt(r.x,r.y+u[b],r.z)):(l.up.set(0,c[b],0),l.position.set(r.x,r.y,r.z),l.lookAt(r.x,r.y,r.z+u[b]));const y=this._cubeSize;mr(s,M*y,b>2?y:0,y,y),d.setRenderTarget(s),m&&d.render(S,l),d.render(t,l)}S.geometry.dispose(),S.material.dispose(),d.toneMapping=p,d.autoClear=h,t.background=f}_textureToCubeUV(t,e){const i=this._renderer,s=t.mapping===ns||t.mapping===is;s?(this._cubemapMaterial===null&&(this._cubemapMaterial=hc()),this._cubemapMaterial.uniforms.flipEnvMap.value=t.isRenderTargetTexture===!1?-1:1):this._equirectMaterial===null&&(this._equirectMaterial=dc());const r=s?this._cubemapMaterial:this._equirectMaterial,a=new mn(this._lodPlanes[0],r),o=r.uniforms;o.envMap.value=t;const l=this._cubeSize;mr(e,0,0,3*l,2*l),i.setRenderTarget(e),i.render(a,Da)}_applyPMREM(t){const e=this._renderer,i=e.autoClear;e.autoClear=!1;const s=this._lodPlanes.length;for(let r=1;r<s;r++){const a=Math.sqrt(this._sigmas[r]*this._sigmas[r]-this._sigmas[r-1]*this._sigmas[r-1]),o=lc[(s-r-1)%lc.length];this._blur(t,r-1,r,a,o)}e.autoClear=i}_blur(t,e,i,s,r){const a=this._pingPongRenderTarget;this._halfBlur(t,a,e,i,s,"latitudinal",r),this._halfBlur(a,t,i,i,s,"longitudinal",r)}_halfBlur(t,e,i,s,r,a,o){const l=this._renderer,c=this._blurMaterial;a!=="latitudinal"&&a!=="longitudinal"&&console.error("blur direction must be either latitudinal or longitudinal!");const u=3,d=new mn(this._lodPlanes[s],c),h=c.uniforms,p=this._sizeLods[i]-1,_=isFinite(r)?Math.PI/(2*p):2*Math.PI/(2*vi-1),S=r/_,m=isFinite(r)?1+Math.floor(u*S):vi;m>vi&&console.warn(`sigmaRadians, ${r}, is too large and will clip, as it requested ${m} samples when the maximum is set to ${vi}`);const f=[];let b=0;for(let A=0;A<vi;++A){const I=A/S,E=Math.exp(-I*I/2);f.push(E),A===0?b+=E:A<m&&(b+=2*E)}for(let A=0;A<f.length;A++)f[A]=f[A]/b;h.envMap.value=t.texture,h.samples.value=m,h.weights.value=f,h.latitudinal.value=a==="latitudinal",o&&(h.poleAxis.value=o);const{_lodMax:M}=this;h.dTheta.value=_,h.mipInt.value=M-i;const y=this._sizeLods[s],P=3*y*(s>M-Xi?s-M+Xi:0),R=4*(this._cubeSize-y);mr(e,P,R,3*y,2*y),l.setRenderTarget(e),l.render(d,Da)}}function Im(n){const t=[],e=[],i=[];let s=n;const r=n-Xi+1+ac.length;for(let a=0;a<r;a++){const o=Math.pow(2,s);e.push(o);let l=1/o;a>n-Xi?l=ac[a-n+Xi-1]:a===0&&(l=0),i.push(l);const c=1/(o-2),u=-c,d=1+c,h=[u,u,d,u,d,d,u,u,d,d,u,d],p=6,_=6,S=3,m=2,f=1,b=new Float32Array(S*_*p),M=new Float32Array(m*_*p),y=new Float32Array(f*_*p);for(let R=0;R<p;R++){const A=R%3*2/3-1,I=R>2?0:-1,E=[A,I,0,A+2/3,I,0,A+2/3,I+1,0,A,I,0,A+2/3,I+1,0,A,I+1,0];b.set(E,S*_*R),M.set(h,m*_*R);const x=[R,R,R,R,R,R];y.set(x,f*_*R)}const P=new xn;P.setAttribute("position",new Xe(b,S)),P.setAttribute("uv",new Xe(M,m)),P.setAttribute("faceIndex",new Xe(y,f)),t.push(P),s>Xi&&s--}return{lodPlanes:t,sizeLods:e,sigmas:i}}function uc(n,t,e){const i=new Ti(n,t,e);return i.texture.mapping=jr,i.texture.name="PMREM.cubeUv",i.scissorTest=!0,i}function mr(n,t,e,i,s){n.viewport.set(t,e,i,s),n.scissor.set(t,e,i,s)}function Um(n,t,e){const i=new Float32Array(vi),s=new L(0,1,0);return new _n({name:"SphericalGaussianBlur",defines:{n:vi,CUBEUV_TEXEL_WIDTH:1/t,CUBEUV_TEXEL_HEIGHT:1/e,CUBEUV_MAX_MIP:`${n}.0`},uniforms:{envMap:{value:null},samples:{value:1},weights:{value:i},latitudinal:{value:!1},dTheta:{value:0},mipInt:{value:0},poleAxis:{value:s}},vertexShader:hl(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;
			uniform int samples;
			uniform float weights[ n ];
			uniform bool latitudinal;
			uniform float dTheta;
			uniform float mipInt;
			uniform vec3 poleAxis;

			#define ENVMAP_TYPE_CUBE_UV
			#include <cube_uv_reflection_fragment>

			vec3 getSample( float theta, vec3 axis ) {

				float cosTheta = cos( theta );
				// Rodrigues' axis-angle rotation
				vec3 sampleDirection = vOutputDirection * cosTheta
					+ cross( axis, vOutputDirection ) * sin( theta )
					+ axis * dot( axis, vOutputDirection ) * ( 1.0 - cosTheta );

				return bilinearCubeUV( envMap, sampleDirection, mipInt );

			}

			void main() {

				vec3 axis = latitudinal ? poleAxis : cross( poleAxis, vOutputDirection );

				if ( all( equal( axis, vec3( 0.0 ) ) ) ) {

					axis = vec3( vOutputDirection.z, 0.0, - vOutputDirection.x );

				}

				axis = normalize( axis );

				gl_FragColor = vec4( 0.0, 0.0, 0.0, 1.0 );
				gl_FragColor.rgb += weights[ 0 ] * getSample( 0.0, axis );

				for ( int i = 1; i < n; i++ ) {

					if ( i >= samples ) {

						break;

					}

					float theta = dTheta * float( i );
					gl_FragColor.rgb += weights[ i ] * getSample( -1.0 * theta, axis );
					gl_FragColor.rgb += weights[ i ] * getSample( theta, axis );

				}

			}
		`,blending:ri,depthTest:!1,depthWrite:!1})}function dc(){return new _n({name:"EquirectangularToCubeUV",uniforms:{envMap:{value:null}},vertexShader:hl(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;

			#include <common>

			void main() {

				vec3 outputDirection = normalize( vOutputDirection );
				vec2 uv = equirectUv( outputDirection );

				gl_FragColor = vec4( texture2D ( envMap, uv ).rgb, 1.0 );

			}
		`,blending:ri,depthTest:!1,depthWrite:!1})}function hc(){return new _n({name:"CubemapToCubeUV",uniforms:{envMap:{value:null},flipEnvMap:{value:-1}},vertexShader:hl(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			uniform float flipEnvMap;

			varying vec3 vOutputDirection;

			uniform samplerCube envMap;

			void main() {

				gl_FragColor = textureCube( envMap, vec3( flipEnvMap * vOutputDirection.x, vOutputDirection.yz ) );

			}
		`,blending:ri,depthTest:!1,depthWrite:!1})}function hl(){return`

		precision mediump float;
		precision mediump int;

		attribute float faceIndex;

		varying vec3 vOutputDirection;

		// RH coordinate system; PMREM face-indexing convention
		vec3 getDirection( vec2 uv, float face ) {

			uv = 2.0 * uv - 1.0;

			vec3 direction = vec3( uv, 1.0 );

			if ( face == 0.0 ) {

				direction = direction.zyx; // ( 1, v, u ) pos x

			} else if ( face == 1.0 ) {

				direction = direction.xzy;
				direction.xz *= -1.0; // ( -u, 1, -v ) pos y

			} else if ( face == 2.0 ) {

				direction.x *= -1.0; // ( -u, v, 1 ) pos z

			} else if ( face == 3.0 ) {

				direction = direction.zyx;
				direction.xz *= -1.0; // ( -1, v, -u ) neg x

			} else if ( face == 4.0 ) {

				direction = direction.xzy;
				direction.xy *= -1.0; // ( -u, -1, v ) neg y

			} else if ( face == 5.0 ) {

				direction.z *= -1.0; // ( u, v, -1 ) neg z

			}

			return direction;

		}

		void main() {

			vOutputDirection = getDirection( uv, faceIndex );
			gl_Position = vec4( position, 1.0 );

		}
	`}function Nm(n){let t=new WeakMap,e=null;function i(o){if(o&&o.isTexture){const l=o.mapping,c=l===oo||l===lo,u=l===ns||l===is;if(c||u){let d=t.get(o);const h=d!==void 0?d.texture.pmremVersion:0;if(o.isRenderTargetTexture&&o.pmremVersion!==h)return e===null&&(e=new cc(n)),d=c?e.fromEquirectangular(o,d):e.fromCubemap(o,d),d.texture.pmremVersion=o.pmremVersion,t.set(o,d),d.texture;if(d!==void 0)return d.texture;{const p=o.image;return c&&p&&p.height>0||u&&p&&s(p)?(e===null&&(e=new cc(n)),d=c?e.fromEquirectangular(o):e.fromCubemap(o),d.texture.pmremVersion=o.pmremVersion,t.set(o,d),o.addEventListener("dispose",r),d.texture):null}}}return o}function s(o){let l=0;const c=6;for(let u=0;u<c;u++)o[u]!==void 0&&l++;return l===c}function r(o){const l=o.target;l.removeEventListener("dispose",r);const c=t.get(l);c!==void 0&&(t.delete(l),c.dispose())}function a(){t=new WeakMap,e!==null&&(e.dispose(),e=null)}return{get:i,dispose:a}}function Om(n){const t={};function e(i){if(t[i]!==void 0)return t[i];let s;switch(i){case"WEBGL_depth_texture":s=n.getExtension("WEBGL_depth_texture")||n.getExtension("MOZ_WEBGL_depth_texture")||n.getExtension("WEBKIT_WEBGL_depth_texture");break;case"EXT_texture_filter_anisotropic":s=n.getExtension("EXT_texture_filter_anisotropic")||n.getExtension("MOZ_EXT_texture_filter_anisotropic")||n.getExtension("WEBKIT_EXT_texture_filter_anisotropic");break;case"WEBGL_compressed_texture_s3tc":s=n.getExtension("WEBGL_compressed_texture_s3tc")||n.getExtension("MOZ_WEBGL_compressed_texture_s3tc")||n.getExtension("WEBKIT_WEBGL_compressed_texture_s3tc");break;case"WEBGL_compressed_texture_pvrtc":s=n.getExtension("WEBGL_compressed_texture_pvrtc")||n.getExtension("WEBKIT_WEBGL_compressed_texture_pvrtc");break;default:s=n.getExtension(i)}return t[i]=s,s}return{has:function(i){return e(i)!==null},init:function(){e("EXT_color_buffer_float"),e("WEBGL_clip_cull_distance"),e("OES_texture_float_linear"),e("EXT_color_buffer_half_float"),e("WEBGL_multisampled_render_to_texture"),e("WEBGL_render_shared_exponent")},get:function(i){const s=e(i);return s===null&&Lr("THREE.WebGLRenderer: "+i+" extension not supported."),s}}}function Fm(n,t,e,i){const s={},r=new WeakMap;function a(d){const h=d.target;h.index!==null&&t.remove(h.index);for(const _ in h.attributes)t.remove(h.attributes[_]);h.removeEventListener("dispose",a),delete s[h.id];const p=r.get(h);p&&(t.remove(p),r.delete(h)),i.releaseStatesOfGeometry(h),h.isInstancedBufferGeometry===!0&&delete h._maxInstanceCount,e.memory.geometries--}function o(d,h){return s[h.id]===!0||(h.addEventListener("dispose",a),s[h.id]=!0,e.memory.geometries++),h}function l(d){const h=d.attributes;for(const p in h)t.update(h[p],n.ARRAY_BUFFER)}function c(d){const h=[],p=d.index,_=d.attributes.position;let S=0;if(p!==null){const b=p.array;S=p.version;for(let M=0,y=b.length;M<y;M+=3){const P=b[M+0],R=b[M+1],A=b[M+2];h.push(P,R,R,A,A,P)}}else if(_!==void 0){const b=_.array;S=_.version;for(let M=0,y=b.length/3-1;M<y;M+=3){const P=M+0,R=M+1,A=M+2;h.push(P,R,R,A,A,P)}}else return;const m=new(gu(h)?yu:Su)(h,1);m.version=S;const f=r.get(d);f&&t.remove(f),r.set(d,m)}function u(d){const h=r.get(d);if(h){const p=d.index;p!==null&&h.version<p.version&&c(d)}else c(d);return r.get(d)}return{get:o,update:l,getWireframeAttribute:u}}function Bm(n,t,e){let i;function s(h){i=h}let r,a;function o(h){r=h.type,a=h.bytesPerElement}function l(h,p){n.drawElements(i,p,r,h*a),e.update(p,i,1)}function c(h,p,_){_!==0&&(n.drawElementsInstanced(i,p,r,h*a,_),e.update(p,i,_))}function u(h,p,_){if(_===0)return;t.get("WEBGL_multi_draw").multiDrawElementsWEBGL(i,p,0,r,h,0,_);let m=0;for(let f=0;f<_;f++)m+=p[f];e.update(m,i,1)}function d(h,p,_,S){if(_===0)return;const m=t.get("WEBGL_multi_draw");if(m===null)for(let f=0;f<h.length;f++)c(h[f]/a,p[f],S[f]);else{m.multiDrawElementsInstancedWEBGL(i,p,0,r,h,0,S,0,_);let f=0;for(let b=0;b<_;b++)f+=p[b]*S[b];e.update(f,i,1)}}this.setMode=s,this.setIndex=o,this.render=l,this.renderInstances=c,this.renderMultiDraw=u,this.renderMultiDrawInstances=d}function zm(n){const t={geometries:0,textures:0},e={frame:0,calls:0,triangles:0,points:0,lines:0};function i(r,a,o){switch(e.calls++,a){case n.TRIANGLES:e.triangles+=o*(r/3);break;case n.LINES:e.lines+=o*(r/2);break;case n.LINE_STRIP:e.lines+=o*(r-1);break;case n.LINE_LOOP:e.lines+=o*r;break;case n.POINTS:e.points+=o*r;break;default:console.error("THREE.WebGLInfo: Unknown draw mode:",a);break}}function s(){e.calls=0,e.triangles=0,e.points=0,e.lines=0}return{memory:t,render:e,programs:null,autoReset:!0,reset:s,update:i}}function km(n,t,e){const i=new WeakMap,s=new Kt;function r(a,o,l){const c=a.morphTargetInfluences,u=o.morphAttributes.position||o.morphAttributes.normal||o.morphAttributes.color,d=u!==void 0?u.length:0;let h=i.get(o);if(h===void 0||h.count!==d){let x=function(){I.dispose(),i.delete(o),o.removeEventListener("dispose",x)};var p=x;h!==void 0&&h.texture.dispose();const _=o.morphAttributes.position!==void 0,S=o.morphAttributes.normal!==void 0,m=o.morphAttributes.color!==void 0,f=o.morphAttributes.position||[],b=o.morphAttributes.normal||[],M=o.morphAttributes.color||[];let y=0;_===!0&&(y=1),S===!0&&(y=2),m===!0&&(y=3);let P=o.attributes.position.count*y,R=1;P>t.maxTextureSize&&(R=Math.ceil(P/t.maxTextureSize),P=t.maxTextureSize);const A=new Float32Array(P*R*4*d),I=new _u(A,P,R,d);I.type=Hn,I.needsUpdate=!0;const E=y*4;for(let C=0;C<d;C++){const V=f[C],z=b[C],Y=M[C],j=P*R*4*C;for(let X=0;X<V.count;X++){const Z=X*E;_===!0&&(s.fromBufferAttribute(V,X),A[j+Z+0]=s.x,A[j+Z+1]=s.y,A[j+Z+2]=s.z,A[j+Z+3]=0),S===!0&&(s.fromBufferAttribute(z,X),A[j+Z+4]=s.x,A[j+Z+5]=s.y,A[j+Z+6]=s.z,A[j+Z+7]=0),m===!0&&(s.fromBufferAttribute(Y,X),A[j+Z+8]=s.x,A[j+Z+9]=s.y,A[j+Z+10]=s.z,A[j+Z+11]=Y.itemSize===4?s.w:1)}}h={count:d,texture:I,size:new Tt(P,R)},i.set(o,h),o.addEventListener("dispose",x)}if(a.isInstancedMesh===!0&&a.morphTexture!==null)l.getUniforms().setValue(n,"morphTexture",a.morphTexture,e);else{let _=0;for(let m=0;m<c.length;m++)_+=c[m];const S=o.morphTargetsRelative?1:1-_;l.getUniforms().setValue(n,"morphTargetBaseInfluence",S),l.getUniforms().setValue(n,"morphTargetInfluences",c)}l.getUniforms().setValue(n,"morphTargetsTexture",h.texture,e),l.getUniforms().setValue(n,"morphTargetsTextureSize",h.size)}return{update:r}}function Hm(n,t,e,i){let s=new WeakMap;function r(l){const c=i.render.frame,u=l.geometry,d=t.get(l,u);if(s.get(d)!==c&&(t.update(d),s.set(d,c)),l.isInstancedMesh&&(l.hasEventListener("dispose",o)===!1&&l.addEventListener("dispose",o),s.get(l)!==c&&(e.update(l.instanceMatrix,n.ARRAY_BUFFER),l.instanceColor!==null&&e.update(l.instanceColor,n.ARRAY_BUFFER),s.set(l,c))),l.isSkinnedMesh){const h=l.skeleton;s.get(h)!==c&&(h.update(),s.set(h,c))}return d}function a(){s=new WeakMap}function o(l){const c=l.target;c.removeEventListener("dispose",o),e.remove(c.instanceMatrix),c.instanceColor!==null&&e.remove(c.instanceColor)}return{update:r,dispose:a}}const Cu=new Be,fc=new bu(1,1),Pu=new _u,Lu=new ch,Du=new Tu,pc=[],mc=[],gc=new Float32Array(16),_c=new Float32Array(9),vc=new Float32Array(4);function os(n,t,e){const i=n[0];if(i<=0||i>0)return n;const s=t*e;let r=pc[s];if(r===void 0&&(r=new Float32Array(s),pc[s]=r),t!==0){i.toArray(r,0);for(let a=1,o=0;a!==t;++a)o+=e,n[a].toArray(r,o)}return r}function pe(n,t){if(n.length!==t.length)return!1;for(let e=0,i=n.length;e<i;e++)if(n[e]!==t[e])return!1;return!0}function me(n,t){for(let e=0,i=t.length;e<i;e++)n[e]=t[e]}function Qr(n,t){let e=mc[t];e===void 0&&(e=new Int32Array(t),mc[t]=e);for(let i=0;i!==t;++i)e[i]=n.allocateTextureUnit();return e}function Vm(n,t){const e=this.cache;e[0]!==t&&(n.uniform1f(this.addr,t),e[0]=t)}function Gm(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(n.uniform2f(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(pe(e,t))return;n.uniform2fv(this.addr,t),me(e,t)}}function Wm(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(n.uniform3f(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else if(t.r!==void 0)(e[0]!==t.r||e[1]!==t.g||e[2]!==t.b)&&(n.uniform3f(this.addr,t.r,t.g,t.b),e[0]=t.r,e[1]=t.g,e[2]=t.b);else{if(pe(e,t))return;n.uniform3fv(this.addr,t),me(e,t)}}function Xm(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(n.uniform4f(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(pe(e,t))return;n.uniform4fv(this.addr,t),me(e,t)}}function $m(n,t){const e=this.cache,i=t.elements;if(i===void 0){if(pe(e,t))return;n.uniformMatrix2fv(this.addr,!1,t),me(e,t)}else{if(pe(e,i))return;vc.set(i),n.uniformMatrix2fv(this.addr,!1,vc),me(e,i)}}function qm(n,t){const e=this.cache,i=t.elements;if(i===void 0){if(pe(e,t))return;n.uniformMatrix3fv(this.addr,!1,t),me(e,t)}else{if(pe(e,i))return;_c.set(i),n.uniformMatrix3fv(this.addr,!1,_c),me(e,i)}}function Ym(n,t){const e=this.cache,i=t.elements;if(i===void 0){if(pe(e,t))return;n.uniformMatrix4fv(this.addr,!1,t),me(e,t)}else{if(pe(e,i))return;gc.set(i),n.uniformMatrix4fv(this.addr,!1,gc),me(e,i)}}function jm(n,t){const e=this.cache;e[0]!==t&&(n.uniform1i(this.addr,t),e[0]=t)}function Km(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(n.uniform2i(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(pe(e,t))return;n.uniform2iv(this.addr,t),me(e,t)}}function Zm(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(n.uniform3i(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(pe(e,t))return;n.uniform3iv(this.addr,t),me(e,t)}}function Jm(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(n.uniform4i(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(pe(e,t))return;n.uniform4iv(this.addr,t),me(e,t)}}function Qm(n,t){const e=this.cache;e[0]!==t&&(n.uniform1ui(this.addr,t),e[0]=t)}function tg(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(n.uniform2ui(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(pe(e,t))return;n.uniform2uiv(this.addr,t),me(e,t)}}function eg(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(n.uniform3ui(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(pe(e,t))return;n.uniform3uiv(this.addr,t),me(e,t)}}function ng(n,t){const e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(n.uniform4ui(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(pe(e,t))return;n.uniform4uiv(this.addr,t),me(e,t)}}function ig(n,t,e){const i=this.cache,s=e.allocateTextureUnit();i[0]!==s&&(n.uniform1i(this.addr,s),i[0]=s);let r;this.type===n.SAMPLER_2D_SHADOW?(fc.compareFunction=mu,r=fc):r=Cu,e.setTexture2D(t||r,s)}function sg(n,t,e){const i=this.cache,s=e.allocateTextureUnit();i[0]!==s&&(n.uniform1i(this.addr,s),i[0]=s),e.setTexture3D(t||Lu,s)}function rg(n,t,e){const i=this.cache,s=e.allocateTextureUnit();i[0]!==s&&(n.uniform1i(this.addr,s),i[0]=s),e.setTextureCube(t||Du,s)}function ag(n,t,e){const i=this.cache,s=e.allocateTextureUnit();i[0]!==s&&(n.uniform1i(this.addr,s),i[0]=s),e.setTexture2DArray(t||Pu,s)}function og(n){switch(n){case 5126:return Vm;case 35664:return Gm;case 35665:return Wm;case 35666:return Xm;case 35674:return $m;case 35675:return qm;case 35676:return Ym;case 5124:case 35670:return jm;case 35667:case 35671:return Km;case 35668:case 35672:return Zm;case 35669:case 35673:return Jm;case 5125:return Qm;case 36294:return tg;case 36295:return eg;case 36296:return ng;case 35678:case 36198:case 36298:case 36306:case 35682:return ig;case 35679:case 36299:case 36307:return sg;case 35680:case 36300:case 36308:case 36293:return rg;case 36289:case 36303:case 36311:case 36292:return ag}}function lg(n,t){n.uniform1fv(this.addr,t)}function cg(n,t){const e=os(t,this.size,2);n.uniform2fv(this.addr,e)}function ug(n,t){const e=os(t,this.size,3);n.uniform3fv(this.addr,e)}function dg(n,t){const e=os(t,this.size,4);n.uniform4fv(this.addr,e)}function hg(n,t){const e=os(t,this.size,4);n.uniformMatrix2fv(this.addr,!1,e)}function fg(n,t){const e=os(t,this.size,9);n.uniformMatrix3fv(this.addr,!1,e)}function pg(n,t){const e=os(t,this.size,16);n.uniformMatrix4fv(this.addr,!1,e)}function mg(n,t){n.uniform1iv(this.addr,t)}function gg(n,t){n.uniform2iv(this.addr,t)}function _g(n,t){n.uniform3iv(this.addr,t)}function vg(n,t){n.uniform4iv(this.addr,t)}function xg(n,t){n.uniform1uiv(this.addr,t)}function Sg(n,t){n.uniform2uiv(this.addr,t)}function yg(n,t){n.uniform3uiv(this.addr,t)}function Eg(n,t){n.uniform4uiv(this.addr,t)}function Mg(n,t,e){const i=this.cache,s=t.length,r=Qr(e,s);pe(i,r)||(n.uniform1iv(this.addr,r),me(i,r));for(let a=0;a!==s;++a)e.setTexture2D(t[a]||Cu,r[a])}function Tg(n,t,e){const i=this.cache,s=t.length,r=Qr(e,s);pe(i,r)||(n.uniform1iv(this.addr,r),me(i,r));for(let a=0;a!==s;++a)e.setTexture3D(t[a]||Lu,r[a])}function bg(n,t,e){const i=this.cache,s=t.length,r=Qr(e,s);pe(i,r)||(n.uniform1iv(this.addr,r),me(i,r));for(let a=0;a!==s;++a)e.setTextureCube(t[a]||Du,r[a])}function Ag(n,t,e){const i=this.cache,s=t.length,r=Qr(e,s);pe(i,r)||(n.uniform1iv(this.addr,r),me(i,r));for(let a=0;a!==s;++a)e.setTexture2DArray(t[a]||Pu,r[a])}function wg(n){switch(n){case 5126:return lg;case 35664:return cg;case 35665:return ug;case 35666:return dg;case 35674:return hg;case 35675:return fg;case 35676:return pg;case 5124:case 35670:return mg;case 35667:case 35671:return gg;case 35668:case 35672:return _g;case 35669:case 35673:return vg;case 5125:return xg;case 36294:return Sg;case 36295:return yg;case 36296:return Eg;case 35678:case 36198:case 36298:case 36306:case 35682:return Mg;case 35679:case 36299:case 36307:return Tg;case 35680:case 36300:case 36308:case 36293:return bg;case 36289:case 36303:case 36311:case 36292:return Ag}}class Rg{constructor(t,e,i){this.id=t,this.addr=i,this.cache=[],this.type=e.type,this.setValue=og(e.type)}}class Cg{constructor(t,e,i){this.id=t,this.addr=i,this.cache=[],this.type=e.type,this.size=e.size,this.setValue=wg(e.type)}}class Pg{constructor(t){this.id=t,this.seq=[],this.map={}}setValue(t,e,i){const s=this.seq;for(let r=0,a=s.length;r!==a;++r){const o=s[r];o.setValue(t,e[o.id],i)}}}const Fa=/(\w+)(\])?(\[|\.)?/g;function xc(n,t){n.seq.push(t),n.map[t.id]=t}function Lg(n,t,e){const i=n.name,s=i.length;for(Fa.lastIndex=0;;){const r=Fa.exec(i),a=Fa.lastIndex;let o=r[1];const l=r[2]==="]",c=r[3];if(l&&(o=o|0),c===void 0||c==="["&&a+2===s){xc(e,c===void 0?new Rg(o,n,t):new Cg(o,n,t));break}else{let d=e.map[o];d===void 0&&(d=new Pg(o),xc(e,d)),e=d}}}class Dr{constructor(t,e){this.seq=[],this.map={};const i=t.getProgramParameter(e,t.ACTIVE_UNIFORMS);for(let s=0;s<i;++s){const r=t.getActiveUniform(e,s),a=t.getUniformLocation(e,r.name);Lg(r,a,this)}}setValue(t,e,i,s){const r=this.map[e];r!==void 0&&r.setValue(t,i,s)}setOptional(t,e,i){const s=e[i];s!==void 0&&this.setValue(t,i,s)}static upload(t,e,i,s){for(let r=0,a=e.length;r!==a;++r){const o=e[r],l=i[o.id];l.needsUpdate!==!1&&o.setValue(t,l.value,s)}}static seqWithValue(t,e){const i=[];for(let s=0,r=t.length;s!==r;++s){const a=t[s];a.id in e&&i.push(a)}return i}}function Sc(n,t,e){const i=n.createShader(t);return n.shaderSource(i,e),n.compileShader(i),i}const Dg=37297;let Ig=0;function Ug(n,t){const e=n.split(`
`),i=[],s=Math.max(t-6,0),r=Math.min(t+6,e.length);for(let a=s;a<r;a++){const o=a+1;i.push(`${o===t?">":" "} ${o}: ${e[a]}`)}return i.join(`
`)}const yc=new Pt;function Ng(n){Gt._getMatrix(yc,Gt.workingColorSpace,n);const t=`mat3( ${yc.elements.map(e=>e.toFixed(4))} )`;switch(Gt.getTransfer(n)){case Br:return[t,"LinearTransferOETF"];case Yt:return[t,"sRGBTransferOETF"];default:return console.warn("THREE.WebGLProgram: Unsupported color space: ",n),[t,"LinearTransferOETF"]}}function Ec(n,t,e){const i=n.getShaderParameter(t,n.COMPILE_STATUS),s=n.getShaderInfoLog(t).trim();if(i&&s==="")return"";const r=/ERROR: 0:(\d+)/.exec(s);if(r){const a=parseInt(r[1]);return e.toUpperCase()+`

`+s+`

`+Ug(n.getShaderSource(t),a)}else return s}function Og(n,t){const e=Ng(t);return[`vec4 ${n}( vec4 value ) {`,`	return ${e[1]}( vec4( value.rgb * ${e[0]}, value.a ) );`,"}"].join(`
`)}function Fg(n,t){let e;switch(t){case Id:e="Linear";break;case Ud:e="Reinhard";break;case Nd:e="Cineon";break;case Od:e="ACESFilmic";break;case Bd:e="AgX";break;case zd:e="Neutral";break;case Fd:e="Custom";break;default:console.warn("THREE.WebGLProgram: Unsupported toneMapping:",t),e="Linear"}return"vec3 "+n+"( vec3 color ) { return "+e+"ToneMapping( color ); }"}const gr=new L;function Bg(){Gt.getLuminanceCoefficients(gr);const n=gr.x.toFixed(4),t=gr.y.toFixed(4),e=gr.z.toFixed(4);return["float luminance( const in vec3 rgb ) {",`	const vec3 weights = vec3( ${n}, ${t}, ${e} );`,"	return dot( weights, rgb );","}"].join(`
`)}function zg(n){return[n.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":"",n.extensionMultiDraw?"#extension GL_ANGLE_multi_draw : require":""].filter(Ss).join(`
`)}function kg(n){const t=[];for(const e in n){const i=n[e];i!==!1&&t.push("#define "+e+" "+i)}return t.join(`
`)}function Hg(n,t){const e={},i=n.getProgramParameter(t,n.ACTIVE_ATTRIBUTES);for(let s=0;s<i;s++){const r=n.getActiveAttrib(t,s),a=r.name;let o=1;r.type===n.FLOAT_MAT2&&(o=2),r.type===n.FLOAT_MAT3&&(o=3),r.type===n.FLOAT_MAT4&&(o=4),e[a]={type:r.type,location:n.getAttribLocation(t,a),locationSize:o}}return e}function Ss(n){return n!==""}function Mc(n,t){const e=t.numSpotLightShadows+t.numSpotLightMaps-t.numSpotLightShadowsWithMaps;return n.replace(/NUM_DIR_LIGHTS/g,t.numDirLights).replace(/NUM_SPOT_LIGHTS/g,t.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,t.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,e).replace(/NUM_RECT_AREA_LIGHTS/g,t.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,t.numPointLights).replace(/NUM_HEMI_LIGHTS/g,t.numHemiLights).replace(/NUM_DIR_LIGHT_SHADOWS/g,t.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,t.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,t.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,t.numPointLightShadows)}function Tc(n,t){return n.replace(/NUM_CLIPPING_PLANES/g,t.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,t.numClippingPlanes-t.numClipIntersection)}const Vg=/^[ \t]*#include +<([\w\d./]+)>/gm;function Ho(n){return n.replace(Vg,Wg)}const Gg=new Map;function Wg(n,t){let e=Dt[t];if(e===void 0){const i=Gg.get(t);if(i!==void 0)e=Dt[i],console.warn('THREE.WebGLRenderer: Shader chunk "%s" has been deprecated. Use "%s" instead.',t,i);else throw new Error("Can not resolve #include <"+t+">")}return Ho(e)}const Xg=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function bc(n){return n.replace(Xg,$g)}function $g(n,t,e,i){let s="";for(let r=parseInt(t);r<parseInt(e);r++)s+=i.replace(/\[\s*i\s*\]/g,"[ "+r+" ]").replace(/UNROLLED_LOOP_INDEX/g,r);return s}function Ac(n){let t=`precision ${n.precision} float;
	precision ${n.precision} int;
	precision ${n.precision} sampler2D;
	precision ${n.precision} samplerCube;
	precision ${n.precision} sampler3D;
	precision ${n.precision} sampler2DArray;
	precision ${n.precision} sampler2DShadow;
	precision ${n.precision} samplerCubeShadow;
	precision ${n.precision} sampler2DArrayShadow;
	precision ${n.precision} isampler2D;
	precision ${n.precision} isampler3D;
	precision ${n.precision} isamplerCube;
	precision ${n.precision} isampler2DArray;
	precision ${n.precision} usampler2D;
	precision ${n.precision} usampler3D;
	precision ${n.precision} usamplerCube;
	precision ${n.precision} usampler2DArray;
	`;return n.precision==="highp"?t+=`
#define HIGH_PRECISION`:n.precision==="mediump"?t+=`
#define MEDIUM_PRECISION`:n.precision==="lowp"&&(t+=`
#define LOW_PRECISION`),t}function qg(n){let t="SHADOWMAP_TYPE_BASIC";return n.shadowMapType===nu?t="SHADOWMAP_TYPE_PCF":n.shadowMapType===hd?t="SHADOWMAP_TYPE_PCF_SOFT":n.shadowMapType===Bn&&(t="SHADOWMAP_TYPE_VSM"),t}function Yg(n){let t="ENVMAP_TYPE_CUBE";if(n.envMap)switch(n.envMapMode){case ns:case is:t="ENVMAP_TYPE_CUBE";break;case jr:t="ENVMAP_TYPE_CUBE_UV";break}return t}function jg(n){let t="ENVMAP_MODE_REFLECTION";return n.envMap&&n.envMapMode===is&&(t="ENVMAP_MODE_REFRACTION"),t}function Kg(n){let t="ENVMAP_BLENDING_NONE";if(n.envMap)switch(n.combine){case iu:t="ENVMAP_BLENDING_MULTIPLY";break;case Ld:t="ENVMAP_BLENDING_MIX";break;case Dd:t="ENVMAP_BLENDING_ADD";break}return t}function Zg(n){const t=n.envMapCubeUVHeight;if(t===null)return null;const e=Math.log2(t)-2,i=1/t;return{texelWidth:1/(3*Math.max(Math.pow(2,e),112)),texelHeight:i,maxMip:e}}function Jg(n,t,e,i){const s=n.getContext(),r=e.defines;let a=e.vertexShader,o=e.fragmentShader;const l=qg(e),c=Yg(e),u=jg(e),d=Kg(e),h=Zg(e),p=zg(e),_=kg(r),S=s.createProgram();let m,f,b=e.glslVersion?"#version "+e.glslVersion+`
`:"";e.isRawShaderMaterial?(m=["#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,_].filter(Ss).join(`
`),m.length>0&&(m+=`
`),f=["#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,_].filter(Ss).join(`
`),f.length>0&&(f+=`
`)):(m=[Ac(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,_,e.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",e.batching?"#define USE_BATCHING":"",e.batchingColor?"#define USE_BATCHING_COLOR":"",e.instancing?"#define USE_INSTANCING":"",e.instancingColor?"#define USE_INSTANCING_COLOR":"",e.instancingMorph?"#define USE_INSTANCING_MORPH":"",e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.map?"#define USE_MAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+u:"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.displacementMap?"#define USE_DISPLACEMENTMAP":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.mapUv?"#define MAP_UV "+e.mapUv:"",e.alphaMapUv?"#define ALPHAMAP_UV "+e.alphaMapUv:"",e.lightMapUv?"#define LIGHTMAP_UV "+e.lightMapUv:"",e.aoMapUv?"#define AOMAP_UV "+e.aoMapUv:"",e.emissiveMapUv?"#define EMISSIVEMAP_UV "+e.emissiveMapUv:"",e.bumpMapUv?"#define BUMPMAP_UV "+e.bumpMapUv:"",e.normalMapUv?"#define NORMALMAP_UV "+e.normalMapUv:"",e.displacementMapUv?"#define DISPLACEMENTMAP_UV "+e.displacementMapUv:"",e.metalnessMapUv?"#define METALNESSMAP_UV "+e.metalnessMapUv:"",e.roughnessMapUv?"#define ROUGHNESSMAP_UV "+e.roughnessMapUv:"",e.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+e.anisotropyMapUv:"",e.clearcoatMapUv?"#define CLEARCOATMAP_UV "+e.clearcoatMapUv:"",e.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+e.clearcoatNormalMapUv:"",e.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+e.clearcoatRoughnessMapUv:"",e.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+e.iridescenceMapUv:"",e.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+e.iridescenceThicknessMapUv:"",e.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+e.sheenColorMapUv:"",e.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+e.sheenRoughnessMapUv:"",e.specularMapUv?"#define SPECULARMAP_UV "+e.specularMapUv:"",e.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+e.specularColorMapUv:"",e.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+e.specularIntensityMapUv:"",e.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+e.transmissionMapUv:"",e.thicknessMapUv?"#define THICKNESSMAP_UV "+e.thicknessMapUv:"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.flatShading?"#define FLAT_SHADED":"",e.skinning?"#define USE_SKINNING":"",e.morphTargets?"#define USE_MORPHTARGETS":"",e.morphNormals&&e.flatShading===!1?"#define USE_MORPHNORMALS":"",e.morphColors?"#define USE_MORPHCOLORS":"",e.morphTargetsCount>0?"#define MORPHTARGETS_TEXTURE_STRIDE "+e.morphTextureStride:"",e.morphTargetsCount>0?"#define MORPHTARGETS_COUNT "+e.morphTargetsCount:"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+l:"",e.sizeAttenuation?"#define USE_SIZEATTENUATION":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",e.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","#ifdef USE_INSTANCING_MORPH","	uniform sampler2D morphTexture;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(Ss).join(`
`),f=[Ac(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,_,e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.alphaToCoverage?"#define ALPHA_TO_COVERAGE":"",e.map?"#define USE_MAP":"",e.matcap?"#define USE_MATCAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+c:"",e.envMap?"#define "+u:"",e.envMap?"#define "+d:"",h?"#define CUBEUV_TEXEL_WIDTH "+h.texelWidth:"",h?"#define CUBEUV_TEXEL_HEIGHT "+h.texelHeight:"",h?"#define CUBEUV_MAX_MIP "+h.maxMip+".0":"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoat?"#define USE_CLEARCOAT":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.dispersion?"#define USE_DISPERSION":"",e.iridescence?"#define USE_IRIDESCENCE":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaTest?"#define USE_ALPHATEST":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.sheen?"#define USE_SHEEN":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors||e.instancingColor||e.batchingColor?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.gradientMap?"#define USE_GRADIENTMAP":"",e.flatShading?"#define FLAT_SHADED":"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+l:"",e.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",e.decodeVideoTextureEmissive?"#define DECODE_VIDEO_TEXTURE_EMISSIVE":"",e.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",e.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",e.toneMapping!==ai?"#define TONE_MAPPING":"",e.toneMapping!==ai?Dt.tonemapping_pars_fragment:"",e.toneMapping!==ai?Fg("toneMapping",e.toneMapping):"",e.dithering?"#define DITHERING":"",e.opaque?"#define OPAQUE":"",Dt.colorspace_pars_fragment,Og("linearToOutputTexel",e.outputColorSpace),Bg(),e.useDepthPacking?"#define DEPTH_PACKING "+e.depthPacking:"",`
`].filter(Ss).join(`
`)),a=Ho(a),a=Mc(a,e),a=Tc(a,e),o=Ho(o),o=Mc(o,e),o=Tc(o,e),a=bc(a),o=bc(o),e.isRawShaderMaterial!==!0&&(b=`#version 300 es
`,m=[p,"#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+m,f=["#define varying in",e.glslVersion===Dl?"":"layout(location = 0) out highp vec4 pc_fragColor;",e.glslVersion===Dl?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+f);const M=b+m+a,y=b+f+o,P=Sc(s,s.VERTEX_SHADER,M),R=Sc(s,s.FRAGMENT_SHADER,y);s.attachShader(S,P),s.attachShader(S,R),e.index0AttributeName!==void 0?s.bindAttribLocation(S,0,e.index0AttributeName):e.morphTargets===!0&&s.bindAttribLocation(S,0,"position"),s.linkProgram(S);function A(C){if(n.debug.checkShaderErrors){const V=s.getProgramInfoLog(S).trim(),z=s.getShaderInfoLog(P).trim(),Y=s.getShaderInfoLog(R).trim();let j=!0,X=!0;if(s.getProgramParameter(S,s.LINK_STATUS)===!1)if(j=!1,typeof n.debug.onShaderError=="function")n.debug.onShaderError(s,S,P,R);else{const Z=Ec(s,P,"vertex"),H=Ec(s,R,"fragment");console.error("THREE.WebGLProgram: Shader Error "+s.getError()+" - VALIDATE_STATUS "+s.getProgramParameter(S,s.VALIDATE_STATUS)+`

Material Name: `+C.name+`
Material Type: `+C.type+`

Program Info Log: `+V+`
`+Z+`
`+H)}else V!==""?console.warn("THREE.WebGLProgram: Program Info Log:",V):(z===""||Y==="")&&(X=!1);X&&(C.diagnostics={runnable:j,programLog:V,vertexShader:{log:z,prefix:m},fragmentShader:{log:Y,prefix:f}})}s.deleteShader(P),s.deleteShader(R),I=new Dr(s,S),E=Hg(s,S)}let I;this.getUniforms=function(){return I===void 0&&A(this),I};let E;this.getAttributes=function(){return E===void 0&&A(this),E};let x=e.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return x===!1&&(x=s.getProgramParameter(S,Dg)),x},this.destroy=function(){i.releaseStatesOfProgram(this),s.deleteProgram(S),this.program=void 0},this.type=e.shaderType,this.name=e.shaderName,this.id=Ig++,this.cacheKey=t,this.usedTimes=1,this.program=S,this.vertexShader=P,this.fragmentShader=R,this}let Qg=0;class t_{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(t){const e=t.vertexShader,i=t.fragmentShader,s=this._getShaderStage(e),r=this._getShaderStage(i),a=this._getShaderCacheForMaterial(t);return a.has(s)===!1&&(a.add(s),s.usedTimes++),a.has(r)===!1&&(a.add(r),r.usedTimes++),this}remove(t){const e=this.materialCache.get(t);for(const i of e)i.usedTimes--,i.usedTimes===0&&this.shaderCache.delete(i.code);return this.materialCache.delete(t),this}getVertexShaderID(t){return this._getShaderStage(t.vertexShader).id}getFragmentShaderID(t){return this._getShaderStage(t.fragmentShader).id}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(t){const e=this.materialCache;let i=e.get(t);return i===void 0&&(i=new Set,e.set(t,i)),i}_getShaderStage(t){const e=this.shaderCache;let i=e.get(t);return i===void 0&&(i=new e_(t),e.set(t,i)),i}}class e_{constructor(t){this.id=Qg++,this.code=t,this.usedTimes=0}}function n_(n,t,e,i,s,r,a){const o=new rl,l=new t_,c=new Set,u=[],d=s.logarithmicDepthBuffer,h=s.vertexTextures;let p=s.precision;const _={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distanceRGBA",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function S(E){return c.add(E),E===0?"uv":`uv${E}`}function m(E,x,C,V,z){const Y=V.fog,j=z.geometry,X=E.isMeshStandardMaterial?V.environment:null,Z=(E.isMeshStandardMaterial?e:t).get(E.envMap||X),H=Z&&Z.mapping===jr?Z.image.height:null,it=_[E.type];E.precision!==null&&(p=s.getMaxPrecision(E.precision),p!==E.precision&&console.warn("THREE.WebGLProgram.getParameters:",E.precision,"not supported, using",p,"instead."));const ut=j.morphAttributes.position||j.morphAttributes.normal||j.morphAttributes.color,vt=ut!==void 0?ut.length:0;let Ut=0;j.morphAttributes.position!==void 0&&(Ut=1),j.morphAttributes.normal!==void 0&&(Ut=2),j.morphAttributes.color!==void 0&&(Ut=3);let Zt,W,tt,mt;if(it){const qt=En[it];Zt=qt.vertexShader,W=qt.fragmentShader}else Zt=E.vertexShader,W=E.fragmentShader,l.update(E),tt=l.getVertexShaderID(E),mt=l.getFragmentShaderID(E);const st=n.getRenderTarget(),Et=n.state.buffers.depth.getReversed(),Wt=z.isInstancedMesh===!0,bt=z.isBatchedMesh===!0,oe=!!E.map,ne=!!E.matcap,Ot=!!Z,w=!!E.aoMap,qe=!!E.lightMap,zt=!!E.bumpMap,Ft=!!E.normalMap,xt=!!E.displacementMap,Qt=!!E.emissiveMap,_t=!!E.metalnessMap,T=!!E.roughnessMap,g=E.anisotropy>0,O=E.clearcoat>0,$=E.dispersion>0,K=E.iridescence>0,G=E.sheen>0,gt=E.transmission>0,rt=g&&!!E.anisotropyMap,dt=O&&!!E.clearcoatMap,kt=O&&!!E.clearcoatNormalMap,Q=O&&!!E.clearcoatRoughnessMap,ht=K&&!!E.iridescenceMap,Mt=K&&!!E.iridescenceThicknessMap,wt=G&&!!E.sheenColorMap,ft=G&&!!E.sheenRoughnessMap,Bt=!!E.specularMap,Lt=!!E.specularColorMap,Jt=!!E.specularIntensityMap,D=gt&&!!E.transmissionMap,at=gt&&!!E.thicknessMap,k=!!E.gradientMap,q=!!E.alphaMap,lt=E.alphaTest>0,ot=!!E.alphaHash,Ct=!!E.extensions;let se=ai;E.toneMapped&&(st===null||st.isXRRenderTarget===!0)&&(se=n.toneMapping);const be={shaderID:it,shaderType:E.type,shaderName:E.name,vertexShader:Zt,fragmentShader:W,defines:E.defines,customVertexShaderID:tt,customFragmentShaderID:mt,isRawShaderMaterial:E.isRawShaderMaterial===!0,glslVersion:E.glslVersion,precision:p,batching:bt,batchingColor:bt&&z._colorsTexture!==null,instancing:Wt,instancingColor:Wt&&z.instanceColor!==null,instancingMorph:Wt&&z.morphTexture!==null,supportsVertexTextures:h,outputColorSpace:st===null?n.outputColorSpace:st.isXRRenderTarget===!0?st.texture.colorSpace:ss,alphaToCoverage:!!E.alphaToCoverage,map:oe,matcap:ne,envMap:Ot,envMapMode:Ot&&Z.mapping,envMapCubeUVHeight:H,aoMap:w,lightMap:qe,bumpMap:zt,normalMap:Ft,displacementMap:h&&xt,emissiveMap:Qt,normalMapObjectSpace:Ft&&E.normalMapType===Wd,normalMapTangentSpace:Ft&&E.normalMapType===Gd,metalnessMap:_t,roughnessMap:T,anisotropy:g,anisotropyMap:rt,clearcoat:O,clearcoatMap:dt,clearcoatNormalMap:kt,clearcoatRoughnessMap:Q,dispersion:$,iridescence:K,iridescenceMap:ht,iridescenceThicknessMap:Mt,sheen:G,sheenColorMap:wt,sheenRoughnessMap:ft,specularMap:Bt,specularColorMap:Lt,specularIntensityMap:Jt,transmission:gt,transmissionMap:D,thicknessMap:at,gradientMap:k,opaque:E.transparent===!1&&E.blending===Ki&&E.alphaToCoverage===!1,alphaMap:q,alphaTest:lt,alphaHash:ot,combine:E.combine,mapUv:oe&&S(E.map.channel),aoMapUv:w&&S(E.aoMap.channel),lightMapUv:qe&&S(E.lightMap.channel),bumpMapUv:zt&&S(E.bumpMap.channel),normalMapUv:Ft&&S(E.normalMap.channel),displacementMapUv:xt&&S(E.displacementMap.channel),emissiveMapUv:Qt&&S(E.emissiveMap.channel),metalnessMapUv:_t&&S(E.metalnessMap.channel),roughnessMapUv:T&&S(E.roughnessMap.channel),anisotropyMapUv:rt&&S(E.anisotropyMap.channel),clearcoatMapUv:dt&&S(E.clearcoatMap.channel),clearcoatNormalMapUv:kt&&S(E.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:Q&&S(E.clearcoatRoughnessMap.channel),iridescenceMapUv:ht&&S(E.iridescenceMap.channel),iridescenceThicknessMapUv:Mt&&S(E.iridescenceThicknessMap.channel),sheenColorMapUv:wt&&S(E.sheenColorMap.channel),sheenRoughnessMapUv:ft&&S(E.sheenRoughnessMap.channel),specularMapUv:Bt&&S(E.specularMap.channel),specularColorMapUv:Lt&&S(E.specularColorMap.channel),specularIntensityMapUv:Jt&&S(E.specularIntensityMap.channel),transmissionMapUv:D&&S(E.transmissionMap.channel),thicknessMapUv:at&&S(E.thicknessMap.channel),alphaMapUv:q&&S(E.alphaMap.channel),vertexTangents:!!j.attributes.tangent&&(Ft||g),vertexColors:E.vertexColors,vertexAlphas:E.vertexColors===!0&&!!j.attributes.color&&j.attributes.color.itemSize===4,pointsUvs:z.isPoints===!0&&!!j.attributes.uv&&(oe||q),fog:!!Y,useFog:E.fog===!0,fogExp2:!!Y&&Y.isFogExp2,flatShading:E.flatShading===!0,sizeAttenuation:E.sizeAttenuation===!0,logarithmicDepthBuffer:d,reverseDepthBuffer:Et,skinning:z.isSkinnedMesh===!0,morphTargets:j.morphAttributes.position!==void 0,morphNormals:j.morphAttributes.normal!==void 0,morphColors:j.morphAttributes.color!==void 0,morphTargetsCount:vt,morphTextureStride:Ut,numDirLights:x.directional.length,numPointLights:x.point.length,numSpotLights:x.spot.length,numSpotLightMaps:x.spotLightMap.length,numRectAreaLights:x.rectArea.length,numHemiLights:x.hemi.length,numDirLightShadows:x.directionalShadowMap.length,numPointLightShadows:x.pointShadowMap.length,numSpotLightShadows:x.spotShadowMap.length,numSpotLightShadowsWithMaps:x.numSpotLightShadowsWithMaps,numLightProbes:x.numLightProbes,numClippingPlanes:a.numPlanes,numClipIntersection:a.numIntersection,dithering:E.dithering,shadowMapEnabled:n.shadowMap.enabled&&C.length>0,shadowMapType:n.shadowMap.type,toneMapping:se,decodeVideoTexture:oe&&E.map.isVideoTexture===!0&&Gt.getTransfer(E.map.colorSpace)===Yt,decodeVideoTextureEmissive:Qt&&E.emissiveMap.isVideoTexture===!0&&Gt.getTransfer(E.emissiveMap.colorSpace)===Yt,premultipliedAlpha:E.premultipliedAlpha,doubleSided:E.side===zn,flipSided:E.side===Le,useDepthPacking:E.depthPacking>=0,depthPacking:E.depthPacking||0,index0AttributeName:E.index0AttributeName,extensionClipCullDistance:Ct&&E.extensions.clipCullDistance===!0&&i.has("WEBGL_clip_cull_distance"),extensionMultiDraw:(Ct&&E.extensions.multiDraw===!0||bt)&&i.has("WEBGL_multi_draw"),rendererExtensionParallelShaderCompile:i.has("KHR_parallel_shader_compile"),customProgramCacheKey:E.customProgramCacheKey()};return be.vertexUv1s=c.has(1),be.vertexUv2s=c.has(2),be.vertexUv3s=c.has(3),c.clear(),be}function f(E){const x=[];if(E.shaderID?x.push(E.shaderID):(x.push(E.customVertexShaderID),x.push(E.customFragmentShaderID)),E.defines!==void 0)for(const C in E.defines)x.push(C),x.push(E.defines[C]);return E.isRawShaderMaterial===!1&&(b(x,E),M(x,E),x.push(n.outputColorSpace)),x.push(E.customProgramCacheKey),x.join()}function b(E,x){E.push(x.precision),E.push(x.outputColorSpace),E.push(x.envMapMode),E.push(x.envMapCubeUVHeight),E.push(x.mapUv),E.push(x.alphaMapUv),E.push(x.lightMapUv),E.push(x.aoMapUv),E.push(x.bumpMapUv),E.push(x.normalMapUv),E.push(x.displacementMapUv),E.push(x.emissiveMapUv),E.push(x.metalnessMapUv),E.push(x.roughnessMapUv),E.push(x.anisotropyMapUv),E.push(x.clearcoatMapUv),E.push(x.clearcoatNormalMapUv),E.push(x.clearcoatRoughnessMapUv),E.push(x.iridescenceMapUv),E.push(x.iridescenceThicknessMapUv),E.push(x.sheenColorMapUv),E.push(x.sheenRoughnessMapUv),E.push(x.specularMapUv),E.push(x.specularColorMapUv),E.push(x.specularIntensityMapUv),E.push(x.transmissionMapUv),E.push(x.thicknessMapUv),E.push(x.combine),E.push(x.fogExp2),E.push(x.sizeAttenuation),E.push(x.morphTargetsCount),E.push(x.morphAttributeCount),E.push(x.numDirLights),E.push(x.numPointLights),E.push(x.numSpotLights),E.push(x.numSpotLightMaps),E.push(x.numHemiLights),E.push(x.numRectAreaLights),E.push(x.numDirLightShadows),E.push(x.numPointLightShadows),E.push(x.numSpotLightShadows),E.push(x.numSpotLightShadowsWithMaps),E.push(x.numLightProbes),E.push(x.shadowMapType),E.push(x.toneMapping),E.push(x.numClippingPlanes),E.push(x.numClipIntersection),E.push(x.depthPacking)}function M(E,x){o.disableAll(),x.supportsVertexTextures&&o.enable(0),x.instancing&&o.enable(1),x.instancingColor&&o.enable(2),x.instancingMorph&&o.enable(3),x.matcap&&o.enable(4),x.envMap&&o.enable(5),x.normalMapObjectSpace&&o.enable(6),x.normalMapTangentSpace&&o.enable(7),x.clearcoat&&o.enable(8),x.iridescence&&o.enable(9),x.alphaTest&&o.enable(10),x.vertexColors&&o.enable(11),x.vertexAlphas&&o.enable(12),x.vertexUv1s&&o.enable(13),x.vertexUv2s&&o.enable(14),x.vertexUv3s&&o.enable(15),x.vertexTangents&&o.enable(16),x.anisotropy&&o.enable(17),x.alphaHash&&o.enable(18),x.batching&&o.enable(19),x.dispersion&&o.enable(20),x.batchingColor&&o.enable(21),E.push(o.mask),o.disableAll(),x.fog&&o.enable(0),x.useFog&&o.enable(1),x.flatShading&&o.enable(2),x.logarithmicDepthBuffer&&o.enable(3),x.reverseDepthBuffer&&o.enable(4),x.skinning&&o.enable(5),x.morphTargets&&o.enable(6),x.morphNormals&&o.enable(7),x.morphColors&&o.enable(8),x.premultipliedAlpha&&o.enable(9),x.shadowMapEnabled&&o.enable(10),x.doubleSided&&o.enable(11),x.flipSided&&o.enable(12),x.useDepthPacking&&o.enable(13),x.dithering&&o.enable(14),x.transmission&&o.enable(15),x.sheen&&o.enable(16),x.opaque&&o.enable(17),x.pointsUvs&&o.enable(18),x.decodeVideoTexture&&o.enable(19),x.decodeVideoTextureEmissive&&o.enable(20),x.alphaToCoverage&&o.enable(21),E.push(o.mask)}function y(E){const x=_[E.type];let C;if(x){const V=En[x];C=Eh.clone(V.uniforms)}else C=E.uniforms;return C}function P(E,x){let C;for(let V=0,z=u.length;V<z;V++){const Y=u[V];if(Y.cacheKey===x){C=Y,++C.usedTimes;break}}return C===void 0&&(C=new Jg(n,x,E,r),u.push(C)),C}function R(E){if(--E.usedTimes===0){const x=u.indexOf(E);u[x]=u[u.length-1],u.pop(),E.destroy()}}function A(E){l.remove(E)}function I(){l.dispose()}return{getParameters:m,getProgramCacheKey:f,getUniforms:y,acquireProgram:P,releaseProgram:R,releaseShaderCache:A,programs:u,dispose:I}}function i_(){let n=new WeakMap;function t(a){return n.has(a)}function e(a){let o=n.get(a);return o===void 0&&(o={},n.set(a,o)),o}function i(a){n.delete(a)}function s(a,o,l){n.get(a)[o]=l}function r(){n=new WeakMap}return{has:t,get:e,remove:i,update:s,dispose:r}}function s_(n,t){return n.groupOrder!==t.groupOrder?n.groupOrder-t.groupOrder:n.renderOrder!==t.renderOrder?n.renderOrder-t.renderOrder:n.material.id!==t.material.id?n.material.id-t.material.id:n.z!==t.z?n.z-t.z:n.id-t.id}function wc(n,t){return n.groupOrder!==t.groupOrder?n.groupOrder-t.groupOrder:n.renderOrder!==t.renderOrder?n.renderOrder-t.renderOrder:n.z!==t.z?t.z-n.z:n.id-t.id}function Rc(){const n=[];let t=0;const e=[],i=[],s=[];function r(){t=0,e.length=0,i.length=0,s.length=0}function a(d,h,p,_,S,m){let f=n[t];return f===void 0?(f={id:d.id,object:d,geometry:h,material:p,groupOrder:_,renderOrder:d.renderOrder,z:S,group:m},n[t]=f):(f.id=d.id,f.object=d,f.geometry=h,f.material=p,f.groupOrder=_,f.renderOrder=d.renderOrder,f.z=S,f.group=m),t++,f}function o(d,h,p,_,S,m){const f=a(d,h,p,_,S,m);p.transmission>0?i.push(f):p.transparent===!0?s.push(f):e.push(f)}function l(d,h,p,_,S,m){const f=a(d,h,p,_,S,m);p.transmission>0?i.unshift(f):p.transparent===!0?s.unshift(f):e.unshift(f)}function c(d,h){e.length>1&&e.sort(d||s_),i.length>1&&i.sort(h||wc),s.length>1&&s.sort(h||wc)}function u(){for(let d=t,h=n.length;d<h;d++){const p=n[d];if(p.id===null)break;p.id=null,p.object=null,p.geometry=null,p.material=null,p.group=null}}return{opaque:e,transmissive:i,transparent:s,init:r,push:o,unshift:l,finish:u,sort:c}}function r_(){let n=new WeakMap;function t(i,s){const r=n.get(i);let a;return r===void 0?(a=new Rc,n.set(i,[a])):s>=r.length?(a=new Rc,r.push(a)):a=r[s],a}function e(){n=new WeakMap}return{get:t,dispose:e}}function a_(){const n={};return{get:function(t){if(n[t.id]!==void 0)return n[t.id];let e;switch(t.type){case"DirectionalLight":e={direction:new L,color:new It};break;case"SpotLight":e={position:new L,direction:new L,color:new It,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":e={position:new L,color:new It,distance:0,decay:0};break;case"HemisphereLight":e={direction:new L,skyColor:new It,groundColor:new It};break;case"RectAreaLight":e={color:new It,position:new L,halfWidth:new L,halfHeight:new L};break}return n[t.id]=e,e}}}function o_(){const n={};return{get:function(t){if(n[t.id]!==void 0)return n[t.id];let e;switch(t.type){case"DirectionalLight":e={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Tt};break;case"SpotLight":e={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Tt};break;case"PointLight":e={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Tt,shadowCameraNear:1,shadowCameraFar:1e3};break}return n[t.id]=e,e}}}let l_=0;function c_(n,t){return(t.castShadow?2:0)-(n.castShadow?2:0)+(t.map?1:0)-(n.map?1:0)}function u_(n){const t=new a_,e=o_(),i={version:0,hash:{directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let c=0;c<9;c++)i.probe.push(new L);const s=new L,r=new te,a=new te;function o(c){let u=0,d=0,h=0;for(let E=0;E<9;E++)i.probe[E].set(0,0,0);let p=0,_=0,S=0,m=0,f=0,b=0,M=0,y=0,P=0,R=0,A=0;c.sort(c_);for(let E=0,x=c.length;E<x;E++){const C=c[E],V=C.color,z=C.intensity,Y=C.distance,j=C.shadow&&C.shadow.map?C.shadow.map.texture:null;if(C.isAmbientLight)u+=V.r*z,d+=V.g*z,h+=V.b*z;else if(C.isLightProbe){for(let X=0;X<9;X++)i.probe[X].addScaledVector(C.sh.coefficients[X],z);A++}else if(C.isDirectionalLight){const X=t.get(C);if(X.color.copy(C.color).multiplyScalar(C.intensity),C.castShadow){const Z=C.shadow,H=e.get(C);H.shadowIntensity=Z.intensity,H.shadowBias=Z.bias,H.shadowNormalBias=Z.normalBias,H.shadowRadius=Z.radius,H.shadowMapSize=Z.mapSize,i.directionalShadow[p]=H,i.directionalShadowMap[p]=j,i.directionalShadowMatrix[p]=C.shadow.matrix,b++}i.directional[p]=X,p++}else if(C.isSpotLight){const X=t.get(C);X.position.setFromMatrixPosition(C.matrixWorld),X.color.copy(V).multiplyScalar(z),X.distance=Y,X.coneCos=Math.cos(C.angle),X.penumbraCos=Math.cos(C.angle*(1-C.penumbra)),X.decay=C.decay,i.spot[S]=X;const Z=C.shadow;if(C.map&&(i.spotLightMap[P]=C.map,P++,Z.updateMatrices(C),C.castShadow&&R++),i.spotLightMatrix[S]=Z.matrix,C.castShadow){const H=e.get(C);H.shadowIntensity=Z.intensity,H.shadowBias=Z.bias,H.shadowNormalBias=Z.normalBias,H.shadowRadius=Z.radius,H.shadowMapSize=Z.mapSize,i.spotShadow[S]=H,i.spotShadowMap[S]=j,y++}S++}else if(C.isRectAreaLight){const X=t.get(C);X.color.copy(V).multiplyScalar(z),X.halfWidth.set(C.width*.5,0,0),X.halfHeight.set(0,C.height*.5,0),i.rectArea[m]=X,m++}else if(C.isPointLight){const X=t.get(C);if(X.color.copy(C.color).multiplyScalar(C.intensity),X.distance=C.distance,X.decay=C.decay,C.castShadow){const Z=C.shadow,H=e.get(C);H.shadowIntensity=Z.intensity,H.shadowBias=Z.bias,H.shadowNormalBias=Z.normalBias,H.shadowRadius=Z.radius,H.shadowMapSize=Z.mapSize,H.shadowCameraNear=Z.camera.near,H.shadowCameraFar=Z.camera.far,i.pointShadow[_]=H,i.pointShadowMap[_]=j,i.pointShadowMatrix[_]=C.shadow.matrix,M++}i.point[_]=X,_++}else if(C.isHemisphereLight){const X=t.get(C);X.skyColor.copy(C.color).multiplyScalar(z),X.groundColor.copy(C.groundColor).multiplyScalar(z),i.hemi[f]=X,f++}}m>0&&(n.has("OES_texture_float_linear")===!0?(i.rectAreaLTC1=et.LTC_FLOAT_1,i.rectAreaLTC2=et.LTC_FLOAT_2):(i.rectAreaLTC1=et.LTC_HALF_1,i.rectAreaLTC2=et.LTC_HALF_2)),i.ambient[0]=u,i.ambient[1]=d,i.ambient[2]=h;const I=i.hash;(I.directionalLength!==p||I.pointLength!==_||I.spotLength!==S||I.rectAreaLength!==m||I.hemiLength!==f||I.numDirectionalShadows!==b||I.numPointShadows!==M||I.numSpotShadows!==y||I.numSpotMaps!==P||I.numLightProbes!==A)&&(i.directional.length=p,i.spot.length=S,i.rectArea.length=m,i.point.length=_,i.hemi.length=f,i.directionalShadow.length=b,i.directionalShadowMap.length=b,i.pointShadow.length=M,i.pointShadowMap.length=M,i.spotShadow.length=y,i.spotShadowMap.length=y,i.directionalShadowMatrix.length=b,i.pointShadowMatrix.length=M,i.spotLightMatrix.length=y+P-R,i.spotLightMap.length=P,i.numSpotLightShadowsWithMaps=R,i.numLightProbes=A,I.directionalLength=p,I.pointLength=_,I.spotLength=S,I.rectAreaLength=m,I.hemiLength=f,I.numDirectionalShadows=b,I.numPointShadows=M,I.numSpotShadows=y,I.numSpotMaps=P,I.numLightProbes=A,i.version=l_++)}function l(c,u){let d=0,h=0,p=0,_=0,S=0;const m=u.matrixWorldInverse;for(let f=0,b=c.length;f<b;f++){const M=c[f];if(M.isDirectionalLight){const y=i.directional[d];y.direction.setFromMatrixPosition(M.matrixWorld),s.setFromMatrixPosition(M.target.matrixWorld),y.direction.sub(s),y.direction.transformDirection(m),d++}else if(M.isSpotLight){const y=i.spot[p];y.position.setFromMatrixPosition(M.matrixWorld),y.position.applyMatrix4(m),y.direction.setFromMatrixPosition(M.matrixWorld),s.setFromMatrixPosition(M.target.matrixWorld),y.direction.sub(s),y.direction.transformDirection(m),p++}else if(M.isRectAreaLight){const y=i.rectArea[_];y.position.setFromMatrixPosition(M.matrixWorld),y.position.applyMatrix4(m),a.identity(),r.copy(M.matrixWorld),r.premultiply(m),a.extractRotation(r),y.halfWidth.set(M.width*.5,0,0),y.halfHeight.set(0,M.height*.5,0),y.halfWidth.applyMatrix4(a),y.halfHeight.applyMatrix4(a),_++}else if(M.isPointLight){const y=i.point[h];y.position.setFromMatrixPosition(M.matrixWorld),y.position.applyMatrix4(m),h++}else if(M.isHemisphereLight){const y=i.hemi[S];y.direction.setFromMatrixPosition(M.matrixWorld),y.direction.transformDirection(m),S++}}}return{setup:o,setupView:l,state:i}}function Cc(n){const t=new u_(n),e=[],i=[];function s(u){c.camera=u,e.length=0,i.length=0}function r(u){e.push(u)}function a(u){i.push(u)}function o(){t.setup(e)}function l(u){t.setupView(e,u)}const c={lightsArray:e,shadowsArray:i,camera:null,lights:t,transmissionRenderTarget:{}};return{init:s,state:c,setupLights:o,setupLightsView:l,pushLight:r,pushShadow:a}}function d_(n){let t=new WeakMap;function e(s,r=0){const a=t.get(s);let o;return a===void 0?(o=new Cc(n),t.set(s,[o])):r>=a.length?(o=new Cc(n),a.push(o)):o=a[r],o}function i(){t=new WeakMap}return{get:e,dispose:i}}const h_=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,f_=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
#include <packing>
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = unpackRGBATo2Half( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ) );
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = unpackRGBAToDepth( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ) );
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( squared_mean - mean * mean );
	gl_FragColor = pack2HalfToRGBA( vec2( mean, std_dev ) );
}`;function p_(n,t,e){let i=new ol;const s=new Tt,r=new Tt,a=new Kt,o=new Ih({depthPacking:Vd}),l=new Uh,c={},u=e.maxTextureSize,d={[oi]:Le,[Le]:oi,[zn]:zn},h=new _n({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new Tt},radius:{value:4}},vertexShader:h_,fragmentShader:f_}),p=h.clone();p.defines.HORIZONTAL_PASS=1;const _=new xn;_.setAttribute("position",new Xe(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));const S=new mn(_,h),m=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=nu;let f=this.type;this.render=function(R,A,I){if(m.enabled===!1||m.autoUpdate===!1&&m.needsUpdate===!1||R.length===0)return;const E=n.getRenderTarget(),x=n.getActiveCubeFace(),C=n.getActiveMipmapLevel(),V=n.state;V.setBlending(ri),V.buffers.color.setClear(1,1,1,1),V.buffers.depth.setTest(!0),V.setScissorTest(!1);const z=f!==Bn&&this.type===Bn,Y=f===Bn&&this.type!==Bn;for(let j=0,X=R.length;j<X;j++){const Z=R[j],H=Z.shadow;if(H===void 0){console.warn("THREE.WebGLShadowMap:",Z,"has no shadow.");continue}if(H.autoUpdate===!1&&H.needsUpdate===!1)continue;s.copy(H.mapSize);const it=H.getFrameExtents();if(s.multiply(it),r.copy(H.mapSize),(s.x>u||s.y>u)&&(s.x>u&&(r.x=Math.floor(u/it.x),s.x=r.x*it.x,H.mapSize.x=r.x),s.y>u&&(r.y=Math.floor(u/it.y),s.y=r.y*it.y,H.mapSize.y=r.y)),H.map===null||z===!0||Y===!0){const vt=this.type!==Bn?{minFilter:gn,magFilter:gn}:{};H.map!==null&&H.map.dispose(),H.map=new Ti(s.x,s.y,vt),H.map.texture.name=Z.name+".shadowMap",H.camera.updateProjectionMatrix()}n.setRenderTarget(H.map),n.clear();const ut=H.getViewportCount();for(let vt=0;vt<ut;vt++){const Ut=H.getViewport(vt);a.set(r.x*Ut.x,r.y*Ut.y,r.x*Ut.z,r.y*Ut.w),V.viewport(a),H.updateMatrices(Z,vt),i=H.getFrustum(),y(A,I,H.camera,Z,this.type)}H.isPointLightShadow!==!0&&this.type===Bn&&b(H,I),H.needsUpdate=!1}f=this.type,m.needsUpdate=!1,n.setRenderTarget(E,x,C)};function b(R,A){const I=t.update(S);h.defines.VSM_SAMPLES!==R.blurSamples&&(h.defines.VSM_SAMPLES=R.blurSamples,p.defines.VSM_SAMPLES=R.blurSamples,h.needsUpdate=!0,p.needsUpdate=!0),R.mapPass===null&&(R.mapPass=new Ti(s.x,s.y)),h.uniforms.shadow_pass.value=R.map.texture,h.uniforms.resolution.value=R.mapSize,h.uniforms.radius.value=R.radius,n.setRenderTarget(R.mapPass),n.clear(),n.renderBufferDirect(A,null,I,h,S,null),p.uniforms.shadow_pass.value=R.mapPass.texture,p.uniforms.resolution.value=R.mapSize,p.uniforms.radius.value=R.radius,n.setRenderTarget(R.map),n.clear(),n.renderBufferDirect(A,null,I,p,S,null)}function M(R,A,I,E){let x=null;const C=I.isPointLight===!0?R.customDistanceMaterial:R.customDepthMaterial;if(C!==void 0)x=C;else if(x=I.isPointLight===!0?l:o,n.localClippingEnabled&&A.clipShadows===!0&&Array.isArray(A.clippingPlanes)&&A.clippingPlanes.length!==0||A.displacementMap&&A.displacementScale!==0||A.alphaMap&&A.alphaTest>0||A.map&&A.alphaTest>0){const V=x.uuid,z=A.uuid;let Y=c[V];Y===void 0&&(Y={},c[V]=Y);let j=Y[z];j===void 0&&(j=x.clone(),Y[z]=j,A.addEventListener("dispose",P)),x=j}if(x.visible=A.visible,x.wireframe=A.wireframe,E===Bn?x.side=A.shadowSide!==null?A.shadowSide:A.side:x.side=A.shadowSide!==null?A.shadowSide:d[A.side],x.alphaMap=A.alphaMap,x.alphaTest=A.alphaTest,x.map=A.map,x.clipShadows=A.clipShadows,x.clippingPlanes=A.clippingPlanes,x.clipIntersection=A.clipIntersection,x.displacementMap=A.displacementMap,x.displacementScale=A.displacementScale,x.displacementBias=A.displacementBias,x.wireframeLinewidth=A.wireframeLinewidth,x.linewidth=A.linewidth,I.isPointLight===!0&&x.isMeshDistanceMaterial===!0){const V=n.properties.get(x);V.light=I}return x}function y(R,A,I,E,x){if(R.visible===!1)return;if(R.layers.test(A.layers)&&(R.isMesh||R.isLine||R.isPoints)&&(R.castShadow||R.receiveShadow&&x===Bn)&&(!R.frustumCulled||i.intersectsObject(R))){R.modelViewMatrix.multiplyMatrices(I.matrixWorldInverse,R.matrixWorld);const z=t.update(R),Y=R.material;if(Array.isArray(Y)){const j=z.groups;for(let X=0,Z=j.length;X<Z;X++){const H=j[X],it=Y[H.materialIndex];if(it&&it.visible){const ut=M(R,it,E,x);R.onBeforeShadow(n,R,A,I,z,ut,H),n.renderBufferDirect(I,null,z,ut,R,H),R.onAfterShadow(n,R,A,I,z,ut,H)}}}else if(Y.visible){const j=M(R,Y,E,x);R.onBeforeShadow(n,R,A,I,z,j,null),n.renderBufferDirect(I,null,z,j,R,null),R.onAfterShadow(n,R,A,I,z,j,null)}}const V=R.children;for(let z=0,Y=V.length;z<Y;z++)y(V[z],A,I,E,x)}function P(R){R.target.removeEventListener("dispose",P);for(const I in c){const E=c[I],x=R.target.uuid;x in E&&(E[x].dispose(),delete E[x])}}}const m_={[to]:eo,[no]:ro,[io]:ao,[es]:so,[eo]:to,[ro]:no,[ao]:io,[so]:es};function g_(n,t){function e(){let D=!1;const at=new Kt;let k=null;const q=new Kt(0,0,0,0);return{setMask:function(lt){k!==lt&&!D&&(n.colorMask(lt,lt,lt,lt),k=lt)},setLocked:function(lt){D=lt},setClear:function(lt,ot,Ct,se,be){be===!0&&(lt*=se,ot*=se,Ct*=se),at.set(lt,ot,Ct,se),q.equals(at)===!1&&(n.clearColor(lt,ot,Ct,se),q.copy(at))},reset:function(){D=!1,k=null,q.set(-1,0,0,0)}}}function i(){let D=!1,at=!1,k=null,q=null,lt=null;return{setReversed:function(ot){if(at!==ot){const Ct=t.get("EXT_clip_control");ot?Ct.clipControlEXT(Ct.LOWER_LEFT_EXT,Ct.ZERO_TO_ONE_EXT):Ct.clipControlEXT(Ct.LOWER_LEFT_EXT,Ct.NEGATIVE_ONE_TO_ONE_EXT),at=ot;const se=lt;lt=null,this.setClear(se)}},getReversed:function(){return at},setTest:function(ot){ot?st(n.DEPTH_TEST):Et(n.DEPTH_TEST)},setMask:function(ot){k!==ot&&!D&&(n.depthMask(ot),k=ot)},setFunc:function(ot){if(at&&(ot=m_[ot]),q!==ot){switch(ot){case to:n.depthFunc(n.NEVER);break;case eo:n.depthFunc(n.ALWAYS);break;case no:n.depthFunc(n.LESS);break;case es:n.depthFunc(n.LEQUAL);break;case io:n.depthFunc(n.EQUAL);break;case so:n.depthFunc(n.GEQUAL);break;case ro:n.depthFunc(n.GREATER);break;case ao:n.depthFunc(n.NOTEQUAL);break;default:n.depthFunc(n.LEQUAL)}q=ot}},setLocked:function(ot){D=ot},setClear:function(ot){lt!==ot&&(at&&(ot=1-ot),n.clearDepth(ot),lt=ot)},reset:function(){D=!1,k=null,q=null,lt=null,at=!1}}}function s(){let D=!1,at=null,k=null,q=null,lt=null,ot=null,Ct=null,se=null,be=null;return{setTest:function(qt){D||(qt?st(n.STENCIL_TEST):Et(n.STENCIL_TEST))},setMask:function(qt){at!==qt&&!D&&(n.stencilMask(qt),at=qt)},setFunc:function(qt,an,Pn){(k!==qt||q!==an||lt!==Pn)&&(n.stencilFunc(qt,an,Pn),k=qt,q=an,lt=Pn)},setOp:function(qt,an,Pn){(ot!==qt||Ct!==an||se!==Pn)&&(n.stencilOp(qt,an,Pn),ot=qt,Ct=an,se=Pn)},setLocked:function(qt){D=qt},setClear:function(qt){be!==qt&&(n.clearStencil(qt),be=qt)},reset:function(){D=!1,at=null,k=null,q=null,lt=null,ot=null,Ct=null,se=null,be=null}}}const r=new e,a=new i,o=new s,l=new WeakMap,c=new WeakMap;let u={},d={},h=new WeakMap,p=[],_=null,S=!1,m=null,f=null,b=null,M=null,y=null,P=null,R=null,A=new It(0,0,0),I=0,E=!1,x=null,C=null,V=null,z=null,Y=null;const j=n.getParameter(n.MAX_COMBINED_TEXTURE_IMAGE_UNITS);let X=!1,Z=0;const H=n.getParameter(n.VERSION);H.indexOf("WebGL")!==-1?(Z=parseFloat(/^WebGL (\d)/.exec(H)[1]),X=Z>=1):H.indexOf("OpenGL ES")!==-1&&(Z=parseFloat(/^OpenGL ES (\d)/.exec(H)[1]),X=Z>=2);let it=null,ut={};const vt=n.getParameter(n.SCISSOR_BOX),Ut=n.getParameter(n.VIEWPORT),Zt=new Kt().fromArray(vt),W=new Kt().fromArray(Ut);function tt(D,at,k,q){const lt=new Uint8Array(4),ot=n.createTexture();n.bindTexture(D,ot),n.texParameteri(D,n.TEXTURE_MIN_FILTER,n.NEAREST),n.texParameteri(D,n.TEXTURE_MAG_FILTER,n.NEAREST);for(let Ct=0;Ct<k;Ct++)D===n.TEXTURE_3D||D===n.TEXTURE_2D_ARRAY?n.texImage3D(at,0,n.RGBA,1,1,q,0,n.RGBA,n.UNSIGNED_BYTE,lt):n.texImage2D(at+Ct,0,n.RGBA,1,1,0,n.RGBA,n.UNSIGNED_BYTE,lt);return ot}const mt={};mt[n.TEXTURE_2D]=tt(n.TEXTURE_2D,n.TEXTURE_2D,1),mt[n.TEXTURE_CUBE_MAP]=tt(n.TEXTURE_CUBE_MAP,n.TEXTURE_CUBE_MAP_POSITIVE_X,6),mt[n.TEXTURE_2D_ARRAY]=tt(n.TEXTURE_2D_ARRAY,n.TEXTURE_2D_ARRAY,1,1),mt[n.TEXTURE_3D]=tt(n.TEXTURE_3D,n.TEXTURE_3D,1,1),r.setClear(0,0,0,1),a.setClear(1),o.setClear(0),st(n.DEPTH_TEST),a.setFunc(es),zt(!1),Ft(wl),st(n.CULL_FACE),w(ri);function st(D){u[D]!==!0&&(n.enable(D),u[D]=!0)}function Et(D){u[D]!==!1&&(n.disable(D),u[D]=!1)}function Wt(D,at){return d[D]!==at?(n.bindFramebuffer(D,at),d[D]=at,D===n.DRAW_FRAMEBUFFER&&(d[n.FRAMEBUFFER]=at),D===n.FRAMEBUFFER&&(d[n.DRAW_FRAMEBUFFER]=at),!0):!1}function bt(D,at){let k=p,q=!1;if(D){k=h.get(at),k===void 0&&(k=[],h.set(at,k));const lt=D.textures;if(k.length!==lt.length||k[0]!==n.COLOR_ATTACHMENT0){for(let ot=0,Ct=lt.length;ot<Ct;ot++)k[ot]=n.COLOR_ATTACHMENT0+ot;k.length=lt.length,q=!0}}else k[0]!==n.BACK&&(k[0]=n.BACK,q=!0);q&&n.drawBuffers(k)}function oe(D){return _!==D?(n.useProgram(D),_=D,!0):!1}const ne={[_i]:n.FUNC_ADD,[pd]:n.FUNC_SUBTRACT,[md]:n.FUNC_REVERSE_SUBTRACT};ne[gd]=n.MIN,ne[_d]=n.MAX;const Ot={[vd]:n.ZERO,[xd]:n.ONE,[Sd]:n.SRC_COLOR,[Ja]:n.SRC_ALPHA,[Ad]:n.SRC_ALPHA_SATURATE,[Td]:n.DST_COLOR,[Ed]:n.DST_ALPHA,[yd]:n.ONE_MINUS_SRC_COLOR,[Qa]:n.ONE_MINUS_SRC_ALPHA,[bd]:n.ONE_MINUS_DST_COLOR,[Md]:n.ONE_MINUS_DST_ALPHA,[wd]:n.CONSTANT_COLOR,[Rd]:n.ONE_MINUS_CONSTANT_COLOR,[Cd]:n.CONSTANT_ALPHA,[Pd]:n.ONE_MINUS_CONSTANT_ALPHA};function w(D,at,k,q,lt,ot,Ct,se,be,qt){if(D===ri){S===!0&&(Et(n.BLEND),S=!1);return}if(S===!1&&(st(n.BLEND),S=!0),D!==fd){if(D!==m||qt!==E){if((f!==_i||y!==_i)&&(n.blendEquation(n.FUNC_ADD),f=_i,y=_i),qt)switch(D){case Ki:n.blendFuncSeparate(n.ONE,n.ONE_MINUS_SRC_ALPHA,n.ONE,n.ONE_MINUS_SRC_ALPHA);break;case Fr:n.blendFunc(n.ONE,n.ONE);break;case Rl:n.blendFuncSeparate(n.ZERO,n.ONE_MINUS_SRC_COLOR,n.ZERO,n.ONE);break;case Cl:n.blendFuncSeparate(n.ZERO,n.SRC_COLOR,n.ZERO,n.SRC_ALPHA);break;default:console.error("THREE.WebGLState: Invalid blending: ",D);break}else switch(D){case Ki:n.blendFuncSeparate(n.SRC_ALPHA,n.ONE_MINUS_SRC_ALPHA,n.ONE,n.ONE_MINUS_SRC_ALPHA);break;case Fr:n.blendFunc(n.SRC_ALPHA,n.ONE);break;case Rl:n.blendFuncSeparate(n.ZERO,n.ONE_MINUS_SRC_COLOR,n.ZERO,n.ONE);break;case Cl:n.blendFunc(n.ZERO,n.SRC_COLOR);break;default:console.error("THREE.WebGLState: Invalid blending: ",D);break}b=null,M=null,P=null,R=null,A.set(0,0,0),I=0,m=D,E=qt}return}lt=lt||at,ot=ot||k,Ct=Ct||q,(at!==f||lt!==y)&&(n.blendEquationSeparate(ne[at],ne[lt]),f=at,y=lt),(k!==b||q!==M||ot!==P||Ct!==R)&&(n.blendFuncSeparate(Ot[k],Ot[q],Ot[ot],Ot[Ct]),b=k,M=q,P=ot,R=Ct),(se.equals(A)===!1||be!==I)&&(n.blendColor(se.r,se.g,se.b,be),A.copy(se),I=be),m=D,E=!1}function qe(D,at){D.side===zn?Et(n.CULL_FACE):st(n.CULL_FACE);let k=D.side===Le;at&&(k=!k),zt(k),D.blending===Ki&&D.transparent===!1?w(ri):w(D.blending,D.blendEquation,D.blendSrc,D.blendDst,D.blendEquationAlpha,D.blendSrcAlpha,D.blendDstAlpha,D.blendColor,D.blendAlpha,D.premultipliedAlpha),a.setFunc(D.depthFunc),a.setTest(D.depthTest),a.setMask(D.depthWrite),r.setMask(D.colorWrite);const q=D.stencilWrite;o.setTest(q),q&&(o.setMask(D.stencilWriteMask),o.setFunc(D.stencilFunc,D.stencilRef,D.stencilFuncMask),o.setOp(D.stencilFail,D.stencilZFail,D.stencilZPass)),Qt(D.polygonOffset,D.polygonOffsetFactor,D.polygonOffsetUnits),D.alphaToCoverage===!0?st(n.SAMPLE_ALPHA_TO_COVERAGE):Et(n.SAMPLE_ALPHA_TO_COVERAGE)}function zt(D){x!==D&&(D?n.frontFace(n.CW):n.frontFace(n.CCW),x=D)}function Ft(D){D!==ud?(st(n.CULL_FACE),D!==C&&(D===wl?n.cullFace(n.BACK):D===dd?n.cullFace(n.FRONT):n.cullFace(n.FRONT_AND_BACK))):Et(n.CULL_FACE),C=D}function xt(D){D!==V&&(X&&n.lineWidth(D),V=D)}function Qt(D,at,k){D?(st(n.POLYGON_OFFSET_FILL),(z!==at||Y!==k)&&(n.polygonOffset(at,k),z=at,Y=k)):Et(n.POLYGON_OFFSET_FILL)}function _t(D){D?st(n.SCISSOR_TEST):Et(n.SCISSOR_TEST)}function T(D){D===void 0&&(D=n.TEXTURE0+j-1),it!==D&&(n.activeTexture(D),it=D)}function g(D,at,k){k===void 0&&(it===null?k=n.TEXTURE0+j-1:k=it);let q=ut[k];q===void 0&&(q={type:void 0,texture:void 0},ut[k]=q),(q.type!==D||q.texture!==at)&&(it!==k&&(n.activeTexture(k),it=k),n.bindTexture(D,at||mt[D]),q.type=D,q.texture=at)}function O(){const D=ut[it];D!==void 0&&D.type!==void 0&&(n.bindTexture(D.type,null),D.type=void 0,D.texture=void 0)}function $(){try{n.compressedTexImage2D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function K(){try{n.compressedTexImage3D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function G(){try{n.texSubImage2D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function gt(){try{n.texSubImage3D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function rt(){try{n.compressedTexSubImage2D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function dt(){try{n.compressedTexSubImage3D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function kt(){try{n.texStorage2D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function Q(){try{n.texStorage3D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function ht(){try{n.texImage2D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function Mt(){try{n.texImage3D(...arguments)}catch(D){console.error("THREE.WebGLState:",D)}}function wt(D){Zt.equals(D)===!1&&(n.scissor(D.x,D.y,D.z,D.w),Zt.copy(D))}function ft(D){W.equals(D)===!1&&(n.viewport(D.x,D.y,D.z,D.w),W.copy(D))}function Bt(D,at){let k=c.get(at);k===void 0&&(k=new WeakMap,c.set(at,k));let q=k.get(D);q===void 0&&(q=n.getUniformBlockIndex(at,D.name),k.set(D,q))}function Lt(D,at){const q=c.get(at).get(D);l.get(at)!==q&&(n.uniformBlockBinding(at,q,D.__bindingPointIndex),l.set(at,q))}function Jt(){n.disable(n.BLEND),n.disable(n.CULL_FACE),n.disable(n.DEPTH_TEST),n.disable(n.POLYGON_OFFSET_FILL),n.disable(n.SCISSOR_TEST),n.disable(n.STENCIL_TEST),n.disable(n.SAMPLE_ALPHA_TO_COVERAGE),n.blendEquation(n.FUNC_ADD),n.blendFunc(n.ONE,n.ZERO),n.blendFuncSeparate(n.ONE,n.ZERO,n.ONE,n.ZERO),n.blendColor(0,0,0,0),n.colorMask(!0,!0,!0,!0),n.clearColor(0,0,0,0),n.depthMask(!0),n.depthFunc(n.LESS),a.setReversed(!1),n.clearDepth(1),n.stencilMask(4294967295),n.stencilFunc(n.ALWAYS,0,4294967295),n.stencilOp(n.KEEP,n.KEEP,n.KEEP),n.clearStencil(0),n.cullFace(n.BACK),n.frontFace(n.CCW),n.polygonOffset(0,0),n.activeTexture(n.TEXTURE0),n.bindFramebuffer(n.FRAMEBUFFER,null),n.bindFramebuffer(n.DRAW_FRAMEBUFFER,null),n.bindFramebuffer(n.READ_FRAMEBUFFER,null),n.useProgram(null),n.lineWidth(1),n.scissor(0,0,n.canvas.width,n.canvas.height),n.viewport(0,0,n.canvas.width,n.canvas.height),u={},it=null,ut={},d={},h=new WeakMap,p=[],_=null,S=!1,m=null,f=null,b=null,M=null,y=null,P=null,R=null,A=new It(0,0,0),I=0,E=!1,x=null,C=null,V=null,z=null,Y=null,Zt.set(0,0,n.canvas.width,n.canvas.height),W.set(0,0,n.canvas.width,n.canvas.height),r.reset(),a.reset(),o.reset()}return{buffers:{color:r,depth:a,stencil:o},enable:st,disable:Et,bindFramebuffer:Wt,drawBuffers:bt,useProgram:oe,setBlending:w,setMaterial:qe,setFlipSided:zt,setCullFace:Ft,setLineWidth:xt,setPolygonOffset:Qt,setScissorTest:_t,activeTexture:T,bindTexture:g,unbindTexture:O,compressedTexImage2D:$,compressedTexImage3D:K,texImage2D:ht,texImage3D:Mt,updateUBOMapping:Bt,uniformBlockBinding:Lt,texStorage2D:kt,texStorage3D:Q,texSubImage2D:G,texSubImage3D:gt,compressedTexSubImage2D:rt,compressedTexSubImage3D:dt,scissor:wt,viewport:ft,reset:Jt}}function __(n,t,e,i,s,r,a){const o=t.has("WEBGL_multisampled_render_to_texture")?t.get("WEBGL_multisampled_render_to_texture"):null,l=typeof navigator>"u"?!1:/OculusBrowser/g.test(navigator.userAgent),c=new Tt,u=new WeakMap;let d;const h=new WeakMap;let p=!1;try{p=typeof OffscreenCanvas<"u"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function _(T,g){return p?new OffscreenCanvas(T,g):kr("canvas")}function S(T,g,O){let $=1;const K=_t(T);if((K.width>O||K.height>O)&&($=O/Math.max(K.width,K.height)),$<1)if(typeof HTMLImageElement<"u"&&T instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&T instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&T instanceof ImageBitmap||typeof VideoFrame<"u"&&T instanceof VideoFrame){const G=Math.floor($*K.width),gt=Math.floor($*K.height);d===void 0&&(d=_(G,gt));const rt=g?_(G,gt):d;return rt.width=G,rt.height=gt,rt.getContext("2d").drawImage(T,0,0,G,gt),console.warn("THREE.WebGLRenderer: Texture has been resized from ("+K.width+"x"+K.height+") to ("+G+"x"+gt+")."),rt}else return"data"in T&&console.warn("THREE.WebGLRenderer: Image in DataTexture is too big ("+K.width+"x"+K.height+")."),T;return T}function m(T){return T.generateMipmaps}function f(T){n.generateMipmap(T)}function b(T){return T.isWebGLCubeRenderTarget?n.TEXTURE_CUBE_MAP:T.isWebGL3DRenderTarget?n.TEXTURE_3D:T.isWebGLArrayRenderTarget||T.isCompressedArrayTexture?n.TEXTURE_2D_ARRAY:n.TEXTURE_2D}function M(T,g,O,$,K=!1){if(T!==null){if(n[T]!==void 0)return n[T];console.warn("THREE.WebGLRenderer: Attempt to use non-existing WebGL internal format '"+T+"'")}let G=g;if(g===n.RED&&(O===n.FLOAT&&(G=n.R32F),O===n.HALF_FLOAT&&(G=n.R16F),O===n.UNSIGNED_BYTE&&(G=n.R8)),g===n.RED_INTEGER&&(O===n.UNSIGNED_BYTE&&(G=n.R8UI),O===n.UNSIGNED_SHORT&&(G=n.R16UI),O===n.UNSIGNED_INT&&(G=n.R32UI),O===n.BYTE&&(G=n.R8I),O===n.SHORT&&(G=n.R16I),O===n.INT&&(G=n.R32I)),g===n.RG&&(O===n.FLOAT&&(G=n.RG32F),O===n.HALF_FLOAT&&(G=n.RG16F),O===n.UNSIGNED_BYTE&&(G=n.RG8)),g===n.RG_INTEGER&&(O===n.UNSIGNED_BYTE&&(G=n.RG8UI),O===n.UNSIGNED_SHORT&&(G=n.RG16UI),O===n.UNSIGNED_INT&&(G=n.RG32UI),O===n.BYTE&&(G=n.RG8I),O===n.SHORT&&(G=n.RG16I),O===n.INT&&(G=n.RG32I)),g===n.RGB_INTEGER&&(O===n.UNSIGNED_BYTE&&(G=n.RGB8UI),O===n.UNSIGNED_SHORT&&(G=n.RGB16UI),O===n.UNSIGNED_INT&&(G=n.RGB32UI),O===n.BYTE&&(G=n.RGB8I),O===n.SHORT&&(G=n.RGB16I),O===n.INT&&(G=n.RGB32I)),g===n.RGBA_INTEGER&&(O===n.UNSIGNED_BYTE&&(G=n.RGBA8UI),O===n.UNSIGNED_SHORT&&(G=n.RGBA16UI),O===n.UNSIGNED_INT&&(G=n.RGBA32UI),O===n.BYTE&&(G=n.RGBA8I),O===n.SHORT&&(G=n.RGBA16I),O===n.INT&&(G=n.RGBA32I)),g===n.RGB&&O===n.UNSIGNED_INT_5_9_9_9_REV&&(G=n.RGB9_E5),g===n.RGBA){const gt=K?Br:Gt.getTransfer($);O===n.FLOAT&&(G=n.RGBA32F),O===n.HALF_FLOAT&&(G=n.RGBA16F),O===n.UNSIGNED_BYTE&&(G=gt===Yt?n.SRGB8_ALPHA8:n.RGBA8),O===n.UNSIGNED_SHORT_4_4_4_4&&(G=n.RGBA4),O===n.UNSIGNED_SHORT_5_5_5_1&&(G=n.RGB5_A1)}return(G===n.R16F||G===n.R32F||G===n.RG16F||G===n.RG32F||G===n.RGBA16F||G===n.RGBA32F)&&t.get("EXT_color_buffer_float"),G}function y(T,g){let O;return T?g===null||g===Mi||g===Ls?O=n.DEPTH24_STENCIL8:g===Hn?O=n.DEPTH32F_STENCIL8:g===Ps&&(O=n.DEPTH24_STENCIL8,console.warn("DepthTexture: 16 bit depth attachment is not supported with stencil. Using 24-bit attachment.")):g===null||g===Mi||g===Ls?O=n.DEPTH_COMPONENT24:g===Hn?O=n.DEPTH_COMPONENT32F:g===Ps&&(O=n.DEPTH_COMPONENT16),O}function P(T,g){return m(T)===!0||T.isFramebufferTexture&&T.minFilter!==gn&&T.minFilter!==Rn?Math.log2(Math.max(g.width,g.height))+1:T.mipmaps!==void 0&&T.mipmaps.length>0?T.mipmaps.length:T.isCompressedTexture&&Array.isArray(T.image)?g.mipmaps.length:1}function R(T){const g=T.target;g.removeEventListener("dispose",R),I(g),g.isVideoTexture&&u.delete(g)}function A(T){const g=T.target;g.removeEventListener("dispose",A),x(g)}function I(T){const g=i.get(T);if(g.__webglInit===void 0)return;const O=T.source,$=h.get(O);if($){const K=$[g.__cacheKey];K.usedTimes--,K.usedTimes===0&&E(T),Object.keys($).length===0&&h.delete(O)}i.remove(T)}function E(T){const g=i.get(T);n.deleteTexture(g.__webglTexture);const O=T.source,$=h.get(O);delete $[g.__cacheKey],a.memory.textures--}function x(T){const g=i.get(T);if(T.depthTexture&&(T.depthTexture.dispose(),i.remove(T.depthTexture)),T.isWebGLCubeRenderTarget)for(let $=0;$<6;$++){if(Array.isArray(g.__webglFramebuffer[$]))for(let K=0;K<g.__webglFramebuffer[$].length;K++)n.deleteFramebuffer(g.__webglFramebuffer[$][K]);else n.deleteFramebuffer(g.__webglFramebuffer[$]);g.__webglDepthbuffer&&n.deleteRenderbuffer(g.__webglDepthbuffer[$])}else{if(Array.isArray(g.__webglFramebuffer))for(let $=0;$<g.__webglFramebuffer.length;$++)n.deleteFramebuffer(g.__webglFramebuffer[$]);else n.deleteFramebuffer(g.__webglFramebuffer);if(g.__webglDepthbuffer&&n.deleteRenderbuffer(g.__webglDepthbuffer),g.__webglMultisampledFramebuffer&&n.deleteFramebuffer(g.__webglMultisampledFramebuffer),g.__webglColorRenderbuffer)for(let $=0;$<g.__webglColorRenderbuffer.length;$++)g.__webglColorRenderbuffer[$]&&n.deleteRenderbuffer(g.__webglColorRenderbuffer[$]);g.__webglDepthRenderbuffer&&n.deleteRenderbuffer(g.__webglDepthRenderbuffer)}const O=T.textures;for(let $=0,K=O.length;$<K;$++){const G=i.get(O[$]);G.__webglTexture&&(n.deleteTexture(G.__webglTexture),a.memory.textures--),i.remove(O[$])}i.remove(T)}let C=0;function V(){C=0}function z(){const T=C;return T>=s.maxTextures&&console.warn("THREE.WebGLTextures: Trying to use "+T+" texture units while this GPU supports only "+s.maxTextures),C+=1,T}function Y(T){const g=[];return g.push(T.wrapS),g.push(T.wrapT),g.push(T.wrapR||0),g.push(T.magFilter),g.push(T.minFilter),g.push(T.anisotropy),g.push(T.internalFormat),g.push(T.format),g.push(T.type),g.push(T.generateMipmaps),g.push(T.premultiplyAlpha),g.push(T.flipY),g.push(T.unpackAlignment),g.push(T.colorSpace),g.join()}function j(T,g){const O=i.get(T);if(T.isVideoTexture&&xt(T),T.isRenderTargetTexture===!1&&T.version>0&&O.__version!==T.version){const $=T.image;if($===null)console.warn("THREE.WebGLRenderer: Texture marked for update but no image data found.");else if($.complete===!1)console.warn("THREE.WebGLRenderer: Texture marked for update but image is incomplete");else{W(O,T,g);return}}e.bindTexture(n.TEXTURE_2D,O.__webglTexture,n.TEXTURE0+g)}function X(T,g){const O=i.get(T);if(T.version>0&&O.__version!==T.version){W(O,T,g);return}e.bindTexture(n.TEXTURE_2D_ARRAY,O.__webglTexture,n.TEXTURE0+g)}function Z(T,g){const O=i.get(T);if(T.version>0&&O.__version!==T.version){W(O,T,g);return}e.bindTexture(n.TEXTURE_3D,O.__webglTexture,n.TEXTURE0+g)}function H(T,g){const O=i.get(T);if(T.version>0&&O.__version!==T.version){tt(O,T,g);return}e.bindTexture(n.TEXTURE_CUBE_MAP,O.__webglTexture,n.TEXTURE0+g)}const it={[co]:n.REPEAT,[xi]:n.CLAMP_TO_EDGE,[uo]:n.MIRRORED_REPEAT},ut={[gn]:n.NEAREST,[kd]:n.NEAREST_MIPMAP_NEAREST,[Ys]:n.NEAREST_MIPMAP_LINEAR,[Rn]:n.LINEAR,[aa]:n.LINEAR_MIPMAP_NEAREST,[Si]:n.LINEAR_MIPMAP_LINEAR},vt={[Xd]:n.NEVER,[Zd]:n.ALWAYS,[$d]:n.LESS,[mu]:n.LEQUAL,[qd]:n.EQUAL,[Kd]:n.GEQUAL,[Yd]:n.GREATER,[jd]:n.NOTEQUAL};function Ut(T,g){if(g.type===Hn&&t.has("OES_texture_float_linear")===!1&&(g.magFilter===Rn||g.magFilter===aa||g.magFilter===Ys||g.magFilter===Si||g.minFilter===Rn||g.minFilter===aa||g.minFilter===Ys||g.minFilter===Si)&&console.warn("THREE.WebGLRenderer: Unable to use linear filtering with floating point textures. OES_texture_float_linear not supported on this device."),n.texParameteri(T,n.TEXTURE_WRAP_S,it[g.wrapS]),n.texParameteri(T,n.TEXTURE_WRAP_T,it[g.wrapT]),(T===n.TEXTURE_3D||T===n.TEXTURE_2D_ARRAY)&&n.texParameteri(T,n.TEXTURE_WRAP_R,it[g.wrapR]),n.texParameteri(T,n.TEXTURE_MAG_FILTER,ut[g.magFilter]),n.texParameteri(T,n.TEXTURE_MIN_FILTER,ut[g.minFilter]),g.compareFunction&&(n.texParameteri(T,n.TEXTURE_COMPARE_MODE,n.COMPARE_REF_TO_TEXTURE),n.texParameteri(T,n.TEXTURE_COMPARE_FUNC,vt[g.compareFunction])),t.has("EXT_texture_filter_anisotropic")===!0){if(g.magFilter===gn||g.minFilter!==Ys&&g.minFilter!==Si||g.type===Hn&&t.has("OES_texture_float_linear")===!1)return;if(g.anisotropy>1||i.get(g).__currentAnisotropy){const O=t.get("EXT_texture_filter_anisotropic");n.texParameterf(T,O.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(g.anisotropy,s.getMaxAnisotropy())),i.get(g).__currentAnisotropy=g.anisotropy}}}function Zt(T,g){let O=!1;T.__webglInit===void 0&&(T.__webglInit=!0,g.addEventListener("dispose",R));const $=g.source;let K=h.get($);K===void 0&&(K={},h.set($,K));const G=Y(g);if(G!==T.__cacheKey){K[G]===void 0&&(K[G]={texture:n.createTexture(),usedTimes:0},a.memory.textures++,O=!0),K[G].usedTimes++;const gt=K[T.__cacheKey];gt!==void 0&&(K[T.__cacheKey].usedTimes--,gt.usedTimes===0&&E(g)),T.__cacheKey=G,T.__webglTexture=K[G].texture}return O}function W(T,g,O){let $=n.TEXTURE_2D;(g.isDataArrayTexture||g.isCompressedArrayTexture)&&($=n.TEXTURE_2D_ARRAY),g.isData3DTexture&&($=n.TEXTURE_3D);const K=Zt(T,g),G=g.source;e.bindTexture($,T.__webglTexture,n.TEXTURE0+O);const gt=i.get(G);if(G.version!==gt.__version||K===!0){e.activeTexture(n.TEXTURE0+O);const rt=Gt.getPrimaries(Gt.workingColorSpace),dt=g.colorSpace===ni?null:Gt.getPrimaries(g.colorSpace),kt=g.colorSpace===ni||rt===dt?n.NONE:n.BROWSER_DEFAULT_WEBGL;n.pixelStorei(n.UNPACK_FLIP_Y_WEBGL,g.flipY),n.pixelStorei(n.UNPACK_PREMULTIPLY_ALPHA_WEBGL,g.premultiplyAlpha),n.pixelStorei(n.UNPACK_ALIGNMENT,g.unpackAlignment),n.pixelStorei(n.UNPACK_COLORSPACE_CONVERSION_WEBGL,kt);let Q=S(g.image,!1,s.maxTextureSize);Q=Qt(g,Q);const ht=r.convert(g.format,g.colorSpace),Mt=r.convert(g.type);let wt=M(g.internalFormat,ht,Mt,g.colorSpace,g.isVideoTexture);Ut($,g);let ft;const Bt=g.mipmaps,Lt=g.isVideoTexture!==!0,Jt=gt.__version===void 0||K===!0,D=G.dataReady,at=P(g,Q);if(g.isDepthTexture)wt=y(g.format===Is,g.type),Jt&&(Lt?e.texStorage2D(n.TEXTURE_2D,1,wt,Q.width,Q.height):e.texImage2D(n.TEXTURE_2D,0,wt,Q.width,Q.height,0,ht,Mt,null));else if(g.isDataTexture)if(Bt.length>0){Lt&&Jt&&e.texStorage2D(n.TEXTURE_2D,at,wt,Bt[0].width,Bt[0].height);for(let k=0,q=Bt.length;k<q;k++)ft=Bt[k],Lt?D&&e.texSubImage2D(n.TEXTURE_2D,k,0,0,ft.width,ft.height,ht,Mt,ft.data):e.texImage2D(n.TEXTURE_2D,k,wt,ft.width,ft.height,0,ht,Mt,ft.data);g.generateMipmaps=!1}else Lt?(Jt&&e.texStorage2D(n.TEXTURE_2D,at,wt,Q.width,Q.height),D&&e.texSubImage2D(n.TEXTURE_2D,0,0,0,Q.width,Q.height,ht,Mt,Q.data)):e.texImage2D(n.TEXTURE_2D,0,wt,Q.width,Q.height,0,ht,Mt,Q.data);else if(g.isCompressedTexture)if(g.isCompressedArrayTexture){Lt&&Jt&&e.texStorage3D(n.TEXTURE_2D_ARRAY,at,wt,Bt[0].width,Bt[0].height,Q.depth);for(let k=0,q=Bt.length;k<q;k++)if(ft=Bt[k],g.format!==pn)if(ht!==null)if(Lt){if(D)if(g.layerUpdates.size>0){const lt=rc(ft.width,ft.height,g.format,g.type);for(const ot of g.layerUpdates){const Ct=ft.data.subarray(ot*lt/ft.data.BYTES_PER_ELEMENT,(ot+1)*lt/ft.data.BYTES_PER_ELEMENT);e.compressedTexSubImage3D(n.TEXTURE_2D_ARRAY,k,0,0,ot,ft.width,ft.height,1,ht,Ct)}g.clearLayerUpdates()}else e.compressedTexSubImage3D(n.TEXTURE_2D_ARRAY,k,0,0,0,ft.width,ft.height,Q.depth,ht,ft.data)}else e.compressedTexImage3D(n.TEXTURE_2D_ARRAY,k,wt,ft.width,ft.height,Q.depth,0,ft.data,0,0);else console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()");else Lt?D&&e.texSubImage3D(n.TEXTURE_2D_ARRAY,k,0,0,0,ft.width,ft.height,Q.depth,ht,Mt,ft.data):e.texImage3D(n.TEXTURE_2D_ARRAY,k,wt,ft.width,ft.height,Q.depth,0,ht,Mt,ft.data)}else{Lt&&Jt&&e.texStorage2D(n.TEXTURE_2D,at,wt,Bt[0].width,Bt[0].height);for(let k=0,q=Bt.length;k<q;k++)ft=Bt[k],g.format!==pn?ht!==null?Lt?D&&e.compressedTexSubImage2D(n.TEXTURE_2D,k,0,0,ft.width,ft.height,ht,ft.data):e.compressedTexImage2D(n.TEXTURE_2D,k,wt,ft.width,ft.height,0,ft.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):Lt?D&&e.texSubImage2D(n.TEXTURE_2D,k,0,0,ft.width,ft.height,ht,Mt,ft.data):e.texImage2D(n.TEXTURE_2D,k,wt,ft.width,ft.height,0,ht,Mt,ft.data)}else if(g.isDataArrayTexture)if(Lt){if(Jt&&e.texStorage3D(n.TEXTURE_2D_ARRAY,at,wt,Q.width,Q.height,Q.depth),D)if(g.layerUpdates.size>0){const k=rc(Q.width,Q.height,g.format,g.type);for(const q of g.layerUpdates){const lt=Q.data.subarray(q*k/Q.data.BYTES_PER_ELEMENT,(q+1)*k/Q.data.BYTES_PER_ELEMENT);e.texSubImage3D(n.TEXTURE_2D_ARRAY,0,0,0,q,Q.width,Q.height,1,ht,Mt,lt)}g.clearLayerUpdates()}else e.texSubImage3D(n.TEXTURE_2D_ARRAY,0,0,0,0,Q.width,Q.height,Q.depth,ht,Mt,Q.data)}else e.texImage3D(n.TEXTURE_2D_ARRAY,0,wt,Q.width,Q.height,Q.depth,0,ht,Mt,Q.data);else if(g.isData3DTexture)Lt?(Jt&&e.texStorage3D(n.TEXTURE_3D,at,wt,Q.width,Q.height,Q.depth),D&&e.texSubImage3D(n.TEXTURE_3D,0,0,0,0,Q.width,Q.height,Q.depth,ht,Mt,Q.data)):e.texImage3D(n.TEXTURE_3D,0,wt,Q.width,Q.height,Q.depth,0,ht,Mt,Q.data);else if(g.isFramebufferTexture){if(Jt)if(Lt)e.texStorage2D(n.TEXTURE_2D,at,wt,Q.width,Q.height);else{let k=Q.width,q=Q.height;for(let lt=0;lt<at;lt++)e.texImage2D(n.TEXTURE_2D,lt,wt,k,q,0,ht,Mt,null),k>>=1,q>>=1}}else if(Bt.length>0){if(Lt&&Jt){const k=_t(Bt[0]);e.texStorage2D(n.TEXTURE_2D,at,wt,k.width,k.height)}for(let k=0,q=Bt.length;k<q;k++)ft=Bt[k],Lt?D&&e.texSubImage2D(n.TEXTURE_2D,k,0,0,ht,Mt,ft):e.texImage2D(n.TEXTURE_2D,k,wt,ht,Mt,ft);g.generateMipmaps=!1}else if(Lt){if(Jt){const k=_t(Q);e.texStorage2D(n.TEXTURE_2D,at,wt,k.width,k.height)}D&&e.texSubImage2D(n.TEXTURE_2D,0,0,0,ht,Mt,Q)}else e.texImage2D(n.TEXTURE_2D,0,wt,ht,Mt,Q);m(g)&&f($),gt.__version=G.version,g.onUpdate&&g.onUpdate(g)}T.__version=g.version}function tt(T,g,O){if(g.image.length!==6)return;const $=Zt(T,g),K=g.source;e.bindTexture(n.TEXTURE_CUBE_MAP,T.__webglTexture,n.TEXTURE0+O);const G=i.get(K);if(K.version!==G.__version||$===!0){e.activeTexture(n.TEXTURE0+O);const gt=Gt.getPrimaries(Gt.workingColorSpace),rt=g.colorSpace===ni?null:Gt.getPrimaries(g.colorSpace),dt=g.colorSpace===ni||gt===rt?n.NONE:n.BROWSER_DEFAULT_WEBGL;n.pixelStorei(n.UNPACK_FLIP_Y_WEBGL,g.flipY),n.pixelStorei(n.UNPACK_PREMULTIPLY_ALPHA_WEBGL,g.premultiplyAlpha),n.pixelStorei(n.UNPACK_ALIGNMENT,g.unpackAlignment),n.pixelStorei(n.UNPACK_COLORSPACE_CONVERSION_WEBGL,dt);const kt=g.isCompressedTexture||g.image[0].isCompressedTexture,Q=g.image[0]&&g.image[0].isDataTexture,ht=[];for(let q=0;q<6;q++)!kt&&!Q?ht[q]=S(g.image[q],!0,s.maxCubemapSize):ht[q]=Q?g.image[q].image:g.image[q],ht[q]=Qt(g,ht[q]);const Mt=ht[0],wt=r.convert(g.format,g.colorSpace),ft=r.convert(g.type),Bt=M(g.internalFormat,wt,ft,g.colorSpace),Lt=g.isVideoTexture!==!0,Jt=G.__version===void 0||$===!0,D=K.dataReady;let at=P(g,Mt);Ut(n.TEXTURE_CUBE_MAP,g);let k;if(kt){Lt&&Jt&&e.texStorage2D(n.TEXTURE_CUBE_MAP,at,Bt,Mt.width,Mt.height);for(let q=0;q<6;q++){k=ht[q].mipmaps;for(let lt=0;lt<k.length;lt++){const ot=k[lt];g.format!==pn?wt!==null?Lt?D&&e.compressedTexSubImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt,0,0,ot.width,ot.height,wt,ot.data):e.compressedTexImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt,Bt,ot.width,ot.height,0,ot.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):Lt?D&&e.texSubImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt,0,0,ot.width,ot.height,wt,ft,ot.data):e.texImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt,Bt,ot.width,ot.height,0,wt,ft,ot.data)}}}else{if(k=g.mipmaps,Lt&&Jt){k.length>0&&at++;const q=_t(ht[0]);e.texStorage2D(n.TEXTURE_CUBE_MAP,at,Bt,q.width,q.height)}for(let q=0;q<6;q++)if(Q){Lt?D&&e.texSubImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,0,0,0,ht[q].width,ht[q].height,wt,ft,ht[q].data):e.texImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,0,Bt,ht[q].width,ht[q].height,0,wt,ft,ht[q].data);for(let lt=0;lt<k.length;lt++){const Ct=k[lt].image[q].image;Lt?D&&e.texSubImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt+1,0,0,Ct.width,Ct.height,wt,ft,Ct.data):e.texImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt+1,Bt,Ct.width,Ct.height,0,wt,ft,Ct.data)}}else{Lt?D&&e.texSubImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,0,0,0,wt,ft,ht[q]):e.texImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,0,Bt,wt,ft,ht[q]);for(let lt=0;lt<k.length;lt++){const ot=k[lt];Lt?D&&e.texSubImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt+1,0,0,wt,ft,ot.image[q]):e.texImage2D(n.TEXTURE_CUBE_MAP_POSITIVE_X+q,lt+1,Bt,wt,ft,ot.image[q])}}}m(g)&&f(n.TEXTURE_CUBE_MAP),G.__version=K.version,g.onUpdate&&g.onUpdate(g)}T.__version=g.version}function mt(T,g,O,$,K,G){const gt=r.convert(O.format,O.colorSpace),rt=r.convert(O.type),dt=M(O.internalFormat,gt,rt,O.colorSpace),kt=i.get(g),Q=i.get(O);if(Q.__renderTarget=g,!kt.__hasExternalTextures){const ht=Math.max(1,g.width>>G),Mt=Math.max(1,g.height>>G);K===n.TEXTURE_3D||K===n.TEXTURE_2D_ARRAY?e.texImage3D(K,G,dt,ht,Mt,g.depth,0,gt,rt,null):e.texImage2D(K,G,dt,ht,Mt,0,gt,rt,null)}e.bindFramebuffer(n.FRAMEBUFFER,T),Ft(g)?o.framebufferTexture2DMultisampleEXT(n.FRAMEBUFFER,$,K,Q.__webglTexture,0,zt(g)):(K===n.TEXTURE_2D||K>=n.TEXTURE_CUBE_MAP_POSITIVE_X&&K<=n.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&n.framebufferTexture2D(n.FRAMEBUFFER,$,K,Q.__webglTexture,G),e.bindFramebuffer(n.FRAMEBUFFER,null)}function st(T,g,O){if(n.bindRenderbuffer(n.RENDERBUFFER,T),g.depthBuffer){const $=g.depthTexture,K=$&&$.isDepthTexture?$.type:null,G=y(g.stencilBuffer,K),gt=g.stencilBuffer?n.DEPTH_STENCIL_ATTACHMENT:n.DEPTH_ATTACHMENT,rt=zt(g);Ft(g)?o.renderbufferStorageMultisampleEXT(n.RENDERBUFFER,rt,G,g.width,g.height):O?n.renderbufferStorageMultisample(n.RENDERBUFFER,rt,G,g.width,g.height):n.renderbufferStorage(n.RENDERBUFFER,G,g.width,g.height),n.framebufferRenderbuffer(n.FRAMEBUFFER,gt,n.RENDERBUFFER,T)}else{const $=g.textures;for(let K=0;K<$.length;K++){const G=$[K],gt=r.convert(G.format,G.colorSpace),rt=r.convert(G.type),dt=M(G.internalFormat,gt,rt,G.colorSpace),kt=zt(g);O&&Ft(g)===!1?n.renderbufferStorageMultisample(n.RENDERBUFFER,kt,dt,g.width,g.height):Ft(g)?o.renderbufferStorageMultisampleEXT(n.RENDERBUFFER,kt,dt,g.width,g.height):n.renderbufferStorage(n.RENDERBUFFER,dt,g.width,g.height)}}n.bindRenderbuffer(n.RENDERBUFFER,null)}function Et(T,g){if(g&&g.isWebGLCubeRenderTarget)throw new Error("Depth Texture with cube render targets is not supported");if(e.bindFramebuffer(n.FRAMEBUFFER,T),!(g.depthTexture&&g.depthTexture.isDepthTexture))throw new Error("renderTarget.depthTexture must be an instance of THREE.DepthTexture");const $=i.get(g.depthTexture);$.__renderTarget=g,(!$.__webglTexture||g.depthTexture.image.width!==g.width||g.depthTexture.image.height!==g.height)&&(g.depthTexture.image.width=g.width,g.depthTexture.image.height=g.height,g.depthTexture.needsUpdate=!0),j(g.depthTexture,0);const K=$.__webglTexture,G=zt(g);if(g.depthTexture.format===Ds)Ft(g)?o.framebufferTexture2DMultisampleEXT(n.FRAMEBUFFER,n.DEPTH_ATTACHMENT,n.TEXTURE_2D,K,0,G):n.framebufferTexture2D(n.FRAMEBUFFER,n.DEPTH_ATTACHMENT,n.TEXTURE_2D,K,0);else if(g.depthTexture.format===Is)Ft(g)?o.framebufferTexture2DMultisampleEXT(n.FRAMEBUFFER,n.DEPTH_STENCIL_ATTACHMENT,n.TEXTURE_2D,K,0,G):n.framebufferTexture2D(n.FRAMEBUFFER,n.DEPTH_STENCIL_ATTACHMENT,n.TEXTURE_2D,K,0);else throw new Error("Unknown depthTexture format")}function Wt(T){const g=i.get(T),O=T.isWebGLCubeRenderTarget===!0;if(g.__boundDepthTexture!==T.depthTexture){const $=T.depthTexture;if(g.__depthDisposeCallback&&g.__depthDisposeCallback(),$){const K=()=>{delete g.__boundDepthTexture,delete g.__depthDisposeCallback,$.removeEventListener("dispose",K)};$.addEventListener("dispose",K),g.__depthDisposeCallback=K}g.__boundDepthTexture=$}if(T.depthTexture&&!g.__autoAllocateDepthBuffer){if(O)throw new Error("target.depthTexture not supported in Cube render targets");Et(g.__webglFramebuffer,T)}else if(O){g.__webglDepthbuffer=[];for(let $=0;$<6;$++)if(e.bindFramebuffer(n.FRAMEBUFFER,g.__webglFramebuffer[$]),g.__webglDepthbuffer[$]===void 0)g.__webglDepthbuffer[$]=n.createRenderbuffer(),st(g.__webglDepthbuffer[$],T,!1);else{const K=T.stencilBuffer?n.DEPTH_STENCIL_ATTACHMENT:n.DEPTH_ATTACHMENT,G=g.__webglDepthbuffer[$];n.bindRenderbuffer(n.RENDERBUFFER,G),n.framebufferRenderbuffer(n.FRAMEBUFFER,K,n.RENDERBUFFER,G)}}else if(e.bindFramebuffer(n.FRAMEBUFFER,g.__webglFramebuffer),g.__webglDepthbuffer===void 0)g.__webglDepthbuffer=n.createRenderbuffer(),st(g.__webglDepthbuffer,T,!1);else{const $=T.stencilBuffer?n.DEPTH_STENCIL_ATTACHMENT:n.DEPTH_ATTACHMENT,K=g.__webglDepthbuffer;n.bindRenderbuffer(n.RENDERBUFFER,K),n.framebufferRenderbuffer(n.FRAMEBUFFER,$,n.RENDERBUFFER,K)}e.bindFramebuffer(n.FRAMEBUFFER,null)}function bt(T,g,O){const $=i.get(T);g!==void 0&&mt($.__webglFramebuffer,T,T.texture,n.COLOR_ATTACHMENT0,n.TEXTURE_2D,0),O!==void 0&&Wt(T)}function oe(T){const g=T.texture,O=i.get(T),$=i.get(g);T.addEventListener("dispose",A);const K=T.textures,G=T.isWebGLCubeRenderTarget===!0,gt=K.length>1;if(gt||($.__webglTexture===void 0&&($.__webglTexture=n.createTexture()),$.__version=g.version,a.memory.textures++),G){O.__webglFramebuffer=[];for(let rt=0;rt<6;rt++)if(g.mipmaps&&g.mipmaps.length>0){O.__webglFramebuffer[rt]=[];for(let dt=0;dt<g.mipmaps.length;dt++)O.__webglFramebuffer[rt][dt]=n.createFramebuffer()}else O.__webglFramebuffer[rt]=n.createFramebuffer()}else{if(g.mipmaps&&g.mipmaps.length>0){O.__webglFramebuffer=[];for(let rt=0;rt<g.mipmaps.length;rt++)O.__webglFramebuffer[rt]=n.createFramebuffer()}else O.__webglFramebuffer=n.createFramebuffer();if(gt)for(let rt=0,dt=K.length;rt<dt;rt++){const kt=i.get(K[rt]);kt.__webglTexture===void 0&&(kt.__webglTexture=n.createTexture(),a.memory.textures++)}if(T.samples>0&&Ft(T)===!1){O.__webglMultisampledFramebuffer=n.createFramebuffer(),O.__webglColorRenderbuffer=[],e.bindFramebuffer(n.FRAMEBUFFER,O.__webglMultisampledFramebuffer);for(let rt=0;rt<K.length;rt++){const dt=K[rt];O.__webglColorRenderbuffer[rt]=n.createRenderbuffer(),n.bindRenderbuffer(n.RENDERBUFFER,O.__webglColorRenderbuffer[rt]);const kt=r.convert(dt.format,dt.colorSpace),Q=r.convert(dt.type),ht=M(dt.internalFormat,kt,Q,dt.colorSpace,T.isXRRenderTarget===!0),Mt=zt(T);n.renderbufferStorageMultisample(n.RENDERBUFFER,Mt,ht,T.width,T.height),n.framebufferRenderbuffer(n.FRAMEBUFFER,n.COLOR_ATTACHMENT0+rt,n.RENDERBUFFER,O.__webglColorRenderbuffer[rt])}n.bindRenderbuffer(n.RENDERBUFFER,null),T.depthBuffer&&(O.__webglDepthRenderbuffer=n.createRenderbuffer(),st(O.__webglDepthRenderbuffer,T,!0)),e.bindFramebuffer(n.FRAMEBUFFER,null)}}if(G){e.bindTexture(n.TEXTURE_CUBE_MAP,$.__webglTexture),Ut(n.TEXTURE_CUBE_MAP,g);for(let rt=0;rt<6;rt++)if(g.mipmaps&&g.mipmaps.length>0)for(let dt=0;dt<g.mipmaps.length;dt++)mt(O.__webglFramebuffer[rt][dt],T,g,n.COLOR_ATTACHMENT0,n.TEXTURE_CUBE_MAP_POSITIVE_X+rt,dt);else mt(O.__webglFramebuffer[rt],T,g,n.COLOR_ATTACHMENT0,n.TEXTURE_CUBE_MAP_POSITIVE_X+rt,0);m(g)&&f(n.TEXTURE_CUBE_MAP),e.unbindTexture()}else if(gt){for(let rt=0,dt=K.length;rt<dt;rt++){const kt=K[rt],Q=i.get(kt);e.bindTexture(n.TEXTURE_2D,Q.__webglTexture),Ut(n.TEXTURE_2D,kt),mt(O.__webglFramebuffer,T,kt,n.COLOR_ATTACHMENT0+rt,n.TEXTURE_2D,0),m(kt)&&f(n.TEXTURE_2D)}e.unbindTexture()}else{let rt=n.TEXTURE_2D;if((T.isWebGL3DRenderTarget||T.isWebGLArrayRenderTarget)&&(rt=T.isWebGL3DRenderTarget?n.TEXTURE_3D:n.TEXTURE_2D_ARRAY),e.bindTexture(rt,$.__webglTexture),Ut(rt,g),g.mipmaps&&g.mipmaps.length>0)for(let dt=0;dt<g.mipmaps.length;dt++)mt(O.__webglFramebuffer[dt],T,g,n.COLOR_ATTACHMENT0,rt,dt);else mt(O.__webglFramebuffer,T,g,n.COLOR_ATTACHMENT0,rt,0);m(g)&&f(rt),e.unbindTexture()}T.depthBuffer&&Wt(T)}function ne(T){const g=T.textures;for(let O=0,$=g.length;O<$;O++){const K=g[O];if(m(K)){const G=b(T),gt=i.get(K).__webglTexture;e.bindTexture(G,gt),f(G),e.unbindTexture()}}}const Ot=[],w=[];function qe(T){if(T.samples>0){if(Ft(T)===!1){const g=T.textures,O=T.width,$=T.height;let K=n.COLOR_BUFFER_BIT;const G=T.stencilBuffer?n.DEPTH_STENCIL_ATTACHMENT:n.DEPTH_ATTACHMENT,gt=i.get(T),rt=g.length>1;if(rt)for(let dt=0;dt<g.length;dt++)e.bindFramebuffer(n.FRAMEBUFFER,gt.__webglMultisampledFramebuffer),n.framebufferRenderbuffer(n.FRAMEBUFFER,n.COLOR_ATTACHMENT0+dt,n.RENDERBUFFER,null),e.bindFramebuffer(n.FRAMEBUFFER,gt.__webglFramebuffer),n.framebufferTexture2D(n.DRAW_FRAMEBUFFER,n.COLOR_ATTACHMENT0+dt,n.TEXTURE_2D,null,0);e.bindFramebuffer(n.READ_FRAMEBUFFER,gt.__webglMultisampledFramebuffer),e.bindFramebuffer(n.DRAW_FRAMEBUFFER,gt.__webglFramebuffer);for(let dt=0;dt<g.length;dt++){if(T.resolveDepthBuffer&&(T.depthBuffer&&(K|=n.DEPTH_BUFFER_BIT),T.stencilBuffer&&T.resolveStencilBuffer&&(K|=n.STENCIL_BUFFER_BIT)),rt){n.framebufferRenderbuffer(n.READ_FRAMEBUFFER,n.COLOR_ATTACHMENT0,n.RENDERBUFFER,gt.__webglColorRenderbuffer[dt]);const kt=i.get(g[dt]).__webglTexture;n.framebufferTexture2D(n.DRAW_FRAMEBUFFER,n.COLOR_ATTACHMENT0,n.TEXTURE_2D,kt,0)}n.blitFramebuffer(0,0,O,$,0,0,O,$,K,n.NEAREST),l===!0&&(Ot.length=0,w.length=0,Ot.push(n.COLOR_ATTACHMENT0+dt),T.depthBuffer&&T.resolveDepthBuffer===!1&&(Ot.push(G),w.push(G),n.invalidateFramebuffer(n.DRAW_FRAMEBUFFER,w)),n.invalidateFramebuffer(n.READ_FRAMEBUFFER,Ot))}if(e.bindFramebuffer(n.READ_FRAMEBUFFER,null),e.bindFramebuffer(n.DRAW_FRAMEBUFFER,null),rt)for(let dt=0;dt<g.length;dt++){e.bindFramebuffer(n.FRAMEBUFFER,gt.__webglMultisampledFramebuffer),n.framebufferRenderbuffer(n.FRAMEBUFFER,n.COLOR_ATTACHMENT0+dt,n.RENDERBUFFER,gt.__webglColorRenderbuffer[dt]);const kt=i.get(g[dt]).__webglTexture;e.bindFramebuffer(n.FRAMEBUFFER,gt.__webglFramebuffer),n.framebufferTexture2D(n.DRAW_FRAMEBUFFER,n.COLOR_ATTACHMENT0+dt,n.TEXTURE_2D,kt,0)}e.bindFramebuffer(n.DRAW_FRAMEBUFFER,gt.__webglMultisampledFramebuffer)}else if(T.depthBuffer&&T.resolveDepthBuffer===!1&&l){const g=T.stencilBuffer?n.DEPTH_STENCIL_ATTACHMENT:n.DEPTH_ATTACHMENT;n.invalidateFramebuffer(n.DRAW_FRAMEBUFFER,[g])}}}function zt(T){return Math.min(s.maxSamples,T.samples)}function Ft(T){const g=i.get(T);return T.samples>0&&t.has("WEBGL_multisampled_render_to_texture")===!0&&g.__useRenderToTexture!==!1}function xt(T){const g=a.render.frame;u.get(T)!==g&&(u.set(T,g),T.update())}function Qt(T,g){const O=T.colorSpace,$=T.format,K=T.type;return T.isCompressedTexture===!0||T.isVideoTexture===!0||O!==ss&&O!==ni&&(Gt.getTransfer(O)===Yt?($!==pn||K!==Wn)&&console.warn("THREE.WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):console.error("THREE.WebGLTextures: Unsupported texture color space:",O)),g}function _t(T){return typeof HTMLImageElement<"u"&&T instanceof HTMLImageElement?(c.width=T.naturalWidth||T.width,c.height=T.naturalHeight||T.height):typeof VideoFrame<"u"&&T instanceof VideoFrame?(c.width=T.displayWidth,c.height=T.displayHeight):(c.width=T.width,c.height=T.height),c}this.allocateTextureUnit=z,this.resetTextureUnits=V,this.setTexture2D=j,this.setTexture2DArray=X,this.setTexture3D=Z,this.setTextureCube=H,this.rebindTextures=bt,this.setupRenderTarget=oe,this.updateRenderTargetMipmap=ne,this.updateMultisampleRenderTarget=qe,this.setupDepthRenderbuffer=Wt,this.setupFrameBufferTexture=mt,this.useMultisampledRTT=Ft}function v_(n,t){function e(i,s=ni){let r;const a=Gt.getTransfer(s);if(i===Wn)return n.UNSIGNED_BYTE;if(i===Qo)return n.UNSIGNED_SHORT_4_4_4_4;if(i===tl)return n.UNSIGNED_SHORT_5_5_5_1;if(i===ou)return n.UNSIGNED_INT_5_9_9_9_REV;if(i===ru)return n.BYTE;if(i===au)return n.SHORT;if(i===Ps)return n.UNSIGNED_SHORT;if(i===Jo)return n.INT;if(i===Mi)return n.UNSIGNED_INT;if(i===Hn)return n.FLOAT;if(i===zs)return n.HALF_FLOAT;if(i===lu)return n.ALPHA;if(i===cu)return n.RGB;if(i===pn)return n.RGBA;if(i===uu)return n.LUMINANCE;if(i===du)return n.LUMINANCE_ALPHA;if(i===Ds)return n.DEPTH_COMPONENT;if(i===Is)return n.DEPTH_STENCIL;if(i===hu)return n.RED;if(i===el)return n.RED_INTEGER;if(i===fu)return n.RG;if(i===nl)return n.RG_INTEGER;if(i===il)return n.RGBA_INTEGER;if(i===br||i===Ar||i===wr||i===Rr)if(a===Yt)if(r=t.get("WEBGL_compressed_texture_s3tc_srgb"),r!==null){if(i===br)return r.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(i===Ar)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(i===wr)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(i===Rr)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(r=t.get("WEBGL_compressed_texture_s3tc"),r!==null){if(i===br)return r.COMPRESSED_RGB_S3TC_DXT1_EXT;if(i===Ar)return r.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(i===wr)return r.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(i===Rr)return r.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(i===ho||i===fo||i===po||i===mo)if(r=t.get("WEBGL_compressed_texture_pvrtc"),r!==null){if(i===ho)return r.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(i===fo)return r.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(i===po)return r.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(i===mo)return r.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(i===go||i===_o||i===vo)if(r=t.get("WEBGL_compressed_texture_etc"),r!==null){if(i===go||i===_o)return a===Yt?r.COMPRESSED_SRGB8_ETC2:r.COMPRESSED_RGB8_ETC2;if(i===vo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:r.COMPRESSED_RGBA8_ETC2_EAC}else return null;if(i===xo||i===So||i===yo||i===Eo||i===Mo||i===To||i===bo||i===Ao||i===wo||i===Ro||i===Co||i===Po||i===Lo||i===Do)if(r=t.get("WEBGL_compressed_texture_astc"),r!==null){if(i===xo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:r.COMPRESSED_RGBA_ASTC_4x4_KHR;if(i===So)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:r.COMPRESSED_RGBA_ASTC_5x4_KHR;if(i===yo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:r.COMPRESSED_RGBA_ASTC_5x5_KHR;if(i===Eo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:r.COMPRESSED_RGBA_ASTC_6x5_KHR;if(i===Mo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:r.COMPRESSED_RGBA_ASTC_6x6_KHR;if(i===To)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:r.COMPRESSED_RGBA_ASTC_8x5_KHR;if(i===bo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:r.COMPRESSED_RGBA_ASTC_8x6_KHR;if(i===Ao)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:r.COMPRESSED_RGBA_ASTC_8x8_KHR;if(i===wo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:r.COMPRESSED_RGBA_ASTC_10x5_KHR;if(i===Ro)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:r.COMPRESSED_RGBA_ASTC_10x6_KHR;if(i===Co)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:r.COMPRESSED_RGBA_ASTC_10x8_KHR;if(i===Po)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:r.COMPRESSED_RGBA_ASTC_10x10_KHR;if(i===Lo)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:r.COMPRESSED_RGBA_ASTC_12x10_KHR;if(i===Do)return a===Yt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:r.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(i===Cr||i===Io||i===Uo)if(r=t.get("EXT_texture_compression_bptc"),r!==null){if(i===Cr)return a===Yt?r.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:r.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(i===Io)return r.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(i===Uo)return r.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(i===pu||i===No||i===Oo||i===Fo)if(r=t.get("EXT_texture_compression_rgtc"),r!==null){if(i===Cr)return r.COMPRESSED_RED_RGTC1_EXT;if(i===No)return r.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(i===Oo)return r.COMPRESSED_RED_GREEN_RGTC2_EXT;if(i===Fo)return r.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return i===Ls?n.UNSIGNED_INT_24_8:n[i]!==void 0?n[i]:null}return{convert:e}}const x_=`
void main() {

	gl_Position = vec4( position, 1.0 );

}`,S_=`
uniform sampler2DArray depthColor;
uniform float depthWidth;
uniform float depthHeight;

void main() {

	vec2 coord = vec2( gl_FragCoord.x / depthWidth, gl_FragCoord.y / depthHeight );

	if ( coord.x >= 1.0 ) {

		gl_FragDepth = texture( depthColor, vec3( coord.x - 1.0, coord.y, 1 ) ).r;

	} else {

		gl_FragDepth = texture( depthColor, vec3( coord.x, coord.y, 0 ) ).r;

	}

}`;class y_{constructor(){this.texture=null,this.mesh=null,this.depthNear=0,this.depthFar=0}init(t,e,i){if(this.texture===null){const s=new Be,r=t.properties.get(s);r.__webglTexture=e.texture,(e.depthNear!==i.depthNear||e.depthFar!==i.depthFar)&&(this.depthNear=e.depthNear,this.depthFar=e.depthFar),this.texture=s}}getMesh(t){if(this.texture!==null&&this.mesh===null){const e=t.cameras[0].viewport,i=new _n({vertexShader:x_,fragmentShader:S_,uniforms:{depthColor:{value:this.texture},depthWidth:{value:e.z},depthHeight:{value:e.w}}});this.mesh=new mn(new Jr(20,20),i)}return this.mesh}reset(){this.texture=null,this.mesh=null}getDepthTexture(){return this.texture}}class E_ extends wi{constructor(t,e){super();const i=this;let s=null,r=1,a=null,o="local-floor",l=1,c=null,u=null,d=null,h=null,p=null,_=null;const S=new y_,m=e.getContextAttributes();let f=null,b=null;const M=[],y=[],P=new Tt;let R=null;const A=new Ge;A.viewport=new Kt;const I=new Ge;I.viewport=new Kt;const E=[A,I],x=new zh;let C=null,V=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(W){let tt=M[W];return tt===void 0&&(tt=new wa,M[W]=tt),tt.getTargetRaySpace()},this.getControllerGrip=function(W){let tt=M[W];return tt===void 0&&(tt=new wa,M[W]=tt),tt.getGripSpace()},this.getHand=function(W){let tt=M[W];return tt===void 0&&(tt=new wa,M[W]=tt),tt.getHandSpace()};function z(W){const tt=y.indexOf(W.inputSource);if(tt===-1)return;const mt=M[tt];mt!==void 0&&(mt.update(W.inputSource,W.frame,c||a),mt.dispatchEvent({type:W.type,data:W.inputSource}))}function Y(){s.removeEventListener("select",z),s.removeEventListener("selectstart",z),s.removeEventListener("selectend",z),s.removeEventListener("squeeze",z),s.removeEventListener("squeezestart",z),s.removeEventListener("squeezeend",z),s.removeEventListener("end",Y),s.removeEventListener("inputsourceschange",j);for(let W=0;W<M.length;W++){const tt=y[W];tt!==null&&(y[W]=null,M[W].disconnect(tt))}C=null,V=null,S.reset(),t.setRenderTarget(f),p=null,h=null,d=null,s=null,b=null,Zt.stop(),i.isPresenting=!1,t.setPixelRatio(R),t.setSize(P.width,P.height,!1),i.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(W){r=W,i.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(W){o=W,i.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return c||a},this.setReferenceSpace=function(W){c=W},this.getBaseLayer=function(){return h!==null?h:p},this.getBinding=function(){return d},this.getFrame=function(){return _},this.getSession=function(){return s},this.setSession=async function(W){if(s=W,s!==null){if(f=t.getRenderTarget(),s.addEventListener("select",z),s.addEventListener("selectstart",z),s.addEventListener("selectend",z),s.addEventListener("squeeze",z),s.addEventListener("squeezestart",z),s.addEventListener("squeezeend",z),s.addEventListener("end",Y),s.addEventListener("inputsourceschange",j),m.xrCompatible!==!0&&await e.makeXRCompatible(),R=t.getPixelRatio(),t.getSize(P),typeof XRWebGLBinding<"u"&&"createProjectionLayer"in XRWebGLBinding.prototype){let mt=null,st=null,Et=null;m.depth&&(Et=m.stencil?e.DEPTH24_STENCIL8:e.DEPTH_COMPONENT24,mt=m.stencil?Is:Ds,st=m.stencil?Ls:Mi);const Wt={colorFormat:e.RGBA8,depthFormat:Et,scaleFactor:r};d=new XRWebGLBinding(s,e),h=d.createProjectionLayer(Wt),s.updateRenderState({layers:[h]}),t.setPixelRatio(1),t.setSize(h.textureWidth,h.textureHeight,!1),b=new Ti(h.textureWidth,h.textureHeight,{format:pn,type:Wn,depthTexture:new bu(h.textureWidth,h.textureHeight,st,void 0,void 0,void 0,void 0,void 0,void 0,mt),stencilBuffer:m.stencil,colorSpace:t.outputColorSpace,samples:m.antialias?4:0,resolveDepthBuffer:h.ignoreDepthValues===!1,resolveStencilBuffer:h.ignoreDepthValues===!1})}else{const mt={antialias:m.antialias,alpha:!0,depth:m.depth,stencil:m.stencil,framebufferScaleFactor:r};p=new XRWebGLLayer(s,e,mt),s.updateRenderState({baseLayer:p}),t.setPixelRatio(1),t.setSize(p.framebufferWidth,p.framebufferHeight,!1),b=new Ti(p.framebufferWidth,p.framebufferHeight,{format:pn,type:Wn,colorSpace:t.outputColorSpace,stencilBuffer:m.stencil,resolveDepthBuffer:p.ignoreDepthValues===!1,resolveStencilBuffer:p.ignoreDepthValues===!1})}b.isXRRenderTarget=!0,this.setFoveation(l),c=null,a=await s.requestReferenceSpace(o),Zt.setContext(s),Zt.start(),i.isPresenting=!0,i.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(s!==null)return s.environmentBlendMode},this.getDepthTexture=function(){return S.getDepthTexture()};function j(W){for(let tt=0;tt<W.removed.length;tt++){const mt=W.removed[tt],st=y.indexOf(mt);st>=0&&(y[st]=null,M[st].disconnect(mt))}for(let tt=0;tt<W.added.length;tt++){const mt=W.added[tt];let st=y.indexOf(mt);if(st===-1){for(let Wt=0;Wt<M.length;Wt++)if(Wt>=y.length){y.push(mt),st=Wt;break}else if(y[Wt]===null){y[Wt]=mt,st=Wt;break}if(st===-1)break}const Et=M[st];Et&&Et.connect(mt)}}const X=new L,Z=new L;function H(W,tt,mt){X.setFromMatrixPosition(tt.matrixWorld),Z.setFromMatrixPosition(mt.matrixWorld);const st=X.distanceTo(Z),Et=tt.projectionMatrix.elements,Wt=mt.projectionMatrix.elements,bt=Et[14]/(Et[10]-1),oe=Et[14]/(Et[10]+1),ne=(Et[9]+1)/Et[5],Ot=(Et[9]-1)/Et[5],w=(Et[8]-1)/Et[0],qe=(Wt[8]+1)/Wt[0],zt=bt*w,Ft=bt*qe,xt=st/(-w+qe),Qt=xt*-w;if(tt.matrixWorld.decompose(W.position,W.quaternion,W.scale),W.translateX(Qt),W.translateZ(xt),W.matrixWorld.compose(W.position,W.quaternion,W.scale),W.matrixWorldInverse.copy(W.matrixWorld).invert(),Et[10]===-1)W.projectionMatrix.copy(tt.projectionMatrix),W.projectionMatrixInverse.copy(tt.projectionMatrixInverse);else{const _t=bt+xt,T=oe+xt,g=zt-Qt,O=Ft+(st-Qt),$=ne*oe/T*_t,K=Ot*oe/T*_t;W.projectionMatrix.makePerspective(g,O,$,K,_t,T),W.projectionMatrixInverse.copy(W.projectionMatrix).invert()}}function it(W,tt){tt===null?W.matrixWorld.copy(W.matrix):W.matrixWorld.multiplyMatrices(tt.matrixWorld,W.matrix),W.matrixWorldInverse.copy(W.matrixWorld).invert()}this.updateCamera=function(W){if(s===null)return;let tt=W.near,mt=W.far;S.texture!==null&&(S.depthNear>0&&(tt=S.depthNear),S.depthFar>0&&(mt=S.depthFar)),x.near=I.near=A.near=tt,x.far=I.far=A.far=mt,(C!==x.near||V!==x.far)&&(s.updateRenderState({depthNear:x.near,depthFar:x.far}),C=x.near,V=x.far),A.layers.mask=W.layers.mask|2,I.layers.mask=W.layers.mask|4,x.layers.mask=A.layers.mask|I.layers.mask;const st=W.parent,Et=x.cameras;it(x,st);for(let Wt=0;Wt<Et.length;Wt++)it(Et[Wt],st);Et.length===2?H(x,A,I):x.projectionMatrix.copy(A.projectionMatrix),ut(W,x,st)};function ut(W,tt,mt){mt===null?W.matrix.copy(tt.matrixWorld):(W.matrix.copy(mt.matrixWorld),W.matrix.invert(),W.matrix.multiply(tt.matrixWorld)),W.matrix.decompose(W.position,W.quaternion,W.scale),W.updateMatrixWorld(!0),W.projectionMatrix.copy(tt.projectionMatrix),W.projectionMatrixInverse.copy(tt.projectionMatrixInverse),W.isPerspectiveCamera&&(W.fov=Bo*2*Math.atan(1/W.projectionMatrix.elements[5]),W.zoom=1)}this.getCamera=function(){return x},this.getFoveation=function(){if(!(h===null&&p===null))return l},this.setFoveation=function(W){l=W,h!==null&&(h.fixedFoveation=W),p!==null&&p.fixedFoveation!==void 0&&(p.fixedFoveation=W)},this.hasDepthSensing=function(){return S.texture!==null},this.getDepthSensingMesh=function(){return S.getMesh(x)};let vt=null;function Ut(W,tt){if(u=tt.getViewerPose(c||a),_=tt,u!==null){const mt=u.views;p!==null&&(t.setRenderTargetFramebuffer(b,p.framebuffer),t.setRenderTarget(b));let st=!1;mt.length!==x.cameras.length&&(x.cameras.length=0,st=!0);for(let bt=0;bt<mt.length;bt++){const oe=mt[bt];let ne=null;if(p!==null)ne=p.getViewport(oe);else{const w=d.getViewSubImage(h,oe);ne=w.viewport,bt===0&&(t.setRenderTargetTextures(b,w.colorTexture,w.depthStencilTexture),t.setRenderTarget(b))}let Ot=E[bt];Ot===void 0&&(Ot=new Ge,Ot.layers.enable(bt),Ot.viewport=new Kt,E[bt]=Ot),Ot.matrix.fromArray(oe.transform.matrix),Ot.matrix.decompose(Ot.position,Ot.quaternion,Ot.scale),Ot.projectionMatrix.fromArray(oe.projectionMatrix),Ot.projectionMatrixInverse.copy(Ot.projectionMatrix).invert(),Ot.viewport.set(ne.x,ne.y,ne.width,ne.height),bt===0&&(x.matrix.copy(Ot.matrix),x.matrix.decompose(x.position,x.quaternion,x.scale)),st===!0&&x.cameras.push(Ot)}const Et=s.enabledFeatures;if(Et&&Et.includes("depth-sensing")&&s.depthUsage=="gpu-optimized"&&d){const bt=d.getDepthInformation(mt[0]);bt&&bt.isValid&&bt.texture&&S.init(t,bt,s.renderState)}}for(let mt=0;mt<M.length;mt++){const st=y[mt],Et=M[mt];st!==null&&Et!==void 0&&Et.update(st,tt,c||a)}vt&&vt(W,tt),tt.detectedPlanes&&i.dispatchEvent({type:"planesdetected",data:tt}),_=null}const Zt=new Ru;Zt.setAnimationLoop(Ut),this.setAnimationLoop=function(W){vt=W},this.dispose=function(){}}}const mi=new Xn,M_=new te;function T_(n,t){function e(m,f){m.matrixAutoUpdate===!0&&m.updateMatrix(),f.value.copy(m.matrix)}function i(m,f){f.color.getRGB(m.fogColor.value,Eu(n)),f.isFog?(m.fogNear.value=f.near,m.fogFar.value=f.far):f.isFogExp2&&(m.fogDensity.value=f.density)}function s(m,f,b,M,y){f.isMeshBasicMaterial||f.isMeshLambertMaterial?r(m,f):f.isMeshToonMaterial?(r(m,f),d(m,f)):f.isMeshPhongMaterial?(r(m,f),u(m,f)):f.isMeshStandardMaterial?(r(m,f),h(m,f),f.isMeshPhysicalMaterial&&p(m,f,y)):f.isMeshMatcapMaterial?(r(m,f),_(m,f)):f.isMeshDepthMaterial?r(m,f):f.isMeshDistanceMaterial?(r(m,f),S(m,f)):f.isMeshNormalMaterial?r(m,f):f.isLineBasicMaterial?(a(m,f),f.isLineDashedMaterial&&o(m,f)):f.isPointsMaterial?l(m,f,b,M):f.isSpriteMaterial?c(m,f):f.isShadowMaterial?(m.color.value.copy(f.color),m.opacity.value=f.opacity):f.isShaderMaterial&&(f.uniformsNeedUpdate=!1)}function r(m,f){m.opacity.value=f.opacity,f.color&&m.diffuse.value.copy(f.color),f.emissive&&m.emissive.value.copy(f.emissive).multiplyScalar(f.emissiveIntensity),f.map&&(m.map.value=f.map,e(f.map,m.mapTransform)),f.alphaMap&&(m.alphaMap.value=f.alphaMap,e(f.alphaMap,m.alphaMapTransform)),f.bumpMap&&(m.bumpMap.value=f.bumpMap,e(f.bumpMap,m.bumpMapTransform),m.bumpScale.value=f.bumpScale,f.side===Le&&(m.bumpScale.value*=-1)),f.normalMap&&(m.normalMap.value=f.normalMap,e(f.normalMap,m.normalMapTransform),m.normalScale.value.copy(f.normalScale),f.side===Le&&m.normalScale.value.negate()),f.displacementMap&&(m.displacementMap.value=f.displacementMap,e(f.displacementMap,m.displacementMapTransform),m.displacementScale.value=f.displacementScale,m.displacementBias.value=f.displacementBias),f.emissiveMap&&(m.emissiveMap.value=f.emissiveMap,e(f.emissiveMap,m.emissiveMapTransform)),f.specularMap&&(m.specularMap.value=f.specularMap,e(f.specularMap,m.specularMapTransform)),f.alphaTest>0&&(m.alphaTest.value=f.alphaTest);const b=t.get(f),M=b.envMap,y=b.envMapRotation;M&&(m.envMap.value=M,mi.copy(y),mi.x*=-1,mi.y*=-1,mi.z*=-1,M.isCubeTexture&&M.isRenderTargetTexture===!1&&(mi.y*=-1,mi.z*=-1),m.envMapRotation.value.setFromMatrix4(M_.makeRotationFromEuler(mi)),m.flipEnvMap.value=M.isCubeTexture&&M.isRenderTargetTexture===!1?-1:1,m.reflectivity.value=f.reflectivity,m.ior.value=f.ior,m.refractionRatio.value=f.refractionRatio),f.lightMap&&(m.lightMap.value=f.lightMap,m.lightMapIntensity.value=f.lightMapIntensity,e(f.lightMap,m.lightMapTransform)),f.aoMap&&(m.aoMap.value=f.aoMap,m.aoMapIntensity.value=f.aoMapIntensity,e(f.aoMap,m.aoMapTransform))}function a(m,f){m.diffuse.value.copy(f.color),m.opacity.value=f.opacity,f.map&&(m.map.value=f.map,e(f.map,m.mapTransform))}function o(m,f){m.dashSize.value=f.dashSize,m.totalSize.value=f.dashSize+f.gapSize,m.scale.value=f.scale}function l(m,f,b,M){m.diffuse.value.copy(f.color),m.opacity.value=f.opacity,m.size.value=f.size*b,m.scale.value=M*.5,f.map&&(m.map.value=f.map,e(f.map,m.uvTransform)),f.alphaMap&&(m.alphaMap.value=f.alphaMap,e(f.alphaMap,m.alphaMapTransform)),f.alphaTest>0&&(m.alphaTest.value=f.alphaTest)}function c(m,f){m.diffuse.value.copy(f.color),m.opacity.value=f.opacity,m.rotation.value=f.rotation,f.map&&(m.map.value=f.map,e(f.map,m.mapTransform)),f.alphaMap&&(m.alphaMap.value=f.alphaMap,e(f.alphaMap,m.alphaMapTransform)),f.alphaTest>0&&(m.alphaTest.value=f.alphaTest)}function u(m,f){m.specular.value.copy(f.specular),m.shininess.value=Math.max(f.shininess,1e-4)}function d(m,f){f.gradientMap&&(m.gradientMap.value=f.gradientMap)}function h(m,f){m.metalness.value=f.metalness,f.metalnessMap&&(m.metalnessMap.value=f.metalnessMap,e(f.metalnessMap,m.metalnessMapTransform)),m.roughness.value=f.roughness,f.roughnessMap&&(m.roughnessMap.value=f.roughnessMap,e(f.roughnessMap,m.roughnessMapTransform)),f.envMap&&(m.envMapIntensity.value=f.envMapIntensity)}function p(m,f,b){m.ior.value=f.ior,f.sheen>0&&(m.sheenColor.value.copy(f.sheenColor).multiplyScalar(f.sheen),m.sheenRoughness.value=f.sheenRoughness,f.sheenColorMap&&(m.sheenColorMap.value=f.sheenColorMap,e(f.sheenColorMap,m.sheenColorMapTransform)),f.sheenRoughnessMap&&(m.sheenRoughnessMap.value=f.sheenRoughnessMap,e(f.sheenRoughnessMap,m.sheenRoughnessMapTransform))),f.clearcoat>0&&(m.clearcoat.value=f.clearcoat,m.clearcoatRoughness.value=f.clearcoatRoughness,f.clearcoatMap&&(m.clearcoatMap.value=f.clearcoatMap,e(f.clearcoatMap,m.clearcoatMapTransform)),f.clearcoatRoughnessMap&&(m.clearcoatRoughnessMap.value=f.clearcoatRoughnessMap,e(f.clearcoatRoughnessMap,m.clearcoatRoughnessMapTransform)),f.clearcoatNormalMap&&(m.clearcoatNormalMap.value=f.clearcoatNormalMap,e(f.clearcoatNormalMap,m.clearcoatNormalMapTransform),m.clearcoatNormalScale.value.copy(f.clearcoatNormalScale),f.side===Le&&m.clearcoatNormalScale.value.negate())),f.dispersion>0&&(m.dispersion.value=f.dispersion),f.iridescence>0&&(m.iridescence.value=f.iridescence,m.iridescenceIOR.value=f.iridescenceIOR,m.iridescenceThicknessMinimum.value=f.iridescenceThicknessRange[0],m.iridescenceThicknessMaximum.value=f.iridescenceThicknessRange[1],f.iridescenceMap&&(m.iridescenceMap.value=f.iridescenceMap,e(f.iridescenceMap,m.iridescenceMapTransform)),f.iridescenceThicknessMap&&(m.iridescenceThicknessMap.value=f.iridescenceThicknessMap,e(f.iridescenceThicknessMap,m.iridescenceThicknessMapTransform))),f.transmission>0&&(m.transmission.value=f.transmission,m.transmissionSamplerMap.value=b.texture,m.transmissionSamplerSize.value.set(b.width,b.height),f.transmissionMap&&(m.transmissionMap.value=f.transmissionMap,e(f.transmissionMap,m.transmissionMapTransform)),m.thickness.value=f.thickness,f.thicknessMap&&(m.thicknessMap.value=f.thicknessMap,e(f.thicknessMap,m.thicknessMapTransform)),m.attenuationDistance.value=f.attenuationDistance,m.attenuationColor.value.copy(f.attenuationColor)),f.anisotropy>0&&(m.anisotropyVector.value.set(f.anisotropy*Math.cos(f.anisotropyRotation),f.anisotropy*Math.sin(f.anisotropyRotation)),f.anisotropyMap&&(m.anisotropyMap.value=f.anisotropyMap,e(f.anisotropyMap,m.anisotropyMapTransform))),m.specularIntensity.value=f.specularIntensity,m.specularColor.value.copy(f.specularColor),f.specularColorMap&&(m.specularColorMap.value=f.specularColorMap,e(f.specularColorMap,m.specularColorMapTransform)),f.specularIntensityMap&&(m.specularIntensityMap.value=f.specularIntensityMap,e(f.specularIntensityMap,m.specularIntensityMapTransform))}function _(m,f){f.matcap&&(m.matcap.value=f.matcap)}function S(m,f){const b=t.get(f).light;m.referencePosition.value.setFromMatrixPosition(b.matrixWorld),m.nearDistance.value=b.shadow.camera.near,m.farDistance.value=b.shadow.camera.far}return{refreshFogUniforms:i,refreshMaterialUniforms:s}}function b_(n,t,e,i){let s={},r={},a=[];const o=n.getParameter(n.MAX_UNIFORM_BUFFER_BINDINGS);function l(b,M){const y=M.program;i.uniformBlockBinding(b,y)}function c(b,M){let y=s[b.id];y===void 0&&(_(b),y=u(b),s[b.id]=y,b.addEventListener("dispose",m));const P=M.program;i.updateUBOMapping(b,P);const R=t.render.frame;r[b.id]!==R&&(h(b),r[b.id]=R)}function u(b){const M=d();b.__bindingPointIndex=M;const y=n.createBuffer(),P=b.__size,R=b.usage;return n.bindBuffer(n.UNIFORM_BUFFER,y),n.bufferData(n.UNIFORM_BUFFER,P,R),n.bindBuffer(n.UNIFORM_BUFFER,null),n.bindBufferBase(n.UNIFORM_BUFFER,M,y),y}function d(){for(let b=0;b<o;b++)if(a.indexOf(b)===-1)return a.push(b),b;return console.error("THREE.WebGLRenderer: Maximum number of simultaneously usable uniforms groups reached."),0}function h(b){const M=s[b.id],y=b.uniforms,P=b.__cache;n.bindBuffer(n.UNIFORM_BUFFER,M);for(let R=0,A=y.length;R<A;R++){const I=Array.isArray(y[R])?y[R]:[y[R]];for(let E=0,x=I.length;E<x;E++){const C=I[E];if(p(C,R,E,P)===!0){const V=C.__offset,z=Array.isArray(C.value)?C.value:[C.value];let Y=0;for(let j=0;j<z.length;j++){const X=z[j],Z=S(X);typeof X=="number"||typeof X=="boolean"?(C.__data[0]=X,n.bufferSubData(n.UNIFORM_BUFFER,V+Y,C.__data)):X.isMatrix3?(C.__data[0]=X.elements[0],C.__data[1]=X.elements[1],C.__data[2]=X.elements[2],C.__data[3]=0,C.__data[4]=X.elements[3],C.__data[5]=X.elements[4],C.__data[6]=X.elements[5],C.__data[7]=0,C.__data[8]=X.elements[6],C.__data[9]=X.elements[7],C.__data[10]=X.elements[8],C.__data[11]=0):(X.toArray(C.__data,Y),Y+=Z.storage/Float32Array.BYTES_PER_ELEMENT)}n.bufferSubData(n.UNIFORM_BUFFER,V,C.__data)}}}n.bindBuffer(n.UNIFORM_BUFFER,null)}function p(b,M,y,P){const R=b.value,A=M+"_"+y;if(P[A]===void 0)return typeof R=="number"||typeof R=="boolean"?P[A]=R:P[A]=R.clone(),!0;{const I=P[A];if(typeof R=="number"||typeof R=="boolean"){if(I!==R)return P[A]=R,!0}else if(I.equals(R)===!1)return I.copy(R),!0}return!1}function _(b){const M=b.uniforms;let y=0;const P=16;for(let A=0,I=M.length;A<I;A++){const E=Array.isArray(M[A])?M[A]:[M[A]];for(let x=0,C=E.length;x<C;x++){const V=E[x],z=Array.isArray(V.value)?V.value:[V.value];for(let Y=0,j=z.length;Y<j;Y++){const X=z[Y],Z=S(X),H=y%P,it=H%Z.boundary,ut=H+it;y+=it,ut!==0&&P-ut<Z.storage&&(y+=P-ut),V.__data=new Float32Array(Z.storage/Float32Array.BYTES_PER_ELEMENT),V.__offset=y,y+=Z.storage}}}const R=y%P;return R>0&&(y+=P-R),b.__size=y,b.__cache={},this}function S(b){const M={boundary:0,storage:0};return typeof b=="number"||typeof b=="boolean"?(M.boundary=4,M.storage=4):b.isVector2?(M.boundary=8,M.storage=8):b.isVector3||b.isColor?(M.boundary=16,M.storage=12):b.isVector4?(M.boundary=16,M.storage=16):b.isMatrix3?(M.boundary=48,M.storage=48):b.isMatrix4?(M.boundary=64,M.storage=64):b.isTexture?console.warn("THREE.WebGLRenderer: Texture samplers can not be part of an uniforms group."):console.warn("THREE.WebGLRenderer: Unsupported uniform value type.",b),M}function m(b){const M=b.target;M.removeEventListener("dispose",m);const y=a.indexOf(M.__bindingPointIndex);a.splice(y,1),n.deleteBuffer(s[M.id]),delete s[M.id],delete r[M.id]}function f(){for(const b in s)n.deleteBuffer(s[b]);a=[],s={},r={}}return{bind:l,update:c,dispose:f}}class A_{constructor(t={}){const{canvas:e=th(),context:i=null,depth:s=!0,stencil:r=!1,alpha:a=!1,antialias:o=!1,premultipliedAlpha:l=!0,preserveDrawingBuffer:c=!1,powerPreference:u="default",failIfMajorPerformanceCaveat:d=!1,reverseDepthBuffer:h=!1}=t;this.isWebGLRenderer=!0;let p;if(i!==null){if(typeof WebGLRenderingContext<"u"&&i instanceof WebGLRenderingContext)throw new Error("THREE.WebGLRenderer: WebGL 1 is not supported since r163.");p=i.getContextAttributes().alpha}else p=a;const _=new Uint32Array(4),S=new Int32Array(4);let m=null,f=null;const b=[],M=[];this.domElement=e,this.debug={checkShaderErrors:!0,onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this.toneMapping=ai,this.toneMappingExposure=1,this.transmissionResolutionScale=1;const y=this;let P=!1;this._outputColorSpace=Qe;let R=0,A=0,I=null,E=-1,x=null;const C=new Kt,V=new Kt;let z=null;const Y=new It(0);let j=0,X=e.width,Z=e.height,H=1,it=null,ut=null;const vt=new Kt(0,0,X,Z),Ut=new Kt(0,0,X,Z);let Zt=!1;const W=new ol;let tt=!1,mt=!1;const st=new te,Et=new te,Wt=new L,bt=new Kt,oe={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0};let ne=!1;function Ot(){return I===null?H:1}let w=i;function qe(v,U){return e.getContext(v,U)}try{const v={alpha:!0,depth:s,stencil:r,antialias:o,premultipliedAlpha:l,preserveDrawingBuffer:c,powerPreference:u,failIfMajorPerformanceCaveat:d};if("setAttribute"in e&&e.setAttribute("data-engine",`three.js r${Zo}`),e.addEventListener("webglcontextlost",q,!1),e.addEventListener("webglcontextrestored",lt,!1),e.addEventListener("webglcontextcreationerror",ot,!1),w===null){const U="webgl2";if(w=qe(U,v),w===null)throw qe(U)?new Error("Error creating WebGL context with your selected attributes."):new Error("Error creating WebGL context.")}}catch(v){throw console.error("THREE.WebGLRenderer: "+v.message),v}let zt,Ft,xt,Qt,_t,T,g,O,$,K,G,gt,rt,dt,kt,Q,ht,Mt,wt,ft,Bt,Lt,Jt,D;function at(){zt=new Om(w),zt.init(),Lt=new v_(w,zt),Ft=new Cm(w,zt,t,Lt),xt=new g_(w,zt),Ft.reverseDepthBuffer&&h&&xt.buffers.depth.setReversed(!0),Qt=new zm(w),_t=new i_,T=new __(w,zt,xt,_t,Ft,Lt,Qt),g=new Lm(y),O=new Nm(y),$=new Wh(w),Jt=new wm(w,$),K=new Fm(w,$,Qt,Jt),G=new Hm(w,K,$,Qt),wt=new km(w,Ft,T),Q=new Pm(_t),gt=new n_(y,g,O,zt,Ft,Jt,Q),rt=new T_(y,_t),dt=new r_,kt=new d_(zt),Mt=new Am(y,g,O,xt,G,p,l),ht=new p_(y,G,Ft),D=new b_(w,Qt,Ft,xt),ft=new Rm(w,zt,Qt),Bt=new Bm(w,zt,Qt),Qt.programs=gt.programs,y.capabilities=Ft,y.extensions=zt,y.properties=_t,y.renderLists=dt,y.shadowMap=ht,y.state=xt,y.info=Qt}at();const k=new E_(y,w);this.xr=k,this.getContext=function(){return w},this.getContextAttributes=function(){return w.getContextAttributes()},this.forceContextLoss=function(){const v=zt.get("WEBGL_lose_context");v&&v.loseContext()},this.forceContextRestore=function(){const v=zt.get("WEBGL_lose_context");v&&v.restoreContext()},this.getPixelRatio=function(){return H},this.setPixelRatio=function(v){v!==void 0&&(H=v,this.setSize(X,Z,!1))},this.getSize=function(v){return v.set(X,Z)},this.setSize=function(v,U,F=!0){if(k.isPresenting){console.warn("THREE.WebGLRenderer: Can't change size while VR device is presenting.");return}X=v,Z=U,e.width=Math.floor(v*H),e.height=Math.floor(U*H),F===!0&&(e.style.width=v+"px",e.style.height=U+"px"),this.setViewport(0,0,v,U)},this.getDrawingBufferSize=function(v){return v.set(X*H,Z*H).floor()},this.setDrawingBufferSize=function(v,U,F){X=v,Z=U,H=F,e.width=Math.floor(v*F),e.height=Math.floor(U*F),this.setViewport(0,0,v,U)},this.getCurrentViewport=function(v){return v.copy(C)},this.getViewport=function(v){return v.copy(vt)},this.setViewport=function(v,U,F,B){v.isVector4?vt.set(v.x,v.y,v.z,v.w):vt.set(v,U,F,B),xt.viewport(C.copy(vt).multiplyScalar(H).round())},this.getScissor=function(v){return v.copy(Ut)},this.setScissor=function(v,U,F,B){v.isVector4?Ut.set(v.x,v.y,v.z,v.w):Ut.set(v,U,F,B),xt.scissor(V.copy(Ut).multiplyScalar(H).round())},this.getScissorTest=function(){return Zt},this.setScissorTest=function(v){xt.setScissorTest(Zt=v)},this.setOpaqueSort=function(v){it=v},this.setTransparentSort=function(v){ut=v},this.getClearColor=function(v){return v.copy(Mt.getClearColor())},this.setClearColor=function(){Mt.setClearColor(...arguments)},this.getClearAlpha=function(){return Mt.getClearAlpha()},this.setClearAlpha=function(){Mt.setClearAlpha(...arguments)},this.clear=function(v=!0,U=!0,F=!0){let B=0;if(v){let N=!1;if(I!==null){const J=I.texture.format;N=J===il||J===nl||J===el}if(N){const J=I.texture.type,nt=J===Wn||J===Mi||J===Ps||J===Ls||J===Qo||J===tl,ct=Mt.getClearColor(),pt=Mt.getClearAlpha(),Rt=ct.r,At=ct.g,St=ct.b;nt?(_[0]=Rt,_[1]=At,_[2]=St,_[3]=pt,w.clearBufferuiv(w.COLOR,0,_)):(S[0]=Rt,S[1]=At,S[2]=St,S[3]=pt,w.clearBufferiv(w.COLOR,0,S))}else B|=w.COLOR_BUFFER_BIT}U&&(B|=w.DEPTH_BUFFER_BIT),F&&(B|=w.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),w.clear(B)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.dispose=function(){e.removeEventListener("webglcontextlost",q,!1),e.removeEventListener("webglcontextrestored",lt,!1),e.removeEventListener("webglcontextcreationerror",ot,!1),Mt.dispose(),dt.dispose(),kt.dispose(),_t.dispose(),g.dispose(),O.dispose(),G.dispose(),Jt.dispose(),D.dispose(),gt.dispose(),k.dispose(),k.removeEventListener("sessionstart",xl),k.removeEventListener("sessionend",Sl),li.stop()};function q(v){v.preventDefault(),console.log("THREE.WebGLRenderer: Context Lost."),P=!0}function lt(){console.log("THREE.WebGLRenderer: Context Restored."),P=!1;const v=Qt.autoReset,U=ht.enabled,F=ht.autoUpdate,B=ht.needsUpdate,N=ht.type;at(),Qt.autoReset=v,ht.enabled=U,ht.autoUpdate=F,ht.needsUpdate=B,ht.type=N}function ot(v){console.error("THREE.WebGLRenderer: A WebGL context could not be created. Reason: ",v.statusMessage)}function Ct(v){const U=v.target;U.removeEventListener("dispose",Ct),se(U)}function se(v){be(v),_t.remove(v)}function be(v){const U=_t.get(v).programs;U!==void 0&&(U.forEach(function(F){gt.releaseProgram(F)}),v.isShaderMaterial&&gt.releaseShaderCache(v))}this.renderBufferDirect=function(v,U,F,B,N,J){U===null&&(U=oe);const nt=N.isMesh&&N.matrixWorld.determinant()<0,ct=ed(v,U,F,B,N);xt.setMaterial(B,nt);let pt=F.index,Rt=1;if(B.wireframe===!0){if(pt=K.getWireframeAttribute(F),pt===void 0)return;Rt=2}const At=F.drawRange,St=F.attributes.position;let Ht=At.start*Rt,Xt=(At.start+At.count)*Rt;J!==null&&(Ht=Math.max(Ht,J.start*Rt),Xt=Math.min(Xt,(J.start+J.count)*Rt)),pt!==null?(Ht=Math.max(Ht,0),Xt=Math.min(Xt,pt.count)):St!=null&&(Ht=Math.max(Ht,0),Xt=Math.min(Xt,St.count));const ce=Xt-Ht;if(ce<0||ce===1/0)return;Jt.setup(N,B,ct,F,pt);let re,Vt=ft;if(pt!==null&&(re=$.get(pt),Vt=Bt,Vt.setIndex(re)),N.isMesh)B.wireframe===!0?(xt.setLineWidth(B.wireframeLinewidth*Ot()),Vt.setMode(w.LINES)):Vt.setMode(w.TRIANGLES);else if(N.isLine){let yt=B.linewidth;yt===void 0&&(yt=1),xt.setLineWidth(yt*Ot()),N.isLineSegments?Vt.setMode(w.LINES):N.isLineLoop?Vt.setMode(w.LINE_LOOP):Vt.setMode(w.LINE_STRIP)}else N.isPoints?Vt.setMode(w.POINTS):N.isSprite&&Vt.setMode(w.TRIANGLES);if(N.isBatchedMesh)if(N._multiDrawInstances!==null)Lr("THREE.WebGLRenderer: renderMultiDrawInstances has been deprecated and will be removed in r184. Append to renderMultiDraw arguments and use indirection."),Vt.renderMultiDrawInstances(N._multiDrawStarts,N._multiDrawCounts,N._multiDrawCount,N._multiDrawInstances);else if(zt.get("WEBGL_multi_draw"))Vt.renderMultiDraw(N._multiDrawStarts,N._multiDrawCounts,N._multiDrawCount);else{const yt=N._multiDrawStarts,ye=N._multiDrawCounts,$t=N._multiDrawCount,on=pt?$.get(pt).bytesPerElement:1,Ri=_t.get(B).currentProgram.getUniforms();for(let ze=0;ze<$t;ze++)Ri.setValue(w,"_gl_DrawID",ze),Vt.render(yt[ze]/on,ye[ze])}else if(N.isInstancedMesh)Vt.renderInstances(Ht,ce,N.count);else if(F.isInstancedBufferGeometry){const yt=F._maxInstanceCount!==void 0?F._maxInstanceCount:1/0,ye=Math.min(F.instanceCount,yt);Vt.renderInstances(Ht,ce,ye)}else Vt.render(Ht,ce)};function qt(v,U,F){v.transparent===!0&&v.side===zn&&v.forceSinglePass===!1?(v.side=Le,v.needsUpdate=!0,qs(v,U,F),v.side=oi,v.needsUpdate=!0,qs(v,U,F),v.side=zn):qs(v,U,F)}this.compile=function(v,U,F=null){F===null&&(F=v),f=kt.get(F),f.init(U),M.push(f),F.traverseVisible(function(N){N.isLight&&N.layers.test(U.layers)&&(f.pushLight(N),N.castShadow&&f.pushShadow(N))}),v!==F&&v.traverseVisible(function(N){N.isLight&&N.layers.test(U.layers)&&(f.pushLight(N),N.castShadow&&f.pushShadow(N))}),f.setupLights();const B=new Set;return v.traverse(function(N){if(!(N.isMesh||N.isPoints||N.isLine||N.isSprite))return;const J=N.material;if(J)if(Array.isArray(J))for(let nt=0;nt<J.length;nt++){const ct=J[nt];qt(ct,F,N),B.add(ct)}else qt(J,F,N),B.add(J)}),f=M.pop(),B},this.compileAsync=function(v,U,F=null){const B=this.compile(v,U,F);return new Promise(N=>{function J(){if(B.forEach(function(nt){_t.get(nt).currentProgram.isReady()&&B.delete(nt)}),B.size===0){N(v);return}setTimeout(J,10)}zt.get("KHR_parallel_shader_compile")!==null?J():setTimeout(J,10)})};let an=null;function Pn(v){an&&an(v)}function xl(){li.stop()}function Sl(){li.start()}const li=new Ru;li.setAnimationLoop(Pn),typeof self<"u"&&li.setContext(self),this.setAnimationLoop=function(v){an=v,k.setAnimationLoop(v),v===null?li.stop():li.start()},k.addEventListener("sessionstart",xl),k.addEventListener("sessionend",Sl),this.render=function(v,U){if(U!==void 0&&U.isCamera!==!0){console.error("THREE.WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(P===!0)return;if(v.matrixWorldAutoUpdate===!0&&v.updateMatrixWorld(),U.parent===null&&U.matrixWorldAutoUpdate===!0&&U.updateMatrixWorld(),k.enabled===!0&&k.isPresenting===!0&&(k.cameraAutoUpdate===!0&&k.updateCamera(U),U=k.getCamera()),v.isScene===!0&&v.onBeforeRender(y,v,U,I),f=kt.get(v,M.length),f.init(U),M.push(f),Et.multiplyMatrices(U.projectionMatrix,U.matrixWorldInverse),W.setFromProjectionMatrix(Et),mt=this.localClippingEnabled,tt=Q.init(this.clippingPlanes,mt),m=dt.get(v,b.length),m.init(),b.push(m),k.enabled===!0&&k.isPresenting===!0){const J=y.xr.getDepthSensingMesh();J!==null&&ia(J,U,-1/0,y.sortObjects)}ia(v,U,0,y.sortObjects),m.finish(),y.sortObjects===!0&&m.sort(it,ut),ne=k.enabled===!1||k.isPresenting===!1||k.hasDepthSensing()===!1,ne&&Mt.addToRenderList(m,v),this.info.render.frame++,tt===!0&&Q.beginShadows();const F=f.state.shadowsArray;ht.render(F,v,U),tt===!0&&Q.endShadows(),this.info.autoReset===!0&&this.info.reset();const B=m.opaque,N=m.transmissive;if(f.setupLights(),U.isArrayCamera){const J=U.cameras;if(N.length>0)for(let nt=0,ct=J.length;nt<ct;nt++){const pt=J[nt];El(B,N,v,pt)}ne&&Mt.render(v);for(let nt=0,ct=J.length;nt<ct;nt++){const pt=J[nt];yl(m,v,pt,pt.viewport)}}else N.length>0&&El(B,N,v,U),ne&&Mt.render(v),yl(m,v,U);I!==null&&A===0&&(T.updateMultisampleRenderTarget(I),T.updateRenderTargetMipmap(I)),v.isScene===!0&&v.onAfterRender(y,v,U),Jt.resetDefaultState(),E=-1,x=null,M.pop(),M.length>0?(f=M[M.length-1],tt===!0&&Q.setGlobalState(y.clippingPlanes,f.state.camera)):f=null,b.pop(),b.length>0?m=b[b.length-1]:m=null};function ia(v,U,F,B){if(v.visible===!1)return;if(v.layers.test(U.layers)){if(v.isGroup)F=v.renderOrder;else if(v.isLOD)v.autoUpdate===!0&&v.update(U);else if(v.isLight)f.pushLight(v),v.castShadow&&f.pushShadow(v);else if(v.isSprite){if(!v.frustumCulled||W.intersectsSprite(v)){B&&bt.setFromMatrixPosition(v.matrixWorld).applyMatrix4(Et);const nt=G.update(v),ct=v.material;ct.visible&&m.push(v,nt,ct,F,bt.z,null)}}else if((v.isMesh||v.isLine||v.isPoints)&&(!v.frustumCulled||W.intersectsObject(v))){const nt=G.update(v),ct=v.material;if(B&&(v.boundingSphere!==void 0?(v.boundingSphere===null&&v.computeBoundingSphere(),bt.copy(v.boundingSphere.center)):(nt.boundingSphere===null&&nt.computeBoundingSphere(),bt.copy(nt.boundingSphere.center)),bt.applyMatrix4(v.matrixWorld).applyMatrix4(Et)),Array.isArray(ct)){const pt=nt.groups;for(let Rt=0,At=pt.length;Rt<At;Rt++){const St=pt[Rt],Ht=ct[St.materialIndex];Ht&&Ht.visible&&m.push(v,nt,Ht,F,bt.z,St)}}else ct.visible&&m.push(v,nt,ct,F,bt.z,null)}}const J=v.children;for(let nt=0,ct=J.length;nt<ct;nt++)ia(J[nt],U,F,B)}function yl(v,U,F,B){const N=v.opaque,J=v.transmissive,nt=v.transparent;f.setupLightsView(F),tt===!0&&Q.setGlobalState(y.clippingPlanes,F),B&&xt.viewport(C.copy(B)),N.length>0&&$s(N,U,F),J.length>0&&$s(J,U,F),nt.length>0&&$s(nt,U,F),xt.buffers.depth.setTest(!0),xt.buffers.depth.setMask(!0),xt.buffers.color.setMask(!0),xt.setPolygonOffset(!1)}function El(v,U,F,B){if((F.isScene===!0?F.overrideMaterial:null)!==null)return;f.state.transmissionRenderTarget[B.id]===void 0&&(f.state.transmissionRenderTarget[B.id]=new Ti(1,1,{generateMipmaps:!0,type:zt.has("EXT_color_buffer_half_float")||zt.has("EXT_color_buffer_float")?zs:Wn,minFilter:Si,samples:4,stencilBuffer:r,resolveDepthBuffer:!1,resolveStencilBuffer:!1,colorSpace:Gt.workingColorSpace}));const J=f.state.transmissionRenderTarget[B.id],nt=B.viewport||C;J.setSize(nt.z*y.transmissionResolutionScale,nt.w*y.transmissionResolutionScale);const ct=y.getRenderTarget();y.setRenderTarget(J),y.getClearColor(Y),j=y.getClearAlpha(),j<1&&y.setClearColor(16777215,.5),y.clear(),ne&&Mt.render(F);const pt=y.toneMapping;y.toneMapping=ai;const Rt=B.viewport;if(B.viewport!==void 0&&(B.viewport=void 0),f.setupLightsView(B),tt===!0&&Q.setGlobalState(y.clippingPlanes,B),$s(v,F,B),T.updateMultisampleRenderTarget(J),T.updateRenderTargetMipmap(J),zt.has("WEBGL_multisampled_render_to_texture")===!1){let At=!1;for(let St=0,Ht=U.length;St<Ht;St++){const Xt=U[St],ce=Xt.object,re=Xt.geometry,Vt=Xt.material,yt=Xt.group;if(Vt.side===zn&&ce.layers.test(B.layers)){const ye=Vt.side;Vt.side=Le,Vt.needsUpdate=!0,Ml(ce,F,B,re,Vt,yt),Vt.side=ye,Vt.needsUpdate=!0,At=!0}}At===!0&&(T.updateMultisampleRenderTarget(J),T.updateRenderTargetMipmap(J))}y.setRenderTarget(ct),y.setClearColor(Y,j),Rt!==void 0&&(B.viewport=Rt),y.toneMapping=pt}function $s(v,U,F){const B=U.isScene===!0?U.overrideMaterial:null;for(let N=0,J=v.length;N<J;N++){const nt=v[N],ct=nt.object,pt=nt.geometry,Rt=nt.group;let At=nt.material;At.allowOverride===!0&&B!==null&&(At=B),ct.layers.test(F.layers)&&Ml(ct,U,F,pt,At,Rt)}}function Ml(v,U,F,B,N,J){v.onBeforeRender(y,U,F,B,N,J),v.modelViewMatrix.multiplyMatrices(F.matrixWorldInverse,v.matrixWorld),v.normalMatrix.getNormalMatrix(v.modelViewMatrix),N.onBeforeRender(y,U,F,B,v,J),N.transparent===!0&&N.side===zn&&N.forceSinglePass===!1?(N.side=Le,N.needsUpdate=!0,y.renderBufferDirect(F,U,B,N,v,J),N.side=oi,N.needsUpdate=!0,y.renderBufferDirect(F,U,B,N,v,J),N.side=zn):y.renderBufferDirect(F,U,B,N,v,J),v.onAfterRender(y,U,F,B,N,J)}function qs(v,U,F){U.isScene!==!0&&(U=oe);const B=_t.get(v),N=f.state.lights,J=f.state.shadowsArray,nt=N.state.version,ct=gt.getParameters(v,N.state,J,U,F),pt=gt.getProgramCacheKey(ct);let Rt=B.programs;B.environment=v.isMeshStandardMaterial?U.environment:null,B.fog=U.fog,B.envMap=(v.isMeshStandardMaterial?O:g).get(v.envMap||B.environment),B.envMapRotation=B.environment!==null&&v.envMap===null?U.environmentRotation:v.envMapRotation,Rt===void 0&&(v.addEventListener("dispose",Ct),Rt=new Map,B.programs=Rt);let At=Rt.get(pt);if(At!==void 0){if(B.currentProgram===At&&B.lightsStateVersion===nt)return bl(v,ct),At}else ct.uniforms=gt.getUniforms(v),v.onBeforeCompile(ct,y),At=gt.acquireProgram(ct,pt),Rt.set(pt,At),B.uniforms=ct.uniforms;const St=B.uniforms;return(!v.isShaderMaterial&&!v.isRawShaderMaterial||v.clipping===!0)&&(St.clippingPlanes=Q.uniform),bl(v,ct),B.needsLights=id(v),B.lightsStateVersion=nt,B.needsLights&&(St.ambientLightColor.value=N.state.ambient,St.lightProbe.value=N.state.probe,St.directionalLights.value=N.state.directional,St.directionalLightShadows.value=N.state.directionalShadow,St.spotLights.value=N.state.spot,St.spotLightShadows.value=N.state.spotShadow,St.rectAreaLights.value=N.state.rectArea,St.ltc_1.value=N.state.rectAreaLTC1,St.ltc_2.value=N.state.rectAreaLTC2,St.pointLights.value=N.state.point,St.pointLightShadows.value=N.state.pointShadow,St.hemisphereLights.value=N.state.hemi,St.directionalShadowMap.value=N.state.directionalShadowMap,St.directionalShadowMatrix.value=N.state.directionalShadowMatrix,St.spotShadowMap.value=N.state.spotShadowMap,St.spotLightMatrix.value=N.state.spotLightMatrix,St.spotLightMap.value=N.state.spotLightMap,St.pointShadowMap.value=N.state.pointShadowMap,St.pointShadowMatrix.value=N.state.pointShadowMatrix),B.currentProgram=At,B.uniformsList=null,At}function Tl(v){if(v.uniformsList===null){const U=v.currentProgram.getUniforms();v.uniformsList=Dr.seqWithValue(U.seq,v.uniforms)}return v.uniformsList}function bl(v,U){const F=_t.get(v);F.outputColorSpace=U.outputColorSpace,F.batching=U.batching,F.batchingColor=U.batchingColor,F.instancing=U.instancing,F.instancingColor=U.instancingColor,F.instancingMorph=U.instancingMorph,F.skinning=U.skinning,F.morphTargets=U.morphTargets,F.morphNormals=U.morphNormals,F.morphColors=U.morphColors,F.morphTargetsCount=U.morphTargetsCount,F.numClippingPlanes=U.numClippingPlanes,F.numIntersection=U.numClipIntersection,F.vertexAlphas=U.vertexAlphas,F.vertexTangents=U.vertexTangents,F.toneMapping=U.toneMapping}function ed(v,U,F,B,N){U.isScene!==!0&&(U=oe),T.resetTextureUnits();const J=U.fog,nt=B.isMeshStandardMaterial?U.environment:null,ct=I===null?y.outputColorSpace:I.isXRRenderTarget===!0?I.texture.colorSpace:ss,pt=(B.isMeshStandardMaterial?O:g).get(B.envMap||nt),Rt=B.vertexColors===!0&&!!F.attributes.color&&F.attributes.color.itemSize===4,At=!!F.attributes.tangent&&(!!B.normalMap||B.anisotropy>0),St=!!F.morphAttributes.position,Ht=!!F.morphAttributes.normal,Xt=!!F.morphAttributes.color;let ce=ai;B.toneMapped&&(I===null||I.isXRRenderTarget===!0)&&(ce=y.toneMapping);const re=F.morphAttributes.position||F.morphAttributes.normal||F.morphAttributes.color,Vt=re!==void 0?re.length:0,yt=_t.get(B),ye=f.state.lights;if(tt===!0&&(mt===!0||v!==x)){const Ce=v===x&&B.id===E;Q.setState(B,v,Ce)}let $t=!1;B.version===yt.__version?(yt.needsLights&&yt.lightsStateVersion!==ye.state.version||yt.outputColorSpace!==ct||N.isBatchedMesh&&yt.batching===!1||!N.isBatchedMesh&&yt.batching===!0||N.isBatchedMesh&&yt.batchingColor===!0&&N.colorTexture===null||N.isBatchedMesh&&yt.batchingColor===!1&&N.colorTexture!==null||N.isInstancedMesh&&yt.instancing===!1||!N.isInstancedMesh&&yt.instancing===!0||N.isSkinnedMesh&&yt.skinning===!1||!N.isSkinnedMesh&&yt.skinning===!0||N.isInstancedMesh&&yt.instancingColor===!0&&N.instanceColor===null||N.isInstancedMesh&&yt.instancingColor===!1&&N.instanceColor!==null||N.isInstancedMesh&&yt.instancingMorph===!0&&N.morphTexture===null||N.isInstancedMesh&&yt.instancingMorph===!1&&N.morphTexture!==null||yt.envMap!==pt||B.fog===!0&&yt.fog!==J||yt.numClippingPlanes!==void 0&&(yt.numClippingPlanes!==Q.numPlanes||yt.numIntersection!==Q.numIntersection)||yt.vertexAlphas!==Rt||yt.vertexTangents!==At||yt.morphTargets!==St||yt.morphNormals!==Ht||yt.morphColors!==Xt||yt.toneMapping!==ce||yt.morphTargetsCount!==Vt)&&($t=!0):($t=!0,yt.__version=B.version);let on=yt.currentProgram;$t===!0&&(on=qs(B,U,N));let Ri=!1,ze=!1,ls=!1;const ee=on.getUniforms(),Ye=yt.uniforms;if(xt.useProgram(on.program)&&(Ri=!0,ze=!0,ls=!0),B.id!==E&&(E=B.id,ze=!0),Ri||x!==v){xt.buffers.depth.getReversed()?(st.copy(v.projectionMatrix),nh(st),ih(st),ee.setValue(w,"projectionMatrix",st)):ee.setValue(w,"projectionMatrix",v.projectionMatrix),ee.setValue(w,"viewMatrix",v.matrixWorldInverse);const De=ee.map.cameraPosition;De!==void 0&&De.setValue(w,Wt.setFromMatrixPosition(v.matrixWorld)),Ft.logarithmicDepthBuffer&&ee.setValue(w,"logDepthBufFC",2/(Math.log(v.far+1)/Math.LN2)),(B.isMeshPhongMaterial||B.isMeshToonMaterial||B.isMeshLambertMaterial||B.isMeshBasicMaterial||B.isMeshStandardMaterial||B.isShaderMaterial)&&ee.setValue(w,"isOrthographic",v.isOrthographicCamera===!0),x!==v&&(x=v,ze=!0,ls=!0)}if(N.isSkinnedMesh){ee.setOptional(w,N,"bindMatrix"),ee.setOptional(w,N,"bindMatrixInverse");const Ce=N.skeleton;Ce&&(Ce.boneTexture===null&&Ce.computeBoneTexture(),ee.setValue(w,"boneTexture",Ce.boneTexture,T))}N.isBatchedMesh&&(ee.setOptional(w,N,"batchingTexture"),ee.setValue(w,"batchingTexture",N._matricesTexture,T),ee.setOptional(w,N,"batchingIdTexture"),ee.setValue(w,"batchingIdTexture",N._indirectTexture,T),ee.setOptional(w,N,"batchingColorTexture"),N._colorsTexture!==null&&ee.setValue(w,"batchingColorTexture",N._colorsTexture,T));const je=F.morphAttributes;if((je.position!==void 0||je.normal!==void 0||je.color!==void 0)&&wt.update(N,F,on),(ze||yt.receiveShadow!==N.receiveShadow)&&(yt.receiveShadow=N.receiveShadow,ee.setValue(w,"receiveShadow",N.receiveShadow)),B.isMeshGouraudMaterial&&B.envMap!==null&&(Ye.envMap.value=pt,Ye.flipEnvMap.value=pt.isCubeTexture&&pt.isRenderTargetTexture===!1?-1:1),B.isMeshStandardMaterial&&B.envMap===null&&U.environment!==null&&(Ye.envMapIntensity.value=U.environmentIntensity),ze&&(ee.setValue(w,"toneMappingExposure",y.toneMappingExposure),yt.needsLights&&nd(Ye,ls),J&&B.fog===!0&&rt.refreshFogUniforms(Ye,J),rt.refreshMaterialUniforms(Ye,B,H,Z,f.state.transmissionRenderTarget[v.id]),Dr.upload(w,Tl(yt),Ye,T)),B.isShaderMaterial&&B.uniformsNeedUpdate===!0&&(Dr.upload(w,Tl(yt),Ye,T),B.uniformsNeedUpdate=!1),B.isSpriteMaterial&&ee.setValue(w,"center",N.center),ee.setValue(w,"modelViewMatrix",N.modelViewMatrix),ee.setValue(w,"normalMatrix",N.normalMatrix),ee.setValue(w,"modelMatrix",N.matrixWorld),B.isShaderMaterial||B.isRawShaderMaterial){const Ce=B.uniformsGroups;for(let De=0,sa=Ce.length;De<sa;De++){const ci=Ce[De];D.update(ci,on),D.bind(ci,on)}}return on}function nd(v,U){v.ambientLightColor.needsUpdate=U,v.lightProbe.needsUpdate=U,v.directionalLights.needsUpdate=U,v.directionalLightShadows.needsUpdate=U,v.pointLights.needsUpdate=U,v.pointLightShadows.needsUpdate=U,v.spotLights.needsUpdate=U,v.spotLightShadows.needsUpdate=U,v.rectAreaLights.needsUpdate=U,v.hemisphereLights.needsUpdate=U}function id(v){return v.isMeshLambertMaterial||v.isMeshToonMaterial||v.isMeshPhongMaterial||v.isMeshStandardMaterial||v.isShadowMaterial||v.isShaderMaterial&&v.lights===!0}this.getActiveCubeFace=function(){return R},this.getActiveMipmapLevel=function(){return A},this.getRenderTarget=function(){return I},this.setRenderTargetTextures=function(v,U,F){const B=_t.get(v);B.__autoAllocateDepthBuffer=v.resolveDepthBuffer===!1,B.__autoAllocateDepthBuffer===!1&&(B.__useRenderToTexture=!1),_t.get(v.texture).__webglTexture=U,_t.get(v.depthTexture).__webglTexture=B.__autoAllocateDepthBuffer?void 0:F,B.__hasExternalTextures=!0},this.setRenderTargetFramebuffer=function(v,U){const F=_t.get(v);F.__webglFramebuffer=U,F.__useDefaultFramebuffer=U===void 0};const sd=w.createFramebuffer();this.setRenderTarget=function(v,U=0,F=0){I=v,R=U,A=F;let B=!0,N=null,J=!1,nt=!1;if(v){const pt=_t.get(v);if(pt.__useDefaultFramebuffer!==void 0)xt.bindFramebuffer(w.FRAMEBUFFER,null),B=!1;else if(pt.__webglFramebuffer===void 0)T.setupRenderTarget(v);else if(pt.__hasExternalTextures)T.rebindTextures(v,_t.get(v.texture).__webglTexture,_t.get(v.depthTexture).__webglTexture);else if(v.depthBuffer){const St=v.depthTexture;if(pt.__boundDepthTexture!==St){if(St!==null&&_t.has(St)&&(v.width!==St.image.width||v.height!==St.image.height))throw new Error("WebGLRenderTarget: Attached DepthTexture is initialized to the incorrect size.");T.setupDepthRenderbuffer(v)}}const Rt=v.texture;(Rt.isData3DTexture||Rt.isDataArrayTexture||Rt.isCompressedArrayTexture)&&(nt=!0);const At=_t.get(v).__webglFramebuffer;v.isWebGLCubeRenderTarget?(Array.isArray(At[U])?N=At[U][F]:N=At[U],J=!0):v.samples>0&&T.useMultisampledRTT(v)===!1?N=_t.get(v).__webglMultisampledFramebuffer:Array.isArray(At)?N=At[F]:N=At,C.copy(v.viewport),V.copy(v.scissor),z=v.scissorTest}else C.copy(vt).multiplyScalar(H).floor(),V.copy(Ut).multiplyScalar(H).floor(),z=Zt;if(F!==0&&(N=sd),xt.bindFramebuffer(w.FRAMEBUFFER,N)&&B&&xt.drawBuffers(v,N),xt.viewport(C),xt.scissor(V),xt.setScissorTest(z),J){const pt=_t.get(v.texture);w.framebufferTexture2D(w.FRAMEBUFFER,w.COLOR_ATTACHMENT0,w.TEXTURE_CUBE_MAP_POSITIVE_X+U,pt.__webglTexture,F)}else if(nt){const pt=_t.get(v.texture),Rt=U;w.framebufferTextureLayer(w.FRAMEBUFFER,w.COLOR_ATTACHMENT0,pt.__webglTexture,F,Rt)}else if(v!==null&&F!==0){const pt=_t.get(v.texture);w.framebufferTexture2D(w.FRAMEBUFFER,w.COLOR_ATTACHMENT0,w.TEXTURE_2D,pt.__webglTexture,F)}E=-1},this.readRenderTargetPixels=function(v,U,F,B,N,J,nt){if(!(v&&v.isWebGLRenderTarget)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let ct=_t.get(v).__webglFramebuffer;if(v.isWebGLCubeRenderTarget&&nt!==void 0&&(ct=ct[nt]),ct){xt.bindFramebuffer(w.FRAMEBUFFER,ct);try{const pt=v.texture,Rt=pt.format,At=pt.type;if(!Ft.textureFormatReadable(Rt)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}if(!Ft.textureTypeReadable(At)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}U>=0&&U<=v.width-B&&F>=0&&F<=v.height-N&&w.readPixels(U,F,B,N,Lt.convert(Rt),Lt.convert(At),J)}finally{const pt=I!==null?_t.get(I).__webglFramebuffer:null;xt.bindFramebuffer(w.FRAMEBUFFER,pt)}}},this.readRenderTargetPixelsAsync=async function(v,U,F,B,N,J,nt){if(!(v&&v.isWebGLRenderTarget))throw new Error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");let ct=_t.get(v).__webglFramebuffer;if(v.isWebGLCubeRenderTarget&&nt!==void 0&&(ct=ct[nt]),ct)if(U>=0&&U<=v.width-B&&F>=0&&F<=v.height-N){xt.bindFramebuffer(w.FRAMEBUFFER,ct);const pt=v.texture,Rt=pt.format,At=pt.type;if(!Ft.textureFormatReadable(Rt))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in RGBA or implementation defined format.");if(!Ft.textureTypeReadable(At))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in UnsignedByteType or implementation defined type.");const St=w.createBuffer();w.bindBuffer(w.PIXEL_PACK_BUFFER,St),w.bufferData(w.PIXEL_PACK_BUFFER,J.byteLength,w.STREAM_READ),w.readPixels(U,F,B,N,Lt.convert(Rt),Lt.convert(At),0);const Ht=I!==null?_t.get(I).__webglFramebuffer:null;xt.bindFramebuffer(w.FRAMEBUFFER,Ht);const Xt=w.fenceSync(w.SYNC_GPU_COMMANDS_COMPLETE,0);return w.flush(),await eh(w,Xt,4),w.bindBuffer(w.PIXEL_PACK_BUFFER,St),w.getBufferSubData(w.PIXEL_PACK_BUFFER,0,J),w.deleteBuffer(St),w.deleteSync(Xt),J}else throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: requested read bounds are out of range.")},this.copyFramebufferToTexture=function(v,U=null,F=0){const B=Math.pow(2,-F),N=Math.floor(v.image.width*B),J=Math.floor(v.image.height*B),nt=U!==null?U.x:0,ct=U!==null?U.y:0;T.setTexture2D(v,0),w.copyTexSubImage2D(w.TEXTURE_2D,F,0,0,nt,ct,N,J),xt.unbindTexture()};const rd=w.createFramebuffer(),ad=w.createFramebuffer();this.copyTextureToTexture=function(v,U,F=null,B=null,N=0,J=null){J===null&&(N!==0?(Lr("WebGLRenderer: copyTextureToTexture function signature has changed to support src and dst mipmap levels."),J=N,N=0):J=0);let nt,ct,pt,Rt,At,St,Ht,Xt,ce;const re=v.isCompressedTexture?v.mipmaps[J]:v.image;if(F!==null)nt=F.max.x-F.min.x,ct=F.max.y-F.min.y,pt=F.isBox3?F.max.z-F.min.z:1,Rt=F.min.x,At=F.min.y,St=F.isBox3?F.min.z:0;else{const je=Math.pow(2,-N);nt=Math.floor(re.width*je),ct=Math.floor(re.height*je),v.isDataArrayTexture?pt=re.depth:v.isData3DTexture?pt=Math.floor(re.depth*je):pt=1,Rt=0,At=0,St=0}B!==null?(Ht=B.x,Xt=B.y,ce=B.z):(Ht=0,Xt=0,ce=0);const Vt=Lt.convert(U.format),yt=Lt.convert(U.type);let ye;U.isData3DTexture?(T.setTexture3D(U,0),ye=w.TEXTURE_3D):U.isDataArrayTexture||U.isCompressedArrayTexture?(T.setTexture2DArray(U,0),ye=w.TEXTURE_2D_ARRAY):(T.setTexture2D(U,0),ye=w.TEXTURE_2D),w.pixelStorei(w.UNPACK_FLIP_Y_WEBGL,U.flipY),w.pixelStorei(w.UNPACK_PREMULTIPLY_ALPHA_WEBGL,U.premultiplyAlpha),w.pixelStorei(w.UNPACK_ALIGNMENT,U.unpackAlignment);const $t=w.getParameter(w.UNPACK_ROW_LENGTH),on=w.getParameter(w.UNPACK_IMAGE_HEIGHT),Ri=w.getParameter(w.UNPACK_SKIP_PIXELS),ze=w.getParameter(w.UNPACK_SKIP_ROWS),ls=w.getParameter(w.UNPACK_SKIP_IMAGES);w.pixelStorei(w.UNPACK_ROW_LENGTH,re.width),w.pixelStorei(w.UNPACK_IMAGE_HEIGHT,re.height),w.pixelStorei(w.UNPACK_SKIP_PIXELS,Rt),w.pixelStorei(w.UNPACK_SKIP_ROWS,At),w.pixelStorei(w.UNPACK_SKIP_IMAGES,St);const ee=v.isDataArrayTexture||v.isData3DTexture,Ye=U.isDataArrayTexture||U.isData3DTexture;if(v.isDepthTexture){const je=_t.get(v),Ce=_t.get(U),De=_t.get(je.__renderTarget),sa=_t.get(Ce.__renderTarget);xt.bindFramebuffer(w.READ_FRAMEBUFFER,De.__webglFramebuffer),xt.bindFramebuffer(w.DRAW_FRAMEBUFFER,sa.__webglFramebuffer);for(let ci=0;ci<pt;ci++)ee&&(w.framebufferTextureLayer(w.READ_FRAMEBUFFER,w.COLOR_ATTACHMENT0,_t.get(v).__webglTexture,N,St+ci),w.framebufferTextureLayer(w.DRAW_FRAMEBUFFER,w.COLOR_ATTACHMENT0,_t.get(U).__webglTexture,J,ce+ci)),w.blitFramebuffer(Rt,At,nt,ct,Ht,Xt,nt,ct,w.DEPTH_BUFFER_BIT,w.NEAREST);xt.bindFramebuffer(w.READ_FRAMEBUFFER,null),xt.bindFramebuffer(w.DRAW_FRAMEBUFFER,null)}else if(N!==0||v.isRenderTargetTexture||_t.has(v)){const je=_t.get(v),Ce=_t.get(U);xt.bindFramebuffer(w.READ_FRAMEBUFFER,rd),xt.bindFramebuffer(w.DRAW_FRAMEBUFFER,ad);for(let De=0;De<pt;De++)ee?w.framebufferTextureLayer(w.READ_FRAMEBUFFER,w.COLOR_ATTACHMENT0,je.__webglTexture,N,St+De):w.framebufferTexture2D(w.READ_FRAMEBUFFER,w.COLOR_ATTACHMENT0,w.TEXTURE_2D,je.__webglTexture,N),Ye?w.framebufferTextureLayer(w.DRAW_FRAMEBUFFER,w.COLOR_ATTACHMENT0,Ce.__webglTexture,J,ce+De):w.framebufferTexture2D(w.DRAW_FRAMEBUFFER,w.COLOR_ATTACHMENT0,w.TEXTURE_2D,Ce.__webglTexture,J),N!==0?w.blitFramebuffer(Rt,At,nt,ct,Ht,Xt,nt,ct,w.COLOR_BUFFER_BIT,w.NEAREST):Ye?w.copyTexSubImage3D(ye,J,Ht,Xt,ce+De,Rt,At,nt,ct):w.copyTexSubImage2D(ye,J,Ht,Xt,Rt,At,nt,ct);xt.bindFramebuffer(w.READ_FRAMEBUFFER,null),xt.bindFramebuffer(w.DRAW_FRAMEBUFFER,null)}else Ye?v.isDataTexture||v.isData3DTexture?w.texSubImage3D(ye,J,Ht,Xt,ce,nt,ct,pt,Vt,yt,re.data):U.isCompressedArrayTexture?w.compressedTexSubImage3D(ye,J,Ht,Xt,ce,nt,ct,pt,Vt,re.data):w.texSubImage3D(ye,J,Ht,Xt,ce,nt,ct,pt,Vt,yt,re):v.isDataTexture?w.texSubImage2D(w.TEXTURE_2D,J,Ht,Xt,nt,ct,Vt,yt,re.data):v.isCompressedTexture?w.compressedTexSubImage2D(w.TEXTURE_2D,J,Ht,Xt,re.width,re.height,Vt,re.data):w.texSubImage2D(w.TEXTURE_2D,J,Ht,Xt,nt,ct,Vt,yt,re);w.pixelStorei(w.UNPACK_ROW_LENGTH,$t),w.pixelStorei(w.UNPACK_IMAGE_HEIGHT,on),w.pixelStorei(w.UNPACK_SKIP_PIXELS,Ri),w.pixelStorei(w.UNPACK_SKIP_ROWS,ze),w.pixelStorei(w.UNPACK_SKIP_IMAGES,ls),J===0&&U.generateMipmaps&&w.generateMipmap(ye),xt.unbindTexture()},this.copyTextureToTexture3D=function(v,U,F=null,B=null,N=0){return Lr('WebGLRenderer: copyTextureToTexture3D function has been deprecated. Use "copyTextureToTexture" instead.'),this.copyTextureToTexture(v,U,F,B,N)},this.initRenderTarget=function(v){_t.get(v).__webglFramebuffer===void 0&&T.setupRenderTarget(v)},this.initTexture=function(v){v.isCubeTexture?T.setTextureCube(v,0):v.isData3DTexture?T.setTexture3D(v,0):v.isDataArrayTexture||v.isCompressedArrayTexture?T.setTexture2DArray(v,0):T.setTexture2D(v,0),xt.unbindTexture()},this.resetState=function(){R=0,A=0,I=null,xt.reset(),Jt.reset()},typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return Vn}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(t){this._outputColorSpace=t;const e=this.getContext();e.drawingBufferColorSpace=Gt._getDrawingBufferColorSpace(t),e.unpackColorSpace=Gt._getUnpackColorSpace()}}const Pc={type:"change"},fl={type:"start"},Iu={type:"end"},_r=new Zr,Lc=new ti,w_=Math.cos(70*Qd.DEG2RAD),he=new L,Ue=2*Math.PI,jt={NONE:-1,ROTATE:0,DOLLY:1,PAN:2,TOUCH_ROTATE:3,TOUCH_PAN:4,TOUCH_DOLLY_PAN:5,TOUCH_DOLLY_ROTATE:6},Ba=1e-6;class R_ extends Vh{constructor(t,e=null){super(t,e),this.state=jt.NONE,this.target=new L,this.cursor=new L,this.minDistance=0,this.maxDistance=1/0,this.minZoom=0,this.maxZoom=1/0,this.minTargetRadius=0,this.maxTargetRadius=1/0,this.minPolarAngle=0,this.maxPolarAngle=Math.PI,this.minAzimuthAngle=-1/0,this.maxAzimuthAngle=1/0,this.enableDamping=!1,this.dampingFactor=.05,this.enableZoom=!0,this.zoomSpeed=1,this.enableRotate=!0,this.rotateSpeed=1,this.keyRotateSpeed=1,this.enablePan=!0,this.panSpeed=1,this.screenSpacePanning=!0,this.keyPanSpeed=7,this.zoomToCursor=!1,this.autoRotate=!1,this.autoRotateSpeed=2,this.keys={LEFT:"ArrowLeft",UP:"ArrowUp",RIGHT:"ArrowRight",BOTTOM:"ArrowDown"},this.mouseButtons={LEFT:ji.ROTATE,MIDDLE:ji.DOLLY,RIGHT:ji.PAN},this.touches={ONE:Wi.ROTATE,TWO:Wi.DOLLY_PAN},this.target0=this.target.clone(),this.position0=this.object.position.clone(),this.zoom0=this.object.zoom,this._domElementKeyEvents=null,this._lastPosition=new L,this._lastQuaternion=new bi,this._lastTargetPosition=new L,this._quat=new bi().setFromUnitVectors(t.up,new L(0,1,0)),this._quatInverse=this._quat.clone().invert(),this._spherical=new sc,this._sphericalDelta=new sc,this._scale=1,this._panOffset=new L,this._rotateStart=new Tt,this._rotateEnd=new Tt,this._rotateDelta=new Tt,this._panStart=new Tt,this._panEnd=new Tt,this._panDelta=new Tt,this._dollyStart=new Tt,this._dollyEnd=new Tt,this._dollyDelta=new Tt,this._dollyDirection=new L,this._mouse=new Tt,this._performCursorZoom=!1,this._pointers=[],this._pointerPositions={},this._controlActive=!1,this._onPointerMove=P_.bind(this),this._onPointerDown=C_.bind(this),this._onPointerUp=L_.bind(this),this._onContextMenu=B_.bind(this),this._onMouseWheel=U_.bind(this),this._onKeyDown=N_.bind(this),this._onTouchStart=O_.bind(this),this._onTouchMove=F_.bind(this),this._onMouseDown=D_.bind(this),this._onMouseMove=I_.bind(this),this._interceptControlDown=z_.bind(this),this._interceptControlUp=k_.bind(this),this.domElement!==null&&this.connect(this.domElement),this.update()}connect(t){super.connect(t),this.domElement.addEventListener("pointerdown",this._onPointerDown),this.domElement.addEventListener("pointercancel",this._onPointerUp),this.domElement.addEventListener("contextmenu",this._onContextMenu),this.domElement.addEventListener("wheel",this._onMouseWheel,{passive:!1}),this.domElement.getRootNode().addEventListener("keydown",this._interceptControlDown,{passive:!0,capture:!0}),this.domElement.style.touchAction="none"}disconnect(){this.domElement.removeEventListener("pointerdown",this._onPointerDown),this.domElement.removeEventListener("pointermove",this._onPointerMove),this.domElement.removeEventListener("pointerup",this._onPointerUp),this.domElement.removeEventListener("pointercancel",this._onPointerUp),this.domElement.removeEventListener("wheel",this._onMouseWheel),this.domElement.removeEventListener("contextmenu",this._onContextMenu),this.stopListenToKeyEvents(),this.domElement.getRootNode().removeEventListener("keydown",this._interceptControlDown,{capture:!0}),this.domElement.style.touchAction="auto"}dispose(){this.disconnect()}getPolarAngle(){return this._spherical.phi}getAzimuthalAngle(){return this._spherical.theta}getDistance(){return this.object.position.distanceTo(this.target)}listenToKeyEvents(t){t.addEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=t}stopListenToKeyEvents(){this._domElementKeyEvents!==null&&(this._domElementKeyEvents.removeEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=null)}saveState(){this.target0.copy(this.target),this.position0.copy(this.object.position),this.zoom0=this.object.zoom}reset(){this.target.copy(this.target0),this.object.position.copy(this.position0),this.object.zoom=this.zoom0,this.object.updateProjectionMatrix(),this.dispatchEvent(Pc),this.update(),this.state=jt.NONE}update(t=null){const e=this.object.position;he.copy(e).sub(this.target),he.applyQuaternion(this._quat),this._spherical.setFromVector3(he),this.autoRotate&&this.state===jt.NONE&&this._rotateLeft(this._getAutoRotationAngle(t)),this.enableDamping?(this._spherical.theta+=this._sphericalDelta.theta*this.dampingFactor,this._spherical.phi+=this._sphericalDelta.phi*this.dampingFactor):(this._spherical.theta+=this._sphericalDelta.theta,this._spherical.phi+=this._sphericalDelta.phi);let i=this.minAzimuthAngle,s=this.maxAzimuthAngle;isFinite(i)&&isFinite(s)&&(i<-Math.PI?i+=Ue:i>Math.PI&&(i-=Ue),s<-Math.PI?s+=Ue:s>Math.PI&&(s-=Ue),i<=s?this._spherical.theta=Math.max(i,Math.min(s,this._spherical.theta)):this._spherical.theta=this._spherical.theta>(i+s)/2?Math.max(i,this._spherical.theta):Math.min(s,this._spherical.theta)),this._spherical.phi=Math.max(this.minPolarAngle,Math.min(this.maxPolarAngle,this._spherical.phi)),this._spherical.makeSafe(),this.enableDamping===!0?this.target.addScaledVector(this._panOffset,this.dampingFactor):this.target.add(this._panOffset),this.target.sub(this.cursor),this.target.clampLength(this.minTargetRadius,this.maxTargetRadius),this.target.add(this.cursor);let r=!1;if(this.zoomToCursor&&this._performCursorZoom||this.object.isOrthographicCamera)this._spherical.radius=this._clampDistance(this._spherical.radius);else{const a=this._spherical.radius;this._spherical.radius=this._clampDistance(this._spherical.radius*this._scale),r=a!=this._spherical.radius}if(he.setFromSpherical(this._spherical),he.applyQuaternion(this._quatInverse),e.copy(this.target).add(he),this.object.lookAt(this.target),this.enableDamping===!0?(this._sphericalDelta.theta*=1-this.dampingFactor,this._sphericalDelta.phi*=1-this.dampingFactor,this._panOffset.multiplyScalar(1-this.dampingFactor)):(this._sphericalDelta.set(0,0,0),this._panOffset.set(0,0,0)),this.zoomToCursor&&this._performCursorZoom){let a=null;if(this.object.isPerspectiveCamera){const o=he.length();a=this._clampDistance(o*this._scale);const l=o-a;this.object.position.addScaledVector(this._dollyDirection,l),this.object.updateMatrixWorld(),r=!!l}else if(this.object.isOrthographicCamera){const o=new L(this._mouse.x,this._mouse.y,0);o.unproject(this.object);const l=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),this.object.updateProjectionMatrix(),r=l!==this.object.zoom;const c=new L(this._mouse.x,this._mouse.y,0);c.unproject(this.object),this.object.position.sub(c).add(o),this.object.updateMatrixWorld(),a=he.length()}else console.warn("WARNING: OrbitControls.js encountered an unknown camera type - zoom to cursor disabled."),this.zoomToCursor=!1;a!==null&&(this.screenSpacePanning?this.target.set(0,0,-1).transformDirection(this.object.matrix).multiplyScalar(a).add(this.object.position):(_r.origin.copy(this.object.position),_r.direction.set(0,0,-1).transformDirection(this.object.matrix),Math.abs(this.object.up.dot(_r.direction))<w_?this.object.lookAt(this.target):(Lc.setFromNormalAndCoplanarPoint(this.object.up,this.target),_r.intersectPlane(Lc,this.target))))}else if(this.object.isOrthographicCamera){const a=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),a!==this.object.zoom&&(this.object.updateProjectionMatrix(),r=!0)}return this._scale=1,this._performCursorZoom=!1,r||this._lastPosition.distanceToSquared(this.object.position)>Ba||8*(1-this._lastQuaternion.dot(this.object.quaternion))>Ba||this._lastTargetPosition.distanceToSquared(this.target)>Ba?(this.dispatchEvent(Pc),this._lastPosition.copy(this.object.position),this._lastQuaternion.copy(this.object.quaternion),this._lastTargetPosition.copy(this.target),!0):!1}_getAutoRotationAngle(t){return t!==null?Ue/60*this.autoRotateSpeed*t:Ue/60/60*this.autoRotateSpeed}_getZoomScale(t){const e=Math.abs(t*.01);return Math.pow(.95,this.zoomSpeed*e)}_rotateLeft(t){this._sphericalDelta.theta-=t}_rotateUp(t){this._sphericalDelta.phi-=t}_panLeft(t,e){he.setFromMatrixColumn(e,0),he.multiplyScalar(-t),this._panOffset.add(he)}_panUp(t,e){this.screenSpacePanning===!0?he.setFromMatrixColumn(e,1):(he.setFromMatrixColumn(e,0),he.crossVectors(this.object.up,he)),he.multiplyScalar(t),this._panOffset.add(he)}_pan(t,e){const i=this.domElement;if(this.object.isPerspectiveCamera){const s=this.object.position;he.copy(s).sub(this.target);let r=he.length();r*=Math.tan(this.object.fov/2*Math.PI/180),this._panLeft(2*t*r/i.clientHeight,this.object.matrix),this._panUp(2*e*r/i.clientHeight,this.object.matrix)}else this.object.isOrthographicCamera?(this._panLeft(t*(this.object.right-this.object.left)/this.object.zoom/i.clientWidth,this.object.matrix),this._panUp(e*(this.object.top-this.object.bottom)/this.object.zoom/i.clientHeight,this.object.matrix)):(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - pan disabled."),this.enablePan=!1)}_dollyOut(t){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale/=t:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_dollyIn(t){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale*=t:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_updateZoomParameters(t,e){if(!this.zoomToCursor)return;this._performCursorZoom=!0;const i=this.domElement.getBoundingClientRect(),s=t-i.left,r=e-i.top,a=i.width,o=i.height;this._mouse.x=s/a*2-1,this._mouse.y=-(r/o)*2+1,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()}_clampDistance(t){return Math.max(this.minDistance,Math.min(this.maxDistance,t))}_handleMouseDownRotate(t){this._rotateStart.set(t.clientX,t.clientY)}_handleMouseDownDolly(t){this._updateZoomParameters(t.clientX,t.clientX),this._dollyStart.set(t.clientX,t.clientY)}_handleMouseDownPan(t){this._panStart.set(t.clientX,t.clientY)}_handleMouseMoveRotate(t){this._rotateEnd.set(t.clientX,t.clientY),this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);const e=this.domElement;this._rotateLeft(Ue*this._rotateDelta.x/e.clientHeight),this._rotateUp(Ue*this._rotateDelta.y/e.clientHeight),this._rotateStart.copy(this._rotateEnd),this.update()}_handleMouseMoveDolly(t){this._dollyEnd.set(t.clientX,t.clientY),this._dollyDelta.subVectors(this._dollyEnd,this._dollyStart),this._dollyDelta.y>0?this._dollyOut(this._getZoomScale(this._dollyDelta.y)):this._dollyDelta.y<0&&this._dollyIn(this._getZoomScale(this._dollyDelta.y)),this._dollyStart.copy(this._dollyEnd),this.update()}_handleMouseMovePan(t){this._panEnd.set(t.clientX,t.clientY),this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd),this.update()}_handleMouseWheel(t){this._updateZoomParameters(t.clientX,t.clientY),t.deltaY<0?this._dollyIn(this._getZoomScale(t.deltaY)):t.deltaY>0&&this._dollyOut(this._getZoomScale(t.deltaY)),this.update()}_handleKeyDown(t){let e=!1;switch(t.code){case this.keys.UP:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateUp(Ue*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(0,this.keyPanSpeed),e=!0;break;case this.keys.BOTTOM:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateUp(-Ue*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(0,-this.keyPanSpeed),e=!0;break;case this.keys.LEFT:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateLeft(Ue*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(this.keyPanSpeed,0),e=!0;break;case this.keys.RIGHT:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateLeft(-Ue*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(-this.keyPanSpeed,0),e=!0;break}e&&(t.preventDefault(),this.update())}_handleTouchStartRotate(t){if(this._pointers.length===1)this._rotateStart.set(t.pageX,t.pageY);else{const e=this._getSecondPointerPosition(t),i=.5*(t.pageX+e.x),s=.5*(t.pageY+e.y);this._rotateStart.set(i,s)}}_handleTouchStartPan(t){if(this._pointers.length===1)this._panStart.set(t.pageX,t.pageY);else{const e=this._getSecondPointerPosition(t),i=.5*(t.pageX+e.x),s=.5*(t.pageY+e.y);this._panStart.set(i,s)}}_handleTouchStartDolly(t){const e=this._getSecondPointerPosition(t),i=t.pageX-e.x,s=t.pageY-e.y,r=Math.sqrt(i*i+s*s);this._dollyStart.set(0,r)}_handleTouchStartDollyPan(t){this.enableZoom&&this._handleTouchStartDolly(t),this.enablePan&&this._handleTouchStartPan(t)}_handleTouchStartDollyRotate(t){this.enableZoom&&this._handleTouchStartDolly(t),this.enableRotate&&this._handleTouchStartRotate(t)}_handleTouchMoveRotate(t){if(this._pointers.length==1)this._rotateEnd.set(t.pageX,t.pageY);else{const i=this._getSecondPointerPosition(t),s=.5*(t.pageX+i.x),r=.5*(t.pageY+i.y);this._rotateEnd.set(s,r)}this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);const e=this.domElement;this._rotateLeft(Ue*this._rotateDelta.x/e.clientHeight),this._rotateUp(Ue*this._rotateDelta.y/e.clientHeight),this._rotateStart.copy(this._rotateEnd)}_handleTouchMovePan(t){if(this._pointers.length===1)this._panEnd.set(t.pageX,t.pageY);else{const e=this._getSecondPointerPosition(t),i=.5*(t.pageX+e.x),s=.5*(t.pageY+e.y);this._panEnd.set(i,s)}this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd)}_handleTouchMoveDolly(t){const e=this._getSecondPointerPosition(t),i=t.pageX-e.x,s=t.pageY-e.y,r=Math.sqrt(i*i+s*s);this._dollyEnd.set(0,r),this._dollyDelta.set(0,Math.pow(this._dollyEnd.y/this._dollyStart.y,this.zoomSpeed)),this._dollyOut(this._dollyDelta.y),this._dollyStart.copy(this._dollyEnd);const a=(t.pageX+e.x)*.5,o=(t.pageY+e.y)*.5;this._updateZoomParameters(a,o)}_handleTouchMoveDollyPan(t){this.enableZoom&&this._handleTouchMoveDolly(t),this.enablePan&&this._handleTouchMovePan(t)}_handleTouchMoveDollyRotate(t){this.enableZoom&&this._handleTouchMoveDolly(t),this.enableRotate&&this._handleTouchMoveRotate(t)}_addPointer(t){this._pointers.push(t.pointerId)}_removePointer(t){delete this._pointerPositions[t.pointerId];for(let e=0;e<this._pointers.length;e++)if(this._pointers[e]==t.pointerId){this._pointers.splice(e,1);return}}_isTrackingPointer(t){for(let e=0;e<this._pointers.length;e++)if(this._pointers[e]==t.pointerId)return!0;return!1}_trackPointer(t){let e=this._pointerPositions[t.pointerId];e===void 0&&(e=new Tt,this._pointerPositions[t.pointerId]=e),e.set(t.pageX,t.pageY)}_getSecondPointerPosition(t){const e=t.pointerId===this._pointers[0]?this._pointers[1]:this._pointers[0];return this._pointerPositions[e]}_customWheelEvent(t){const e=t.deltaMode,i={clientX:t.clientX,clientY:t.clientY,deltaY:t.deltaY};switch(e){case 1:i.deltaY*=16;break;case 2:i.deltaY*=100;break}return t.ctrlKey&&!this._controlActive&&(i.deltaY*=10),i}}function C_(n){this.enabled!==!1&&(this._pointers.length===0&&(this.domElement.setPointerCapture(n.pointerId),this.domElement.addEventListener("pointermove",this._onPointerMove),this.domElement.addEventListener("pointerup",this._onPointerUp)),!this._isTrackingPointer(n)&&(this._addPointer(n),n.pointerType==="touch"?this._onTouchStart(n):this._onMouseDown(n)))}function P_(n){this.enabled!==!1&&(n.pointerType==="touch"?this._onTouchMove(n):this._onMouseMove(n))}function L_(n){switch(this._removePointer(n),this._pointers.length){case 0:this.domElement.releasePointerCapture(n.pointerId),this.domElement.removeEventListener("pointermove",this._onPointerMove),this.domElement.removeEventListener("pointerup",this._onPointerUp),this.dispatchEvent(Iu),this.state=jt.NONE;break;case 1:const t=this._pointers[0],e=this._pointerPositions[t];this._onTouchStart({pointerId:t,pageX:e.x,pageY:e.y});break}}function D_(n){let t;switch(n.button){case 0:t=this.mouseButtons.LEFT;break;case 1:t=this.mouseButtons.MIDDLE;break;case 2:t=this.mouseButtons.RIGHT;break;default:t=-1}switch(t){case ji.DOLLY:if(this.enableZoom===!1)return;this._handleMouseDownDolly(n),this.state=jt.DOLLY;break;case ji.ROTATE:if(n.ctrlKey||n.metaKey||n.shiftKey){if(this.enablePan===!1)return;this._handleMouseDownPan(n),this.state=jt.PAN}else{if(this.enableRotate===!1)return;this._handleMouseDownRotate(n),this.state=jt.ROTATE}break;case ji.PAN:if(n.ctrlKey||n.metaKey||n.shiftKey){if(this.enableRotate===!1)return;this._handleMouseDownRotate(n),this.state=jt.ROTATE}else{if(this.enablePan===!1)return;this._handleMouseDownPan(n),this.state=jt.PAN}break;default:this.state=jt.NONE}this.state!==jt.NONE&&this.dispatchEvent(fl)}function I_(n){switch(this.state){case jt.ROTATE:if(this.enableRotate===!1)return;this._handleMouseMoveRotate(n);break;case jt.DOLLY:if(this.enableZoom===!1)return;this._handleMouseMoveDolly(n);break;case jt.PAN:if(this.enablePan===!1)return;this._handleMouseMovePan(n);break}}function U_(n){this.enabled===!1||this.enableZoom===!1||this.state!==jt.NONE||(n.preventDefault(),this.dispatchEvent(fl),this._handleMouseWheel(this._customWheelEvent(n)),this.dispatchEvent(Iu))}function N_(n){this.enabled!==!1&&this._handleKeyDown(n)}function O_(n){switch(this._trackPointer(n),this._pointers.length){case 1:switch(this.touches.ONE){case Wi.ROTATE:if(this.enableRotate===!1)return;this._handleTouchStartRotate(n),this.state=jt.TOUCH_ROTATE;break;case Wi.PAN:if(this.enablePan===!1)return;this._handleTouchStartPan(n),this.state=jt.TOUCH_PAN;break;default:this.state=jt.NONE}break;case 2:switch(this.touches.TWO){case Wi.DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchStartDollyPan(n),this.state=jt.TOUCH_DOLLY_PAN;break;case Wi.DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchStartDollyRotate(n),this.state=jt.TOUCH_DOLLY_ROTATE;break;default:this.state=jt.NONE}break;default:this.state=jt.NONE}this.state!==jt.NONE&&this.dispatchEvent(fl)}function F_(n){switch(this._trackPointer(n),this.state){case jt.TOUCH_ROTATE:if(this.enableRotate===!1)return;this._handleTouchMoveRotate(n),this.update();break;case jt.TOUCH_PAN:if(this.enablePan===!1)return;this._handleTouchMovePan(n),this.update();break;case jt.TOUCH_DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchMoveDollyPan(n),this.update();break;case jt.TOUCH_DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchMoveDollyRotate(n),this.update();break;default:this.state=jt.NONE}}function B_(n){this.enabled!==!1&&n.preventDefault()}function z_(n){n.key==="Control"&&(this._controlActive=!0,this.domElement.getRootNode().addEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function k_(n){n.key==="Control"&&(this._controlActive=!1,this.domElement.getRootNode().removeEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}let dn,We,ei,Ze,fe,Hr=1,pl=32,H_=new kh,Us=!1,xe=new Tt(0,0),ie=new L(0,0,0);new L(0,0,0);let Vr=new L(0,window.innerWidth<=768?1.2:0,window.innerWidth<=768?14:10),V_=new L(0,0,7),Ai=null,sn={primary:16731714,secondary:12727855,tertiary:16757675};function Dc(){const n=getComputedStyle(document.documentElement),t=n.getPropertyValue("--accent-primary").trim(),e=n.getPropertyValue("--accent-secondary").trim(),i=n.getPropertyValue("--accent-tertiary").trim();sn.primary=new It(t).getHex(),sn.secondary=new It(e).getHex(),sn.tertiary=new It(i).getHex()}let kn=0,vr=0,Uu=0,Nu=0,za=0,ys=0;function G_(n){const t=kn;n==="thinking"?kn=1:n==="responding"?kn=2:(t===2&&(ys=1),kn=0),kn!==t&&(Uu=performance.now())}function W_(n){Nu=n}window.addEventListener("agent-state",n=>G_(n.detail));window.addEventListener("agent-stream",n=>W_(n.detail||0));let Gr=null;function X_(){if(!fe||!We)return{x:window.innerWidth/2,y:window.innerHeight/2};const n=fe.position.clone();return n.project(We),{x:(n.x*.5+.5)*window.innerWidth,y:(-n.y*.5+.5)*window.innerHeight}}function $_(n){Hr=n,Ai=Ns()}function q_(n){pl=n,Ai=Ns()}function Y_(n){const t=n?V_:Vr;gsap.to(We.position,{x:t.x,y:t.y,z:t.z,duration:1.5,ease:"power2.inOut",onUpdate:()=>We.lookAt(0,0,0)})}function Ic(){const n=new xn,t=window.innerWidth<=768?1e3:3e3,e=new Float32Array(t*3),i=new Float32Array(t*3),s=new Float32Array(t),r=new It(sn.primary),a=new It(sn.secondary),o=new It(sn.tertiary);for(let u=0;u<t;u++){e[u*3]=(Math.random()-.5)*100,e[u*3+1]=(Math.random()-.5)*100,e[u*3+2]=(Math.random()-.5)*100;let d;const h=Math.random();h<.33?d=r:h<.66?d=a:d=o,i[u*3]=d.r,i[u*3+1]=d.g,i[u*3+2]=d.b,s[u]=.05}n.setAttribute("position",new Xe(e,3)),n.setAttribute("color",new Xe(i,3)),n.setAttribute("size",new Xe(s,1));const l=new _n({uniforms:{time:{value:0}},vertexShader:`
      attribute float size;
      varying vec3 vColor;
      uniform float time;
      void main() {
        vColor = color;
        vec3 pos = position;
        pos.x += sin(time * 0.1 + position.z * 0.2) * 0.05;
        pos.y += cos(time * 0.1 + position.x * 0.2) * 0.05;
        pos.z += sin(time * 0.1 + position.y * 0.2) * 0.05;
        vec4 mvPosition = modelViewMatrix * vec4(pos, 1.0);
        gl_PointSize = size * (300.0 / -mvPosition.z);
        gl_Position = projectionMatrix * mvPosition;
      }
    `,fragmentShader:`
      varying vec3 vColor;
      void main() {
        float r = distance(gl_PointCoord, vec2(0.5, 0.5));
        if (r > 0.5) discard;
        float glow = 1.0 - (r * 2.0);
        glow = pow(glow, 2.0);
        gl_FragColor = vec4(vColor, glow);
      }
    `,transparent:!0,depthWrite:!1,blending:Fr,vertexColors:!0}),c=new Dh(n,l);return dn.add(c),function(d){l.uniforms.time.value=d}}function Ns(){fe&&dn.remove(fe),fe=new xs;const n=2,t=new cl(n,Math.max(1,Math.floor(pl/8))),e=new _n({uniforms:{time:{value:0},color:{value:new It(sn.primary)},audioLevel:{value:0},distortion:{value:Hr},agentActivity:{value:0}},vertexShader:`
      uniform float time;
      uniform float audioLevel;
      uniform float distortion;
      uniform float agentActivity;
      varying vec3 vNormal;
      varying vec3 vPosition;
      
      vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
      vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
      vec4 permute(vec4 x) { return mod289(((x*34.0)+1.0)*x); }
      vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }
      
      float snoise(vec3 v) {
        const vec2 C = vec2(1.0/6.0, 1.0/3.0);
        const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
        vec3 i  = floor(v + dot(v, C.yyy));
        vec3 x0 = v - i + dot(i, C.xxx);
        vec3 g = step(x0.yzx, x0.xyz);
        vec3 l = 1.0 - g;
        vec3 i1 = min(g.xyz, l.zxy);
        vec3 i2 = max(g.xyz, l.zxy);
        vec3 x1 = x0 - i1 + C.xxx;
        vec3 x2 = x0 - i2 + C.yyy;
        vec3 x3 = x0 - D.yyy;
        i = mod289(i);
        vec4 p = permute(permute(permute(
                i.z + vec4(0.0, i1.z, i2.z, 1.0))
              + i.y + vec4(0.0, i1.y, i2.y, 1.0))
              + i.x + vec4(0.0, i1.x, i2.x, 1.0));
        float n_ = 0.142857142857;
        vec3 ns = n_ * D.wyz - D.xzx;
        vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
        vec4 x_ = floor(j * ns.z);
        vec4 y_ = floor(j - 7.0 * x_);
        vec4 x = x_ *ns.x + ns.yyyy;
        vec4 y = y_ *ns.x + ns.yyyy;
        vec4 h = 1.0 - abs(x) - abs(y);
        vec4 b0 = vec4(x.xy, y.xy);
        vec4 b1 = vec4(x.zw, y.zw);
        vec4 s0 = floor(b0)*2.0 + 1.0;
        vec4 s1 = floor(b1)*2.0 + 1.0;
        vec4 sh = -step(h, vec4(0.0));
        vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
        vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
        vec3 p0 = vec3(a0.xy, h.x);
        vec3 p1 = vec3(a0.zw, h.y);
        vec3 p2 = vec3(a1.xy, h.z);
        vec3 p3 = vec3(a1.zw, h.w);
        vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
        p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
        vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
        m = m * m;
        return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
      }
      
      void main() {
        vNormal = normalize(normalMatrix * normal);
        float slowTime = time * 0.3;
        vec3 pos = position;
        float noise = snoise(vec3(position.x * 0.5, position.y * 0.5, position.z * 0.5 + slowTime));
        pos += normal * noise * 0.2 * distortion * (1.0 + audioLevel);
        vPosition = pos;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
      }
    `,fragmentShader:`
      uniform float time;
      uniform vec3 color;
      uniform float audioLevel;
      uniform float agentActivity;
      varying vec3 vNormal;
      varying vec3 vPosition;
      void main() {
        vec3 viewDirection = normalize(cameraPosition - vPosition);
        float fresnel = 1.0 - max(0.0, dot(viewDirection, vNormal));
        fresnel = pow(fresnel, 2.0 + audioLevel * 2.0);
        // thinking: 脈動加速, responding: 更亮
        float pulse = 0.8 + 0.2 * sin(time * 2.0);
        vec3 finalColor = color * fresnel * pulse * (1.0 + audioLevel * 0.8);
        float alpha = fresnel * (0.7 - audioLevel * 0.3);
        gl_FragColor = vec4(finalColor, alpha);
      }
    `,wireframe:!0,transparent:!0}),i=new mn(t,e);fe.add(i),dn.add(fe);const s=new ul(n*1.2,32,32),r=new _n({uniforms:{time:{value:0},color:{value:new It(sn.primary)},audioLevel:{value:0},agentActivity:{value:0}},vertexShader:`
      varying vec3 vNormal;
      varying vec3 vPosition;
      uniform float audioLevel;
      uniform float agentActivity;
      void main() {
        vNormal = normalize(normalMatrix * normal);
        vPosition = position * (1.0 + audioLevel * 0.2);
        gl_Position = projectionMatrix * modelViewMatrix * vec4(vPosition, 1.0);
      }
    `,fragmentShader:`
      varying vec3 vNormal;
      varying vec3 vPosition;
      uniform vec3 color;
      uniform float time;
      uniform float audioLevel;
      uniform float agentActivity;
      void main() {
        vec3 viewDirection = normalize(cameraPosition - vPosition);
        float fresnel = 1.0 - max(0.0, dot(viewDirection, vNormal));
        fresnel = pow(fresnel, 3.0 + audioLevel * 3.0);
        float pulse = 0.5 + 0.5 * sin(time * 2.0);
        float audioFactor = 1.0 + audioLevel * 3.0;
        vec3 finalColor = color * fresnel * (0.8 + 0.2 * pulse) * audioFactor;
        float alpha = fresnel * (0.3 * audioFactor) * (1.0 - audioLevel * 0.2);
        gl_FragColor = vec4(finalColor, alpha);
      }
    `,transparent:!0,side:Le,blending:Fr,depthWrite:!1}),a=new mn(s,r);return fe.add(a),function(l,c){const u=(performance.now()-Uu)/1e3;let d=0;if(kn===0)d=0;else if(kn===1){const p=.5+Math.min(u/10,1)*1.5,_=Math.sin(u*2.3)*.12+Math.sin(u*5.7)*.08+Math.sin(u*11.3)*.04;d=p+_}else kn===2&&(za+=(Nu-za)*.1,d=.8+za*1.5+Math.sin(l*1.2)*.1);ys>.01?(d+=ys*2.5,ys*=.95):ys=0;const h=kn===0?.02:.06;vr+=(d-vr)*h,e.uniforms.time.value=l,e.uniforms.audioLevel.value=c,e.uniforms.distortion.value=Hr,e.uniforms.agentActivity.value=vr,r.uniforms.time.value=l,r.uniforms.audioLevel.value=c,r.uniforms.agentActivity.value=vr}}function j_(){const n=document.getElementById("three-container"),t=new Hh,e=new Tt;let i=!1,s=new Tt;new L(0,0,0),ie=new L(0,0,0);const r=3;function a(u){const d=u.touches?u.touches[0].clientX:u.clientX,h=u.touches?u.touches[0].clientY:u.clientY;return{x:d/window.innerWidth*2-1,y:-(h/window.innerHeight)*2+1}}function o(u){const d=a(u);e.x=d.x,e.y=d.y,t.setFromCamera(e,We),t.intersectObject(fe,!0).length>0&&(Ze.enabled=!1,i=!0,Us=!0,s.x=e.x,s.y=e.y,u.cancelable&&u.preventDefault())}function l(u){if(!i)return;u.cancelable&&u.preventDefault();const d=a(u);e.x=d.x,e.y=d.y;const h=(e.x-s.x)*5,p=(e.y-s.y)*5;ie.x+=h,ie.y+=p;const _=Math.sqrt(ie.x**2+ie.y**2);if(_>r){const S=r/_;ie.x*=S,ie.y*=S}xe.x=h*2,xe.y=p*2,s.x=e.x,s.y=e.y}function c(){i&&(Ze.enabled=!0,i=!1,Us=!1)}n.addEventListener("mousedown",o),n.addEventListener("mousemove",l),n.addEventListener("mouseup",c),n.addEventListener("mouseleave",c),n.addEventListener("touchstart",o,{passive:!1}),n.addEventListener("touchmove",l,{passive:!1}),n.addEventListener("touchend",c),n.addEventListener("touchcancel",c)}function K_(){if(!Us){xe.x*=.95,xe.y*=.95,ie.x+=xe.x*.1,ie.y+=xe.y*.1;const n=.1;xe.x-=ie.x*n,xe.y-=ie.y*n,Math.abs(ie.x)<.05&&Math.abs(ie.y)<.05&&(ie.set(0,0,0),xe.set(0,0));const t=3,e=.8;Math.abs(ie.x)>t&&(xe.x=-xe.x*e,ie.x=Math.sign(ie.x)*t,Math.abs(xe.x)>.1),Math.abs(ie.y)>t&&(xe.y=-xe.y*e,ie.y=Math.sign(ie.y)*t,Math.abs(xe.y)>.1)}fe.position.x+=(ie.x-fe.position.x)*.2,fe.position.y+=(ie.y-fe.position.y)*.2,Us||(fe.rotation.x+=xe.y*.01,fe.rotation.y+=xe.x*.01)}function Z_(){Hr=1,pl=32,Ai=Ns(),ie.set(0,0,0),xe.set(0,0),fe.position.set(0,0,0)}function J_(n,t,e){Ze.update();const i=H_.getElapsedTime();if(K_(),Ai&&Ai(i,n),Gr&&Gr(i),fe){const s=1+n*e;fe.rotation.y+=.005*t*s,fe.rotation.z+=.002*t*s}ei.render(dn,We)}function Q_(n){We.aspect=window.innerWidth/window.innerHeight,We.updateProjectionMatrix(),ei.setSize(window.innerWidth,window.innerHeight);const t=window.innerWidth<=768,e=t?14:10,i=t?1.2:0;Vr.z=e,Vr.y=i,Us||(We.position.z=e,We.position.y=i),n&&n()}function t0(){dn=new Rh,dn.fog=new al(658967,.05),We=new Ge(60,window.innerWidth/window.innerHeight,.1,1e3),We.position.copy(Vr),ei=new A_({antialias:!0,alpha:!0,powerPreference:"high-performance",stencil:!1,depth:!0}),ei.setSize(window.innerWidth,window.innerHeight),ei.setClearColor(0,0),ei.setPixelRatio(window.devicePixelRatio),document.getElementById("three-container").appendChild(ei.domElement),Ze=new R_(We,ei.domElement),Ze.enableDamping=!0,Ze.dampingFactor=.1,Ze.enableRotate=!1,Ze.enablePan=!1,Ze.zoomSpeed=.7,Ze.minDistance=3,Ze.maxDistance=30,Ze.enableZoom=!1;const n=new Bh(4210752,1.5);dn.add(n);const t=new Fh(16777215,1.5);t.position.set(1,1,1),dn.add(t);const e=new La(sn.primary,1,10);e.position.set(2,2,2),dn.add(e);const i=new La(sn.secondary,1,10);i.position.set(-2,-2,-2),dn.add(i),Ai=Ns(),Gr=Ic(),j_(),Dc(),window.addEventListener("theme-change",()=>{Dc(),Ai=Ns(),Gr=Ic();const s=dn.children.filter(r=>r instanceof La);s[0]&&s[0].color.setHex(sn.primary),s[1]&&s[1].color.setHex(sn.secondary)})}const xr=document.getElementById("notification");function Fe(n){xr&&(xr.textContent=n,xr.style.opacity=1,setTimeout(()=>{xr.style.opacity=0},3e3))}function Me(n,t=!1){window.dispatchEvent(new CustomEvent("terminal-message",{detail:{message:n,isCommand:t}}))}let de=null,tn=null,As=null,$i,hn,Mn=!1,Ws=!1,ka=!1,Vo=!1,ms=null,ta=null,vn=null;function e0(){return $i}function n0(){return hn}function i0(){return tn}function s0(n){vn=n}function Tn(){if(Mn)return!0;try{return de=new(window.AudioContext||window.webkitAudioContext),tn=de.createAnalyser(),tn.fftSize=2048,tn.smoothingTimeConstant=.8,$i=new Uint8Array(tn.frequencyBinCount),hn=new Uint8Array(tn.frequencyBinCount),tn.connect(de.destination),Mn=!0,Me("AUDIO ANALYSIS SYSTEM INITIALIZED."),Fe("AUDIO ANALYSIS SYSTEM ONLINE"),!0}catch(n){return console.error("Audio initialization error:",n),Me("ERROR: AUDIO SYSTEM INITIALIZATION FAILED."),Fe("AUDIO SYSTEM ERROR"),!1}}function ea(){return!de&&!Tn()?!1:(de.state==="suspended"?de.resume().then(()=>{ka||(ka=!0,Me("AUDIO CONTEXT RESUMED."))}).catch(n=>{console.error("Failed to resume audio context:",n),Me("ERROR: FAILED TO RESUME AUDIO CONTEXT.")}):ka=!0,!0)}function r0(){if(As)try{As.disconnect(),Vo=!1,As=null}catch(n){console.log("Error disconnecting previous source:",n)}}function ml(){ms&&ms.parentNode&&ms.parentNode.removeChild(ms);const n=document.createElement("audio");n.id="audio-player",n.className="audio-player",n.crossOrigin="anonymous";const t=document.querySelector(".controls-row"),e=document.querySelector(".audio-controls");return e&&t&&e.insertBefore(n,t),ms=n,n.addEventListener("ended",()=>{Ws=!1,vn&&vn(!1),Me("AUDIO PLAYBACK COMPLETE.")}),n}function gl(n){try{if(!ea())return Me("ERROR: AUDIO CONTEXT NOT AVAILABLE. CLICK ANYWHERE TO ENABLE AUDIO."),!1;r0();try{return Vo||(As=de.createMediaElementSource(n),As.connect(tn),Vo=!0),!0}catch(t){return console.error("Error creating media element source:",t),t.name==="InvalidStateError"&&t.message.includes("already connected")?(Me("AUDIO SOURCE ALREADY CONNECTED. ATTEMPTING TO PLAY ANYWAY."),!0):(Me("ERROR: FAILED TO SETUP AUDIO SOURCE. "+t.message),!1)}}catch(t){return console.error("Error setting up audio source:",t),Me("ERROR: FAILED TO SETUP AUDIO SOURCE."),!1}}function a0(n){try{if(!Mn&&!Tn())return;const t=ml(),e=URL.createObjectURL(n);ta=e,t.src=e,t.onloadeddata=function(){gl(t)&&t.play().then(()=>{Ws=!0,vn&&vn(!0)}).catch(i=>{console.warn("Auto-play prevented:",i),Me("WARNING: AUTO-PLAY PREVENTED BY BROWSER. CLICK PLAY TO START AUDIO.")})},document.getElementById("file-label").textContent=n.name,document.querySelectorAll(".demo-track-btn").forEach(i=>i.classList.remove("active")),Me(`AUDIO FILE LOADED: ${n.name}`),Fe("AUDIO FILE LOADED")}catch(t){console.error("Audio file error:",t),Me("ERROR: AUDIO FILE PROCESSING FAILED."),Fe("AUDIO FILE ERROR")}}function o0(n){try{if(!Mn&&!Tn())return;ea();const t=ml();ta=n,t.src=n,t.onloadeddata=function(){gl(t)&&t.play().then(()=>{Ws=!0,vn&&vn(!0),Me(`PLAYING DEMO TRACK: ${n.split("/").pop()}`),Fe(`PLAYING: ${n.split("/").pop()}`)}).catch(i=>{console.warn("Play prevented:",i),Me("WARNING: AUDIO PLAYBACK PREVENTED BY BROWSER. CLICK PLAY TO START AUDIO."),Fe("CLICK PLAY TO START AUDIO")})};const e=n.split("/").pop();document.getElementById("file-label").textContent=e,Me(`LOADING AUDIO FROM URL: ${n.substring(0,40)}...`),Fe("AUDIO URL LOADED")}catch(t){console.error("Audio URL error:",t),Me("ERROR: AUDIO URL PROCESSING FAILED."),Fe("AUDIO URL ERROR")}}function l0(n,t,e){try{if(!Mn&&!Tn())return;ea();const i=ml();ta=n,i.src=n,i.onloadeddata=function(){gl(i)&&i.play().then(()=>{Ws=!0,vn&&vn(!0)}).catch(s=>{console.warn("TTS play prevented:",s),e&&e()})},i.onerror=()=>{console.error("TTS audio load error"),e&&e()},i.addEventListener("ended",()=>{e&&e()},{once:!0})}catch(i){console.error("TTS audio error:",i),e&&e()}}function c0(n){if(!tn)return;let t=0,e=0;for(let r=0;r<hn.length;r++)hn[r]>t&&(t=hn[r],e=r);const i=de.sampleRate;e*i/(tn.frequencyBinCount*2);let s=0;for(let r=0;r<hn.length;r++)s+=hn[r];s/(hn.length*255)}function u0(n,t){if(!tn)return;let e=0;for(let o=0;o<$i.length;o++)e+=Math.abs($i[o]-128);const s=e/$i.length/$i.length,r=document.getElementById("audio-wave");if(!r)return;const a=1+s*n*(t/5);r.style.transform=`translate(-50%, -50%) scale(${a})`,r.style.borderColor=`rgba(255, 78, 66, ${.1+s*.3})`}function d0(){window.addEventListener("user-interaction",()=>{Mn||Tn(),ea()},{once:!0}),window.addEventListener("tts-play",async t=>{const{url:e,label:i,onEnd:s}=t.detail;if(Mn||Tn(),de&&de.state==="suspended")try{await de.resume()}catch{}l0(e,i,s)}),document.querySelectorAll(".demo-track-btn").forEach(t=>{t.addEventListener("click",function(){Mn||Tn(),de&&de.state==="suspended"&&de.resume();const e=this.dataset.url;ta=e,document.querySelectorAll(".demo-track-btn").forEach(i=>i.classList.remove("active")),this.classList.add("active"),o0(e)})}),document.getElementById("file-btn")?.addEventListener("click",function(){Mn||Tn(),de&&de.state==="suspended"&&de.resume(),document.getElementById("audio-file-input").click()}),document.getElementById("audio-file-input")?.addEventListener("change",function(t){t.target.files.length>0&&a0(t.target.files[0])});const n=document.getElementById("audio-player");n&&n.addEventListener("ended",()=>{Ws=!1,vn&&vn(!1),Me("AUDIO PLAYBACK COMPLETE.")}),document.addEventListener("click",function(){Mn?de&&de.state==="suspended"&&de.resume():Tn()})}function h0(n){if(!tn)return 0;let t=0;for(let e=0;e<hn.length;e++)t+=hn[e];return t/hn.length/255*n/5}let Go=[];function f0(){const n=document.getElementById("floating-particles");if(!n)return;const t=1e3;n.innerHTML="",Go=[];const e=window.innerWidth,i=window.innerHeight,s=e/2,r=i/2;for(let a=0;a<t;a++){const o=document.createElement("div");o.className="particle",o.style.position="absolute",o.style.width="1.5px",o.style.height="1.5px",o.style.backgroundColor=`rgba(255, ${Math.floor(Math.random()*100)+78}, ${Math.floor(Math.random()*100)+66}, ${Math.random()*.5+.2})`,o.style.borderRadius="50%";const l=200,c=Math.max(e,i)*.8,u=Math.random()*Math.PI*2,d=Math.sqrt(Math.random()),h=l+d*(c-l),p=Math.cos(u)*h+s,_=Math.sin(u)*h+r;o.style.left=p+"px",o.style.top=_+"px",Go.push({element:o,x:p,y:_,speed:Math.random()*.5+.1,angle:Math.random()*Math.PI*2,angleSpeed:(Math.random()-.5)*.02,amplitude:Math.random()*50+20,size:1.5,pulseSpeed:Math.random()*.04+.01,pulsePhase:Math.random()*Math.PI*2}),n.appendChild(o)}p0()}function p0(){const n=window.innerWidth/2,t=window.innerHeight/2;let e=0;function i(){e+=.01,Go.forEach(s=>{s.angle+=s.angleSpeed;const r=n+Math.cos(s.angle)*s.amplitude,a=t+Math.sin(s.angle)*s.amplitude,o=Math.sin(e*s.speed+s.angle)*5,l=Math.cos(e*s.speed+s.angle*.7)*5,c=r+o,u=a+l;s.element.style.left=c+"px",s.element.style.top=u+"px";const d=1+Math.sin(e*s.pulseSpeed+s.pulsePhase)*.3,h=s.size*d;s.element.style.width=h+"px",s.element.style.height=h+"px";const p=.2+Math.sin(e*s.pulseSpeed+s.pulsePhase)*.1;s.element.style.opacity=Math.min(.8,p)}),requestAnimationFrame(i)}requestAnimationFrame(i)}function m0(n){const t=[],e=s=>`\0CB${s}\0`;return{text:n.replace(/```(\w*)\n?([\s\S]*?)```/g,(s,r,a)=>(t.push({lang:r,code:a.trimEnd()}),e(t.length-1))),blocks:t,placeholder:e}}function Gi(n){return n.replace(/`([^`]+)`/g,"<code>$1</code>").replace(/\*\*\*(.+?)\*\*\*/g,"<strong><em>$1</em></strong>").replace(/\*\*(.+?)\*\*/g,"<strong>$1</strong>").replace(/\*(.+?)\*/g,"<em>$1</em>").replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>')}function g0(n){return/^\|?[\s-:|]+\|[\s-:|]+\|?$/.test(n.trim())}function Uc(n){return/^\|(.+)\|$/.test(n.trim())}function Nc(n){return n.trim().replace(/^\||\|$/g,"").split("|").map(t=>t.trim())}function Ou(n){if(!n)return"";const{text:t,blocks:e}=m0(n),i=t.split(`
`),s=[];let r=!1,a=null;for(let o=0;o<i.length;o++){const l=i[o],c=l.match(/\x00CB(\d+)\x00/);if(c){r&&(s.push(`</${a}>`),r=!1);const p=e[parseInt(c[1])];s.push(`<pre><code${p.lang?` class="lang-${p.lang}"`:""}>${_0(p.code)}</code></pre>`);continue}if(Uc(l)&&o+1<i.length&&g0(i[o+1])){r&&(s.push(`</${a}>`),r=!1);const p=Nc(l);for(s.push("<table><thead><tr>"),p.forEach(_=>s.push(`<th>${Gi(_)}</th>`)),s.push("</tr></thead><tbody>"),o++;o+1<i.length&&Uc(i[o+1]);){o++;const _=Nc(i[o]);s.push("<tr>"),_.forEach(S=>s.push(`<td>${Gi(S)}</td>`)),s.push("</tr>")}s.push("</tbody></table>");continue}const u=l.match(/^[\s]*[-*+]\s+(.+)/);if(u){(!r||a!=="ul")&&(r&&s.push(`</${a}>`),s.push("<ul>"),r=!0,a="ul"),s.push(`<li>${Gi(u[1])}</li>`);continue}const d=l.match(/^[\s]*\d+[.)]\s+(.+)/);if(d){(!r||a!=="ol")&&(r&&s.push(`</${a}>`),s.push("<ol>"),r=!0,a="ol"),s.push(`<li>${Gi(d[1])}</li>`);continue}r&&(s.push(`</${a}>`),r=!1);const h=l.match(/^(#{1,3})\s+(.+)/);if(h){const p=h[1].length;s.push(`<h${p+2}>${Gi(h[2])}</h${p+2}>`);continue}l.trim()!==""&&s.push(`<p>${Gi(l)}</p>`)}return r&&s.push(`</${a}>`),s.join("")}function _0(n){return n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}const Wr=[],Sr=12,Ha=240,v0=15;let yr=null,Wo=null;function x0(){yr=document.createElement("div"),yr.id="orb-messages",yr.style.cssText=`
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 5;
    overflow: hidden;
  `,document.body.appendChild(yr)}function S0(n){const t=Wr.indexOf(n);t!==-1&&Wr.splice(t,1),n.el.parentNode&&n.el.parentNode.removeChild(n.el)}let Es=0;function Fu(n){if(requestAnimationFrame(Fu),!Es){Es=n;return}const t=Math.min((n-Es)/1e3,.1);Es=n;const e=Wo?Wo():{x:window.innerWidth/2,y:window.innerHeight/2};for(let i=Wr.length-1;i>=0;i--){const s=Wr[i];if(s.age+=t,s.angle+=s.speed*t,s.state==="entering"&&s.age>s.enterDur&&(s.state="orbiting"),s.state==="orbiting"&&s.age>Sr-s.leaveDur&&(s.state="leaving"),s.age>=Sr){S0(s);continue}let r,a;if(s.state==="entering"){const h=s.age/s.enterDur;r=h,a=.7+h*.3}else if(s.state==="leaving"){const h=(s.age-(Sr-s.leaveDur))/s.leaveDur;r=1-h,a=1-h*.2}else r=.85+Math.sin(s.age*1.5)*.15,a=1;const o=s.state==="entering"?Ha*(.3+.7*(s.age/s.enterDur)):s.state==="leaving"?Ha+(s.age-(Sr-s.leaveDur))/s.leaveDur*60:Ha,l=e.x+Math.cos(s.angle)*o,c=Math.sin(s.age*.8+s.floatPhase)*v0,u=e.y+Math.sin(s.angle)*o*.45*(1+s.tiltY)+c,d=.85+.15*((Math.sin(s.angle)+1)/2);s.el.style.opacity=Math.max(0,r*d),s.el.style.transform=`translate(-50%, -50%) scale(${a*d})`,s.el.style.left=l+"px",s.el.style.top=u+"px",s.el.style.zIndex=Math.round(d*10)}}function y0(n){Wo=n,x0(),Es=0,requestAnimationFrame(Fu)}function Oc(n){return`rgba(${Bs()}, ${n})`}const ws=document.getElementById("cpu-canvas"),ae=ws?ws.getContext("2d"):null,Xr=new Array(60).fill(0),Fc=document.getElementById("cpu-value"),Bc=document.getElementById("mem-value"),Er=document.getElementById("uptime-value"),zc=document.getElementById("proc-value"),Mr=document.getElementById("model-indicator");let Tr=0,kc=null;function Bu(){if(!ae||!ws)return;const n=ws.width,t=ws.height;ae.clearRect(0,0,n,t),ae.strokeStyle=Oc(.1),ae.lineWidth=.5;for(let s=0;s<=t;s+=t/4)ae.beginPath(),ae.moveTo(0,s),ae.lineTo(n,s),ae.stroke();const e=Ko();ae.strokeStyle=e,ae.lineWidth=1.5,ae.shadowColor=e,ae.shadowBlur=4,ae.beginPath();const i=n/(Xr.length-1);Xr.forEach((s,r)=>{const a=r*i,o=t-s/100*t;r===0?ae.moveTo(a,o):ae.lineTo(a,o)}),ae.stroke(),ae.shadowBlur=0,ae.lineTo(n,t),ae.lineTo(0,t),ae.closePath(),ae.fillStyle=Oc(.08),ae.fill()}function Hc(n){const t=Math.floor(n/86400),e=Math.floor(n%86400/3600),i=Math.floor(n%3600/60),s=Math.floor(n%60);return t>0?`${t}d ${String(e).padStart(2,"0")}:${String(i).padStart(2,"0")}:${String(s).padStart(2,"0")}`:`${String(e).padStart(2,"0")}:${String(i).padStart(2,"0")}:${String(s).padStart(2,"0")}`}function E0(n){const t=n.cpu||0;Xr.push(t),Xr.shift(),Fc&&(Fc.textContent=`${Math.round(t)}%`),Bc&&(Bc.textContent=`${n.mem.used} / ${n.mem.total} GB`),zc&&(zc.textContent=n.procs||0),Tr=n.uptime,Er&&(Er.textContent=Hc(Tr)),kc||(kc=setInterval(()=>{Tr++,Er&&(Er.textContent=Hc(Tr))},1e3)),Mr&&(t>80?Mr.style.color=Ko():t>50?Mr.style.color="#fbbf24":Mr.style.color="#4ade80"),Bu()}function M0(){Bu()}const Re=document.getElementById("terminal-content"),Se=document.getElementById("chat-input"),Oe=document.getElementById("chat-send"),Vc=document.getElementById("model-name"),T0=document.getElementById("tokens-in"),b0=document.getElementById("tokens-out"),A0=document.getElementById("context-value"),w0=document.getElementById("context-bar"),Gc=document.getElementById("context-bar-label");let Va=0,Ga=0,Wc=128e3;const R0=window.matchMedia("(max-width: 768px)").matches;function C0(n){!n||n.dataset.odometer==="ready"||(n.dataset.odometer="ready",n.style.cssText+=`
    display: inline-flex;
    overflow: hidden;
    height: 1.2em;
    line-height: 1.2em;
    vertical-align: bottom;
  `)}function Wa(n,t,e=800){if(!n)return;if(R0){const r=typeof t=="string"?t:t.toLocaleString();n.textContent=r;return}C0(n);const s=(typeof t=="string"?t:t.toLocaleString()).split("");for(n.querySelector(".odo-col")||(n.textContent="");n.children.length>s.length;)n.removeChild(n.lastChild);s.forEach((r,a)=>{let o=n.children[a];if(o||(o=document.createElement("span"),o.className="odo-col",n.appendChild(o)),!/\d/.test(r)){o.style.cssText=`
        display: inline-block;
        width: auto;
        height: 1.2em;
        line-height: 1.2em;
        overflow: hidden;
      `,o.innerHTML="",o.textContent=r,o.className="odo-col odo-sep";return}const l=parseInt(r);o.className="odo-col",o.style.cssText=`
      display: inline-block;
      width: 0.65em;
      height: 1.2em;
      overflow: hidden;
      position: relative;
      text-align: center;
    `;let c=o.querySelector(".odo-strip");c||(c=document.createElement("span"),c.className="odo-strip",c.style.cssText=`
        display: block;
        transition: transform ${e}ms cubic-bezier(0.23, 1, 0.32, 1);
        will-change: transform;
      `,c.innerHTML="0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9",o.innerHTML="",o.appendChild(c)),c.style.transitionDuration=e+"ms",requestAnimationFrame(()=>{c.style.transform=`translateY(-${l*1.2}em)`})})}function P0(n,t,e=800){n&&(n.style.transition=`width ${e}ms cubic-bezier(0.23, 1, 0.32, 1)`,n.style.width=t+"%")}async function _l(){try{const n=await fetch("/api/model-status");if(!n.ok)return;const t=await n.json();if(t.model&&Vc){const s=t.provider?`${t.provider}/${t.model}`.toUpperCase():t.model.toUpperCase();Vc.textContent=s}t.contextWindow&&(Wc=t.contextWindow),t.usage&&(Va=t.usage.input||0,Ga=t.usage.output||0),Wa(T0,Va),Wa(b0,Ga);const e=t.totalTokens||Va+Ga,i=Math.min(100,Math.round(e/Wc*100));Wa(A0,i+"%"),P0(w0,i),Gc&&(Gc.textContent=i+"%")}catch{}}let Qn=!1,Je=null,yn="",ii=null;async function L0(n){if(!n)return;const t=Ve;t&&window.__toggleListening&&window.__toggleListening();try{const e=n.replace(/\*\*(.*?)\*\*/g,"$1").replace(/\*(.*?)\*/g,"$1").replace(/```[\s\S]*?```/g,"").replace(/`([^`]+)`/g,"$1").replace(/^#{1,6}\s+/gm,"").replace(/\n{3,}/g,`
`).trim(),i=800,s=[];for(let r=0;r<e.length;r+=i)s.push(e.slice(r,r+i));for(let r=0;r<s.length;r++){const a=await fetch("/api/tts",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({text:s[r]})});if(!a.ok)continue;const o=await a.blob(),l=URL.createObjectURL(o);let c=document.getElementById("houdini-tts-player");c||(c=document.createElement("audio"),c.id="houdini-tts-player",c.style.display="none",document.getElementById("audio-controls")?.appendChild(c)||document.body.appendChild(c)),c.src=l,await new Promise(u=>{c.onended=()=>{URL.revokeObjectURL(l),u()},c.onerror=()=>{URL.revokeObjectURL(l),u()},c.play().catch(()=>{URL.revokeObjectURL(l),u()})})}t&&window.__toggleListening&&!Ve&&window.__toggleListening()}catch{}}let Xa=0,$a=0,en=null;async function D0(){try{const n=parseInt(localStorage.getItem("jarvis-history-limit")||"50"),t=n*4,e=await fetch(`/api/history?limit=${t}`);if(!e.ok)return;const s=(await e.json()).messages||[],r=[];for(const o of s){if(o.role!=="user"&&o.role!=="assistant")continue;const l=(o.content||[]).some(u=>u.type==="toolCall"),c=(o.content||[]).filter(u=>u.type==="text"&&u.text?.trim()).map(u=>{let d=u.text.trim();if(d.startsWith("Conversation info")){const h=d.split("\n```\n\n");d=h.length>1?h.slice(1).join("\n```\n\n").trim():""}return d}).filter(u=>u&&!u.startsWith("Read HEARTBEAT")).filter(u=>u!=="HEARTBEAT_OK").filter(u=>u!=="NO_REPLY").filter(u=>!u.startsWith("System:")).filter(u=>!u.startsWith("Pre-compaction"));c.length&&(o.role==="assistant"&&l&&!o.stopReason?.includes("end_turn")||r.push({role:o.role,text:c.join(`
`),timestamp:o.timestamp}))}if(!r.length)return;const a=r.slice(-n);le(`── HISTORIAL (${a.length}) ──`,"system-line");for(const o of a){const l=o.role==="user"?"user-line":"jin-line",c=le("",l);if(!c)continue;if(o.timestamp){const d=c.querySelector(".msg-time");if(d){const h=new Date(o.timestamp),p=String(h.getHours()).padStart(2,"0"),_=String(h.getMinutes()).padStart(2,"0");d.textContent=`${h.getMonth()+1}/${h.getDate()} ${p}:${_}`}}const u=c.querySelector(".msg-text");u&&(o.role==="assistant"?u.innerHTML=Ou(o.text):u.textContent=o.text)}le("── FIN HISTORIAL ──","system-line"),Re&&(Re.scrollTop=Re.scrollHeight)}catch{}}function I0(){const n=new EventSource("/api/events");window.__jarvisSSE=n,n.onmessage=t=>{try{const e=JSON.parse(t.data);if(e.type==="connected"){le("FLUJO GATEWAY CONECTADO ✓","system-line");return}if(e.type==="system"){E0(e);return}U0(e)}catch{}},n.onerror=()=>{}}function U0(n){const t=n.text||"",e=n.done||!1;if(n.state==="from_assistant"&&n.text_user){le(n.text_user,"user-line"),le(n.text,"jin-line"),window.dispatchEvent(new CustomEvent("agent-state",{detail:"idle"}));return}if(!(n.runId&&ii&&n.runId!==ii)){if(t&&(Je||(Je=le("","jin-line"),yn="",Xa=0,$a=performance.now(),window.dispatchEvent(new CustomEvent("agent-state",{detail:"responding"})),en&&clearInterval(en),en=setInterval(()=>{const i=performance.now(),s=(i-$a)/1e3;if(s>0){const r=(yn.length-Xa)/s,a=Math.min(1,r/50);window.dispatchEvent(new CustomEvent("agent-stream",{detail:a})),Xa=yn.length,$a=i}},200)),yn=t,Je)){const i=Je.querySelector(".msg-text");i&&(i.textContent=yn),Re.scrollTop=Re.scrollHeight}if(e){if(en&&(clearInterval(en),en=null),window.dispatchEvent(new CustomEvent("agent-stream",{detail:0})),_l(),yn&&(Yr()?.agent?.name,Je)){const s=Je.querySelector(".msg-body");if(s){const r=s.querySelector(".msg-time");s.innerHTML=Ou(yn),r&&s.appendChild(r)}Je.classList.add("markdown-rendered"),Re.scrollTop=Re.scrollHeight}Je=null,yn="",ii=null,Qn=!1,window.dispatchEvent(new CustomEvent("agent-state",{detail:"idle"})),Oe&&(Oe.textContent="ENVIAR")}}}function N0(){return new Date().toLocaleTimeString("es",{hour:"2-digit",minute:"2-digit"})}function le(n,t,e=[]){if(!Re)return null;const i=document.createElement("div");if(i.className=`terminal-line ${t}`,t.includes("system-line")||t.includes("command-line"))i.textContent=n;else{const a=document.createElement("span");a.className="msg-sender";const o=Yr();a.textContent=t.includes("user-line")?"TÚ":(o?.agent?.name||"HOUDINI").toUpperCase(),i.appendChild(a);const l=document.createElement("div");if(l.className="msg-body",e.length){const d=document.createElement("div");d.className="msg-images",e.forEach(h=>{const p=document.createElement("img");p.src=h,p.className="msg-image",p.addEventListener("click",()=>window.open(h,"_blank")),d.appendChild(p)}),l.appendChild(d)}const c=document.createElement("span");c.className="msg-text",c.textContent=n,l.appendChild(c);const u=document.createElement("span");u.className="msg-time",u.textContent=N0(),l.appendChild(u),i.appendChild(l)}Re.appendChild(i);const s=100,r=Re.querySelectorAll(".terminal-line");if(r.length>s){const a=r.length-s;for(let o=0;o<a;o++)r[o].remove()}return Re.scrollTop=Re.scrollHeight,i}function O0(n,t=!1){if(!Re)return;const e=document.createElement("div");e.className=t?"terminal-line command-line":"terminal-line system-line",e.textContent=n,Re.appendChild(e),Re.scrollTop=Re.scrollHeight}const Ji=document.getElementById("chat-attach"),qi=document.getElementById("chat-file-input");let Cn=[];const Xc='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.44 11.05l-9.19 9.19a6 6 0 01-8.49-8.49l9.19-9.19a4 4 0 015.66 5.66l-9.2 9.19a2 2 0 01-2.83-2.83l8.49-8.48"/></svg>';function na(n){Ji&&(Ji.classList.toggle("has-files",n>0),Ji.innerHTML=n>0?`${Xc}<span class="attach-badge">${n}</span>`:Xc)}Ji&&qi&&(Ji.addEventListener("click",()=>qi.click()),qi.addEventListener("change",()=>{Cn=Array.from(qi.files||[]),na(Cn.length)}));const Os=document.getElementById("three-container")||document.body;["dragenter","dragover"].forEach(n=>{Os.addEventListener(n,t=>{t.preventDefault(),t.stopPropagation(),Os.classList.add("drag-over")})});["dragleave","drop"].forEach(n=>{Os.addEventListener(n,t=>{t.preventDefault(),t.stopPropagation(),Os.classList.remove("drag-over")})});Os.addEventListener("drop",n=>{const t=Array.from(n.dataTransfer?.files||[]);t.length&&(Cn=t,na(t.length),Se.value=Se.value||"Analiza estos archivos",$r())});function F0(){let n=localStorage.getItem("houdini-session-id");return n||(n="houdini-"+Date.now().toString(36)+"-"+Math.random().toString(36).slice(2,8),localStorage.setItem("houdini-session-id",n)),n}async function $r(){if(!Se||Qn)return;const n=Se.value.trim(),t=Cn.length>0;if(!(!n&&!t)){if(window.dispatchEvent(new Event("user-interaction")),t){const e=[],i=[];Cn.forEach(s=>{i.push(s.name),s.type.startsWith("image/")&&e.push(URL.createObjectURL(s))}),le(n||`📎 ${i.join(", ")}`,"user-line",e)}else le(n,"user-line");Se.value="",Qn=!0,window.dispatchEvent(new CustomEvent("agent-state",{detail:"thinking"})),Oe&&(Oe.textContent="..."),Je=null,yn="";try{let e;if(t){const s=new FormData;s.append("message",n),Cn.forEach(r=>s.append("files",r)),e=await fetch("/api/chat/upload",{method:"POST",body:s}),Cn=[],Ji&&na(0),qi&&(qi.value="")}else e=await fetch("/api/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:n,session_id:F0()})});const i=await e.json();if(!e.ok){le(`ERROR: ${i.error||"Error desconocido"}`,"system-line"),Je=null,ii=null,Qn=!1,window.dispatchEvent(new CustomEvent("agent-state",{detail:"idle"})),Oe&&(Oe.textContent="ENVIAR");return}if(i.text){const r=Yr()?.agent?.name||"HOUDINI";if(le(i.text,"jin-line"),L0(i.text),window.dispatchEvent(new CustomEvent("agent-state",{detail:"idle"})),Oe&&(Oe.textContent="ENVIAR"),Qn=!1,i.pending_save&&Object.keys(i.pending_save).length>0){const a={name:"📝 nombre",telegram_chat_id:"💬 Chat ID de Telegram"},o=[];for(const[l,c]of Object.entries(i.pending_save))o.push(`${a[l]||l}: ${c}`);setTimeout(()=>{le(`💾 He detectado estos datos: ${o.join(", ")}. ¿Deseas guardarlos para no tener que repetirlos?`,"system-line");const l=le("","system-line");if(l){const c=document.createElement("div");c.style.cssText="display:flex;gap:8px;margin-top:4px";const u=document.createElement("button");u.textContent="✅ GUARDAR",u.className="btn",u.style.cssText="padding:4px 12px;font-size:11px;border:1px solid var(--accent-primary);background:rgba(var(--accent-rgb),0.15);color:var(--accent-primary);cursor:pointer;border-radius:4px",u.addEventListener("click",async()=>{try{(await(await fetch("/api/profile/save",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({data:i.pending_save})})).json()).ok&&le("✅ Datos guardados permanentemente.","system-line")}catch{}});const d=document.createElement("button");d.textContent="❌ NO GUARDAR",d.className="btn",d.style.cssText="padding:4px 12px;font-size:11px;border:1px solid #666;background:transparent;color:#999;cursor:pointer;border-radius:4px",d.addEventListener("click",()=>{le(" Entendido, no guardo nada.","system-line")}),c.appendChild(u),c.appendChild(d),l.appendChild(c)}},500)}ii=null,_l();return}ii=i.runId||null,setTimeout(()=>{Qn&&ii===i.runId&&(yn||le("TIMEOUT — TIEMPO AGOTADO","system-line"),en&&(clearInterval(en),en=null),window.dispatchEvent(new CustomEvent("agent-stream",{detail:0})),Je=null,ii=null,Qn=!1,window.dispatchEvent(new CustomEvent("agent-state",{detail:"idle"})),Oe&&(Oe.textContent="ENVIAR"))},6e4)}catch(e){le(`CONNECTION ERROR: ${e.message}`,"system-line"),en&&(clearInterval(en),en=null),window.dispatchEvent(new CustomEvent("agent-stream",{detail:0})),Je=null,Qn=!1,window.dispatchEvent(new CustomEvent("agent-state",{detail:"idle"})),Oe&&(Oe.textContent="ENVIAR")}}}let Jn=null,Ve=!1,gs=null;const Ne=document.getElementById("chat-mic");function B0(){if(!("webkitSpeechRecognition"in window)&&!("SpeechRecognition"in window)){Ne&&(Ne.style.display="none");return}const n=window.SpeechRecognition||window.webkitSpeechRecognition;function t(){const r=new n;return r.lang="es-CO",r.continuous=!0,r.interimResults=!0,r.maxAlternatives=1,r}function e(r){let a="",o="";for(let c=r.resultIndex;c<r.results.length;c++){const u=r.results[c];u.isFinal?a+=u[0].transcript:o+=u[0].transcript}const l=(a+" "+o).trim();l&&Se&&(Se.value=l,Se.placeholder="🎤 ESCUCHANDO..."),gs&&clearTimeout(gs),a.trim()&&(gs=setTimeout(()=>{Se&&Se.value.trim()&&(Se.placeholder="🎤 Procesando...",$r())},1800))}function i(){if(!Ve){Ve=!0,Jn=t(),Jn.onresult=e,Jn.onend=function(){if(Ve)try{const r=t();r.onresult=e,r.onend=arguments.callee,r.onerror=function(a){Ve&&setTimeout(i,500)},r.start(),Jn=r}catch{Ve&&setTimeout(i,1e3)}},Jn.onerror=function(r){if(r.error==="not-allowed"){Ve=!1,Ne&&(Ne.style.display="none");return}Ve&&setTimeout(i,500)};try{Jn.start(),Ne&&Ne.classList.add("recording"),Se&&(Se.placeholder="🎤 Siempre escuchando...")}catch{Ve=!1,setTimeout(i,1e3)}}}function s(){if(Ve=!1,Jn)try{Jn.stop()}catch{}gs&&clearTimeout(gs),Ne&&Ne.classList.remove("recording"),Se&&(Se.placeholder="ESCRIBE UN MENSAJE...")}window.__toggleListening=function(){Ve?(s(),Ne&&(Ne.title="ACTIVAR VOZ")):(i(),Ne&&(Ne.title="MODO SIEMPRE ACTIVO"))},Ne&&Ne.addEventListener("click",window.__toggleListening),window.addEventListener("agent-state",function(r){r.detail==="idle"&&setTimeout(function(){Ve&&i()},800)})}function $c(){}function z0(){window.addEventListener("terminal-message",r=>{const{message:a,isCommand:o}=r.detail;O0(a,o)}),Oe&&Oe.addEventListener("click",$r),Se&&(Se.addEventListener("keydown",r=>{r.key==="Enter"&&!r.isComposing&&$r()}),Se.addEventListener("paste",r=>{const o=Array.from(r.clipboardData?.items||[]).filter(c=>c.type.startsWith("image/"));if(!o.length)return;r.preventDefault();const l=o.map(c=>c.getAsFile()).filter(Boolean);Cn=[...Cn,...l],na(Cn.length),le(`📋 ${l.length} imagen(es) pegada(s). Escribe un mensaje y envía.`,"system-line")}));const n=Yr(),t=n?.agent?.name||"JARVIS";if(n?.agent?.emoji,setTimeout(()=>{le(`SISTEMA INICIALIZADO. INTERFAZ ${t.toUpperCase()} EN LÍNEA.`,"system-line")},1e3),window.matchMedia("(max-width: 768px)").matches){const r=document.querySelector(".terminal-panel.chat-panel .terminal-header");if(r){let a=!1;r.addEventListener("click",()=>{if(a){a=!1;return}const l=document.querySelector(".terminal-panel.chat-panel");l&&(l.classList.remove("chat-fullscreen"),l.classList.toggle("chat-collapsed"))});let o=0;r.addEventListener("touchstart",l=>{o=l.touches[0].clientY,a=!1},{passive:!0}),r.addEventListener("touchend",l=>{const c=o-l.changedTouches[0].clientY,u=document.querySelector(".terminal-panel.chat-panel");u&&(c>50?(a=!0,u.classList.remove("chat-collapsed"),u.classList.add("chat-fullscreen")):c<-50&&(a=!0,u.classList.remove("chat-fullscreen")))},{passive:!0})}}const e=document.getElementById("history-limit");if(e){const r=localStorage.getItem("jarvis-history-limit");r&&(e.value=r),e.addEventListener("change",()=>{localStorage.setItem("jarvis-history-limit",e.value)})}D0().then(()=>{setTimeout(I0,500)}),setTimeout(_l,3500),setTimeout(async()=>{try{(await(await fetch("/api/status")).json()).gateway&&le("GATEWAY OPENCLAW EN LÍNEA ✓","system-line")}catch{le("BACKEND NO DISPONIBLE — MODO DEMO","system-line")}},3e3),setTimeout(B0,1500);const i=document.getElementById("chat-collapse-btn"),s=document.querySelector(".terminal-panel.chat-panel");i&&s&&(i.addEventListener("click",function(){const r=s.classList.toggle("chat-minimized");i.textContent=r?"▸":"▾",i.title=r?"EXPANDIR":"MINIMIZAR";const a=s.querySelector(".terminal-content"),o=s.querySelector(".chat-input-bar");a&&(a.style.display=r?"none":""),o&&(o.style.display=r?"none":""),localStorage.setItem("houdini-chat-minimized",r?"1":"0")}),localStorage.getItem("houdini-chat-minimized")==="1"&&i.click())}function k0(){document.querySelectorAll(".tab-btn-r").forEach(n=>{n.addEventListener("click",()=>{const t=n.dataset.rtab;document.querySelectorAll(".tab-btn-r").forEach(i=>i.classList.remove("active")),n.classList.add("active"),document.querySelectorAll(".rtab-content").forEach(i=>i.classList.remove("active"));const e=document.getElementById(`rtab-${t}`);e&&e.classList.add("active")})})}function H0(){k0()}function zu(){return{critical:{label:"CRÍT",color:"#ff2d2d",icon:"⚠"},high:{label:"ALTA",color:Ko(),icon:"▲"},medium:{label:"MED",color:"#ff8c42",icon:"●"},low:{label:"BAJA",color:"#666",icon:"▽"}}}zu();const qc={pending:{label:"PENDIENTE",icon:"○",class:"pending"},running:{label:"EJECUTANDO",icon:"▶",class:"active"},done:{label:"HECHO",icon:"✓",class:"done"},failed:{label:"FALLIDO",icon:"✗",class:"failed"},deferred:{label:"APLAZADO",icon:"◇",class:"deferred"}};let rn=[],si="all";async function ku(){try{const n=await fetch("/api/tasks");if(!n.ok)throw new Error("fetch failed");rn=await n.json(),Xs()}catch(n){console.error("[TASKS] fetch error:",n)}}async function V0(n){try{const t=await fetch("/api/tasks",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)});if(!t.ok)throw new Error("create failed");const e=await t.json();return rn.unshift(e),Xs(),e}catch(t){console.error("[TASKS] create error:",t)}}async function Hu(n,t){try{const e=await fetch(`/api/tasks/${n}`,{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify(t)});if(!e.ok)throw new Error("update failed");const i=await e.json(),s=rn.findIndex(r=>r.id===n);return s>=0&&(rn[s]=i),Xs(),i}catch(e){console.error("[TASKS] update error:",e)}}async function G0(n){try{if(!(await fetch(`/api/tasks/${n}`,{method:"DELETE"})).ok)throw new Error("delete failed");rn=rn.filter(e=>e.id!==n),Xs()}catch(t){console.error("[TASKS] delete error:",t)}}async function W0(n){const t=rn.find(r=>r.id===n);if(!t)return;const e=["pending","running","done"],i=e.indexOf(t.status),s=e[(i+1)%e.length];await Hu(n,{status:s})}async function X0(n){const t=rn.find(r=>r.id===n);if(!t)return;const e=["low","medium","high","critical"],i=e.indexOf(t.priority),s=e[(i+1)%e.length];await Hu(n,{priority:s})}function $0(){let n=[...rn];si==="active"&&(n=n.filter(i=>i.status!=="done")),si==="done"&&(n=n.filter(i=>i.status==="done"));const t={critical:0,high:1,medium:2,low:3},e={running:0,pending:1,deferred:2,failed:3,done:4};return n.sort((i,s)=>{const r=e[i.status]??5,a=e[s.status]??5;if(r!==a)return r-a;const o=t[i.priority]??3,l=t[s.priority]??3;return o!==l?o-l:(s.createdAt||0)-(i.createdAt||0)}),n}function q0(n){if(!n)return"";const t=new Date(n),e=new Date,i=e-t;return i<6e4?"AHORA":i<36e5?`${Math.floor(i/6e4)}MIN`:i<864e5?`${Math.floor(i/36e5)}H`:t.getFullYear()===e.getFullYear()?`${String(t.getMonth()+1).padStart(2,"0")}/${String(t.getDate()).padStart(2,"0")}`:`${t.getFullYear()}/${String(t.getMonth()+1).padStart(2,"0")}/${String(t.getDate()).padStart(2,"0")}`}function Y0(n){return n.schedule?n.schedule.type==="once"?`⏰ ${new Date(n.schedule.at).toLocaleString("es",{month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit"})}`:n.schedule.type==="recurring"?`🔄 ${n.schedule.label||n.schedule.cron||"RECURRING"}`:"":""}function j0(n){const t=qc[n.status]||qc.pending,e=zu(),i=e[n.priority]||e.medium,s=n.progress??null,r=Y0(n),a=q0(n.createdAt);return`
    <div class="task-item-v2 ${t.class}" data-id="${n.id}">
      <div class="task-row-main">
        <button class="task-status-btn ${t.class}" data-action="cycle-status" title="CAMBIAR ESTADO">
          ${t.icon}
        </button>
        <span class="task-text-v2">${qa(n.title)}</span>
        <button class="task-priority-btn" data-action="cycle-priority" 
                style="color:${i.color}" title="${i.label}">
          ${i.icon}
        </button>
        <button class="task-delete-btn" data-action="delete" title="ELIMINAR">×</button>
      </div>
      ${n.description?`<div class="task-desc">${qa(n.description)}</div>`:""}
      <div class="task-row-meta">
        ${s!==null?`
          <div class="task-progress">
            <div class="task-progress-bar" style="width:${s}%"></div>
            <span class="task-progress-text">${s}%</span>
          </div>
        `:""}
        ${r?`<span class="task-meta-tag schedule">${r}</span>`:""}
        ${n.tags?.length?n.tags.map(o=>`<span class="task-meta-tag tag">${qa(o)}</span>`).join(""):""}
        <span class="task-time">${a}</span>
      </div>
    </div>
  `}function qa(n){return n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}function Xs(){const n=document.getElementById("rtab-tasks");if(!n)return;const t=$0(),e={all:rn.length,active:rn.filter(i=>i.status!=="done").length,done:rn.filter(i=>i.status==="done").length};n.innerHTML=`
    <div class="tasks-header">
      <div class="tasks-filters">
        <button class="tasks-filter-btn ${si==="all"?"active":""}" data-filter="all">
          TODAS <span class="tasks-count">${e.all}</span>
        </button>
        <button class="tasks-filter-btn ${si==="active"?"active":""}" data-filter="active">
          ACTIVAS <span class="tasks-count">${e.active}</span>
        </button>
        <button class="tasks-filter-btn ${si==="done"?"active":""}" data-filter="done">
          HECHAS <span class="tasks-count">${e.done}</span>
        </button>
      </div>
      <button class="tasks-add-btn" id="tasks-add-btn" title="NUEVA TAREA">+</button>
    </div>

    <div class="tasks-add-form" id="tasks-add-form" style="display:none">
      <input type="text" class="tasks-input" id="tasks-input-title" placeholder="TÍTULO DE TAREA..." />
      <div class="tasks-form-row">
        <select class="tasks-select" id="tasks-input-priority">
          <option value="medium">● MED</option>
          <option value="low">▽ BAJA</option>
          <option value="high">▲ ALTA</option>
          <option value="critical">⚠ CRÍT</option>
        </select>
        <input type="text" class="tasks-input tasks-input-tags" id="tasks-input-tags" placeholder="ETIQUETAS (SEP. COMA)" />
        <button class="tasks-submit-btn" id="tasks-submit-btn">AÑADIR</button>
      </div>
    </div>

    <div class="tasks-list-v2" id="tasks-list">
      ${t.length===0?`<div class="tasks-empty">SIN TAREAS ${si!=="all"?`(${si.toUpperCase()})`:""}</div>`:t.map(j0).join("")}
    </div>

    <div class="tasks-stats">
      <span>${e.active} ACTIVAS</span>
      <span class="tasks-stats-sep">|</span>
      <span>${e.done} COMPLETADAS</span>
    </div>
  `,K0(n)}function K0(n){n.querySelectorAll(".tasks-filter-btn").forEach(r=>{r.addEventListener("click",()=>{si=r.dataset.filter,Xs()})});const t=n.querySelector("#tasks-add-btn"),e=n.querySelector("#tasks-add-form");t&&e&&t.addEventListener("click",()=>{const r=e.style.display!=="none";e.style.display=r?"none":"flex",r||n.querySelector("#tasks-input-title")?.focus()});const i=n.querySelector("#tasks-submit-btn"),s=n.querySelector("#tasks-input-title");if(i&&s){const r=()=>{const a=s.value.trim();if(!a)return;const o=n.querySelector("#tasks-input-priority")?.value||"medium",c=(n.querySelector("#tasks-input-tags")?.value||"").split(",").map(u=>u.trim()).filter(Boolean);V0({title:a,priority:o,tags:c}),s.value="",n.querySelector("#tasks-input-tags")&&(n.querySelector("#tasks-input-tags").value=""),e.style.display="none"};i.addEventListener("click",r),s.addEventListener("keydown",a=>{a.key==="Enter"&&r()})}n.querySelectorAll(".task-item-v2").forEach(r=>{const a=r.dataset.id;r.querySelector('[data-action="cycle-status"]')?.addEventListener("click",o=>{o.stopPropagation(),W0(a)}),r.querySelector('[data-action="cycle-priority"]')?.addEventListener("click",o=>{o.stopPropagation(),X0(a)}),r.querySelector('[data-action="delete"]')?.addEventListener("click",o=>{o.stopPropagation(),G0(a)})})}function Z0(){const n=()=>{const t=window.__jarvisSSE;if(!t){setTimeout(n,1e3);return}t.addEventListener("message",e=>{try{JSON.parse(e.data).type==="task-update"&&ku()}catch{}})};n()}function J0(){ku(),Z0()}let Qi=[],ts="workspace",Ms=null;async function Vu(){try{const n=await fetch("/api/skills");if(!n.ok)throw new Error("fetch failed");Qi=await n.json(),Ir()}catch(n){console.error("[SKILLS] fetch error:",n)}}function Ya(n){return n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}function Q0(){return ts==="all"?Qi:Qi.filter(n=>n.source===ts)}function tv(n){const t=Ms===n.slug,e=n.source==="workspace"?"LOCAL":"GLOBAL",i=n.source==="workspace"?"source-local":"source-global";return`
    <div class="skill-item-v2 ${t?"expanded":""}" data-slug="${n.slug}">
      <div class="skill-row-main">
        <span class="skill-icon-v2">${n.emoji}</span>
        <span class="skill-name-v2">${Ya(n.name.toUpperCase())}</span>
        <span class="skill-source-tag ${i}">${e}</span>
        <button class="skill-expand-btn" data-action="toggle" title="DETALLES">
          ${t?"▾":"▸"}
        </button>
      </div>
      ${t?`
        <div class="skill-details">
          <div class="skill-desc">${Ya(n.description||"Sin descripción")}</div>
          <div class="skill-path-row">
            <span class="skill-path-label">RUTA:</span>
            <span class="skill-path-value">${Ya(n.path)}</span>
          </div>
        </div>
      `:""}
    </div>
  `}function Ir(){const n=document.getElementById("rtab-skills");if(!n)return;const t=Q0(),e={all:Qi.length,workspace:Qi.filter(i=>i.source==="workspace").length,global:Qi.filter(i=>i.source==="global").length};n.innerHTML=`
    <div class="skills-header">
      <div class="skills-filters">
        <button class="skills-filter-btn ${ts==="all"?"active":""}" data-filter="all">
          TODAS <span class="skills-count">${e.all}</span>
        </button>
        <button class="skills-filter-btn ${ts==="workspace"?"active":""}" data-filter="workspace">
          LOCALES <span class="skills-count">${e.workspace}</span>
        </button>
        <button class="skills-filter-btn ${ts==="global"?"active":""}" data-filter="global">
          GLOBALES <span class="skills-count">${e.global}</span>
        </button>
      </div>
      <button class="skills-refresh-btn" id="skills-refresh-btn" title="ACTUALIZAR">⟳</button>
    </div>

    <div class="skills-list-v2" id="skills-list">
      ${t.length===0?'<div class="skills-empty">SIN HABILIDADES</div>':t.map(tv).join("")}
    </div>

    <div class="skills-stats">
      <span>${e.workspace} LOCALES</span>
      <span class="skills-stats-sep">|</span>
      <span>${e.global} GLOBALES</span>
      <span class="skills-stats-sep">|</span>
      <span>${e.all} TOTAL</span>
    </div>
  `,ev(n)}function ev(n){n.querySelectorAll(".skills-filter-btn").forEach(t=>{t.addEventListener("click",()=>{ts=t.dataset.filter,Ir()})}),n.querySelector("#skills-refresh-btn")?.addEventListener("click",()=>{Vu()}),n.querySelectorAll(".skill-item-v2").forEach(t=>{const e=t.dataset.slug;t.querySelector('[data-action="toggle"]')?.addEventListener("click",i=>{i.stopPropagation(),Ms=Ms===e?null:e,Ir()}),t.querySelector(".skill-row-main")?.addEventListener("click",()=>{Ms=Ms===e?null:e,Ir()})})}function nv(){Vu()}const iv=7;let Rs=[],Gu=0,Wu="",Xu=!1,$u=0,Ur=new Set;async function qu(n=0,t=!1){try{const e=await fetch(`/api/memory?limit=${iv}&offset=${n}`);if(!e.ok)throw new Error("fetch failed");const i=await e.json();t?Rs=[...Rs,...i.days]:Rs=i.days,Gu=i.totalFiles,Wu=i.lastUpdate,Xu=i.hasMore,$u=n+i.days.length,Yu()}catch(e){console.error("[MEMORY] fetch error:",e)}}function Yc(n){return n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}function sv(n){const t=Ur.has(n.date),e=t?"▸":"▾",i=n.label?` <span class="mem-day-label">${n.label}</span>`:"";return`
    <div class="mem-day" data-date="${n.date}">
      <div class="mem-day-header" data-action="toggle">
        <span class="mem-day-arrow">${e}</span>
        <span class="mem-day-date">${Yc(n.displayDate)}</span>
        ${i}
        <span class="mem-day-count">${n.topics.length}</span>
      </div>
      ${t?"":`
        <div class="mem-day-topics">
          ${n.topics.length>0?n.topics.map(s=>`<div class="mem-topic">${Yc(s)}</div>`).join(""):'<div class="mem-topic mem-topic-empty">Sin entradas</div>'}
        </div>
      `}
    </div>
  `}function Yu(){const n=document.getElementById("rtab-memory");n&&(n.innerHTML=`
    <div class="mem-header">
      <div class="data-row">
        <span class="data-label">ARCHIVOS:</span>
        <span class="data-value">${Gu}</span>
      </div>
      <div class="data-row">
        <span class="data-label">ACTUALIZADO:</span>
        <span class="data-value">${Wu||"—"}</span>
      </div>
    </div>

    <div class="mem-timeline">
      ${Rs.length===0?'<div class="mem-empty">SIN ARCHIVOS DE MEMORIA</div>':Rs.map(sv).join("")}
    </div>

    ${Xu?`
      <div class="mem-more-wrapper">
        <button class="mem-more-btn" id="mem-more-btn">▼ MÁS</button>
      </div>
    `:""}
  `,rv(n))}function rv(n){n.querySelectorAll(".mem-day-header").forEach(t=>{t.addEventListener("click",()=>{const e=t.closest(".mem-day").dataset.date;Ur.has(e)?Ur.delete(e):Ur.add(e),Yu()})}),n.querySelector("#mem-more-btn")?.addEventListener("click",()=>{qu($u,!0)})}function av(){qu(0)}let Sn=null,Fs=[];const Yi={pulse:'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',clock:'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',play:'<svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>',pause:'<svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>',check:'<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',x:'<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'};async function ju(){try{const n=await fetch("/api/schedule");if(!n.ok)throw new Error("fetch failed");const t=await n.json();Sn=t.heartbeat,Fs=t.jobs,Ku()}catch(n){console.error("[SCHEDULE] fetch error:",n)}}async function ov(n,t){try{if(!(await fetch(`/api/schedule/${n}`,{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify({enabled:t})})).ok)throw new Error("toggle failed");const i=Fs.find(s=>s.id===n);i&&(i.enabled=t),Ku()}catch(e){console.error("[SCHEDULE] toggle error:",e)}}function lv(n){if(!n)return"—";if(n.kind==="cron"){const t=n.expr,e=t.split(/\s+/);if(e.length===5){const[i,s,r,a,o]=e,l=["日","一","二","三","四","五","六"];if(r==="*"&&a==="*"&&o==="*"&&!s.includes("/")&&!i.includes("/"))return`每天 ${s.padStart(2,"0")}:${i.padStart(2,"0")}`;if(s.startsWith("*/"))return`每 ${s.slice(2)} 小時`;if(i.startsWith("*/"))return`每 ${i.slice(2)} 分鐘`;if(r==="*"&&a==="*"&&/^\d$/.test(o))return`每週${l[parseInt(o)]} ${s.padStart(2,"0")}:${i.padStart(2,"0")}`}return t}if(n.kind==="every"){const t=n.everyMs;return t>=36e5?`每 ${t/36e5} 小時`:t>=6e4?`每 ${t/6e4} 分鐘`:`每 ${t/1e3} 秒`}return n.kind==="at"?new Date(n.at).toLocaleString("en-CA",{timeZone:"Asia/Taipei",hour:"2-digit",minute:"2-digit",hour12:!1}):"—"}function cv(n){if(!n)return"每 30 分鐘";const t=n.match(/^(\d+)(ms|s|m|h)$/i);if(!t)return n;const e=parseInt(t[1]),i=t[2].toLowerCase();return i==="h"?`每 ${e} 小時`:i==="m"?`每 ${e} 分鐘`:i==="s"?`每 ${e} 秒`:n}function Xo(n){if(!n)return"—";const t=new Date(n),i=new Date().toLocaleDateString("en-CA",{timeZone:"Asia/Taipei"}),s=t.toLocaleDateString("en-CA",{timeZone:"Asia/Taipei"}),r=t.toLocaleTimeString("en-CA",{timeZone:"Asia/Taipei",hour:"2-digit",minute:"2-digit",hour12:!1});return s===i?r:`${s.slice(5)} ${r}`}function qr(n){return n.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}function Ku(){const n=document.getElementById("rtab-schedule");n&&(n.innerHTML=`
    <div class="sched-section">
      <div class="sched-section-title">${Yi.pulse} SYSTEM</div>
      <div class="sched-items">
        ${Sn?`
          <div class="sched-item">
            <div class="sched-row-main">
              <span class="sched-expr">${qr(cv(Sn.every))}</span>
              <span class="sched-name">HEARTBEAT</span>
              <span class="sched-status ${Sn.enabled?"on":"off"}">
                ${Sn.enabled?Yi.check:Yi.x}
              </span>
            </div>
            <div class="sched-row-meta">
              <span class="sched-meta">LAST: ${Xo(Sn.lastRun)}${Sn.lastStatus?` · ${Sn.lastStatus.toUpperCase().replace("OK-TOKEN","OK")}`:""}</span>
            </div>
            ${Sn.content?`
              <div class="sched-hb-toggle" data-action="expand-hb">▸ 查看內容</div>
              <div class="sched-hb-content hidden">
                <pre class="sched-hb-pre">${qr(Sn.content)}</pre>
              </div>
            `:""}
          </div>
        `:""}
      </div>
    </div>

    <div class="sched-section">
      <div class="sched-section-title">${Yi.clock} CRON JOBS</div>
      <div class="sched-items">
        ${Fs.length===0?'<div class="sched-empty">SIN TAREAS PROGRAMADAS</div>':Fs.map(uv).join("")}
      </div>
    </div>
  `,dv(n))}function uv(n){return`
    <div class="sched-item" data-id="${n.id}">
      <div class="sched-row-main">
        <span class="sched-expr">${qr(lv(n.schedule))}</span>
        <span class="sched-name">${qr(n.name)}</span>
        <button class="sched-toggle ${n.enabled?"on":"off"}" data-action="toggle" title="${n.enabled?"DESACTIVAR":"ACTIVAR"}">
          ${n.enabled?Yi.pause:Yi.play}
        </button>
      </div>
      <div class="sched-row-meta">
        <span class="sched-meta">LAST: ${Xo(n.lastRun)}${n.lastStatus?` · ${n.lastStatus.toUpperCase()}`:""}</span>
        <span class="sched-meta">NEXT: ${Xo(n.nextRun)}</span>
      </div>
    </div>
  `}function dv(n){n.querySelectorAll('[data-action="toggle"]').forEach(t=>{t.addEventListener("click",e=>{e.stopPropagation();const s=t.closest(".sched-item").dataset.id,r=Fs.find(a=>a.id===s);r&&ov(s,!r.enabled)})}),n.querySelectorAll('[data-action="expand-hb"]').forEach(t=>{t.addEventListener("click",()=>{const e=t.nextElementSibling;e.classList.contains("hidden")?(e.classList.remove("hidden"),t.textContent="▾ 隱藏內容"):(e.classList.add("hidden"),t.textContent="▸ 查看內容")})})}function hv(){const n=()=>{const t=window.__jarvisSSE;if(!t){setTimeout(n,1e3);return}t.addEventListener("message",e=>{try{JSON.parse(e.data).type==="schedule-update"&&ju()}catch{}})};n()}function fv(){ju(),hv()}const vl="jarvis-panel-positions",Zu=[".terminal-panel.chat-panel",".spectrum-analyzer",".info-center"];function pv(){return new Promise(n=>{if(typeof Draggable<"u")return n();const t=setInterval(()=>{typeof Draggable<"u"&&(clearInterval(t),n())},50);setTimeout(()=>{clearInterval(t),n()},5e3)})}function Ju(){const n={};Zu.forEach(t=>{const e=document.querySelector(t);if(!e)return;const i=Draggable.get(e),s={};i&&(s.x=i.x,s.y=i.y),e.style.width&&(s.width=e.style.width),e.style.height&&(s.height=e.style.height),e.classList.contains("chat-collapsed")&&(s.collapsed=!0),n[t]=s}),localStorage.setItem(vl,JSON.stringify(n))}function mv(){try{const n=JSON.parse(localStorage.getItem(vl));if(!n)return;Object.entries(n).forEach(([t,e])=>{const i=document.querySelector(t);if(i){if(e.x!=null&&typeof gsap<"u"){gsap.set(i,{x:e.x,y:e.y});const s=Draggable.get(i);s&&s.update()}e.width&&(i.style.width=e.width),e.height&&(i.style.height=e.height),e.collapsed&&i.classList.add("chat-collapsed")}})}catch{}}function gv(){Zu.forEach(n=>{const t=document.querySelector(n);if(!t)return;typeof gsap<"u"?gsap.set(t,{x:0,y:0,clearProps:"transform"}):t.style.transform="",t.style.width="",t.style.height="",t.classList.remove("chat-collapsed");const e=Draggable.get(t);e&&e.update()}),localStorage.removeItem(vl)}function ja(n,t=null){n&&(typeof Draggable>"u"||Draggable.create(n,{type:"x,y",edgeResistance:.65,bounds:document.body,handle:t||n,inertia:!0,throwResistance:.85,onDragStart:function(){const e=document.querySelectorAll(".terminal-panel, .spectrum-analyzer, .data-panel");let i=10;e.forEach(s=>{const r=parseInt(window.getComputedStyle(s).zIndex);r>i&&(i=r)}),n.style.zIndex=i+1},onDragEnd:function(){Ju()}}))}const _v=window.matchMedia("(max-width: 768px)").matches;async function vv(){if(!_v){if(await pv(),typeof Draggable>"u"){console.warn("[JARVIS] GSAP Draggable not loaded, skipping drag");return}ja(document.querySelector(".terminal-panel"),document.querySelector(".terminal-header")),ja(document.querySelector(".spectrum-analyzer"),document.getElementById("spectrum-handle")),ja(document.querySelector(".info-center"),document.getElementById("info-center-handle")),mv()}}let Nr=1,Or=5,Ts=null,bs=null;function xv(){return Nr}function Sv(){return Or}function yv({onDistortion:n,onResolution:t}){Ts=n,bs=t}function Ev(){const n=document.getElementById("rotation-slider"),t=document.getElementById("resolution-slider"),e=document.getElementById("distortion-slider"),i=document.getElementById("reactivity-slider"),s=document.getElementById("sensitivity-slider");n?.addEventListener("input",function(){document.getElementById("rotation-value").textContent=this.value}),t?.addEventListener("input",function(){const r=parseInt(this.value);document.getElementById("resolution-value").textContent=r,bs&&bs(r)}),e?.addEventListener("input",function(){const r=parseFloat(this.value);document.getElementById("distortion-value").textContent=r.toFixed(1),Ts&&Ts(r)}),i?.addEventListener("input",function(){Nr=parseFloat(this.value),document.getElementById("reactivity-value").textContent=Nr.toFixed(1)}),s?.addEventListener("input",function(){Or=parseFloat(this.value),document.getElementById("sensitivity-value").textContent=Or.toString()}),document.getElementById("reset-btn")?.addEventListener("click",function(){n.value=1,document.getElementById("rotation-value").textContent="1.0",t.value=32,document.getElementById("resolution-value").textContent="32",e.value=1,document.getElementById("distortion-value").textContent="1.0",i.value=1,document.getElementById("reactivity-value").textContent="1.0",Nr=1,s.value=5,document.getElementById("sensitivity-value").textContent="5.0",Or=5,Ts&&Ts(1),bs&&bs(32),gv(),window.__jarvisResetAnomaly&&window.__jarvisResetAnomaly(),Fe("TODO RESTABLECIDO")}),document.getElementById("save-btn")?.addEventListener("click",function(){Ju(),Fe("DISTRIBUCIÓN GUARDADA")}),Mv(),bv(),wv()}function Mv(){const n=document.getElementById("theme-palette");if(!n)return;const t=Cs();cd.forEach(e=>{const i=document.createElement("button");i.className="theme-color-btn",i.title=e.name,i.dataset.hue=e.hue;const s=e.hue===t;i.style.cssText=`
      width: 24px;
      height: 24px;
      border: 2px solid ${s?"rgba(255,255,255,0.6)":"transparent"};
      background: hsl(${e.hue}, 80%, 55%);
      border-radius: 50%;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: ${s?`0 0 8px hsl(${e.hue}, 80%, 55%)`:"none"};
    `,i.addEventListener("mouseenter",function(){this.style.transform="scale(1.2)",this.style.boxShadow=`0 0 10px hsl(${e.hue}, 80%, 55%)`}),i.addEventListener("mouseleave",function(){this.style.transform="scale(1)",parseInt(this.dataset.hue)!==Cs()&&(this.style.boxShadow="none")}),i.addEventListener("click",function(){const r=parseInt(this.dataset.hue);eu(r),Fe(`TEMA CAMBIADO A ${e.name.toUpperCase()}`),Tv()}),n.appendChild(i)})}function Tv(){const n=Cs();document.querySelectorAll(".theme-color-btn").forEach(e=>{const i=parseInt(e.dataset.hue),s=i===n;e.style.border=`2px solid ${s?"rgba(255,255,255,0.6)":"transparent"}`,e.style.boxShadow=s?`0 0 8px hsl(${i}, 80%, 55%)`:"none"})}async function bv(){const n=document.getElementById("tts-engine-btns"),t=document.getElementById("tts-engine-label");if(n)try{const e=await fetch("/api/tts/engines");if(!e.ok)return;const i=await e.json();t.textContent=i.engines.find(s=>s.selected)?.name||"—",i.engines.forEach(s=>{if(!s.available)return;const r=document.createElement("button");r.className="btn tts-engine-btn",r.textContent=s.name.toUpperCase(),r.dataset.engine=s.id,r.style.cssText=`
        flex: 1;
        padding: 6px 12px;
        font-size: 0.6875rem;
        border: 1px solid ${s.selected?"rgba(var(--accent-rgb), 0.8)":"rgba(var(--accent-rgb), 0.3)"};
        background: ${s.selected?"rgba(var(--accent-rgb), 0.15)":"transparent"};
        color: var(--text-primary);
        cursor: pointer;
        font-family: "TheGoodMonolith", monospace;
        letter-spacing: 1px;
      `,r.addEventListener("click",async()=>{(await fetch("/api/tts/engine",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({engine:s.id})})).ok&&(Fe(`MOTOR TTS: ${s.name.toUpperCase()}`),t.textContent=s.name,Av(s.id))}),n.appendChild(r)})}catch{}}function Av(n){document.querySelectorAll(".tts-engine-btn").forEach(t=>{const e=t.dataset.engine===n;t.style.border=`1px solid rgba(var(--accent-rgb), ${e?"0.8":"0.3"})`,t.style.background=e?"rgba(var(--accent-rgb), 0.15)":"transparent"})}async function Ka(){const n=document.getElementById("profile-info"),t=document.getElementById("profile-indicator");if(n)try{const s=(await(await fetch("/api/profile")).json()).profile||{},r=[];s.name&&r.push(`📝 ${s.name}`),s.telegram_chat_id&&r.push(`💬 ID: ${s.telegram_chat_id}`),r.length?(n.innerHTML=r.join("<br>"),n.style.color="var(--accent-primary, #00d4ff)",t&&(t.textContent=`${r.length} dato(s)`)):(n.textContent="Sin datos guardados",n.style.color="var(--text-secondary, #888)",t&&(t.textContent="—"))}catch{n.textContent="Error al cargar"}}function wv(){const n=document.getElementById("profile-refresh-btn"),t=document.getElementById("profile-clear-btn");n&&n.addEventListener("click",Ka),t&&t.addEventListener("click",async()=>{if(confirm("¿Borrar todos los datos guardados?"))try{(await(await fetch("/api/profile/delete",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({keys:["name","telegram_chat_id"]})})).json()).ok&&(Ka(),Fe("DATOS BORRADOS"))}catch{}}),setTimeout(Ka,2e3)}function as(n){return`rgba(${Bs()}, ${n})`}function Rv(){const n=document.getElementById("spectrum-collapse");n&&n.addEventListener("click",()=>{const t=document.querySelector(".spectrum-analyzer");t&&t.classList.toggle("collapsed")})}const bn=document.getElementById("spectrum-canvas"),_e=bn?bn.getContext("2d"):null;function $o(){bn&&(bn.width=bn.offsetWidth,bn.height=bn.offsetHeight)}function Cv(n,t){if(!_e||!bn)return;const e=bn.width,i=bn.height;_e.clearRect(0,0,e,i);const s=e/256;let r=0;for(let o=0;o<256;o++){const l=n[o]/255*i*(t/5),c=Cs()+o/256*20;_e.fillStyle=`hsl(${c}, 100%, 50%)`,_e.fillRect(r,i-l,s-1,l),r+=s}_e.strokeStyle=as(.2),_e.lineWidth=1;for(let o=0;o<5;o++){const l=i*(o/4);_e.beginPath(),_e.moveTo(0,l),_e.lineTo(e,l),_e.stroke()}for(let o=0;o<9;o++){const l=e*(o/8);_e.beginPath(),_e.moveTo(l,0),_e.lineTo(l,i),_e.stroke()}_e.fillStyle=as(.7),_e.font='10px "TheGoodMonolith", monospace',_e.textAlign="center";const a=["0","1K","2K","4K","8K","16K"];for(let o=0;o<a.length;o++){const l=e/(a.length-1)*o;_e.fillText(a[o],l,i-5)}}const An=document.getElementById("circular-canvas"),Ee=An?An.getContext("2d"):null;function qo(){An&&(An.width=An.offsetWidth,An.height=An.offsetHeight)}function Pv(n,t,e){if(!Ee||!An)return;const i=An.width,s=An.height,r=i/2,a=s/2;Ee.clearRect(0,0,i,s);const o=180,l=Math.min(i,s)*.4;Ee.beginPath(),Ee.arc(r,a,l*1.2,0,Math.PI*2),Ee.fillStyle=as(.05),Ee.fill();const c=3,u=n.length;for(let d=0;d<c;d++){const h=l*(.7+d*.15),p=.8-d*.2;Ee.beginPath();for(let m=0;m<o;m++){const f=Math.floor(d*u/(c*1.5)),M=Math.floor((d+1)*u/(c*1.5))-f;let y=0;const P=Math.floor(M/o);for(let V=0;V<P;V++){const z=f+(m*P+V)%M;y+=n[z]}const A=y/(P*255)*(t/5)*e,I=h*(1+A*.5),E=m/o*Math.PI*2,x=r+Math.cos(E)*I,C=a+Math.sin(E)*I;m===0?Ee.moveTo(x,C):Ee.lineTo(x,C)}Ee.closePath();const _=Bs();let S;S=Ee.createRadialGradient(r,a,h*.8,r,a,h*1.2),S.addColorStop(0,`rgba(${_}, ${p})`),S.addColorStop(1,`rgba(${_}, ${p*.7})`),Ee.strokeStyle=S,Ee.lineWidth=2+(c-d),Ee.stroke(),Ee.shadowBlur=15,Ee.shadowColor=as(.7)}Ee.shadowBlur=0}const wn=document.getElementById("waveform-canvas"),ve=wn?wn.getContext("2d"):null;function Yo(){!wn||!ve||(wn.width=wn.offsetWidth*window.devicePixelRatio,wn.height=wn.offsetHeight*window.devicePixelRatio,ve.scale(window.devicePixelRatio,window.devicePixelRatio))}function Lv(n){if(!ve||!wn)return;const t=wn.width/window.devicePixelRatio,e=wn.height/window.devicePixelRatio;if(ve.clearRect(0,0,t,e),ve.fillStyle="rgba(0, 0, 0, 0.2)",ve.fillRect(0,0,t,e),n){ve.beginPath(),ve.strokeStyle=as(.8),ve.lineWidth=2;const i=t/n.length;let s=0;for(let r=0;r<n.length;r++){const o=n[r]/128*e/2;r===0?ve.moveTo(s,o):ve.lineTo(s,o),s+=i}ve.stroke()}else{ve.beginPath(),ve.strokeStyle=as(.8),ve.lineWidth=1;const i=Date.now()/1e3,s=t/100;let r=0;for(let a=0;a<100;a++){const o=a/100,l=e/2+Math.sin(o*10+i)*5+Math.sin(o*20+i*1.5)*3+Math.sin(o*30+i*.5)*7+(Math.random()-.5)*2;a===0?ve.moveTo(r,l):ve.lineTo(r,l),r+=s}ve.stroke()}}function Dv(){$o(),qo(),Yo(),window.addEventListener("resize",()=>{$o(),qo(),Yo()})}function Qu(){$o(),qo(),Yo()}function Iv(){const n=document.getElementById("preloader-canvas");if(!n)return;const t=n.getContext("2d"),e=n.width/2,i=n.height/2;let s=0,r=0;const a=80,o=5,l=24;function c(u){r||(r=u);const d=u-r;r=u,s+=d*.001,t.clearRect(0,0,n.width,n.height);const h=Bs();t.beginPath(),t.arc(e,i,3,0,Math.PI*2),t.fillStyle=`rgba(${h}, 0.9)`,t.fill();for(let p=0;p<o;p++){const _=(s*.3+p/o)%1,S=_*a,m=1-_;t.beginPath(),t.arc(e,i,S,0,Math.PI*2),t.strokeStyle=`rgba(${h}, ${m*.2})`,t.lineWidth=1,t.stroke();for(let f=0;f<l;f++){const b=f/l*Math.PI*2,M=e+Math.cos(b)*S,y=i+Math.sin(b)*S,P=2*(1-_*.5);t.beginPath(),t.moveTo(e,i),t.lineTo(M,y),t.strokeStyle=`rgba(${h}, ${m*.1})`,t.lineWidth=1,t.stroke(),t.beginPath(),t.arc(M,y,P,0,Math.PI*2),t.fillStyle=`rgba(${h}, ${m*.9})`,t.fill()}}document.getElementById("loading-overlay").style.display!=="none"&&requestAnimationFrame(c)}requestAnimationFrame(c)}function Uv(){function n(){const t=new Date,e=String(t.getHours()).padStart(2,"0"),i=String(t.getMinutes()).padStart(2,"0"),s=String(t.getSeconds()).padStart(2,"0"),r=document.getElementById("timestamp");r&&(r.textContent=`${e}:${i}:${s}`)}setInterval(n,1e3),n()}const jc=["Analizando intención del usuario...","PARSING CONTEXT WINDOW: 128K TOKENS LOADED","Buscando en memoria... memory/2026-02-12.md","EVALUATING RESPONSE CANDIDATES...","Verificando consistencia de personalidad...","AUDIO FREQUENCY ANALYSIS: PEAK AT 440HZ","Vinculando memoria a largo y corto plazo","GSAP.TIMELINE({SMOOTHNESS: 0.85})","推理鏈：前提 → 分析 → 結論 → 驗證","SCANNING SKILL REGISTRY: 6 MODULES ACTIVE","Comprensión semántica... confianza 0.94","THREE.VECTOR3 → ANOMALY.POSITION.UPDATE()","Análisis emocional: positivo 0.7 / 中性 0.2 / 負面 0.1","HEARTBEAT.CHECK() — ALL SYSTEMS NOMINAL","Organizando estructura de respuesta... 3 párrafos","CONTEXT.RELEVANCE.SCORE = 0.89","Revisando últimos 5 mensajes para coherencia","MODEL.INFERENCE({TEMP: 0.7, TOP_P: 0.95})","Determinando: requiere respuesta técnica","LOADING AGENT.JSON — CONFIG PASSED","Buscando la mejor expresión...",'NEURAL.PATHWAY("CREATIVE_REASONING")',"Validación cruzada: memoria × contexto × instrucción","OPTIMIZER.RUN({BEAM_SEARCH, WIDTH: 4})","Idea interesante... desarrollando...","SYSTEM.COHERENCE.CHECK — PASSED ✓","Balanceando eficiencia e integridad...","TOKEN.BUDGET.REMAINING: 45,231","Nuevo patrón detectado... guardando en memoria","ATTENTION.LAYER[32].REDISTRIBUTING..."];let _s=null,yi=null,Kc=0,On=null,vs=null;function Nv(){_s=document.createElement("div"),_s.id="thought-stream",_s.style.cssText=`
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    width: 45%;
    max-width: 600px;
    height: 250px;
    pointer-events: none;
    z-index: 2;
    overflow: hidden;
    -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,0.3) 30%, rgba(0,0,0,0.8) 70%, rgba(0,0,0,1) 100%);
    mask-image: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,0.3) 30%, rgba(0,0,0,0.8) 70%, rgba(0,0,0,1) 100%);
  `,yi=document.createElement("div"),yi.style.cssText=`
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 6px;
    padding: 0 10px;
  `,_s.appendChild(yi),document.body.appendChild(_s)}function Zc(){const n=jc[Kc%jc.length];Kc++;const t=document.createElement("div");for(t.style.cssText=`
    font-family: "TheGoodMonolith", monospace;
    font-size: 14px;
    letter-spacing: 1.5px;
    line-height: 1.8;
    color: rgba(var(--accent-rgb), 0.45);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
  `,t.textContent="",yi.appendChild(t);yi.children.length>12;)yi.removeChild(yi.firstChild);On={el:t,text:n,charIdx:0},vs&&clearInterval(vs),vs=setInterval(()=>{On&&(On.charIdx<On.text.length?(On.el.textContent=On.text.substring(0,On.charIdx+1),On.charIdx++):(clearInterval(vs),vs=null,On=null))},40)}function Ov(){Nv(),setTimeout(()=>{Zc(),setInterval(Zc,3500)},4e3)}const Fv=window.matchMedia("(max-width: 768px)").matches,td={spectrum:".spectrum-analyzer","info-center":".info-center"};let Ei=null;function jo(){if(!Ei)return;const n=document.querySelector(td[Ei]);n&&(n.classList.remove("mobile-open"),setTimeout(()=>{n.classList.contains("mobile-open")||n.classList.remove("mobile-slide")},300));const t=document.querySelector(`.mobile-toolbar-btn[data-panel="${Ei}"]`);t&&t.classList.remove("active"),document.getElementById("mobile-overlay").classList.remove("visible"),document.querySelector(".terminal-panel.chat-panel").classList.remove("panel-behind"),Ei=null}function Bv(n){Ei&&jo();const t=document.querySelector(td[n]);if(!t)return;t.classList.add("mobile-slide"),t.offsetHeight,t.classList.add("mobile-open"),setTimeout(()=>Qu(),350);const e=document.querySelector(`.mobile-toolbar-btn[data-panel="${n}"]`);e&&e.classList.add("active"),document.getElementById("mobile-overlay").classList.add("visible"),document.querySelector(".terminal-panel.chat-panel").classList.add("panel-behind"),Ei=n}function zv(){if(!Fv)return;const n=document.getElementById("mobile-toolbar");n&&(n.addEventListener("click",t=>{const e=t.target.closest(".mobile-toolbar-btn");if(!e)return;const i=e.dataset.panel;Ei===i?jo():Bv(i)}),document.getElementById("mobile-overlay").addEventListener("click",jo))}let nn=!1;const Jc="jarvis-powersave";function Za(){return nn}function kv(){nn=localStorage.getItem(Jc)==="true";const n=document.getElementById("powersave-btn");n&&(Qc(n),n.addEventListener("click",()=>{nn=!nn,localStorage.setItem(Jc,nn),Qc(n),tu(),Fe(nn?"🔋 POWER SAVE ON":"⚡ POWER SAVE OFF")}),nn&&tu())}function Qc(n){n.style.border=`1px solid rgba(var(--accent-rgb), ${nn?"0.8":"0.3"})`,n.style.background=nn?"rgba(var(--accent-rgb), 0.15)":"transparent",n.title=nn?"Power Save: ON":"Power Save: OFF"}function tu(){nn?document.body.classList.add("power-save"):document.body.classList.remove("power-save"),window.dispatchEvent(new CustomEvent("powersave-change",{detail:{enabled:nn}}))}document.addEventListener("DOMContentLoaded",async function(){const n=await od();Al(),document.title=n.name||"JARVIS";const t=n.agent?.name||"JARVIS",e=document.querySelector(".terminal-panel.chat-panel .terminal-header span");e&&(e.textContent=`${t} CHAT`);const i=n.agent?.emoji||"⚡";document.documentElement.style.setProperty("--agent-prefix",`"${t} ${i} "`),Iv(),z0(),H0(),J0(),nv(),av(),fv(),Ev(),kv(),Rv(),M0(),Dv(),Uv(),d0(),yv({onDistortion:$_,onResolution:q_}),s0(Y_);const s=document.getElementById("orb-status");if(s){const u={idle:"INACTIVO",thinking:"PENSANDO...",responding:"RESPONDIENDO..."};window.addEventListener("agent-state",d=>{s.textContent=u[d.detail]||d.detail.toUpperCase(),s.className="scanner-id state-"+(d.detail||"idle");const h=document.querySelector(".scanner-line"),p=document.querySelector(".scanner-frame");if(h)switch(d.detail){case"thinking":h.style.animationDuration="1.5s",p?.classList.add("state-active");break;case"responding":h.style.animationDuration="2.5s",p?.classList.add("state-active");break;default:h.style.animationDuration="4s",p?.classList.remove("state-active")}})}const r=document.getElementById("orb-meta");if(r){let u=0,d="";const h=()=>{r.textContent=d?`${d}${u?` · ${u} MSGS`:""}`:u?`${u} MSGS`:""};fetch("/api/status").then(p=>p.json()).then(p=>{d=(p.channel||"").toUpperCase(),u=p.msgCount||0,h()}).catch(()=>{}),window.addEventListener("agent-state",p=>{p.detail==="thinking"&&(u++,h())})}document.addEventListener("mousemove",$c),document.addEventListener("keydown",$c);const a=document.getElementById("loading-overlay");setTimeout(()=>{a.style.opacity=0,setTimeout(()=>{a.style.display="none",Tn(),f0(),vv(),y0(X_),Ov(),zv()},500)},3e3),t0(),window.__jarvisResetAnomaly=Z_,Al(),window.addEventListener("resize",()=>{Q_(Qu)});let o=0;function l(u){if(requestAnimationFrame(l),window.__jarvisHiddenPause?.())return;if(Za()){if(u-o<66)return;o=u}const d=i0(),h=n0(),p=e0(),_=Sv(),S=xv();let m=0;d&&!Za()&&(d.getByteFrequencyData(h),d.getByteTimeDomainData(p),m=h0(_),Pv(h,_,S),Cv(h,_),u0(S,_),c0()),Za()||Lv(d?p:null);const f=parseFloat(document.getElementById("rotation-slider")?.value||1);J_(m,f,S)}l(0);let c=!1;document.addEventListener("visibilitychange",()=>{c=document.hidden}),window.__jarvisHiddenPause=()=>c});"serviceWorker"in navigator&&navigator.serviceWorker.register("/sw.js").catch(()=>{});
