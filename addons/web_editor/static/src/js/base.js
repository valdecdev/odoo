odoo.define('web_editor.base', function (require) {
"use strict";

var core = require('web.core');
var ajax = require('web.ajax');
var qweb = core.qweb;
var _t = core._t;

//////////////////////////////////////////////////////////////////////////////////////////////////////////

var get_context = function (dict) {
    var html = document.documentElement;
    return _.extend({
        'lang': (html.getAttribute('lang') || '').replace('-', '_'),
    }, dict);
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////
/* ----------------------------------------------------
   Async Ready and Template loading
   ---------------------------------------------------- */
var dom_ready = $.Deferred();
$(document).ready(function () {
    dom_ready.resolve();
    // fix for ie
    if($.fn.placeholder) $('input, textarea').placeholder();
});


// todo: remove and load a bundle of translated templates
var all_ready;
var ready = function() {
    if (!all_ready) {
        all_ready = $.when(dom_ready, ajax.loadXML()).then(translations);
    } else if(all_ready.state() === "resolved") { // can add async template
        all_ready = $.when(dom_ready, ajax.loadXML());
    }
    return all_ready;
};

function translations() {
    function translate_node(node){
        if(node.nodeType === 3) { // TEXT_NODE
            if(node.nodeValue.match(/\S/)){
                var space = node.nodeValue.match(/^([\s]*)([\s\S]*?)([\s]*)$/);
                node.nodeValue = space[1] + $.trim(_t(space[2])) + space[3];
            }
        }
        else if(node.nodeType === 1 && node.hasChildNodes()) { // ELEMENT_NODE
            _.each(node.childNodes, translate_node);
        }
    }
    return ajax.jsonRpc(data.url_translations, 'call', {
            'mods': ['web_editor'],
            'lang': data.get_context().lang
        })
        .then(function(trans) {
            _t.database.set_bundle(trans);
        }).then(function () {
            var keys = _.keys(qweb.templates);
            for (var i = 0; i < keys.length; i++){
                translate_node(qweb.templates[keys[i]]);
            }
        }).promise();
}

var data = {
    'get_context': get_context,
    'url_translations': '/web/webclient/translations',
    'dom_ready': dom_ready,
    'ready': ready,
};
return data;

});
