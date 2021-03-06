# -*- coding: utf-8 -*-
import openerp
from openerp.http import request

from openerp.addons.bus.models.bus import dispatch


class BusController(openerp.http.Controller):
    """ Examples:
    openerp.jsonRpc('/longpolling/poll','call',{"channels":["c1"],last:0}).then(function(r){console.log(r)});
    openerp.jsonRpc('/longpolling/send','call',{"channel":"c1","message":"m1"});
    openerp.jsonRpc('/longpolling/send','call',{"channel":"c2","message":"m2"});
    """

    @openerp.http.route('/longpolling/send', type="json", auth="public")
    def send(self, channel, message):
        if not isinstance(channel, basestring):
            raise Exception("bus.Bus only string channels are allowed.")
        return request.env['bus.bus'].sendone(channel, message)

    # override to add channels
    def _poll(self, dbname, channels, last, options):
        request.cr.close()
        request._cr = None
        return dispatch.poll(dbname, channels, last)

    @openerp.http.route('/longpolling/poll', type="json", auth="public")
    def poll(self, channels, last, options=None):
        if options is None:
            options = {}
        if not dispatch:
            raise Exception("bus.Bus unavailable")
        if [c for c in channels if not isinstance(c, basestring)]:
            raise Exception("bus.Bus only string channels are allowed.")
        return self._poll(request.db, channels, last, options)
