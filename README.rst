==============================
``gs.group.member.leave.json``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Web-hook to remove someone from a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-06-15
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This product provides a `web hook`_ that allows a person to be
removed from a group by an external system.

Web hook
========

The ``gs-group-member-leave.json`` page in the **site** context
removes a person from the group.

Request
-------

It takes the following arguments (all required).

``groupId``:
  The identifier for the group.

``userId``:
  The identifier for the user.

``token``:
  The authentication token [#token]_

Response
--------

In response a JSON object will be returned with the following
values:

``status``:
  The exist status:

  * ``0``: Ok, the person has been removed from the group.
  * ``1``: No such group.
  * ``2``: No such user.
  * ``4``: The user and group exist, but the user is not a member
    of the group.

``message``:
  A message for the user.

``groupId``:
  The identifier for the group.

``userId``:
  The identifier for the user.


Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.member.leave.command/
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. [#token] See ``gs.auth.token``
             <https://github.com/groupserver/gs.auth.token/>

..  LocalWords:  html
