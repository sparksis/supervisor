"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[7165],{17165:function(e,t,i){i.r(t),i.d(t,{HaAddonSelector:function(){return w}});var a,n,o,r,s,d=i(88962),l=i(33368),u=i(71650),c=i(82390),h=i(69205),v=i(70906),k=i(91808),f=i(68144),p=i(14243),y=i(99312),b=i(81043),m=i(7323),_=i(47181),g=i(85415),Z=i(34154),C=i(26765),x=function(e){return(0,f.dy)(a||(a=(0,d.Z)(['<mwc-list-item twoline graphic="icon"> <span>','</span> <span slot="secondary">',"</span> "," </mwc-list-item>"])),e.name,e.slug,e.icon?(0,f.dy)(n||(n=(0,d.Z)(['<img alt="" slot="graphic" .src="/api/hassio/addons/','/icon">'])),e.slug):"")},w=((0,k.Z)([(0,p.Mo)("ha-addon-picker")],(function(e,t){var i,a=function(t){(0,h.Z)(a,t);var i=(0,v.Z)(a);function a(){var t;(0,u.Z)(this,a);for(var n=arguments.length,o=new Array(n),r=0;r<n;r++)o[r]=arguments[r];return t=i.call.apply(i,[this].concat(o)),e((0,c.Z)(t)),t}return(0,l.Z)(a)}(t);return{F:a,d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,p.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,p.Cb)()],key:"value",value:function(){return""}},{kind:"field",decorators:[(0,p.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,p.SB)()],key:"_addons",value:void 0},{kind:"field",decorators:[(0,p.Cb)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,p.Cb)({type:Boolean})],key:"required",value:function(){return!1}},{kind:"field",decorators:[(0,p.IO)("ha-combo-box")],key:"_comboBox",value:void 0},{kind:"method",key:"open",value:function(){var e;null===(e=this._comboBox)||void 0===e||e.open()}},{kind:"method",key:"focus",value:function(){var e;null===(e=this._comboBox)||void 0===e||e.focus()}},{kind:"method",key:"firstUpdated",value:function(){this._getAddons()}},{kind:"method",key:"render",value:function(){return this._addons?(0,f.dy)(o||(o=(0,d.Z)([' <ha-combo-box .hass="','" .label="','" .value="','" .required="','" .disabled="','" .helper="','" .renderer="','" .items="','" item-value-path="slug" item-id-path="slug" item-label-path="name" @value-changed="','"></ha-combo-box> '])),this.hass,void 0===this.label&&this.hass?this.hass.localize("ui.components.addon-picker.addon"):this.label,this._value,this.required,this.disabled,this.helper,x,this._addons,this._addonChanged):f.Ld}},{kind:"method",key:"_getAddons",value:(i=(0,b.Z)((0,y.Z)().mark((function e(){var t,i=this;return(0,y.Z)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(e.prev=0,!(0,m.p)(this.hass,"hassio")){e.next=8;break}return e.next=4,(0,Z.yt)(this.hass);case 4:t=e.sent,this._addons=t.addons.filter((function(e){return e.version})).sort((function(e,t){return(0,g.$)(e.name,t.name,i.hass.locale.language)})),e.next=9;break;case 8:(0,C.Ys)(this,{title:this.hass.localize("ui.components.addon-picker.error.no_supervisor.title"),text:this.hass.localize("ui.components.addon-picker.error.no_supervisor.description")});case 9:e.next=14;break;case 11:e.prev=11,e.t0=e.catch(0),(0,C.Ys)(this,{title:this.hass.localize("ui.components.addon-picker.error.fetch_addons.title"),text:this.hass.localize("ui.components.addon-picker.error.fetch_addons.description")});case 14:case"end":return e.stop()}}),e,this,[[0,11]])}))),function(){return i.apply(this,arguments)})},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_addonChanged",value:function(e){e.stopPropagation();var t=e.detail.value;t!==this._value&&this._setValue(t)}},{kind:"method",key:"_setValue",value:function(e){var t=this;this.value=e,setTimeout((function(){(0,_.B)(t,"value-changed",{value:e}),(0,_.B)(t,"change")}),0)}}]}}),f.oi),(0,k.Z)([(0,p.Mo)("ha-selector-addon")],(function(e,t){var i=function(t){(0,h.Z)(a,t);var i=(0,v.Z)(a);function a(){var t;(0,u.Z)(this,a);for(var n=arguments.length,o=new Array(n),r=0;r<n;r++)o[r]=arguments[r];return t=i.call.apply(i,[this].concat(o)),e((0,c.Z)(t)),t}return(0,l.Z)(a)}(t);return{F:i,d:[{kind:"field",decorators:[(0,p.Cb)()],key:"hass",value:void 0},{kind:"field",decorators:[(0,p.Cb)()],key:"selector",value:void 0},{kind:"field",decorators:[(0,p.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,p.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,p.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,p.Cb)({type:Boolean})],key:"disabled",value:function(){return!1}},{kind:"field",decorators:[(0,p.Cb)({type:Boolean})],key:"required",value:function(){return!0}},{kind:"method",key:"render",value:function(){return(0,f.dy)(r||(r=(0,d.Z)(['<ha-addon-picker .hass="','" .value="','" .label="','" .helper="','" .disabled="','" .required="','" allow-custom-entity></ha-addon-picker>'])),this.hass,this.value,this.label,this.helper,this.disabled,this.required)}},{kind:"field",static:!0,key:"styles",value:function(){return(0,f.iv)(s||(s=(0,d.Z)(["ha-addon-picker{width:100%}"])))}}]}}),f.oi))}}]);
//# sourceMappingURL=7165-sbw9f9OwSi8.js.map