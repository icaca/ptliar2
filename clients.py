# -*- coding: utf-8 -*-
#
# PTLiar, a fake seeding software
# Copyright (C) 2011 PTLiar.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

BT_CLIENTS = {
    "uTorrent3.0-1" : {
        "user-agent" : "uTorrent/3000(25756)",
        "prefix"     : "-UT3000-",
        "scrape"     : True,
        "comment"    : "new",
    },
    "uTorrent3.0" : {
        "user-agent" : "uTorrent/3000(25460)",
        "prefix"     : "-UT3000-",
        "scrape"     : True,
        "comment"    : "new",
    },
    "uTorrent2.2.1" : {
        "user-agent" : "uTorrent/2210(25130)",
        "prefix"     : "-UT2210-",
        "scrape"     : False,
        "comment"    : "stable",
    },
    "uTorrent2.0B" : {
        "user-agent" : "uTorrent/200B(17539)",
        "prefix"     : "-UT200B-",
        "scrape"     : False,
        "comment"    : "stable",
    },
    "uTorrent1.85" : {
        "user-agent" : "uTorrent/1850(17414)",
        "prefix"     : "-UT1850-",
        "scrape"     : False,
        "comment"    : "stable",
    },
    "Transmission2.93" : {
        "user-agent" : "Transmission/2.93",
        "prefix"    : "-TR2930-",
        "scrape"     : True,
        "comment"    : "new",
    },
}

DEFAULT_CLIENT = "uTorrent3.0"

def client_list():
    print "Supported clients:"
    for client, stuff in sorted(BT_CLIENTS.items(), reverse=True):
        print "    %-15s -    %-20s" % (client, stuff["comment"])
